---
name: context
description: >
  Get up to speed on a task: inspect the branch, working tree, recent commits,
  and any ticket, issue, or PR the user points at, then summarise what is being
  worked on and what to do next. Use when the user invokes /context, switches
  to a new piece of work, or asks to get oriented or catch up on a branch.
argument-hint: "[ticket, branch, plan file, or guidance]"
allowed-tools: "Bash(git:*), Bash(gh:*)"
---

# Gather task context

Get up to speed with a task. Often used when switching context to a new piece
of work. This is read-only: do not change repository or external state, and do
not switch branches merely to inspect one.

## Understand the intent

Before gathering context, identify what the user gave you:

- **A ticket or issue reference** (`#123`, `PROJ-123`, a URL): the user is about
  to plan an implementation. Fetch the ticket details with an available
  authenticated integration and orient the summary toward next steps.
- **A branch name** (`feature/auth-refactor`, `1234-auth-refactor`): the user
  wants to implement on that branch. Check whether it is already the active
  branch; if not, say so.
- **A plan or document path**: read it and connect it to the repository state.
- **Something else or nothing**: fall back to general context gathering from
  git state.

## Context gathering (run in parallel)

- Current branch: `git branch --show-current`
- Branch status: `git status`
- Staged changes: `git diff --cached --stat`
- Unstaged changes: `git diff --stat`
- Recent commits on branch: `git log --oneline -15`
- Commits relative to the repository's actual default branch:
  `git log --oneline <base>..HEAD`

## Process

1. **Analyse git state.** What branch is this and what is its purpose? What
   commits have been made on it? What files are modified, staged or unstaged?
2. **Extract ticket and issue references** from the branch name, commits, and
   the user's request: `#123` or `GH-123` (GitHub), `PROJ-123` (Jira, Linear),
   URLs to issues, PRs, or docs. Fetch them with `gh issue view`, `gh pr view`,
   or the relevant integration. If a reference cannot be verified, label the
   association as tentative.
3. **Read significant files.** Files changed in recent commits
   (`git diff --name-only <base>..HEAD`) and files currently staged or
   modified. Read the small set needed to understand intent; do not inventory
   the repository.
4. **Apply the user's guidance.** Focus on the areas they named, answer the
   questions they asked, and prioritise accordingly.
5. **Clarify only if needed.** Ask the user a question when the branch purpose
   is unclear, several unrelated changes are present, or the broader goal is
   needed to say anything useful. Otherwise do not end with a question.

## Context window hygiene

After gathering context, if a substantial share of the context window is in
use, suggest the user compact the conversation before starting implementation.

## Output format

```
## Current context

**Branch:** [branch-name]
**Status:** [e.g. "3 commits ahead of main, 2 files staged"]

## What's being worked on

[1-3 sentence summary of the task based on commits and changes]

## Key changes

- [file1.ts]: [what changed and why]
- [file2.ts]: [what changed and why]

## Related references

- [Any tickets, PRs, or docs found]

## Current state

- [What's done]
- [What's in progress]
- [What remains, if discernible]

## Suggested next steps

[e.g. "Plan the implementation", "Continue work on X"]

## Questions

[Any questions for the user, or "Ready to continue work"]
```

## Notes

- Separate facts from inference.
- Use repository-relative file references.
- If on the default branch with no changes, ask the user what they plan to
  work on.
