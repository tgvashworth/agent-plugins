---
description: Commit, push, and open a draft PR
allowed-tools:
  - Bash(git status:*)
  - Bash(git diff:*)
  - Bash(git log:*)
  - Bash(git add:*)
  - Bash(git commit:*)
  - Bash(git branch:*)
  - Bash(git checkout:*)
  - Bash(git push:*)
  - Bash(gh pr create:*)
argument-hint: [guidance]
---

@${CLAUDE_PLUGIN_ROOT}/templates/common.md

# Task

Create a commit, push to remote, and open a draft pull request.

## Context

Gather this information in parallel:

- Current status: `git status`
- Changes to commit: `git diff HEAD`
- All commits in branch: `git log --oneline origin/main..HEAD` (or appropriate base branch)
- Current branch: `git branch --show-current`
- Related issues: Check if the branch name contains an issue number (e.g. `feature/123-foo` → `#123`). Also check user guidance for issue references. If found, run `gh issue view <number>` to confirm it exists.

## User Guidance

$1

## Steps

1. **Create branch if needed**: If on main/master, create a new branch first
2. **Review changes**: Understand what will be committed
3. **Create commit**:
   - Draft commit message per @${CLAUDE_PLUGIN_ROOT}/templates/common.md (incorporating user guidance if provided)
   - Stage files with `git add`
   - Commit with `git commit -m "message"`
   - Handle pre-commit hooks per @${CLAUDE_PLUGIN_ROOT}/templates/common.md
   - Verify with `git status`
4. **Push to remote**:
   - Push branch: `git push -u origin <branch-name>`
   - Verify push succeeded
5. **Create draft PR**:
   - Draft PR description based on ALL commits in the branch (not just the latest)
   - PR format: summary (1-3 bullets), test plan checklist, next steps if relevant
   - **Link to issues**: If a related issue was found in context, include `Closes #<number>` at the end of the PR body. If multiple issues are relevant, list each on its own line (e.g. `Closes #123`, `Closes #456`).
   - Use: `gh pr create --draft --title "title" --body "description"`
   - Return the PR URL

Handle each step carefully and verify success before proceeding to the next.
