---
name: commit-push-pr
description: >
  Commit the current changes, push the branch, and open a pull request ready
  for review, or update an existing PR and mark a draft ready. Use when the
  user invokes /commit-push-pr, says "ship this", "open a PR", or asks to
  commit and push and create a pull request.
argument-hint: "[guidance]"
allowed-tools: "Bash(git status:*), Bash(git diff:*), Bash(git log:*), Bash(git add:*), Bash(git commit:*), Bash(git branch:*), Bash(git checkout:*), Bash(git push:*), Bash(gh pr create:*), Bash(gh pr view:*), Bash(gh pr edit:*), Bash(gh pr ready:*), Bash(gh issue:*), Bash(gh search:*)"
---

# Commit, push, and open a PR

Create a commit, push to the remote, and open a pull request. If a pull request
is already open for this branch, update it instead of creating a new one, and if
it is a draft, mark it ready for review.

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
  means there is none and you will create a fresh PR. Otherwise note the
  number and whether it is a draft.
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
5. **Create or update the PR.** Write the title and body per "Writing a pull
   request" in the pull-request guidance: the two-pass drafting method, the
   format, and the issue-linking rules all apply. Base them on the whole
   branch diff, not only the newest commit. Then, based on the existing-PR
   check:
   - *No PR yet:* `gh pr create --title "title" --body "description"`
   - *A draft PR exists:* update it in place, then mark it ready. Do not
     create a second PR: `gh pr edit <number> --title "title" --body
     "description"`, then `gh pr ready <number>`.
   - *A ready PR exists:* update it in place with `gh pr edit`. Leave its
     state alone.
6. Return the commit SHA and the PR URL.

Verify success at each step before moving to the next.

## After the PR is open

Immediately start the `review-agent` skill on the PR (whether newly created or
just marked ready) to kick off a background review and watch for incoming
feedback from CI, bots, and reviewers. Skip this if the host has no background
process capability, and say so.
