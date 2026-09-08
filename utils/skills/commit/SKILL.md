---
name: commit
description: >
  Create a single git commit from the current changes, with a message in the
  repository's commit style. Use when the user invokes /commit, says "commit
  this", or asks for a commit without a push or pull request.
argument-hint: "[guidance]"
allowed-tools: "Bash(git status:*), Bash(git diff:*), Bash(git log:*), Bash(git add:*), Bash(git commit:*), Bash(git branch:*)"
---

# Commit

Create a single git commit based on the current changes.

Read the shared [commit guidance](../../templates/common.md) first. It defines
the message format, where house style comes from, how to refer to files, and
how to handle pre-commit hooks.

## Context

Gather this information in parallel:

- Current status: `git status`
- Changes to commit: `git diff HEAD`
- House style: per "Where house style comes from" in the commit guidance. Check
  for a style file first, and sample `git log --oneline -20` only if there is
  none.
- Current branch: `git branch --show-current`

## User guidance

If the user supplied guidance with the request (a focus, a phrase to use, a
change to leave out), it shapes the message and the file set. Otherwise infer
both from the diff.

## Steps

1. Review the status and diff to understand what changed.
2. Draft a commit message following the format in the commit guidance,
   incorporating any user guidance.
3. Stage only the files that belong to this change with `git add`. Leave
   unrelated working-tree changes alone.
4. Create the commit with `git commit -m "message"`.
5. Check the exit code and handle pre-commit hooks per the commit guidance.
6. Run `git status` after committing to verify success.

Do not create an empty commit. Do not push. Gather information in parallel
where possible and combine commands where it makes sense.
