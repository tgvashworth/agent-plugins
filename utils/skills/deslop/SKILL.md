---
name: deslop
description: |
  Rewrite words for one-pass comprehension: code comments, user-facing copy
  and microcopy, commit messages, PR titles and bodies, ticket titles and
  bodies. Plain English, short sentences, no filler, no AI tells, no
  personification, no agent working memory. Use when the user says "deslop",
  "fix the copy", "tidy the comments", "clean up this commit message", "make
  this PR readable", or asks for a plain-English pass over any text a person
  will read.
argument-hint: "[file, diff range, PR, commit, ticket, or pasted text]"
---

# Deslop

Make every word in the target hand over its meaning in one pass. You change
the words a person reads. You do not change logic, markup, structure,
interpolation variables, or behaviour.

Read the rules first — they are the authority for every judgement below:

`${CLAUDE_PLUGIN_ROOT}/skills/deslop/references/style.md`

## Phase 0: Resolve the target

Work out what `$ARGUMENTS` points at. Pick the first match:

| Argument | Target | Scope |
|----------|--------|-------|
| *(empty)* | The branch diff (`git diff main...HEAD` plus uncommitted changes) | Comments and user-facing strings on lines the diff added or changed |
| `comments` / `copy` | Same diff, narrowed to that kind of string | As above, one kind only |
| A file path or glob | Those files | Every comment and user-facing string in them (a whole-file pass) |
| `commit`, `HEAD`, or a commit SHA | That commit's message | Subject and body |
| `pr`, a PR number, or a GitHub PR URL | That PR | Title and body |
| A Linear issue key (`ABC-123`) or URL | That ticket | Title and description |
| Anything else — quoted text, a pasted message, a sentence | The text itself | Rewrite it in your reply |

If the argument is ambiguous (a bare number could be a PR or a ticket), check
`gh pr view <n>` first and fall back to a ticket lookup.

Load the target's conventions alongside the style rules:

- Commit messages: the repo's own style from `git log`, then
  `${CLAUDE_PLUGIN_ROOT}/templates/common.md`.
- PRs: `${CLAUDE_PLUGIN_ROOT}/templates/pr-body.md`.
- Copy: the repo's glossary, style guide, or CLAUDE.md if one names terms.

## Phase 1: Collect

Gather every in-scope string with a `file:line` (or field name) reference.
For diffs, only lines the diff touched are in scope — neighbouring legacy
text is fix-on-touch: note it in the report if it is badly off, but do not
rewrite it unless the caller asked for a whole-file pass.

For a PR or ticket, read the *current* branch or issue state too. A stale
description is the most common problem, and the fix is to describe what is
there now, not to polish what was written then.

## Phase 2: Cold read and rewrite

For each string, read it once as a stranger mid-task. Ask:

- Does the meaning arrive whole in one pass, or does it need decoding?
- Does any phrase draw attention to itself — a nice turn, a flourish, a joke?
- Does it hit an anti-pattern or a ban in the rules?
- For comments: could a reader with only the code in front of them use it?
  Does it point at a ticket, a PR, a person, or a moment in time?
- For commit, PR, and ticket text: would someone with no context understand
  the problem and the change?

Rewrite offenders. Keep rewrites minimal — change the words, keep everything
around them. A rewrite must state the same fact. If the right wording depends
on a decision you cannot see (which of two terms is canonical, what a feature
is actually called), flag it instead of guessing.

Delete rather than rewrite when the string says nothing: a comment that
restates the code, a "successfully" with no fact behind it, a filler sentence.

## Phase 3: Apply

How to land the change depends on the target:

| Target | How |
|--------|-----|
| Files | Edit in place. |
| Commit message | If it is `HEAD` and not yet pushed, `git commit --amend`. Otherwise show the rewrite and stop — never rewrite pushed history. |
| PR | `gh pr edit <n> --title … --body …`. |
| Ticket | Update via the Linear tool if one is available; otherwise show the rewrite. |
| Pasted text | Reply with the rewrite. |

Never push. Never touch lines, files, or fields outside the resolved scope.

## Phase 4: Report

End with a table: location, before, after, and the rule that applied. List
separately anything you flagged but left (with the open question) and any
off-style legacy text you noticed outside scope. If everything already
passed, say so in one line.

Then do one last cold read of your own report. It is text a person will read
once too.
