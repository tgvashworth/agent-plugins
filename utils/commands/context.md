---
description: Gather context and get familiar with the current task
argument-hint: [guidance]
allowed-tools:
  - Bash(git:*)
  - Bash(gh:*)
  - Read
  - Glob
  - Grep
  - AskUserQuestion
  - WebFetch
---

# Gather Task Context

Get up to speed with the current task by reviewing git state, recent commits, modified files, and any external references.

## User Guidance

$1

## Context Gathering (run in parallel)

Execute these commands simultaneously:

- Current branch: `git branch --show-current`
- Branch status: `git status`
- Staged changes: `git diff --cached --stat`
- Unstaged changes: `git diff --stat`
- Recent commits on branch: `git log --oneline -15`
- Commits vs main: `git log --oneline main..HEAD` (or master if main doesn't exist)

## Process

1. **Analyze git state**: Review the parallel-gathered information to understand:
   - What branch are we on and what's its purpose?
   - What commits have been made on this branch?
   - What files have been modified (staged and unstaged)?

2. **Extract ticket/issue references**: Look for patterns like:
   - `#123`, `GH-123` (GitHub issues)
   - `PROJ-123` (Jira/Linear)
   - URLs to issues, PRs, or docs

   If found, use `gh issue view` or `gh pr view` to fetch details.

3. **Read significant files**: Identify and read files that have been:
   - Modified in recent commits (`git diff --name-only main..HEAD`)
   - Currently staged or with unstaged changes
   - Focus on understanding the nature of the changes

4. **Incorporate user guidance**: If the user provided guidance in `$1`, use it to:
   - Focus on specific areas they mentioned
   - Answer specific questions they asked
   - Prioritize certain aspects of the context

5. **Clarify if needed**: Use AskUserQuestion if:
   - The branch purpose is unclear
   - Multiple unrelated changes are present
   - You need to understand the broader goal

## Output Format

Provide a summary using this structure:

```
## Current Context

**Branch:** [branch-name]
**Status:** [e.g., "3 commits ahead of main, 2 files staged"]

## What's Being Worked On

[1-3 sentence summary of the task/feature based on commits and changes]

## Key Changes

- [file1.ts]: [what changed and why]
- [file2.ts]: [what changed and why]

## Related References

- [Any tickets, PRs, or docs found]

## Current State

- [What's done]
- [What's in progress]
- [What remains to be done, if discernible]

## Questions/Clarifications

[Any questions for the user, or "Ready to continue work"]
```

## Important Notes

- Gather git information in parallel for efficiency
- Don't read every file - focus on significantly modified ones
- If on main/master with no changes, ask the user what they're planning to work on
- Match any existing context from the user's guidance
