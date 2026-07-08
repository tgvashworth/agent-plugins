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

Pick the instruction file whose **scope matches the instruction**, not just the one at the
project root. A repo can have several (`AGENTS.md` / `CLAUDE.md` at the root and inside
subdirectories, packages, or `.claude/`).

1. **Enumerate all instruction files** in the repo — search for `AGENTS.md` and `CLAUDE.md`
   at the root and in every subdirectory (also check inside `.claude/`).
2. **Decide the instruction's scope.** Is it a project-wide convention, or is it specific to
   one component/package/subdirectory? Judge from what the instruction is about and where the
   relevant code lives (the files under discussion in the conversation are a strong signal).
3. **Match scope to file:**
   - Subdirectory-specific → the instruction file **in that subdirectory**, or the nearest
     ancestor directory that has one.
   - Project-wide → the **root** instruction file.
4. **At the chosen level, prefer `AGENTS.md` over `CLAUDE.md`** when both exist. If only one
   exists, use it.

If the appropriate directory has no instruction file, propose creating one there and wait for
the user to confirm before creating it. Name it to match what the rest of the repo already
uses (`AGENTS.md` if other directories use `AGENTS.md`, otherwise `CLAUDE.md`); if the repo
has none at all, default to `CLAUDE.md`.

If the correct scope is ambiguous (e.g. the instruction could reasonably go in a package file
or the root), ask the user which file to use rather than guessing.

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
