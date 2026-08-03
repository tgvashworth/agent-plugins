# Writing a pull request

How to find the issues a PR relates to, and how to write the title and body.
These rules apply whether the PR is being created for the first time or an
existing one is being rewritten.

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
  got there. Refer to files by their repo-relative path only — never
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
