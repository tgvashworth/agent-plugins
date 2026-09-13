# Learning ledger

Keep the private per-repository record at:

```text
~/.local/state/u/quiz/<repository-id>.md
```

Derive `<repository-id>` from the canonical `origin` URL as
`<host>/<owner>/<repository>`, removing `.git`. Without an origin, use
`_local/<repository-name>-<first-12-chars-of-SHA-256(canonical-root-path)>`.
In each component, replace characters other than letters, numbers, `.`, `_`,
and `-` with `_`. Create parent directories when needed.

Keep the record outside the repository. Do not edit repository instructions or
host memory. Current code always outranks old entries.

Treat understanding as module-specific: a concept demonstrated in one system
is not automatically demonstrated in another. Use a theme broad enough to
recognise in a later change, but narrow enough to have a stable answer within
the named module.

When resolving the first topic, append a session heading and entry. Append
later topics beneath the same heading before asking the next question:

```markdown
## YYYY-MM-DD — <branch, PR, or change>

- Module: <system or package>
  - Lens: design | conventions | behaviour
  - Theme: <reusable concept>
  - Result: demonstrated | prompted | unresolved
  - Learned or discussed: <concise conclusion>
  - Governing source: <repository-relative path or none>
  - Evidence: <file:line, permanent link, doc, or repro>
  - Change: <PR, commit, branch, or local change>
```

Record conclusions rather than verbatim answers or speculation. If the user
ends an unfinished topic, or the close discloses an important untested topic,
record it as unresolved. Do not narrate ledger writes between questions.
