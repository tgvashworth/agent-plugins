---
name: ready-for-review
description: |
  Rewrite an existing draft PR's title and body from scratch, then mark it
  ready for review. Use when the user says "ready for review", "this draft is
  ready", "open my draft PR for review", or asks to tidy up a draft PR's
  description before sending it to reviewers.
argument-hint: "[PR number or URL]"
---

# Ready for review

A draft PR has been sitting there while the work took shape, so its description
is almost certainly stale — written against an early version of the branch, or
never written properly at all. Rewrite it against what the branch actually
contains now, then open it for review.

This complements the other PR skills — `commit-push-draft` (create the draft),
`review-agent` (watch the review), `pr-feedback` (act on it). Use **this** skill
when the code is already pushed and the only thing left is to present it well
and hand it over.

## Phase 0: Resolve the PR

If `$ARGUMENTS` is a PR number or URL, use it. Otherwise detect the PR for the
current branch:

```
gh pr view --json number,title,url,isDraft,baseRefName,headRefName
```

If there's no PR for the branch, tell the user and stop — suggest
`/commit-push-pr` instead.

If the PR is **not** a draft, it is already open for review. Still rewrite the
title and body, but skip the `gh pr ready` step and say so in your reply.

## Phase 1: Check the branch is actually ready

The point of this skill is that reviewers see the finished thing, so make sure
the PR contains all the work:

```
git status --porcelain
git log --oneline origin/<headRefName>..HEAD
```

If there are uncommitted changes or unpushed commits, **stop**. Tell the user
what is outstanding and suggest `/commit-push-pr`, which will commit, push, and
ready the PR in one go. Do not ready a PR whose branch is missing local work —
reviewers would be reading a description of code that isn't there.

## Phase 2: Read the whole change

Base the rewrite on the branch as it stands, not on the existing PR body:

```
git log --oneline <baseRefName>..HEAD
git diff <baseRefName>...HEAD
```

Read the existing body once, only to salvage facts worth keeping (a test plan
that still applies, a genuine caveat). Everything else gets rewritten.

## Phase 3: Write the title and body

Read the PR writing guide and follow it:

`${CLAUDE_PLUGIN_ROOT}/templates/pr-body.md`

It covers finding related issues, the two-pass drafting method, the format, and
the issue-linking rules. Follow it exactly — including the second pass, which
is the one that matters here. A draft body written mid-work is full of context
only you have; the rewrite has to stand on its own for a reviewer coming in
cold.

Rewrite the **title** too. Draft titles are often placeholders ("wip", "try
something") or describe where the work started rather than where it landed.

## Phase 4: Update and open for review

```
gh pr edit <number> --title "<title>" --body "<body>"
gh pr ready <number>
```

Verify both succeeded and return the PR URL.

## Phase 5: Hand over to review

Immediately start the `review-agent` skill on the PR to kick off a background
review and watch for incoming feedback (CI, bots, reviewers).
