---
name: remember
description: >
  Append a convention, fact, or instruction to the project's shared AGENTS.md
  or CLAUDE.md so it is committed to the repo and shared with the team.
  Use when the user wants to persist project knowledge beyond auto memory,
  when they say "remember this", or when a significant convention or
  correction comes up that should be captured for future sessions.
argument-hint: "[instruction or fact]"
---

# Remember

Persist a convention, fact, or instruction to the project's committed instruction files
so learnings are shared with the whole team via source control.

## Step 1: Parse the input

If `$ARGUMENTS` is non-empty, use it as the raw instruction to persist.

If `$ARGUMENTS` is empty, review the current conversation and infer what should be remembered.
Look for:

- Corrections the user made ("no, we always do X", "that's wrong, use Y instead")
- Conventions or patterns established during the session
- Debugging discoveries that would save time in future sessions
- Architectural decisions or constraints that came up

Summarise what you've inferred as a concise instruction and **present it to the user for
confirmation before writing**. Do not write anything until the user approves the wording.

If `$ARGUMENTS` is verbose, tighten the wording while preserving meaning. Confirm the
tightened version with the user before writing. If the user rejects the tightened wording,
offer to use the original verbatim or ask for an alternative phrasing.

## Step 2: Determine the target file

Find the closest relevant instruction file in the project. Search from the project root for
files like `AGENTS.md`, `CLAUDE.md`, or equivalents inside `.claude/`. Prefer `AGENTS.md`
over `CLAUDE.md` when both exist at the same level.

If no instruction file exists, propose creating `CLAUDE.md` at the project root and wait
for the user to confirm before creating it.

## Step 3: Check for duplicates or conflicts

Read the target file. Before appending, check whether the instruction duplicates or
contradicts something already present. If it does, flag it and ask the user how to proceed
rather than writing a conflicting entry.

## Step 4: Append the instruction

- Identify the file's section headings.
- Append the new instruction as a bullet point (`- ...`) under the **most relevant existing
  section heading**.
- If no section is a good fit, append under a `## Conventions` section, creating it at the
  end of the file if absent.
- **Do not rewrite, reorganise, or reformat** existing content.

## Step 5: Confirm

After writing, output:

- The file that was modified (relative path).
- The exact line(s) added.
- A reminder that the change should be committed to share it with the team.

If the target file exceeds 200 lines after the addition, warn the user and suggest
refactoring into smaller files.

## Constraints

- Never modify `CLAUDE.local.md` — that's personal, not shared.
- Never write to auto memory (`~/.claude/projects/*/memory/`). The whole point is
  repo-committed, shared knowledge.
- Never write to `.claude/rules/`.
- Never delete or reorder existing content in the target file.
