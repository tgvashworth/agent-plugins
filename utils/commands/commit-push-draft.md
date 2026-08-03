---
description: Commit, push, and open a draft PR (or update an existing one)
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
  - Bash(gh pr view:*)
  - Bash(gh pr edit:*)
  - Bash(gh issue:*)
  - Bash(gh search:*)
argument-hint: [guidance]
---

@${CLAUDE_PLUGIN_ROOT}/templates/common.md

@${CLAUDE_PLUGIN_ROOT}/templates/pr-body.md

# Task

Create a commit, push to remote, and open a draft pull request. If a pull
request is already open for this branch, update it in place instead of creating
a new one (leave its draft/ready state as it is).

## Context

Gather this information in parallel:

- Current status: `git status`
- Changes to commit: `git diff HEAD`
- All commits in branch: `git log --oneline origin/main..HEAD` (or appropriate base branch)
- Current branch: `git branch --show-current`
- Existing PR: check whether a pull request is already open for this branch with `gh pr view --json number,state,isDraft,url,title` (this returns an error if none exists — that just means you'll be creating a fresh draft PR). Note the number.
- Related issues: find them per "Finding related issues" above.

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
5. **Create or update the draft PR:**
   - **Write the title and body per "Writing a pull request" above** — the two-pass drafting method, the format, and the issue-linking rules all apply.
   - **Then create or update, based on the existing-PR check from Context:**
     - *No PR yet:* `gh pr create --draft --title "title" --body "description"`
     - *A PR already exists:* update it in place instead of creating a second one, and leave its draft/ready state alone: `gh pr edit <number> --title "title" --body "description"`
   - Return the PR URL

Handle each step carefully and verify success before proceeding to the next.
