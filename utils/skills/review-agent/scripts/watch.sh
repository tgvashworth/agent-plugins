#!/usr/bin/env bash
# watch.sh — poll a GitHub PR for CI check failures and review activity from
# AI code-review bots (GitHub Copilot, Cursor Bugbot, CodeRabbit, Greptile,
# Codex, etc.) AND humans.
#
# Each event is emitted as a single stdout line, designed to be consumed by
# Claude Code's Monitor tool. The script seeds itself with the current state
# on startup, then emits only *new* events from then on. It exits on PR
# merge/close.
#
# Comment authorship is classified into three buckets so Claude can treat them
# differently (see SKILL.md):
#   - bots on the BOTS allowlist  → COMMENT / REVIEW-COMMENT / REVIEW       (actionable)
#   - the PR author (self-review) → *-SELF  (actionable: act on your own notes)
#   - any other human (reviewer)  → *-HUMAN (report only; ask before acting)
# Other automation is ignored: GitHub Apps (type=="Bot") not on the allowlist
# (e.g. github-actions, vercel), plus any user-account bots listed in
# IGNORE_LOGINS.
#
# CI checks are noisy, so we only emit *failures / cancellations* plus a single
# "all checks passed" line once everything resolves. Successes and pending/
# running transitions are dropped before they ever reach Claude.
#
# Usage: watch.sh <pr-number> [poll-seconds]

set -uo pipefail

PR="${1:-}"
POLL_INTERVAL="${2:-${PR_WATCH_INTERVAL:-30}}"

if [[ -z "$PR" ]]; then
  echo "usage: watch.sh <pr-number> [poll-seconds]" >&2
  exit 2
fi

# --- Tunables -----------------------------------------------------------------
# AI review-bot GitHub logins whose comments are actionable. Add new entries as
# new review tools start posting on your PRs.
BOTS=(
  "copilot-pull-request-reviewer[bot]"
  "Copilot"
  "cursor[bot]"
  "coderabbitai[bot]"
  "greptile-apps[bot]"
  "chatgpt-codex-connector[bot]"
  "sourcery-ai[bot]"
  "ellipsis-dev[bot]"
  "claude[bot]"
)

# Non-review automation to ignore entirely. GitHub Apps (login ending "[bot]")
# are already filtered by .user.type=="Bot", but some automation posts as a
# normal *user* account — add those logins here so they don't read as humans.
IGNORE_LOGINS=()
# ------------------------------------------------------------------------------

REPO="$(gh repo view --json nameWithOwner -q .nameWithOwner 2>/dev/null)"
if [[ -z "$REPO" ]]; then
  echo "[watch] could not resolve repo via gh — are you in a GitHub repo?" >&2
  exit 2
fi

# PR author login — used to tell self-review notes (*-SELF) from reviewer
# comments (*-HUMAN). Empty if the lookup fails; humans then all read as -HUMAN.
PR_AUTHOR="$(gh pr view "$PR" --json author -q .author.login 2>/dev/null || echo "")"

STATE_DIR="${CLAUDE_JOB_DIR:-/tmp}/review-agent-watch-${REPO//\//-}-${PR}"
mkdir -p "$STATE_DIR"
checks_state="$STATE_DIR/checks.json"
allgreen_flag="$STATE_DIR/all-green"        # present once we've emitted "all passed"
issue_seen="$STATE_DIR/issue-comments.ids"
review_seen="$STATE_DIR/review-comments.ids"
reviews_seen="$STATE_DIR/reviews.ids"
touch "$issue_seen" "$review_seen" "$reviews_seen"

# Build jq array literals of the bot / ignore logins: ["cursor[bot]",...]
bot_array='['
for i in "${!BOTS[@]}"; do
  [[ $i -gt 0 ]] && bot_array+=','
  bot_array+="\"${BOTS[$i]}\""
done
bot_array+=']'
ignore_array='['
for i in "${!IGNORE_LOGINS[@]}"; do
  [[ $i -gt 0 ]] && ignore_array+=','
  ignore_array+="\"${IGNORE_LOGINS[$i]}\""
done
ignore_array+=']'

# Seed snapshots so we don't emit historical state on first iteration. We
# surface human comments too, so seed *all* existing comments/reviews (not just
# bots) — otherwise historical discussion would flood the first poll.
gh pr checks "$PR" --json name,bucket,state,link >"$checks_state" 2>/dev/null || echo '[]' >"$checks_state"
gh api "repos/$REPO/issues/$PR/comments" --paginate \
  --jq ".[] | .id" \
  >>"$issue_seen" 2>/dev/null || true
gh api "repos/$REPO/pulls/$PR/comments" --paginate \
  --jq ".[] | .id" \
  >>"$review_seen" 2>/dev/null || true
gh api "repos/$REPO/pulls/$PR/reviews" --paginate \
  --jq ".[] | .id" \
  >>"$reviews_seen" 2>/dev/null || true

echo "[watch] $REPO#$PR (author: ${PR_AUTHOR:-?}) — polling every ${POLL_INTERVAL}s"

emit_new_ids() {
  # $1 = seen-ids file, stdin = lines of "<id>\t<rest>". Emit "<rest>" for unseen ids.
  local seen="$1"
  while IFS=$'\t' read -r id rest; do
    [[ -z "$id" ]] && continue
    if ! grep -qxF "$id" "$seen"; then
      echo "$id" >>"$seen"
      printf '%s\n' "$rest"
    fi
  done
}

while true; do
  # --- PR lifecycle: stop on merge or close.
  pr_state=$(gh pr view "$PR" --json state -q .state 2>/dev/null || echo "")
  case "$pr_state" in
    MERGED) echo "[watch] PR #$PR merged — stopping"; exit 0 ;;
    CLOSED) echo "[watch] PR #$PR closed — stopping"; exit 0 ;;
  esac

  # --- CI checks: emit failures/cancellations only, plus one all-green summary.
  # Gate on valid JSON rather than gh's exit code (gh pr checks exits non-zero
  # while checks are pending/failing, but still prints valid JSON we want).
  new_checks=$(mktemp)
  gh pr checks "$PR" --json name,bucket,state,link >"$new_checks" 2>/dev/null
  if [[ -s "$new_checks" ]] && jq -e 'type=="array"' "$new_checks" >/dev/null 2>&1; then
    jq -r --slurpfile prev "$checks_state" '
      ($prev[0] // []) as $p |
      .[] as $c |
      ($p | map(select(.name == $c.name)) | .[0]) as $old |
      (($c.bucket == "fail") or ($c.bucket == "cancel")) as $bad |
      if $bad and (($old == null) or ($old.bucket != $c.bucket)) then
        "CHECK \($c.name): \($c.bucket) \($c.link // "")"
      else empty end
    ' "$new_checks" 2>/dev/null || true
    mv "$new_checks" "$checks_state"

    # Single summary line once nothing is pending and nothing failed. Skipped
    # checks aren't failures (nothing to act on) so they don't block the summary,
    # but they're reported separately rather than counted as "passed". The flag
    # resets whenever we re-enter a pending/failed state, so a later clean run
    # (e.g. after a re-push) emits the summary again.
    total=$(jq 'length' "$checks_state" 2>/dev/null || echo 0)
    pending=$(jq '[.[]|select(.bucket=="pending")]|length' "$checks_state" 2>/dev/null || echo 0)
    bad=$(jq '[.[]|select(.bucket=="fail" or .bucket=="cancel")]|length' "$checks_state" 2>/dev/null || echo 0)
    passed=$(jq '[.[]|select(.bucket=="pass")]|length' "$checks_state" 2>/dev/null || echo 0)
    skipped=$(jq '[.[]|select(.bucket=="skipping")]|length' "$checks_state" 2>/dev/null || echo 0)
    if [[ "$total" -gt 0 && "$pending" -eq 0 && "$bad" -eq 0 ]]; then
      if [[ ! -f "$allgreen_flag" ]]; then
        if [[ "$skipped" -gt 0 ]]; then
          echo "CHECK all checks complete — $passed passed, $skipped skipped"
        else
          echo "CHECK all $passed checks passed"
        fi
        touch "$allgreen_flag"
      fi
    else
      rm -f "$allgreen_flag"
    fi
  else
    rm -f "$new_checks"
  fi

  # --- Issue (PR-level) comments: bots + self + human reviewers.
  gh api "repos/$REPO/issues/$PR/comments" --paginate \
    --jq "$bot_array as \$bots | $ignore_array as \$ignore | .[]
          | (.user.login) as \$u
          | (if (\$bots | index(\$u)) then \"COMMENT \(\$u)\"
             elif ((\$ignore | index(\$u)) or (.user.type == \"Bot\")) then \"\"
             elif (\$u == \"$PR_AUTHOR\") then \"COMMENT-SELF \(\$u)\"
             else \"COMMENT-HUMAN \(\$u)\" end) as \$label
          | select(\$label != \"\")
          | \"\(.id)\t\(\$label): \(.body | gsub(\"\\n\";\" \") | .[0:300])  (\(.html_url))\"" \
    2>/dev/null | emit_new_ids "$issue_seen"

  # --- Inline review comments: bots (Bugbot etc.) + self + human reviewers.
  gh api "repos/$REPO/pulls/$PR/comments" --paginate \
    --jq "$bot_array as \$bots | $ignore_array as \$ignore | .[]
          | (.user.login) as \$u
          | (if (\$bots | index(\$u)) then \"REVIEW-COMMENT \(\$u)\"
             elif ((\$ignore | index(\$u)) or (.user.type == \"Bot\")) then \"\"
             elif (\$u == \"$PR_AUTHOR\") then \"REVIEW-COMMENT-SELF \(\$u)\"
             else \"REVIEW-COMMENT-HUMAN \(\$u)\" end) as \$label
          | select(\$label != \"\")
          | \"\(.id)\t\(\$label) at \(.path):\(.line // .original_line // 0): \(.body | gsub(\"\\n\";\" \") | .[0:300])  (\(.html_url))\"" \
    2>/dev/null | emit_new_ids "$review_seen"

  # --- Reviews (approve / changes-requested / commented): bots + self + humans.
  # Skip empty-body COMMENTED reviews — they're just the wrapper around inline
  # comments we've already surfaced, and would double the signal.
  gh api "repos/$REPO/pulls/$PR/reviews" --paginate \
    --jq "$bot_array as \$bots | $ignore_array as \$ignore | .[]
          | select(.state != \"COMMENTED\" or ((.body // \"\") | length > 0))
          | (.user.login) as \$u
          | (if (\$bots | index(\$u)) then \"REVIEW \(\$u)\"
             elif ((\$ignore | index(\$u)) or (.user.type == \"Bot\")) then \"\"
             elif (\$u == \"$PR_AUTHOR\") then \"REVIEW-SELF \(\$u)\"
             else \"REVIEW-HUMAN \(\$u)\" end) as \$label
          | select(\$label != \"\")
          | \"\(.id)\t\(\$label) [\(.state)]: \((.body // \"\") | gsub(\"\\n\";\" \") | .[0:300])  (\(.html_url))\"" \
    2>/dev/null | emit_new_ids "$reviews_seen"

  sleep "$POLL_INTERVAL"
done
