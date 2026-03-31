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

Create structured, multi-stage analysis playbooks for LLM-driven workflows. Use the guided `/playbook create` wizard to scaffold a new playbook, then draw on ~20 skills for stage authoring, quality gates, and advanced patterns like attribution and clustering.

### utils (installed as `u`)

A grab-bag of useful commands:

- `/context` — get up to speed with the current task
- `/commit` — create a commit with an auto-generated message
- `/commit-push-pr` — commit, push, and open a PR
- `/commit-push-draft` — commit, push, and open a draft PR

## Author

Tom Ashworth ([@tgvashworth](https://github.com/tgvashworth))

## License

MIT
