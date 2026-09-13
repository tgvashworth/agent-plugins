---
name: quiz
description: >
  Test the user's understanding of a change or pull request with a fast,
  adaptive, evidence-backed quiz tied to the actual diff. Use when the user
  asks to quiz them, test their understanding, check that they understand
  their change, or find gaps in their mental model of code they just changed.
argument-hint: "[PR, branch, commit range, or omit] [--focus design|conventions|behaviour] [--deep]"
---

# Quiz

Run a five-minute understanding check on code the user just changed. Find and
close the few knowledge gaps that could cause a bug or weak review. This is not
trivia or a code review.

## Prepare

Parse `--deep` and `--focus <design|conventions|behaviour>`, then remove them
before resolving the target:

| Target | Inspect |
|---|---|
| PR | Its diff and head revision |
| Branch | Diff from its merge base with the default branch |
| Commit or range | That diff or range |
| Omitted | The conversation's change; otherwise local changes and branch commits relative to the default branch |

Inspect the complete diff, relevant surrounding code, tests, documentation, PR
discussion, and history silently. Prefer an explicit target. Otherwise check
that the conversation, branch commits, and local diff form one coherent change.
Prefer the conversation-identified local change when it maps cleanly to the
diff; otherwise ask one brief scope question rather than combining unrelated
work. Name the inferred scope before the first quiz question. If there is no
concrete change, ask for one and stop.

Map the touched modules through three lenses:

- **Design:** boundaries, data flow, state ownership, and structural rationale.
- **Conventions:** repository-specific contracts and implementation patterns.
- **Behaviour:** externally visible outcomes, edge cases, and failures.

Find the nearest current sources that govern those modules: applicable
`AGENTS.md` or `CLAUDE.md` files, feature docs, ADRs, schemas, configuration,
interfaces, and focused tests. Confirm that each source covers the changed code.
`--focus` restricts primary questions to one lens, but still disclose an
untested critical invariant outside it. Do not add a topic-selection round trip.

Read and maintain the private, module-scoped learning record as described in
[references/learning-ledger.md](references/learning-ledger.md). Skip a theme
already demonstrated in the same module unless this use is materially harder;
revisit themes that needed help or remained unresolved.

## Choose the questions

Target three primary questions by default, adding a fourth only for an
important remaining gap while the check is still near five minutes. `--deep`
allows up to five. Stop early rather than pad a small change with trivia.

Rank candidate gaps by the likely cost of a wrong model:

1. Authorization, identity, security, data-loss, and irreversible-effect
   invariants that the code does not announce.
2. The change's central rationale when a current source records it.
3. Small code with large effects, especially concurrency, retry, state, and
   failure behaviour.
4. Boundaries or user-visible behaviour whose misunderstanding could cause a
   defect.
5. Conventions specific to the touched module.

Prefer higher-impact candidates within a tier. Reject anything generic, obvious
from the diff, based only on undocumented intent, or whose answer would not
change what you probe, explain, or record. A high-risk gap counts as covered
only when a primary question targets it. If one will not fit, disclose it in
the close.

If the ledger shows this is the user's first encounter with an applicable
written rule, a question may test how that rule shapes a changed line. Never
ask for document recall without connecting it to this change.

Before asking, establish for every selected topic:

- the exact changed line or decision;
- a definitive answer and the causal explanation expected;
- current evidence that proves it; and
- how a correct, partial, or wrong answer will affect the remaining check.

Read [references/verification.md](references/verification.md) before choosing
pointers or proof.

## Run the check

Ask one question, then end the turn. Never batch questions or use a constrained
picker. Include a short question number and a clickable pointer to the exact
code unless explicitly testing recall. Do not reveal the answer's shape or
count. Prefer “How does X work?” and “Why does Y do Z?” over fact lists.

Mix open questions about mechanism or rationale with inline behaviour choices.
For choices, offer two or three plausible models, signal none as correct, and
ask which applies and why. Every distractor must be false for the exact path in
question. Do not use choices more than twice consecutively. Accept free text.

Judge the expressed model, not keywords:

- **Demonstrated:** correct conclusion and relevant cause without rescue.
- **Prompted:** guessed, missing its cause, or completed through the follow-up;
  an unexplained correct choice belongs here.
- **Unresolved:** wrong, unknown, or still unclear after the follow-up.
- **Unassessed:** conflicting evidence or a code/documentation problem means
  there is no definitive answer.

A demonstrated answer gets a brief acknowledgement, confirming evidence, a
silent ledger update, and the next question if one remains. An answer that is
partial, hedged, wrong, or otherwise prompted—including an unexplained correct
choice—gets one short follow-up about the missing mechanism. Then resolve it
briefly with evidence and move on; save broader teaching for the close. For
prompted or unresolved topics, state the missing or mistaken causal link
without quoting the user verbatim. Rerank or replace the remaining questions
after every answer so they target the most important gaps now visible. After
asking the next question, end the turn.

If an answer reveals a real code or documentation problem, say so once and do
not grade against an unproven assumption; mark the topic unassessed. Do not turn
the check into a review. If the user stops, close gracefully.

## Close

Give a compact summary that:

- labels each topic demonstrated, prompted, unresolved, or unassessed;
- corrects prompted or unresolved models with direct evidence;
- names any important gap that exceeded the question budget, with a code
  pointer, and records it as unresolved;
- links governing sources and the quickest confirming code, test, dashboard,
  or repro; and
- states what the user now understands about the affected system.

Mention numerical consequences only when current evidence supports them. Do
not list deliberately skipped minor details or assign a score unless asked.
Link to or print the learning-ledger path.
