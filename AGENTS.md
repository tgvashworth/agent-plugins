# Agent plugin repository

This repository packages reusable Agent Skills for multiple hosts. Every
workflow lives under a plugin's `skills/` directory so that each host sees the
same set; there is no separate `commands/` directory. Claude Code invokes a
skill as `/<plugin>:<name>`, Codex as `$<name>`. The `.claude-plugin/`,
`agents/`, and `CLAUDE.md` files retain the existing Claude integration. `.codex-plugin/`, `AGENTS.md`, and
`.agents/plugins/marketplace.json` provide Codex packaging and discovery.

## Layout

- `playbook-dev/` — skills for designing multi-stage analysis playbooks.
- `utils/` — git, pull-request, writing, and collaboration workflows.
- `skills/<name>/SKILL.md` — host-neutral workflow instructions.
- `skills/<name>/{references,scripts,assets}/` — resources owned by a skill;
  `templates/` and `references/` at plugin root are shared package resources.
- `scripts/validate.py` — repository validation with no third-party packages.

## Editing conventions

- Every skill needs the Agent Skills `name` and `description` fields. Preserve
  host extension fields when they carry useful behavior and other hosts ignore
  them safely.
- Put host-specific adapters at the package edge. Do not use host tool names,
  `${CLAUDE_PLUGIN_ROOT}`, `$ARGUMENTS`, or command interpolation in shared
  `SKILL.md` bodies.
- Refer to packaged resources with paths relative to the current `SKILL.md`.
- Preserve established trigger phrases in descriptions unless the task is
  explicitly about changing discovery behavior.
- Treat compatibility work as compatibility work. Do not rewrite descriptions,
  workflows, or agent definitions unless their existing syntax
  prevents the target host from using them.
- Keep Claude and Codex manifest versions in sync. Use a patch bump for fixes
  and documentation, and a minor bump for new skills or capabilities.
- Preserve authorization boundaries. A skill may describe a mutation, but the
  host and the user's request determine whether it is allowed.

## Verification

Run `python3 scripts/validate.py` after changing skills, manifests, scripts, or
marketplace metadata. This repository has no build step.
