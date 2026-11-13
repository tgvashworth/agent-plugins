# Agent plugins

Reusable Agent Skills packaged as plugins for
[Claude Code](https://docs.anthropic.com/en/docs/claude-code) and Codex.

## Installation

### Claude Code

This repository is a [Claude Code plugin marketplace](https://docs.anthropic.com/en/docs/claude-code/plugins).
In Claude Code, add the marketplace and install either or both plugins:

```
/plugin marketplace add tgvashworth/agent-plugins
/plugin install playbook-dev@tgvashworth-agent-plugins
/plugin install u@tgvashworth-agent-plugins
```

You can also run `/plugin` to browse and install plugins interactively.

### Codex

Add this repository as a Codex marketplace:

```bash
codex plugin marketplace add tgvashworth/agent-plugins
```

Start Codex, run `/plugins`, and install `u`, `playbook-dev`, or both.
Start a new session after installation. Request a skill in plain English or
select one with `$`, for example `$commit-push-pr` or `$playbook-wizard`.

### Other Agent Skills hosts

Each plugin's `skills/` directory contains its reusable workflows.
Point an Agent Skills-compatible host at that directory and preserve the
plugin's relative file layout. The workflows avoid host-specific command
interpolation. Invocation syntax and available tools depend on the host.

## Plugins

### playbook-dev

Create analysis playbooks with multiple stages for LLM workflows.
Use `/playbook-dev:create` for guided setup. The roughly 20 skills cover
stage authoring, quality checks, causal attribution, and clustering.
See the [playbook-dev README](playbook-dev/README.md) for the full list.

### utils (installed as `u`)

Skills for Git, pull requests, writing, and collaboration. Invoke them with
`/u:<name>` in Claude Code or `$<name>` in Codex.
See the [utils README](utils/README.md) for details and links to every skill:

- `/u:context` — get up to speed on a task, ticket, or branch
- `/u:commit` — create a commit with a generated message
- `/u:commit-push-pr` — commit, push, and open a PR
- `/u:commit-push-draft` — commit, push, and open a draft PR
- `/u:ready-for-review` — update a draft PR's title and body, then mark it ready for review
- `pr-comments` — fetch PR comments, reviews, and threads for the review skills
- `/u:pr-feedback` — assess and address PR review feedback
- `/u:pr-respond` — reply to and resolve PR review threads
- `/u:review-cycle` — fix issues, test, push, and reply to reviewers until CI passes and feedback is addressed
- `/u:review-agent` — review a PR without changing it and monitor CI failures and comments
- `/u:remember` — save a convention in the project's shared AGENTS.md or CLAUDE.md
- `/u:write` — help the agent write a clear document for its intended audience
- `/u:tourguide` — understand a change or plan one part at a time
- `/u:quiz` — check your understanding of a change with questions based on its diff
- `/u:what` — explain the last message again in plain English
- `/u:deslop` — rewrite comments, copy, commit messages, PRs, or tickets in plain English
- `/u:bg` — run a task in a background agent
- `/u:slack` — write a Slack message to copy, save as a draft, or send

### Commit and PR title style

The commit and PR skills infer your repository's style from recent commits.
If those commits are poorly worded, new titles can repeat the same problems.

To define the style explicitly, add `.github/COMMIT_STYLE.md` or
`.claude/commit-style.md` to your repository. When a style file exists, the
skills use it as the only source of style instead of the commit log.
Include your rules and examples of wording to avoid and what to use instead.

Without a style file, the skills sample the log and check its wording against
their built-in title rules before using it.

## Examples

You can combine workflows in a plain-English request:

> Commit, push, PR, and review-cycle this change.

The agent commits and pushes the change, opens or updates the PR, then addresses
CI failures and review feedback. Merging requires your authorisation.

Other examples:

| Request | Skills |
| --- | --- |
| "Open a draft PR so I can look at it." | `commit-push-draft` |
| "Explain this branch to me one part at a time." | `tourguide` |
| "Check that I understand this change." | `quiz` |
| "Use the write skill to improve this proposal for the leadership team." | `write` |
| "Rewrite this README in plain English." | `deslop` |

The examples below use explicit Claude Code commands. In Codex, use `$<name>`
in place of `/u:<name>`.

**Commit, push, and open a PR.** Start with a ticket or plan, make the change,
then open a PR:

```
/u:context https://linear.app/acme/issue/ABC-728      # or ~/.claude/plans/<repo>/some-plan.md
... make the change ...
/u:commit-push-pr
```

`/u:commit-push-pr` writes the PR description, opens the PR, and starts
`/u:review-cycle` with the task's existing permissions.

**Address feedback and fix CI failures.** Pass the PR number and any limits
on review rounds, merging, or minor fixes:

```
/u:review-cycle 1236 and merge once CI passes and review feedback is addressed
/u:review-cycle 1365 but skip minor style suggestions
```

`review-cycle` fixes issues, runs tests, pushes changes, and replies to reviewers.
It can use an independent reviewer and limits repeated rounds of minor fixes.
Useful findings outside the PR's scope get follow-up tickets. An agreed
follow-up change is made in a separate PR after the current one merges.
Use `review-agent` to review and monitor a PR without changing it.

**Ask for a clearer explanation.** Quote the confusing phrase or name the
part you want explained again:

```
/u:what "channel matching"
/u:what explain how channel matching works from input to output
```

**Save a project convention.** Use `/u:remember` to add a fact or rule to
AGENTS.md or CLAUDE.md for future sessions:

```
/u:remember the read-only CI credential cannot run the flexipage suite
```

**Understand the change.** Ask the agent to explain the work or a plan one
part at a time. Say "next" to continue, or ask questions before moving on:

```
/u:tourguide this updated auth architecture
```

**Help the agent write better.** Use `/u:write` to set the goal and audience
before planning, drafting, and reviewing a document:

```
/u:write docs/rfc-auth.md
```

**Write a Slack update.** Use `/u:slack` to draft a message from the session.
It returns only the message, ready to copy with `/copy`.
Specify a recipient and `draft` to save it in your Slack drafts:

```
/u:slack
/u:slack draft to Pete: migration is done, needs a sign-off on the flag
```

**Prepare a draft PR for review.** `/u:ready-for-review` rewrites the title
and description to match the current branch. It then marks the PR ready:

```
/u:commit-push-draft
/u:ready-for-review
```

Use `/u:review-cycle` for the full review process. Use `pr-feedback` to assess
feedback and make fixes, `pr-respond` to reply and resolve threads, or
`pr-comments` to read the feedback.

## Author

Tom Ashworth ([@tgvashworth](https://github.com/tgvashworth))

## License

MIT
