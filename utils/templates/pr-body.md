# Writing a pull request

How to find the issues a PR relates to, and how to write the title and body.
These rules apply whether the PR is being created for the first time or an
existing one is being rewritten.

## Writing the title

This governs the PR title and the commit subject (the first line) — under
squash-merge they become the same line, and it is what anyone scanning
`git log`, a release page or a blame has to work from.

### The test

**Name the thing that changed and what now happens to it.** Someone who has
never seen this change should be able to guess which files it touches.

### Rules

- Open with the conventional-commit prefix (`feat:`, `fix:`, `refactor:`,
  `perf:`, `docs:`, `test:`, `chore:`, `build:`, `ci:`, `style:`), then say what
  changed.
- **Name at least one real, findable thing** — the page, model class, management
  command, admin screen, URL, setting, flag or file. If the title contains no
  noun you could grep the codebase for, it fails the test.
- **Never open with an article or "what" followed by a generic noun.** "the
  sweep", "a question", "what the conversions left standing" read as riddles
  because the subject is a pronoun in disguise. This is the most common failure.
- **Do not give code intentions.** Code does not own up, admit, want or decide.
  Say what it now does.
- Under 72 characters where you can.
- Plain, natural English is right; vagueness is not. "stop the equipment admin
  page rebuilding its dropdowns per row" is both natural and specific.
- **Say what you mean, literally.** No metaphor or flourish in the title or
  body: "reduce the retry limit", not "tame the retry storm". A figure of
  speech makes the reader translate and carries connotations you did not
  choose. When a literal phrase is available, use it.

### Where house style comes from

Before drafting, look for a house style file, first match wins:

1. `.github/COMMIT_STYLE.md`
2. `.claude/commit-style.md`

**If one exists, it is the only source of style.** Read it and follow it, and
**do not read `git log` for phrasing** — the log may already carry the drift
that file exists to correct. The rules above still apply; the file refines them.

**If neither exists**, sample `git log --oneline -20` to infer local convention
— but check what you find against the test above before copying it. If recent
titles fail the test, do not imitate them: follow the rules above instead, and
say so in your reply so the drift is visible to the user.

## Finding related issues

Identify **every** issue this change is relevant to. The right issue is often
not obvious, so dig in a few places:

- The branch name (e.g. `feature/123-foo` → `#123`)
- User guidance and the branch's commit messages
- Open issues describing the problem this change solves — run `gh issue list`
  or `gh search issues "<keywords from the diff>"` and match them against what
  actually changed

For each candidate, run `gh issue view <number>` to confirm it exists and that
this change genuinely addresses it, then decide whether the PR *closes* it
(fully resolves it) or merely *relates to* it (touches it without resolving it).

## Drafting the body in two passes

Always draft in two passes. When a PR already exists, re-evaluate it as if
writing from scratch: base the description on the *current* state of the branch
and ignore the existing body rather than lightly editing it.

- *Pass 1 — capture the change:* Based on ALL commits in the branch (not just
  the latest), write what changed and why.
- *Pass 2 — rewrite for a stranger:* Rewrite the description from the
  perspective of someone with no prior context on this change. The PR must
  stand on its own — explain the problem and the change in simple, clear words,
  with enough context to understand it cold. Strip out any references to
  development-discussion internals (review back-and-forth, "as discussed",
  earlier attempts, iteration history); describe the end result, not how you
  got there. Use literal statements, not metaphor or flourish. Refer to files by their repo-relative path only — never
  machine-local or home-directory paths (see "Referring to files" in
  `common.md`).

## Format

Summary (1-3 bullets), test plan checklist, next steps if relevant.

## Linking issues

**Required — do not skip.** In the PR body, reference every relevant issue
found above, each on its own line, using the correct keyword:

- `Closes #<number>` for each issue this PR fully resolves
- `Refs #<number>` for issues that are relevant but not fully resolved here

If, after genuinely checking, no issue is relevant, say so in your reply to the
user (not in the PR body) so it's clear the step wasn't simply forgotten.
