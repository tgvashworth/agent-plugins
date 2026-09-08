# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a Claude Code plugin marketplace repository containing two plugins:

- **playbook-dev** — a plugin for creating structured, multi-stage LLM analysis playbooks via a guided wizard and ~20 specialized skills
- **u** (source: `utils/`) — utility skills for git, PR, and writing workflows (`/u:commit`, `/u:commit-push-pr`, `/u:context`, `/u:slack`, and more)

## Repository Structure

This is a **markdown** codebase with no build step. All plugin functionality is defined in markdown files with YAML frontmatter. Run `python3 scripts/validate.py` after changing skills, manifests, or marketplace metadata.

```
.claude-plugin/marketplace.json   # Claude marketplace registry (lists both plugins)
.agents/plugins/marketplace.json  # Codex marketplace registry
scripts/validate.py               # Cross-host packaging validator
playbook-dev/
  .claude-plugin/plugin.json      # Claude plugin manifest
  .codex-plugin/plugin.json       # Codex plugin manifest (same version)
  agents/                         # Subagent definitions (playbook-validator)
  references/                     # Playbook pattern docs (the core reference)
  skills/                         # ~20 skills (skills/<name>/SKILL.md), incl. create
utils/
  .claude-plugin/plugin.json      # Claude plugin manifest (name: "u")
  .codex-plugin/plugin.json       # Codex plugin manifest (same version)
  skills/                         # All /u skills (commit, context, slack, ...)
  templates/common.md             # Shared commit workflow instructions
```

## Plugin Architecture

Each plugin has a `.claude-plugin/plugin.json` manifest. The marketplace registry at `.claude-plugin/marketplace.json` maps display names to source directories (e.g., `"u"` → `./utils`).

**Skills** (`skills/<name>/SKILL.md`) are the only unit of functionality. Users invoke them as `/<plugin>:<name>` in Claude Code (e.g. `/u:commit`, `/playbook-dev:create`) or `$<name>` in Codex, and hosts may also activate them from the `description` field. There is no `commands/` directory: anything a user can invoke is a skill, so every host can see it.

Skill frontmatter must stay host-neutral: `name` (matching the directory), `description`, and optionally `argument-hint`, `allowed-tools`, `license`, `metadata`, `model`, `user-invocable`, `version`. Quote values that start with `[`. Do not use `disable-model-invocation`; put explicit-only behaviour in `skills/<name>/agents/openai.yaml` (`policy.allow_implicit_invocation: false`) as `what`, `bg`, and `slack` do.

Skill bodies must not use `${CLAUDE_PLUGIN_ROOT}`, `$ARGUMENTS`, `$1`, or `@file` includes. Refer to user input as "the user's guidance" and to shared resources with a relative markdown link, e.g. `[commit guidance](../../templates/common.md)`. Do not name host-specific tools (AskUserQuestion, TodoWrite, Agent, Monitor); describe the action instead.

**Agents** (`agents/<name>.md`) define subagent behavior with `tools`, `model`, and `whenToUse` frontmatter fields.

**Templates** (`templates/*.md`) are shared resources that skills link to with relative paths.

## Key Conventions

- The utils plugin is published as `u` (not `utils`) — the name in `plugin.json` controls this.
- Skills use `argument-hint` frontmatter to show usage hints in the command palette.
- Commit messages: no attribution footers, match existing repo style, short and actionable (see `utils/templates/common.md`).
- **Bump the plugin version** in both manifests (`.claude-plugin/plugin.json` and `.codex-plugin/plugin.json`; the validator requires them to match) as part of any PR that changes that plugin. Use semver: patch for fixes/doc tweaks, minor for new skills or capabilities.
- The playbook-dev plugin follows a 5-stage pipeline pattern (0-setup through 4-finalization) documented in `playbook-dev/references/playbook-pattern.md`.
