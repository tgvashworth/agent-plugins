---
name: task-context
description: Inspect a repository, branch, pull request, or issue and explain the current work, important changes, related references, and useful next steps. Use when the user asks to get oriented, catch up, or gather task context.
---

# Gather task context

Orient the user without changing repository or external state.

## Resolve the focus

Use the user's request as the primary signal:

- For an issue, ticket, or PR reference, fetch it with an available authenticated
  integration and connect the repository state to that work.
- For a branch name, compare it with the active branch and its actual base.
- With no specific reference, explain the current branch and working tree.

Do not switch branches merely to inspect one. Ask a question only when multiple
plausible targets would produce materially different summaries.

## Inspect

Gather independent facts in parallel when possible:

- current branch and `git status`
- staged and unstaged diff summaries
- recent commits on the current branch
- commits and changed files relative to the actual base branch
- linked issue or PR details found in the user's request, branch name, commits,
  or configured repository integrations

Read the small set of changed or central files needed to understand intent. Do
not inventory the whole repository unless the user asks for that.

Separate facts from inference. If a branch name suggests an issue but the issue
cannot be verified, label the association as tentative.

## Report

Lead with a short account of what is being worked on and its current state.
Then cover, as useful:

- branch and working-tree status
- key changes and why they appear to exist
- related issues, PRs, or documents
- completed, in-progress, and apparently remaining work
- the most useful next step

Use repository-relative file references. End with a question only when the user
must choose among genuinely different next actions.
