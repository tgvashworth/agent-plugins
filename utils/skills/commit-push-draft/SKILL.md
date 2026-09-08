---
name: commit-push-draft
description: >
  Commit the current changes, push the branch, and open a draft pull request,
  or update an existing PR in place without changing its draft state. Use when
  the user invokes /commit-push-draft, asks for a draft PR, or wants to push
  work up for a look before it is ready for review.
argument-hint: "[guidance]"
allowed-tools: "Bash(git status:*), Bash(git diff:*), Bash(git log:*), Bash(git add:*), Bash(git commit:*), Bash(git branch:*), Bash(git checkout:*), Bash(git push:*), Bash(gh pr create:*), Bash(gh pr view:*), Bash(gh pr edit:*), Bash(gh issue:*), Bash(gh search:*)"
---

# Commit, push, and open a draft PR

Create a commit, push to the remote, and open a draft pull request. If a pull
request is already open for this branch, update it in place instead of creating
a new one, and leave its draft or ready state as it is.

Read the shared [commit guidance](../../templates/common.md) and the
[pull-request guidance](../../templates/pr-body.md) first. They define the
message and title format, how to find related issues, and how to write the PR
body.

## Context

Gather this information in parallel:

- Current status: `git status`
- Changes to commit: `git diff HEAD`
- Current branch: `git branch --show-current`
- The repository's actual default branch (do not assume `main`), and all
  commits on this branch relative to it: `git log --oneline <base>..HEAD`
- Existing PR: `gh pr view --json number,state,isDraft,url,title`. An error
  means there is none and you will create a fresh draft PR. Otherwise note the
  number.
- Related issues: per "Finding related issues" in the pull-request guidance.

## User guidance

If the user supplied guidance with the request, apply it to the commit message,
the PR title and body, and the file set. Otherwise infer them from the diff.

## Steps

1. **Create a branch if needed.** If on the default branch, create a
   descriptively named branch first.
2. **Review changes.** Understand what will be committed. Stage only files that
   belong to this change.
3. **Create the commit.** Draft the message per the commit guidance, stage with
   `git add`, commit with `git commit -m "message"`, handle pre-commit hooks per
   the commit guidance, and verify with `git status`. If there is nothing to
   commit but the branch already has commits to ship, continue.
4. **Push.** `git push -u origin <branch-name>` (set the upstream only if it
   does not already have one). Verify the push succeeded. Never force-push.
5. **Create or update the draft PR.** Write the title and body per "Writing a
   pull request" in the pull-request guidance: the two-pass drafting method,
   the format, and the issue-linking rules all apply. Base them on the whole
   branch diff, not only the newest commit. Then, based on the existing-PR
   check:
   - *No PR yet:* `gh pr create --draft --title "title" --body "description"`
   - *A PR exists:* update it in place and leave its draft or ready state
     alone: `gh pr edit <number> --title "title" --body "description"`
6. Return the commit SHA and the PR URL.

Verify success at each step before moving to the next. Do not start a review
after a draft PR; that happens when it is marked ready.
