---
name: git-ship
description: Commit current changes, optionally push them, and create or update a draft or ready GitHub pull request. Use when the user asks to commit, ship, push, open a PR, or update the PR for the current branch.
---

# Ship git changes

Complete only the delivery steps the user requested. Infer one of these modes:

- **Commit:** create one local commit.
- **Draft PR:** commit, push, and create a draft PR; update an existing PR
  without changing its draft state.
- **Ready PR:** commit, push, and create a ready PR; update an existing PR and
  mark it ready if it is a draft.

User wording overrides these defaults.

## Prepare

Read the shared [commit guidance](../../templates/common.md). When a PR is in
scope, also read the [pull-request guidance](../../templates/pr-body.md).

Gather the relevant state, in parallel when possible:

- `git status --short`
- `git diff HEAD`
- `git branch --show-current`
- recent commits and commits on the branch relative to its actual base
- the current branch's upstream and push status when pushing
- the current branch's open PR, if any, when creating or updating a PR

Use the repository's actual default/base branch; do not assume it is `main`.
Preserve unrelated user changes and include only files that belong to the
requested change. If the scope is ambiguous, show the proposed file set before
staging it.

For PR modes, create a focused branch first if the current branch is the
repository's default branch. Choose a descriptive branch name from the change.

## Commit

1. Review the full diff and determine whether one coherent commit is possible.
2. Draft the message using the shared guidance and any user-supplied wording.
3. Stage only the intended files and create the commit.
4. Handle hook failures as described in the shared guidance.
5. Verify the resulting commit and working-tree state.

If there is nothing to commit, do not create an empty commit. For a PR mode,
continue only if the branch already contains commits that should be shipped.

## Push

For PR modes, push the current branch to its configured remote. Set an upstream
only when it does not already have one. Never force-push unless the user
explicitly requested history rewriting and the target has been verified.

Verify that the remote contains the intended commit before changing a PR.

## Create or update the PR

Build the title and body from the whole branch diff, not only the newest commit.
Follow the pull-request guidance, including checking related issues and making
the description understandable without conversation context.

- With no existing PR, create one in the requested ready/draft state.
- In **Draft PR** mode, update an existing PR in place and preserve its state.
- In **Ready PR** mode, update an existing PR in place and mark it ready when
  necessary.

Verify the final title, state, head/base branches, and URL. Return the commit
SHA and, when applicable, the PR URL. Report any deliberately uncommitted files.

After a ready PR is open, start the `review-agent` skill when that skill and a
background process capability are available, matching the existing
`commit-push-pr` workflow. Do not start it after a draft PR.
