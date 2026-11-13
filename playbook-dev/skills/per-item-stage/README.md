# per-item-stage

Design Stage 1, where agents analyse individual records in parallel. Define each agent's
task, required outputs, and completion checks.

Each agent finishes one record before receiving another. Configure concurrency and
progress tracking for the dataset.

In Claude Code:

```text
/playbook-dev:per-item-stage design parallel analysis of individual support tickets
```

In Codex:

```text
$per-item-stage design parallel analysis of individual support tickets
```

See [SKILL.md](SKILL.md) for the full workflow.
