# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a Claude Code plugin marketplace repository containing two plugins:

- **playbook-dev** — a plugin for creating structured, multi-stage LLM analysis playbooks via a guided wizard and ~20 specialized skills
- **u** (source: `utils/`) — utility commands for git workflows (`/commit`, `/commit-push-pr`, `/commit-push-draft`, `/context`)

## Repository Structure

This is a **pure-markdown** codebase — no build, lint, or test commands. All plugin functionality is defined in markdown files with YAML frontmatter.

```
.claude-plugin/marketplace.json   # Marketplace registry (lists both plugins)
playbook-dev/
  .claude-plugin/plugin.json      # Plugin manifest
  agents/                         # Subagent definitions (playbook-validator)
  commands/                       # Slash commands (/playbook create)
  references/                     # Playbook pattern docs (the core reference)
  skills/                         # ~20 skill files (SKILL.md with frontmatter)
utils/
  .claude-plugin/plugin.json      # Plugin manifest (name: "u")
  commands/                       # Slash commands (commit, context, etc.)
  templates/common.md             # Shared commit workflow instructions
```

## Plugin Architecture

Each plugin has a `.claude-plugin/plugin.json` manifest. The marketplace registry at `.claude-plugin/marketplace.json` maps display names to source directories (e.g., `"u"` → `./utils`).

**Skills** (`skills/<name>/SKILL.md`) are auto-activated by Claude based on context matching against the `description` field in YAML frontmatter. They are not invoked directly by users.

**Commands** (`commands/<name>.md`) are user-invocable via `/<plugin> <command>` (e.g., `/playbook create`). They use `allowed-tools` in frontmatter to restrict tool access and `$1` as a placeholder for user arguments.

**Agents** (`agents/<name>.md`) define subagent behavior with `tools`, `model`, and `whenToUse` frontmatter fields.

**Templates** are included via `@${CLAUDE_PLUGIN_ROOT}/templates/<name>.md` syntax.

## Key Conventions

- The utils plugin is published as `u` (not `utils`) — the name in `plugin.json` controls this.
- Commands use `argument-hint` frontmatter to show usage hints in the command palette.
- Commit messages: no attribution footers, match existing repo style, short and actionable (see `utils/templates/common.md`).
- The playbook-dev plugin follows a 5-stage pipeline pattern (0-setup through 4-finalization) documented in `playbook-dev/references/playbook-pattern.md`.
