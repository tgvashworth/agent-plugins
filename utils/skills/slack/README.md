# slack

Write a Slack message from the conversation. By default, the reply contains only the
message, ready to copy into Slack.

Specify draft or send and a recipient to use Slack directly. Sending requires an
explicit request.

In Claude Code:

```text
/u:slack draft to Pete: the migration is done and needs approval
```

In Codex:

```text
$slack draft to Pete: the migration is done and needs approval
```

See [SKILL.md](SKILL.md) for the full workflow.
