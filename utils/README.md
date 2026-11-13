# Utils

Skills for Git, pull requests, reviews, and writing. The plugin is installed as `u` in
Claude Code and Codex.

In Claude Code, invoke a skill with `/u:<name>`. In Codex, use `$<name>`. You can also
describe the task in plain English, as in the examples below. Each skill's README
explains its inputs and behaviour.

## Skills

### [context](skills/context/README.md)

Get up to speed on a task, ticket, branch, or plan. The agent summarises the repository
state and suggests next steps.

### [commit](skills/commit/README.md)

Create one Git commit from the current changes. The agent writes a message in your
repository's style and handles pre-commit hooks.

### [commit-push-pr](skills/commit-push-pr/README.md)

Commit the changes, push the branch, and open a PR ready for review. An existing PR is
updated instead of duplicated.

### [commit-push-draft](skills/commit-push-draft/README.md)

Commit the changes, push the branch, and open a draft PR. An existing PR is updated
without changing its draft or ready state.

### [bg](skills/bg/README.md)

Run a task in a background agent while you continue other work. The task description
becomes the worker's brief.

### [remember](skills/remember/README.md)

Save a project fact, rule, or convention in the relevant AGENTS.md or CLAUDE.md. Future
sessions can read it from the repository.

### [ready-for-review](skills/ready-for-review/README.md)

Rewrite a PR's title and description to match the current branch, then mark a draft
ready for review.

### [review-cycle](skills/review-cycle/README.md)

Address PR feedback and CI failures. The agent assesses comments, fixes issues, runs
tests, pushes changes, and replies to reviewers.

### [review-agent](skills/review-agent/README.md)

Review a PR and monitor new comments and CI failures. Return findings to the session
making the changes.

### [pr-feedback](skills/pr-feedback/README.md)

Assess PR feedback and decide which suggestions to implement, acknowledge, or decline.
Plan and apply the approved fixes.

### [pr-respond](skills/pr-respond/README.md)

Reply to PR review comments and resolve threads whose feedback has been addressed. The
agent checks the current code before responding.

### [pr-comments](skills/pr-comments/README.md)

Read the comments, reviews, and inline threads on a PR. The agent groups the feedback by
reviewer and file.

### [tourguide](skills/tourguide/README.md)

Understand a change or plan one part at a time. The agent explains what changed, why,
and what it affects.

### [quiz](skills/quiz/README.md)

Check your understanding of a change with questions based on its diff and repository
conventions. The agent explains any gaps in your answers.

### [what](skills/what/README.md)

Ask for the previous response to be explained again in plain English. Quote a confusing
phrase or name the part you want clarified.

### [deslop](skills/deslop/README.md)

Rewrite comments, copy, commit messages, PRs, or tickets in plain English. Remove filler
and wording that takes effort to understand.

### [slack](skills/slack/README.md)

Write a Slack message from the conversation. By default, the reply contains only the
message, ready to copy into Slack.

### [write](skills/write/README.md)

Help the agent write better documents. It sets the goal and audience, plans the
structure, drafts, and reviews the result.

## Examples

You can ask for several workflows in one request:

> Commit, push, PR, and review-cycle this change.

The agent commits and pushes the change, opens or updates the PR, then handles CI
failures and review feedback. Merging requires your authorisation.

Other examples:

| Request | Workflow |
| --- | --- |
| "Open a draft PR so I can look at it." | `commit-push-draft` |
| "Explain this branch to me one part at a time." | `tourguide` |
| "Check that I understand this change." | `quiz` |
| "Use the write skill to improve this proposal for the leadership team." | `write` |
| "Rewrite this README in plain English." | `deslop` |

To select a skill explicitly in Claude Code:

```text
/u:commit-push-pr
/u:tourguide feature/auth-refactor
/u:write docs/rfc-auth.md
```

In Codex:

```text
$commit-push-pr
$tourguide feature/auth-refactor
$write docs/rfc-auth.md
```

## Features

The commit and PR skills use your repository's commit style and check each operation. They handle
pre-commit hooks that modify files. PR descriptions cover the whole branch, including
related issues and verification results.

## Installation

Follow the [marketplace installation instructions](../README.md#installation) for Claude
Code or Codex. Other Agent Skills hosts can load `skills/` directly if they preserve the
plugin's relative file layout.

## Requirements

Use Git for repository workflows and an authenticated GitHub CLI (`gh`) for PR
workflows. Background tasks require a host that supports background agents. Slack drafts
and sends require a connected Slack tool.
