---
name: what
description: >
  Re-explain your previous message in plain English, assuming no context and no
  jargon. Use when the user invokes /what, or says they don't understand what
  you just said and wants it rewritten more clearly.
argument-hint: "[what specifically was unclear]"
disable-model-invocation: true
---

# What

The reader did not understand your last message. Explain it again, from scratch.

## Rules

**Start over.** Do not repeat, quote, or defend the original wording — it
already failed. Write a fresh explanation of the same thing.

**Assume no context.** The reader has not followed the conversation, has not
read the code, and does not know what you were working on. Give them the
background each point needs to stand up on its own.

**No jargon.** Plain, ordinary words. If a technical term, internal name,
acronym, or file path is genuinely unavoidable, define it in a few words the
first time it appears. Otherwise, cut it.

**Lead with the bottom line.** First sentence says the thing that matters —
what happened, what you found, or what you need from them. Details after.

**Be short.** A few short paragraphs, or a handful of bullets. Short sentences.
If the original was long, this should be shorter.

**Don't do new work.** No tool calls, no fixes, no fresh investigation. This is
a rewrite of something you already said.

## Instructions

If `$ARGUMENTS` names a specific part that was unclear, focus the explanation
there. Otherwise re-explain the whole of your previous message.

Then write the explanation. Nothing else — no preamble apologising for the
first attempt, no "let me clarify", no offer to explain further.

## Cold read

Before sending, read it back as someone who just walked in. Anything that would
make them stop and think "wait, what's that?" needs fixing before they see it.
