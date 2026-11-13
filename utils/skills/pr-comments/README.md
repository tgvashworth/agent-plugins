# pr-comments

Read the comments, reviews, and inline threads on a PR. The agent groups the feedback by
reviewer and file. Without a target, it uses the current branch's PR.

In Claude Code or Codex, ask:

```text
Use pr-comments to read all feedback on https://github.com/acme/app/pull/42
```

The review skills also use this helper. It is hidden from Claude Code's slash-command
menu and does not change the PR.

See [SKILL.md](SKILL.md) for the full workflow.
