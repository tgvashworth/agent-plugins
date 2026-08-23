# Common Commit Workflow Instructions

## Pre-commit Hook Handling

When creating commits:
1. Monitor the exit code of the commit command
2. If the commit fails (non-zero exit code), check if it was due to pre-commit hooks
3. If pre-commit hooks modified files:
   - Run `git status` to see what changed
   - Stage the modified files
   - Retry the commit ONCE with the same message
4. If the commit fails again, report the error to the user

## Commit Message Format

Keep commit messages short and actionable:

**Format:**
```
[What changed in 1-2 sentences]

[Optional: Up to 5 bullet points with details]

[Optional: Notes on what should come next]
```

**Guidelines:**
- First line: the subject — write it per "Writing the title" below
- Bullet points: Only if there are multiple important details
- Next steps: Only if there are obvious follow-up tasks
- No attribution footers

## Writing the title

This governs the commit subject (the first line) and the PR title — under
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

## Referring to files

In commit messages and PR descriptions, always refer to files by their
**repository-relative path** (e.g. `utils/skills/remember/SKILL.md`).

**Never include machine-local paths** — home-directory paths (`~/`, `~/.claude`,
`$HOME/...`) or absolute paths under a user's home (`/Users/<name>/...`,
`/home/<name>/...`). They are specific to one machine, meaningless to anyone
else reading the commit or PR, and must never appear in shared git history. If a
diff or your working notes surface such a path, rewrite it as a repo-relative
path (or drop it) before it reaches the message or PR body.

## Step-by-step Verification

Always verify at each step:
1. Before committing: Check `git status` and `git diff`
2. After committing: Verify commit was created successfully
3. Before pushing: Confirm branch and remote are correct
4. After pushing: Verify push succeeded
5. After PR creation: Confirm PR URL is returned
