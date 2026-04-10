---
name: pr-respond
description: |
  Respond to and resolve PR review comments. Reply to reviewer feedback,
  resolve addressed threads, and post follow-up comments. Use after
  implementing changes from PR feedback or when closing the loop with reviewers.
argument-hint: "[PR number or URL]"
disable-model-invocation: true
---

# PR respond

Reply to PR review comments and resolve threads after addressing feedback.

## Phase 1: Fetch comments

Run the pr-comments fetch script to get all PR comments, reviews, and review threads.

!`${CLAUDE_PLUGIN_ROOT}/skills/pr-comments/scripts/fetch-pr-comments.sh $ARGUMENTS 2>&1`

## Phase 2: Identify actionable threads

Focus on **unresolved** threads. For each one, check the current code to determine
whether the feedback has been addressed, then categorise:

| Category | When | Action |
|----------|------|--------|
| **Addressed** | Code change was made that satisfies the feedback | Resolve the thread; optionally reply explaining what changed |
| **Acknowledged** | Valid point but no code change needed (deliberate choice, out of scope) | Reply explaining why, leave unresolved for reviewer to close |
| **Needs discussion** | Unclear, ambiguous, or you disagree | Draft a reply for user review |

Present the categorisation as a table and **wait for user approval** before posting anything.

## Phase 3: Post replies and resolve threads

After the user approves, work through the plan.

### Reply to a review comment

Use the REST API to reply to the last comment in a thread:

```
gh api repos/{owner}/{repo}/pulls/{pr_number}/comments/{comment_database_id}/replies \
  -f body="..."
```

`{comment_database_id}` is the `databaseId` of the comment you are replying to
(typically the last comment in the thread).

### Resolve a review thread

Use the GraphQL mutation:

```
gh api graphql -f query='
  mutation {
    resolveReviewThread(input: {threadId: "{thread_node_id}"}) {
      thread { isResolved }
    }
  }'
```

`{thread_node_id}` is the `id` field on the review thread node.

### Post a general PR comment

```
gh pr comment {pr_number} --body "..."
```

## Guidelines

- **Never post without user approval.** Always present the plan first.
- **Keep replies concise.** "Fixed in abc1234" or "Good catch — updated to use X instead" is enough.
- **Don't be defensive.** Thank reviewers for catching things.
- **Only resolve addressed threads.** Don't resolve threads where the feedback wasn't acted on
  unless the user explicitly says to.
- **Batch related replies.** If multiple threads are about the same change, one reply
  referencing the fix beats N identical replies.
- **Reference commits when helpful.** "Fixed in abc1234" lets reviewers verify quickly.
- **Leave "acknowledged" threads unresolved.** The reviewer should decide whether to close them.
