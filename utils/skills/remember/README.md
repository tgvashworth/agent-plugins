# remember

Save a project fact, rule, or convention in the relevant AGENTS.md or CLAUDE.md. Future
sessions can read it from the repository.

The agent checks for duplicates and conflicts. It asks before saving wording it inferred
or shortened.

In Claude Code:

```text
/u:remember API handlers must return structured errors using pkg/apierror
```

In Codex:

```text
$remember API handlers must return structured errors using pkg/apierror
```

See [SKILL.md](SKILL.md) for the full workflow.
