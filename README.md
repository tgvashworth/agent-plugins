# Agent plugins

A collection of Agent Skills packaged as plugins for
[Claude Code](https://docs.anthropic.com/en/docs/claude-code) and Codex.

## Installation

### Claude Code

This repo is a [Claude Code plugin marketplace](https://docs.anthropic.com/en/docs/claude-code/plugins). From within Claude Code, add the marketplace and then install the plugins you want:

```
/plugin marketplace add tgvashworth/agent-plugins
/plugin install playbook-dev@tgvashworth-agent-plugins
/plugin install u@tgvashworth-agent-plugins
```

Or run `/plugin` to open the interactive plugin manager and browse available plugins.

### Codex

Add this repository as a Codex marketplace:

```bash
codex plugin marketplace add tgvashworth/agent-plugins
```

Then start Codex, run `/plugins`, and install `u`, `playbook-dev`, or both.
Start a new session after installation. Use natural-language requests or select
a skill explicitly with `$`, for example `$git-ship` or `$playbook-wizard`.

### Other Agent Skills hosts

The reusable workflows live in each plugin's `skills/` directory and avoid
host-specific command interpolation. Point an Agent Skills-compatible host at
that directory while preserving the plugin's relative file layout. Invocation
syntax and available tools remain host-specific.

## Plugins

### playbook-dev

Create structured, multi-stage analysis playbooks for LLM-driven workflows. Use the guided `/playbook-dev:create` wizard to scaffold a new playbook, then draw on ~20 skills for stage authoring, quality gates, and advanced patterns like attribution and clustering.

### utils (installed as `u`)

A grab-bag of useful commands:

- `/u:context` — get up to speed on a task, ticket, or branch
- `/u:commit` — create a commit with an auto-generated message
- `/u:commit-push-pr` — commit, push, and open a PR
- `/u:commit-push-draft` — commit, push, and open a draft PR
- `/u:ready-for-review` — rewrite a stale draft PR's title and body, then open it for review
- `/u:pr-comments` — fetch PR comments, reviews, and threads in one call
- `/u:pr-feedback` — triage and act on PR review feedback
- `/u:pr-respond` — reply to and resolve PR review threads
- `/u:review-agent` — review a PR and watch it for new CI failures and comments
- `/u:remember` — persist a convention to the project's shared AGENTS.md/CLAUDE.md
- `/u:write` — draft or improve a longer document through a structured process
- `/u:tourguide` — walk through changes or a plan one group at a time
- `/u:what` — re-explain the last message in plain English when it didn't land
- `/u:deslop` — plain-English pass over comments, copy, commit messages, PRs, or tickets
- `/u:bg` — run a task in a background agent

### Setting commit and PR title style per repo

The commit and PR commands infer house style from recent commits, which works
until the log drifts — then each new title copies the last, and the drift
compounds.

To pin it instead, add a `.github/COMMIT_STYLE.md` (or `.claude/commit-style.md`)
to the repo. When that file exists it becomes the only source of style and the
log is not read for phrasing at all, so a polluted log stops propagating. Put
the house rules in it, and worked before/after examples if the repo has a
failure mode worth naming.

With no such file the commands fall back to sampling the log, but check what
they find against their built-in title test first, rather than copying it blind.

## Cookbook

These skills are built to work together. The combinations that I find useful:

**Ship a change.** Open with the ticket or plan, work, then ship in one step:

```
/u:context https://linear.app/acme/issue/ABC-728      # or ~/.claude/plans/<repo>/some-plan.md
... some time later ...
/u:commit-push-pr
```

`/u:commit-push-pr` writes the PR body, opens it, and hands off to `/u:review-agent` itself — you don't need to call the review agent after shipping.

**Drive a PR to green.** Pass the number plus how you want it handled — round budget, merge behaviour, how hard to push back:

```
/u:review-agent 1236 and then merge once we're green
/u:review-agent 1365 but with strong pressure not to implement nits
```

**When a reply doesn't land.** Quote the phrase that confused you, or name what you want redone. Most useful right after a dense review report:

```
/u:what "the honest gap"
/u:what explain how this does channel matching now, end-to-end
```

**Capture what review taught you**, the moment it surfaces — so the next session starts knowing it:

```
/u:remember that the read-only CI credential can't run the flexipage suite. that's known.
```

**Hand the work to a human.** Walk them through it live, or turn the session into a document:

```
/u:tourguide this updated auth architecture
/u:write this up
```

**Park a draft, then send it.** `/u:ready-for-review` rebuilds the description from the branch as it now stands, so a draft body written mid-work doesn't reach reviewers:

```
/u:commit-push-draft
/u:ready-for-review
```

`/u:pr-comments`, `/u:pr-feedback` and `/u:pr-respond` are the machinery `/u:review-agent` drives for you. Reach for `pr-feedback` or `pr-respond` directly only when you want that one step on its own; `pr-comments` is internal.

## Author

Tom Ashworth ([@tgvashworth](https://github.com/tgvashworth))

## License

MIT
