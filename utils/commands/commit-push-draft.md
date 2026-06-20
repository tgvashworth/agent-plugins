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
  - Bash(gh issue:*)
  - Bash(gh search:*)
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
- Related issues: Identify **every** issue this change is relevant to. The right issue is often not obvious, so dig in a few places:
  - The branch name (e.g. `feature/123-foo` → `#123`)
  - User guidance and the branch's commit messages
  - Open issues describing the problem this change solves — run `gh issue list` or `gh search issues "<keywords from the diff>"` and match them against what actually changed
  For each candidate, run `gh issue view <number>` to confirm it exists and that this change genuinely addresses it, then decide whether the PR *closes* it (fully resolves it) or merely *relates to* it (touches it without resolving it).

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
   - **Draft the PR description in two passes:**
     - *Pass 1 — capture the change:* Based on ALL commits in the branch (not just the latest), write what changed and why.
     - *Pass 2 — rewrite for a stranger:* Rewrite the description from the perspective of someone with no prior context on this change. The PR must stand on its own — explain the problem and the change in simple, clear words, with enough context to understand it cold. Strip out any references to development-discussion internals (review back-and-forth, "as discussed", earlier attempts, iteration history); describe the end result, not how you got there.
   - PR format: summary (1-3 bullets), test plan checklist, next steps if relevant
   - **Link to issues** (required — do not skip): In the PR body, reference every relevant issue found above, each on its own line, using the correct keyword:
     - `Closes #<number>` for each issue this PR fully resolves
     - `Refs #<number>` for issues that are relevant but not fully resolved here
     If, after genuinely checking, no issue is relevant, say so in your reply to the user (not in the PR body) so it's clear the step wasn't simply forgotten.
   - Use: `gh pr create --draft --title "title" --body "description"`
   - Return the PR URL

Handle each step carefully and verify success before proceeding to the next.
