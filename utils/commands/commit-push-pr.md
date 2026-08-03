---
description: Commit, push, and open a PR (or update and ready an existing draft)
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
  - Bash(gh pr ready:*)
  - Bash(gh issue:*)
  - Bash(gh search:*)
argument-hint: [guidance]
---

@${CLAUDE_PLUGIN_ROOT}/templates/common.md

@${CLAUDE_PLUGIN_ROOT}/templates/pr-body.md

# Task

Create a commit, push to remote, and open a pull request. If a pull request is
already open for this branch, update it instead of creating a new one — and if
it is a draft, mark it ready for review.

## Context

Gather this information in parallel:

- Current status: `git status`
- Changes to commit: `git diff HEAD`
- All commits in branch: `git log --oneline origin/main..HEAD` (or appropriate base branch)
- Current branch: `git branch --show-current`
- Existing PR: check whether a pull request is already open for this branch with `gh pr view --json number,state,isDraft,url,title` (this returns an error if none exists — that just means you'll be creating a fresh PR). Note the number and whether it is a draft.
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
5. **Create or update the PR:**
   - **Write the title and body per "Writing a pull request" above** — the two-pass drafting method, the format, and the issue-linking rules all apply.
   - **Then create or update, based on the existing-PR check from Context:**
     - *No PR yet:* `gh pr create --title "title" --body "description"`
     - *A draft PR already exists:* update it in place, then mark it ready — do not create a second PR:
       - `gh pr edit <number> --title "title" --body "description"`
       - `gh pr ready <number>`
     - *A non-draft PR already exists:* update it in place with `gh pr edit <number> --title "title" --body "description"` (it is already ready for review, so leave its state alone).
   - Return the PR URL

Handle each step carefully and verify success before proceeding to the next.

## After the PR is open

Immediately start the `review-agent` skill on the PR (whether newly created or
just marked ready) to kick off a background review and watch for incoming
feedback (CI, bots, reviewers).
