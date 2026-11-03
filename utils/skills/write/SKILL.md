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
in order. Each phase has one job and one output. Set the goals, audience, and
structure before drafting to avoid rewriting a document that misses its purpose.

Apply the writing guidelines throughout: `references/writing-guidelines.md`

## Before you start

Work out what you're writing from the user's request and the conversation:

- **A file path** → an existing draft to improve. Read it first.
- **A topic or guidance** → a new document to create.
- **Empty** → ask the user what they want to write and, briefly, why.

Also settle where to put the output: a named file, a new file, or inline
in the conversation. Ask only if it is unclear.

You may already know the goals and audience from the conversation. If so, state
your assumptions in Phase 1–3 rather than interrogating the user. Ask only when
you are blocked.

## Phase 1: Fix the goals

State what this writing is trying to achieve. What should the reader know,
believe, or do after reading it? What decision or action does it unblock?

Write this as one or two plain sentences. Later you will check the finished
draft against it. If the document has several goals, rank them.

For example:

- Help the team assess the design proposal and suggest changes before implementation.
- Get leadership approval for the project budget.
- Tell customers how the release affects their work.
- Explain the main findings to readers unfamiliar with the subject.
- Help support staff answer questions about the changes.
- Help prospective customers recognise the organisation and understand what it offers.
- Prompt LinkedIn readers to share how they have handled the problem.

## Phase 2: Outline the key points

Dump every point the writing needs to make, as bullets. Do not write prose yet.

Structure the bullets as an inverted pyramid:

- The most important, must-land points at the **top**.
- Background, supporting detail, caveats, and examples towards the **bottom**.

If the reader only reads the top three bullets, they should still get the point.

This ordering is the raw material for the structure in Phase 4.

## Phase 3: Map the audience

Establish who reads this and what they bring to it. Use specific audience
descriptions. For example:

- A platform team's tech lead, who knows the system well but has limited time.
- A product manager, who understands the project but needs technical concepts explained.
- A passer-by, who has low context and wants to know quickly whether this is for them.
- A new team member, who has some context but is still learning the ropes.
- An external stakeholder, who has limited context and is primarily interested in the impact on their area.
- LinkedIn readers, who are scrolling through their feed and need the main point quickly.

For the primary audience, and any important secondary audience, work out their:

- **Knowledge** — what they already know; what you must not re-explain, and what
  needs to be explained.
- **Understanding** — their mental model; where it differs from the assumptions
  in the conversation.
- **Objectives** — why they are reading; what they want from it; what would make
  them stop reading.

Consider which lens applies, as each wants something different:

- **Colleague** — shares context; wants the specifics and the reasoning.
- **Leadership** — short on time; wants the decision, the impact, and the ask
  up front.
- **Passer-by** — low context; wants to know quickly whether this is for them.
- **Non-technical reader** — wants the plain-English "what" and "so what",
  without the jargon.
- **External stakeholder** — has limited context; wants to know the impact on their area.
- **Public audience** — has low context; wants the high-level impact and key points quickly.
- **Internal stakeholder** — has some context; wants to know the impact on their area.

Name the audience and lens you are writing for.

## Phase 4: Design the structure

Choose the structure that best presents the top points for this audience, given
Phase 3. For a document, define headings with a one-line purpose each. For a
short post or email, outline the opening, main points, and ending.

Example:

```
## What we're changing and why   — the ask and the reason, for a skimming lead
## How it works                  — the mechanism, for the colleague who'll build it
## Risks and rollback            — what could go wrong and the safety net
## Detail and background         — for the reader who wants to go deep
```

Front-load the structure the same way you front-loaded the bullets: the section
carrying the top goal comes first. Where the format uses headings, start them
at H2 and keep them descriptive (see the guidelines).

Adapt the structure to where the audience will encounter the content. For example:

- **LinkedIn** — put the main point in the opening lines and keep paragraphs short.
- **Email** — make the purpose and any requested action clear in the subject and opening.
- **Internal documentation** — use descriptive headings so readers can find specific information.
- **Blog post** — give enough context for readers arriving from search or social media to follow the argument.
- **Presentation** — give each slide a clear point and use visuals that help explain it.

### Checkpoint

Show the user a compact brief — goal, key points, audience and lens, and the
proposed structure — before you write. Resolve any changes before drafting.
Wait for confirmation or feedback, then continue. Skip the checkpoint only if the user
has told you to just write it.

## Phase 5: Write

Slot the Phase 2 bullets into the Phase 4 structure and write each part:

- Restructure the bullets into flowing prose — do not just paste the list.
- Front-load each section, paragraph, and sentence with its point.
- Add what makes each point real: the example, the number, the reason, the
  consequence. Not metaphor. When a literal phrase is available, use it.
- Link the sections so the document reads as one argument, not a stack of notes.
- Follow the writing guidelines as you go — short common words, active voice,
  sentences ≤ ~25 words.

Produce the full draft. Save it to the agreed destination.

## Phase 6: Review — cold read

Hand the draft to an independent worker for a fresh, standalone read when the
host supports delegation. Otherwise perform a separate cold-read pass yourself.
Provide the draft and the **audience description only** — not the goals or the
outline, so the reviewer comes to it as a reader would.

Prompt it with:

> You are reviewing a document as a cold reader: you have the relevant
> background knowledge but you are coming to this text fresh. Here is who you
> are: [paste the Phase 3 audience and lens]. Here is the document:
>
> [paste the draft].
>
> Focus on this question: how can this improve as a standalone piece, in terms of
> clarity, simplicity, and utility? Where do you get lost, bored, or confused?
> What is missing that you need? What could be cut? Return specific, actionable
> feedback tied to sections or sentences — not general praise.

## Phase 7: Review — style and LLM-isms

Hand the same draft to a second independent worker for a style pass. Launch it
in parallel with Phase 6 when the host supports that; otherwise perform the
style pass separately. Give it the draft and the guidelines file.

Prompt it with:

> You are a style editor. Review this document against the writing guidelines
> at `references/writing-guidelines.md` —
> read that file first. Here is the document: [paste the draft].
>
> Flag every LLM-ism and style problem with a specific, quotable fix:
>
> - Mannered prose: metaphor or flourish where a literal phrase exists ("a
>   dial worth turning" for "a parameter worth varying"). Give the literal
>   phrase.
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
