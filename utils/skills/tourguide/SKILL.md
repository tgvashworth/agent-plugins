---
name: tourguide
description: |
  Walk through code changes or a plan in a logical, grouped sequence — one
  group at a time, stopping after each to wait for the user to say "next" (or
  give feedback) before continuing. Instead of showing a raw diff or dumping a
  plan all at once, organise related pieces together and present them
  incrementally. Use this skill when the user asks you to explain, walk
  through, tour, or review a set of changes — whether that's uncommitted work,
  a branch, a commit range, or a PR diff. Also use it when someone says "what
  changed", "show me the changes", or "catch me up on this branch", even if
  they don't say "tour". Use it for plans too — when someone says "walk me
  through the plan", "talk me through the approach", or "explain what you're
  going to do".
argument-hint: "[commit range, branch, PR, plan, or omit for uncommitted changes]"
---

# Tourguide

Walk the reader through a set of changes or a plan, one group at a time, so
they can absorb and react to each piece before seeing the next. **The whole
point of this skill is pacing — if you dump everything in one response, you
have failed the skill.**

## The core rhythm

```
[Step 1] Gather all the material silently
[Step 2] Group it and plan the tour silently
[Step 3] Present the outline → STOP, wait for user
[Step 4] Present group 1 → STOP, wait for user
         Present group 2 → STOP, wait for user
         ... and so on, one group per turn
[Step 5] Wrap up after the final group
```

Each "STOP, wait for user" means end your turn. Do not continue to the next
group until the user replies — typically with "next", "continue", "ok", a
question, or feedback. If they ask a question, answer it and then wait again
before moving on.

This pacing is not optional. The reader is learning. They need time between
each group to read, think, and push back if something's off. Rushing defeats
the purpose.

## Step 1: Gather the material (silent)

Figure out what to tour based on the argument or context:

| Input | What to gather |
|-------|---------------|
| Nothing / no args | Uncommitted changes (`git diff` + `git diff --cached`) |
| A branch name | `git diff main...<branch>` (or the appropriate base) |
| A commit range | `git diff <range>` |
| A PR number/URL | Fetch the PR diff via `gh pr diff` |
| A plan (file or conversation) | Read the plan content |

Read everything so you have the complete picture before presenting anything.
Do this silently — don't narrate the gathering to the user.

## Step 2: Group related pieces (silent)

Organise into logical groups. For code changes, a group is a set of changes
that make sense to explain together — they might touch the same feature, fix
the same bug, or refactor the same concept. A single file might be split
across groups if it contains unrelated changes; multiple files might be in one
group if they're part of the same logical change.

For plans, group by theme or phase — e.g., "data model changes", "API
endpoints", "migration strategy". Order groups so the reader understands
dependencies before the things that depend on them.

Create as many groups as needed. If there are very few changes, one group is
fine.

Give each group a short, descriptive title.

## Step 3: Present the outline, then STOP

Tell the reader what the tour will cover before diving in. Something like:

> I'll walk through this in 4 groups:
> 1. Data model changes
> 2. New API endpoints
> 3. Frontend updates
> 4. Migration and rollout
>
> Say "next" when you're ready for the first one.

Then **end your turn**. Do not proceed to group 1 in the same response.

## Step 4: Present one group per turn

When the user says "next" (or equivalent), present **only the next group**:

1. Group title and a one-sentence summary of what it covers
2. The relevant content (code snippets for diffs, key details for plans)
3. A brief note on why and how things connect, if not obvious
4. A compact progress indicator (e.g., "2 of 4 • Next: Frontend updates")
5. A short prompt inviting "next" or feedback

Then **end your turn**. Wait for the reader to reply.

If the reader asks a question, answer it in your next response but do not
advance to the next group. Wait for them to signal they're ready.

Keep each group's content concise. Let the code speak for itself where it can.
Focus on the "why" more than the "what" — the diff already shows the what.

## Step 5: Wrap up

After presenting the final group, give a brief summary of the full change set
in a sentence or two. If the reader gave feedback during the tour, list any
action items.

## What "done right" looks like

A good tour is a conversation, not a monologue. Over the course of the tour,
the reader should send several short messages ("next", "next", "wait, why
that?", "ok go on"). If you finish the tour in one of your responses, the
skill didn't work.
