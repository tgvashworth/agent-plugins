---
name: tourguide
description: |
  Walk through code changes or a plan in a logical, grouped sequence. Instead
  of showing a raw diff or dumping a plan all at once, organise related pieces
  together and present them one group at a time, pausing for feedback after
  each. Use this skill when the user asks you to explain, walk through, tour,
  or review a set of changes — whether that's uncommitted work, a branch, a
  commit range, or a PR diff. Also use it when someone says "what changed",
  "show me the changes", or "catch me up on this branch", even if they don't
  say "tour". Use it for plans too — when someone says "walk me through the
  plan", "talk me through the approach", or "explain what you're going to do".
argument-hint: "[commit range, branch, PR, plan, or omit for uncommitted changes]"
---

# Tourguide

Walk through a set of changes or a plan in a logical order, grouping related
pieces together so the reader builds understanding incrementally.

## Step 1: Gather the material

Figure out what to tour based on the argument or context:

| Input | What to gather |
|-------|---------------|
| Nothing / no args | Uncommitted changes (`git diff` + `git diff --cached`) |
| A branch name | `git diff main...<branch>` (or the appropriate base) |
| A commit range | `git diff <range>` |
| A PR number/URL | Fetch the PR diff via `gh pr diff` |
| A plan (file or conversation) | Read the plan content |

Read everything so you have the complete picture before presenting anything.

## Step 2: Group related pieces

Organise into logical groups. For code changes, a group is a set of changes that
make sense to explain together — they might touch the same feature, fix the same
bug, or refactor the same concept. A single file might be split across groups if
it contains unrelated changes; multiple files might be in one group if they're
part of the same logical change.

For plans, group by theme or phase — e.g., "data model changes", "API
endpoints", "migration strategy". Order groups so the reader understands
dependencies before the things that depend on them.

You can create as many groups as needed.If there are very few changes, one group is fine. Order
groups so earlier ones provide context for later ones (e.g., data model changes
before the UI that uses them, config before the code that reads it).

Give each group a short, descriptive title.

## Step 3: Present one group at a time

For each group:

1. State the group title and a one-sentence summary of what this group covers
2. Show the relevant content (code snippets for diffs, key details for plans)
3. Briefly explain why and how things connect, if not obvious
4. Ask if the reader has questions or feedback before moving on
5. Show a compact progress indicator (e.g., "2 of 5 • Next: <next group title>")

Keep explanations concise. Let the code speak for itself where it can. Focus on
the "why" more than the "what" — the diff already shows the what.

## Step 4: Wrap up

After all groups, give a brief summary of the full change set in a sentence or
two. If the reader gave feedback during the tour, summarise any action items.
