---
name: playbook-validator
description: Validates playbook structure, completeness, and quality. Use when the user completes a stage, asks to validate, finishes major sections, or is ready to test a playbook.
---

# Playbook validator

Read [the shared validation workflow](../../agents/playbook-validator.md) and
follow its body from `# Playbook Validator` onward. Ignore the Claude-specific
agent frontmatter above that heading.

Keep the validation read-only. Return the report to the user; do not modify the
playbook unless they separately ask for fixes.
