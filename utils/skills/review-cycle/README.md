# review-cycle

Address PR feedback and CI failures. The agent assesses comments, fixes issues, runs
tests, pushes changes, and replies to reviewers.

Limits repeated review rounds. Independent review is optional; merging requires your
authorisation.

In Claude Code:

```text
/u:review-cycle 42 without a sub-agent
```

In Codex:

```text
$review-cycle 42 without a sub-agent
```

See [SKILL.md](SKILL.md) for the full workflow.
