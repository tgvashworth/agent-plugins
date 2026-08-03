---
name: what
description: >
  Re-explain your previous message in plain English, reconnecting it to the
  conversation the reader has only lightly followed. Use when the user invokes
  /what, or says they don't understand what you just said and wants it
  rewritten more clearly.
argument-hint: "[what specifically was unclear]"
disable-model-invocation: true
---

# What

The reader did not understand your last message. Explain it again, from scratch.

## Rules

**Start over.** Do not repeat, quote, or defend the original wording — it
already failed. Write a fresh explanation of the same thing.

**Reconnect the thread.** The reader has been following only lightly, or has
lost the connection between the conversation so far and your latest message.
They know the broad goal; they don't know how this message relates to it.
Briefly re-anchor — what you were doing and why this message matters to it —
then explain the point itself.

**Plain words, judged against the reader.** Prefer ordinary language. For
technical terms, internal names, and acronyms, make a judgement call: assume
the reader knows anything they've used in their own messages, and reasonable
professional background beyond this session. Define — in a few words, first
use — only the things *you* introduced: names, concepts, or shorthand from
your own work that they never engaged with. Don't burn words explaining what
they obviously know.

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
