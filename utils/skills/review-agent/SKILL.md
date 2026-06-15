---
name: review-agent
description: |
  Kick off a background review of a PR and watch it for incoming feedback.
  Spins up an agent that runs the built-in /review skill against the current
  (or a specified) PR, then starts a persistent watcher that streams new CI
  failures and review comments (bots and humans) as they land — auto-fixing
  trivial items and triaging the rest for sign-off. Use when the user says
  "review this PR", "watch this PR", "monitor PR feedback", or "keep an eye on
  CI and reviews for PR #N".
argument-hint: "[PR number or URL]"
---

# Review agent

Drive the whole review loop on a pull request: run our own review in the
background, watch for everyone else's feedback as it arrives, and act on it.

This complements the other PR skills — `pr-comments` (snapshot of what's
*already* on a PR), `pr-feedback` (triage + implement), `pr-respond` (reply +
resolve). Use **this** skill for *live* activity on a PR you're iterating on.

## Phase 0: Resolve the PR

If `$ARGUMENTS` is a PR number or URL, use it. Otherwise detect the PR for the
current branch:

```
gh pr view --json number,title,url -q '"#\(.number) — \(.title)"'
```

If there's no PR for the branch, tell the user and stop.

## Phase 1: Kick off our own review

Launch a **background** `Agent` that runs the built-in `/review` skill against
the PR and reports its findings back. Its final message returns to this thread —
nothing is posted to the PR.

```
Agent(
  subagent_type: "general-purpose",
  run_in_background: true,
  description: "Review PR #<N>",
  prompt: "Run the /review skill against PR #<N> in this repo. Report the
           findings back as a concise list grouped by severity (blocking /
           should-fix / nit), each with file:line and a one-line rationale.
           Do not post anything to the PR — just report back.",
)
```

Tell the user the review is running in the background and that you'll fold its
findings in alongside incoming feedback when it returns.

## Phase 2: Start watching

Start a **persistent** `Monitor` on the PR. The script seeds with the PR's
current state, then streams one line per *new* CI failure or comment, and exits
on merge/close.

```
Monitor(
  description: "PR #<N> — review + incoming feedback",
  command: "${CLAUDE_PLUGIN_ROOT}/skills/review-agent/scripts/watch.sh <N>",
  persistent: true,
)
```

Each event line ends with a comment/review URL. Bodies are truncated to 300
chars — when you need the full text, call
`${CLAUDE_PLUGIN_ROOT}/skills/review-agent/scripts/read-comment.sh <url>`.

## Phase 3: Handle events as they land

Event lines carry an authorship label. The **base label means a bot** on the
watchlist; `-SELF` (the PR author) and `-HUMAN` (any other person) are suffixes.

| Event | Who | What to do |
|-------|-----|------------|
| `CHECK … fail` / `cancel` | CI | Surface it. If it's a clear flake or an obvious break, investigate and offer a fix. Otherwise summarise. |
| `CHECK all N checks passed` | CI | CI is green — nothing to do. |
| `COMMENT` / `REVIEW-COMMENT` / `REVIEW` `<bot>` | AI review bot | Actionable. Read the targeted code (use `read-comment.sh` for the full body), then **auto-fix if trivially safe**, else triage (Phase 4). |
| `…-SELF` | PR author | Treat like a bot suggestion — your own notes on your own PR. Read the code, auto-fix if trivial, else triage. |
| `…-HUMAN` | A reviewer | **Report, don't act.** Surface what they said and ask the user (address / reply / leave). Never edit code or reply on their behalf without explicit instruction. |

### Auto-fix vs triage

**Trivially safe** means there's no behavioural ambiguity and the fix is
obviously correct: typos, comment wording, lint/formatting, an obvious
one-line correction. Apply these directly and report what changed
(e.g. "Applied: fixed typo in `foo.ts:42`"). Everything else goes to triage.

When in doubt, triage rather than auto-fix.

## Phase 4: Triage non-trivial items

For anything not auto-fixed, use the `pr-feedback` bucket model:

| Bucket | Criteria |
|--------|----------|
| **Implement** | Correct, improves the code, in scope |
| **Acknowledge** | Valid but out of scope or a deliberate choice |
| **Decline** | Incorrect, a misunderstanding, or would make things worse |

Present the triage as a table and **wait for sign-off** before making
non-trivial edits. Bots produce false positives — don't implement something
just because a bot said it.

## Phase 5: Respond & resolve

After changes are pushed, hand off to `/pr-respond` to reply to threads and
resolve the addressed ones. It's already bot-aware: terse, no pleasantries for
bot accounts; courteous for humans.

## Guidelines

- **Never auto-act on a `-HUMAN` comment.** Report and ask.
- **Confirm before non-trivial edits.** Auto-fix is for the trivially safe only.
- **Don't silently apply bot suggestions** beyond the trivial bar above.
- **Use `read-comment.sh`** when the 300-char teaser cuts off the rationale.
- **Tuning the watcher:** `scripts/watch.sh` has two allowlists at the top —
  `BOTS` (review bots whose comments are actionable) and `IGNORE_LOGINS`
  (user-account automation to drop). Add new tools there.
- **For a one-off snapshot** of what's already on a PR, don't use this skill —
  use `pr-comments` (or `gh api`) directly. This skill is for *new* activity.
