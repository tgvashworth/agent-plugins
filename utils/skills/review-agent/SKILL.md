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

## Phase 1: Check existing feedback

Before watching for *new* activity, immediately surface what's **already** on
the PR so you start from a complete picture. Run the `pr-comments` fetch script:

```
${CLAUDE_PLUGIN_ROOT}/skills/pr-comments/scripts/fetch-pr-comments.sh <N> 2>&1
```

Triage anything actionable in the existing feedback right away using the same
rules as Phase 4 (auto-fix trivially-safe bot/`-SELF` items, triage the rest,
report `-HUMAN` items and ask). The watcher started in Phase 3 seeds on the
current state and only emits feedback that arrives *after* it starts — so this
phase is the one chance to catch what's already there.

## Phase 2: Kick off our own review

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

## Phase 3: Start watching

Start a **persistent** `Monitor` on the PR. The script seeds with the PR's
current state (which you already reviewed in Phase 1), then streams one line per
*new* CI failure or comment, and exits on merge/close.

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

## Phase 4: Handle events as they land

Each time you handle feedback, push a fix, and draw the next wave is another
**round** of the loop (the initial review pass was round 1) — count them, and
consult the **stop-here score** (below) before starting each new one.

Event lines carry an authorship label. The **base label means a bot** on the
watchlist; `-SELF` (the PR author) and `-HUMAN` (any other person) are suffixes.

| Event | Who | What to do |
|-------|-----|------------|
| `CHECK … fail` / `cancel` | CI | Surface it. If it's a clear flake or an obvious break, investigate and offer a fix. Otherwise summarise. |
| `CHECK all N checks passed` | CI | CI is green — nothing to do. |
| `COMMENT` / `REVIEW-COMMENT` / `REVIEW` `<bot>` | AI review bot | Actionable. Read the targeted code (use `read-comment.sh` for the full body), then **auto-fix if trivially safe**, else triage (Phase 5). |
| `…-SELF` | PR author | Treat like a bot suggestion — your own notes on your own PR. Read the code, auto-fix if trivial, else triage. |
| `…-HUMAN` | A reviewer | **Report, don't act.** Surface what they said and ask the user (address / reply / leave). Never edit code or reply on their behalf without explicit instruction. |

### Auto-fix vs triage

**Trivially safe** means there's no behavioural ambiguity and the fix is
obviously correct: typos, comment wording, lint/formatting, an obvious
one-line correction. Apply these directly and report what changed
(e.g. "Applied: fixed typo in `foo.ts:42`"). Everything else goes to triage.

When in doubt, triage rather than auto-fix.

## Phase 5: Triage non-trivial items

For anything not auto-fixed, use the `pr-feedback` bucket model:

| Bucket | Criteria |
|--------|----------|
| **Implement** | Correct, improves the code, in scope |
| **Acknowledge** | Valid but out of scope or a deliberate choice |
| **Decline** | Incorrect, a misunderstanding, or would make things worse |

Present the triage as a table and **wait for sign-off** before making
non-trivial edits. Bots produce false positives — don't implement something
just because a bot said it.

## Phase 6: Respond & resolve

After changes are pushed, hand off to `/pr-respond` to reply to threads and
resolve the addressed ones. It's already bot-aware: terse, no pleasantries for
bot accounts; courteous for humans.

Then, before the next wave of feedback pulls you into another lap, re-check the
**stop-here score** (below) and decide whether to keep going or hand back.

## Back pressure: the stop-here score

This skill can loop for a long time. Every push triggers fresh CI and another
wave of bot re-reviews, which lands as new events, which you handle, which means
another push. Left unchecked it spins on — and each lap tends to be worth less
than the last. Track how many laps you've done and lean against continuing.

**A round** is one lap of that loop: a batch of incoming feedback (CI +
comments) that you handle — fixing and/or triaging — ending in a push (or a
deliberate decision that nothing needs pushing). The initial review pass
(Phases 1–2) is round 1. Keep a running count across the session.

**The stop-here score** is how hard you should be leaning toward stopping and
handing back to the human. It's driven by the round count, and it climbs faster
when recent rounds have stopped earning their keep:

- Weigh each round's value as you go. A **productive** round lands substantive
  fixes that genuinely improve the PR. A **low-value** round produces only nits,
  formatting, false positives, or nothing actionable. Two low-value rounds in a
  row bump the score up a level early; a run of productive rounds lets you hold
  a level a little longer — but never past the hard stop.

| Rounds | Score | How to behave |
|--------|-------|---------------|
| ~1–2 | **weak** | Normal iteration. Handle events, keep the watcher running, no ceremony. |
| ~3–4 | **moderate** | Be deliberate. Prefer to batch remaining items into one more push rather than chase each new bot comment. Tell the user you're a few rounds deep and roughly what each round has been worth. |
| ~5–7 | **strong** | Default to stopping. Do **not** kick off a fresh `/review`. Summarise everything across all rounds and recommend pausing for human input. Only start another round if there's a clear, high-value reason (a real CI break, a blocking human comment) — and state that reason explicitly before you do. |
| ~8–10 | **hard stop** | Do not start another round, whatever softening the productive rounds bought you. Stop the watcher (end the persistent `Monitor`). Report a summary of every round and all outstanding items to the user, and wait for explicit human direction before doing anything else. |

The round ranges are a guide, not a formula — a low-value round or two pushes you
into the next row early, and a productive streak lets you hold a row a little
longer (never past the hard stop).

At the **start of each round**, announce where you are — e.g.
`Round 4 — stop-here score: moderate (last round was low-value: only nits)`.
This keeps the pressure visible to you and the user, and makes the eventual stop
feel earned rather than abrupt.

The count is about *your own* automated laps. A fresh, explicit instruction from
the user ("keep going", "address the new comments") resets the pressure — start
a new count from there.

## Guidelines

- **Count your rounds and watch the stop-here score.** As you approach ~5
  rounds, default to stopping; by ~10, hard-stop, kill the watcher, and wait for
  the human. Low-value rounds ratchet the pressure up faster.
- **Never auto-act on a `-HUMAN` comment.** Report and ask.
- **Confirm before non-trivial edits.** Auto-fix is for the trivially safe only.
- **Don't silently apply bot suggestions** beyond the trivial bar above.
- **Use `read-comment.sh`** when the 300-char teaser cuts off the rationale.
- **Tuning the watcher:** `scripts/watch.sh` has two allowlists at the top —
  `BOTS` (review bots whose comments are actionable) and `IGNORE_LOGINS`
  (user-account automation to drop). Add new tools there.
- **For a one-off snapshot** with no ongoing watch, use `pr-comments` (or
  `gh api`) directly. This skill checks existing feedback once on start, then
  stays running for *new* activity.
