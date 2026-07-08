# Agent plugins

A collection of plugins for [Claude Code](https://docs.anthropic.com/en/docs/claude-code).

## Installation

This repo is a [Claude Code plugin marketplace](https://docs.anthropic.com/en/docs/claude-code/plugins). From within Claude Code, add the marketplace and then install the plugins you want:

```
/plugin marketplace add tgvashworth/agent-plugins
/plugin install playbook-dev@tgvashworth-agent-plugins
/plugin install u@tgvashworth-agent-plugins
```

Or run `/plugin` to open the interactive plugin manager and browse available plugins.

## Plugins

### playbook-dev

Create structured, multi-stage analysis playbooks for LLM-driven workflows. Use the guided `/playbook-dev:create` wizard to scaffold a new playbook, then draw on ~20 skills for stage authoring, quality gates, and advanced patterns like attribution and clustering.

### utils (installed as `u`)

A grab-bag of useful commands:

- `/u:context` — get up to speed on a task, ticket, or branch
- `/u:commit` — create a commit with an auto-generated message
- `/u:commit-push-pr` — commit, push, and open a PR
- `/u:commit-push-draft` — commit, push, and open a draft PR
- `/u:pr-comments` — fetch PR comments, reviews, and threads in one call
- `/u:pr-feedback` — triage and act on PR review feedback
- `/u:pr-respond` — reply to and resolve PR review threads
- `/u:review-agent` — review a PR and watch it for new CI failures and comments
- `/u:remember` — persist a convention to the project's shared AGENTS.md/CLAUDE.md
- `/u:write` — draft or improve a longer document through a structured process
- `/u:tourguide` — walk through changes or a plan one group at a time
- `/u:bg` — run a task in a background agent

## Author

Tom Ashworth ([@tgvashworth](https://github.com/tgvashworth))

## License

MIT
