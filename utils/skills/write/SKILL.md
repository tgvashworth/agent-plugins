---
name: write
description: >
  Write or improve a substantial document through a structured process: fix the
  goals, outline the key points, map the audience, design the structure, draft
  it, then run two independent review passes (a cold-read for clarity and a
  style pass for LLM-isms and British English). Use when the user wants to
  write, draft, or improve a document, proposal, doc, RFC, README, announcement,
  design write-up, or report — anything longer-form where structure and audience
  matter. Not for commit messages or short replies.
argument-hint: "[topic, draft file path, or guidance]"
---

# Write

Produce a clear, well-structured document by working through the process below
in order. Each phase has one job and one output. Do not skip ahead — the early
phases (goals, audience, structure) are what make the writing land, and getting
them wrong wastes the whole draft.

Apply the writing guidelines throughout:
`${CLAUDE_PLUGIN_ROOT}/skills/write/references/writing-guidelines.md`

## Before you start

Work out what you're writing from `$ARGUMENTS` and the conversation:

- **A file path** → an existing draft to improve. Read it first.
- **A topic or guidance** → a new document to create.
- **Empty** → ask the user what they want to write and, briefly, why.

Also settle where the output goes: a file the user names, a new file, or inline
in the conversation. Ask only if it is unclear.

You may already know the goals and audience from the conversation. If so, state
your assumptions in Phase 1–3 rather than interrogating the user. Ask only when
you are genuinely blocked on something the user alone knows.

## Phase 1: Fix the goals

State what this writing is trying to achieve. What should the reader know,
believe, or do after reading it? What decision or action does it unblock?

Write this as one or two plain sentences. Keep it — you will check the finished
draft against it. If the document has several goals, rank them; the top goal
drives the structure.

## Phase 2: Outline the key points

Dump every point the writing needs to make, as bullets. Do not write prose yet.

Structure the bullets as an inverted pyramid:

- The most important, must-land points at the **top**.
- Supporting detail, caveats, and background towards the **bottom**.

If the reader only reads the top three bullets, they should still get the point.
This ordering is the raw material for the structure in Phase 4.

## Phase 3: Map the audience

Establish who reads this and what they bring to it. Be specific — "the platform
team's tech lead", not "technical people".

For the primary audience, and any important secondary audience, work out their:

- **Knowledge** — what they already know; what you must not re-explain, and what
  you must.
- **Understanding** — their mental model; where it differs from yours.
- **Objectives** — why they are reading; what they want from it; what would make
  them stop reading.

Consider which lens applies, as each wants something different:

- **Colleague** — shares context; wants the specifics and the reasoning.
- **Leadership** — short on time; wants the decision, the impact, and the ask
  up front.
- **Passer-by** — low context; wants to know quickly whether this is for them.
- **Non-technical reader** — wants the plain-English "what" and "so what",
  without the jargon.

Name the audience and lens you are writing for. If you are serving more than
one, say how you will handle the tension.

## Phase 4: Design the structure

Choose the structure that best lands the top points for this audience, given
Phase 3. Define it as a set of headings, each with a one-line purpose.

Example:

```
## What we're changing and why   — the ask and the reason, for a skimming lead
## How it works                  — the mechanism, for the colleague who'll build it
## Risks and rollback            — what could go wrong and the safety net
## Detail and background         — for the reader who wants to go deep
```

Front-load the structure the same way you front-loaded the bullets: the section
carrying the top goal comes first. Start headings at H2 and keep them
descriptive (see the guidelines).

### Checkpoint

Show the user a compact brief — goal, key points, audience and lens, and the
heading structure — before you write. This is the cheap moment to course-correct.
Wait for a nod or feedback, then continue. Skip the checkpoint only if the user
has told you to just write it.

## Phase 5: Write

Slot the Phase 2 bullets into the Phase 4 structure and write each section:

- Restructure the bullets into flowing prose — do not just paste the list.
- Front-load each section, paragraph, and sentence with its point.
- Add the colour that makes each point real: the example, the number, the
  reason, the consequence.
- Link the sections so the document reads as one argument, not a stack of notes.
- Follow the writing guidelines as you go — short common words, active voice,
  sentences ≤ ~25 words.

Produce the full draft. Save it to the agreed destination.

## Phase 6: Review — cold read

Hand the draft to a sub-agent for a fresh, standalone read. Launch an `Agent`
(`general-purpose`, synchronous) with the draft and the **audience description
only** — not the goals or the outline, so the reviewer comes to it as a reader
would.

Prompt it with:

> You are reviewing a document as a cold reader: you have the relevant
> background knowledge but you are coming to this text fresh. Here is who you
> are: [paste the Phase 3 audience and lens]. Here is the document: [paste the
> draft].
>
> Focus on one question: how can this improve as a standalone piece, in terms of
> clarity, simplicity, and utility? Where do you get lost, bored, or confused?
> What is missing that you need? What could be cut? Return specific, actionable
> feedback tied to sections or sentences — not general praise.

## Phase 7: Review — style and LLM-isms

Hand the same draft to a second sub-agent for a style pass. Launch it in the
**same message** as Phase 6 so both run at once. Give it the draft and the
guidelines file.

Prompt it with:

> You are a style editor. Review this document against the writing guidelines
> at `${CLAUDE_PLUGIN_ROOT}/skills/write/references/writing-guidelines.md` —
> read that file first. Here is the document: [paste the draft].
>
> Flag every LLM-ism and style problem with a specific, quotable fix:
> - False antithesis ("It's not X, it's Y", "not only… but also").
> - Staccato triads and rule-of-three padding.
> - Em-dash overuse, filler, hedging, and inflated verbs.
> - Americanisms — the document must use British English.
> - Any breach of the guidelines (passive voice, long sentences, weak titles,
>   buried points).
>
> Return a list of specific suggestions: quote the offending text and give the
> replacement, so the top agent can apply each one directly.

## Phase 8: Implement and wrap up

Apply the feedback from both reviews to the draft. Where the two conflict, or
where a suggestion fights the goal, use your judgement and note the call. Save
the final version.

Then give the user a short wrap-up:

- **What it achieves, and for whom** — the goal and the audience it serves.
- **How** — the structure you chose and how it supports the goal.
- **What changed** in review, if anything notable.

Check the final draft against the Phase 1 goal one last time before you call it
done.
