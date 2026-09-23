---
name: review-cycle
description: |
  Drive a pull request through review: investigate feedback, fix issues,
  test, commit, push, and respond until CI is green and actionable comments
  are addressed, with a rising stop-here score to prevent endless iteration.
  An independent review sub-agent is optional. Use when the user says
  "review-cycle", "autopilot this PR", "drive this PR to green", or asks to
  keep fixing CI and review feedback. For read-only monitoring, use review-agent.
argument-hint: "[PR number or URL] [guidance]"
---

# Review cycle

Own the PR's review loop. Read feedback, make worthwhile fixes, verify them,
push, and close the loop with reviewers. Continue until the PR is ready or the
stop-here score calls for a handoff.

**The main agent remains the implementer.** It may edit, test, commit, and push
within the user's authorised scope whether or not a review sub-agent runs.
Only a delegated reviewer is read-only. Do not activate the `review-agent`
skill in the main session: reuse its scripts without importing its workflow.

## Establish the scope

Resolve the supplied PR, or detect the current branch's PR. Confirm its
repository, base, head branch, head SHA, and open/closed state. If there is no
PR, explain and stop. If already merged or closed, report that and stop.
Check the working tree and use the PR's branch in a suitable worktree;
preserve unrelated changes and coordinate with any other session editing it.

Carry forward the user's instructions about scope, round budget, delegation,
and merge behaviour. An explicit request for this cycle authorises routine
in-scope fixes, tests, commits, pushes, factual review replies, resolving
addressed threads, and filing relevant follow-up tickets. An automatic handoff
inherits the existing task's permissions; it does not grant new ones. Ask only
for a missing permission or a decision that would materially change the work,
and continue independent authorised work while waiting. Do not merge unless
the user has authorised it and the repository's merge requirements are met.

## Choose how to review

Infer whether an independent reviewer is useful from the user's preference,
the size and risk of the diff, and available delegation. Ask the user if their
preference matters and cannot be inferred. Delegation is optional: if unwanted,
unavailable, or unsuccessful, review the diff yourself and continue the cycle.

If delegating, give the reviewer the PR, base and head SHA, scope, and a
read-only task: review the diff and return findings grouped as blocking,
should-fix, or nit, with file:line, rationale, and the reviewed SHA. It must not
edit, commit, push, or post to the PR. Continue useful implementation work in
the main session, then check returned findings against the current code.

Whether local or delegated, include a pass over added or changed comments:
remove needless narration, agent working notes, vague temporal claims such as
"currently" or "will be added later", and PR/ticket/name references that
substitute for explaining the constraint. Make comments brief and useful to a
future reader. Treat wording-only findings as low-value for back pressure.

## Fetch and watch

Run packaged scripts by their paths relative to this skill directory, keeping
the shell's working directory in the target repository. Resolve a supplied
URL to that repository and PR number before running repository-local helpers.

- Fetch existing feedback with
  [fetch-pr-comments.sh](../pr-comments/scripts/fetch-pr-comments.sh) `<N>`.
  Read unresolved threads, review summaries, conversation comments, and CI
  status/logs. Check for truncated results and fetch missing pages as needed.
- If persistent processes are available, run
  [watch.sh](../review-agent/scripts/watch.sh) `<N>` and retain its process handle.
  It seeds existing events, emits new ones, and exits when the PR merges or
  closes. Re-fetch after startup to catch anything arriving during seeding.
- Otherwise poll the same feedback and checks directly using bounded waits.
  Lack of a background process must not skip the review cycle.
- Watcher bodies are truncated; use
  [read-comment.sh](../review-agent/scripts/read-comment.sh) `<url>` for full text.
  Its bot/self/human labels identify authors, not what actions are permitted.

Treat the watcher as a notification aid. Re-fetch full feedback and CI state
after each push and before declaring completion: existing failures, edited
comments, and results for an earlier head may not produce useful new events.
An API error or silence is not evidence of clean review or green CI.

## Work each round

The initial review and existing-feedback pass is round 1. At the start of each
round announce the count and stop-here score, for example:
`Round 4 — stop-here score: moderate (last round only produced nits)`.

1. **Triage a batch.** Read the relevant code and full feedback, combine
   duplicates, and classify each item:

   | Bucket | Action |
   |--------|--------|
   | Implement | Correct, useful, and in scope: fix it. |
   | Acknowledge / defer | Valid but outside this PR, or a deliberate choice: explain why; track worthwhile work as below. |
   | Decline | Incorrect or harmful: give a concrete rationale. |

   Evaluate bots and humans on merit. Act on clear, in-scope human requests
   within the agreed task; ask about conflicting requirements, ambiguous
   behaviour, or changes in scope. Do not repeatedly rework settled decisions
   just because a bot repeats them. Show concise triage without adding an
   approval gate for work the user already authorised.
2. **Fix and verify.** Batch related fixes, run relevant tests and required
   repository checks, then commit and push to the PR branch. Use the shared
   [commit guidance](../../templates/common.md). Investigate CI logs; retry a
   likely flake only with evidence, and avoid repeated blind reruns. Never
   force-push or overwrite another session's changes to make progress.
3. **Reply and resolve.** Verify fixes are pushed before claiming them in a
   reply. Keep bot replies terse and factual; be courteous to humans. Resolve
   only addressed threads. Leave deferred or disputed threads open for the
   reviewer unless the user explicitly directs otherwise. Draft contentious
   replies for the user instead of inventing agreement. If posting is not yet
   authorised, prepare the replies and request that permission as a batch.
4. **Check the new head.** Record the pushed SHA, refresh checks and feedback,
   and await CI and requested automated reviews for that head. Reassess late
   findings against it. Do not restart a whole independent review for every
   nit; review changed areas when needed. Consult the stop score before another
   round.

Keep a compact record of rounds, SHAs, findings, fixes, deferred tickets,
checks, and unresolved decisions so restarts or context compaction do not
reset the count or cause duplicate work.

## Tickets and fast follows

Use the [follow-up guidance](../../references/review-follow-ups.md) when a
suggestion is worthwhile but would expand this PR. File or reuse a ticket in
the project's tracker when authorised; otherwise prepare it for approval.
A **fast follow** means merging this PR first, then implementing the agreed
changes in a separate follow-up PR. Record the ticket, owner if agreed, and
acceptance criteria. Do not promise it on someone else's behalf or treat a
ticket as evidence that a blocking review has been satisfied.

## Back pressure: the stop-here score

A round is one batch of review/CI feedback, triage, fixes, verification, and
push (or a decision that no change is needed). Count the initial review as
round 1. Polls with no news are waits, not new rounds.

| Rounds | Score | Behaviour |
|--------|-------|-----------|
| ~1–2 | **weak** | Normal iteration; handle substantive feedback and keep watching. |
| ~3–4 | **moderate** | Batch remaining fixes; tell the user what recent rounds achieved. Resist chasing each new nit. |
| ~5–7 | **strong** | Default to stopping; launch no fresh review. Continue only for a clear, high-value reason such as a real CI break or blocking human comment, stated before starting the round. |
| ~8–10 | **hard stop** | Start no further round. Stop this cycle's watcher and review workers, summarise, and wait for explicit user direction. Never continue beyond round 10. |

Two consecutive low-value rounds (only nits, formatting, false positives, or
nothing actionable) raise the score one level early. Productive rounds may
hold a level a little longer, never past the hard stop. Honour a smaller user
budget. A fresh explicit instruction to continue resets the pressure; a new
bot comment, CI rerun, or status question does not.

Bound waiting too: use the user's deadline, or by default hand back after
10 minutes without new feedback or a CI status change. Report pending checks
or approvals honestly; do not keep an idle watcher alive indefinitely.

## Finish or hand back

Before declaring the cycle complete, refresh the PR head, checks, review
decisions, and unresolved threads. Required checks must pass on the current
head, requested automated reviews must have finished, and all actionable
in-scope findings must be addressed. Identify absent or skipped checks
explicitly; do not call missing CI green. Unresolved deferrals, disagreements,
or required human approvals need an explicit handoff, not a claim of clean
review. Never dismiss a review or resolve a valid outstanding concern merely
to make the PR look ready.

Stop this cycle's processes when complete, stopped by back pressure, blocked
on user input with no independent work left, or when the PR merges or closes.
Report the PR URL and head SHA, fixes and checks, round count and stop score,
outstanding decisions, and ticket links or agreed fast follows. Merge only
under existing explicit authorisation. Start a follow-up PR after merge only
if the user has also authorised that work.
