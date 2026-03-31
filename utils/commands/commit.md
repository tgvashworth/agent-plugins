---
description: Create a git commit
allowed-tools:
  - Bash(git status:*)
  - Bash(git diff:*)
  - Bash(git log:*)
  - Bash(git add:*)
  - Bash(git commit:*)
  - Bash(git branch:*)
argument-hint: [guidance]
---

@${CLAUDE_PLUGIN_ROOT}/templates/common.md

# Task

Create a single git commit based on the current changes.

## Context

Gather this information in parallel:

- Current status: `git status`
- Changes to commit: `git diff HEAD`
- Recent commits for style: `git log --oneline -10`
- Current branch: `git branch --show-current`

## User Guidance

$1

## Steps

1. Review the git status and diff to understand what changed
2. Draft a commit message following the format in @${CLAUDE_PLUGIN_ROOT}/templates/common.md
3. If user provided guidance, incorporate it into the commit message
4. Stage relevant files with `git add`
5. Create the commit with `git commit -m "message"`
6. Check the exit code and handle pre-commit hooks per @${CLAUDE_PLUGIN_ROOT}/templates/common.md
7. Run `git status` after committing to verify success

Execute all git commands efficiently - gather info in parallel where possible, and combine operations where it makes sense.
