# Utils

`/u`: useful Claude commands, with the same workflows available as Agent Skills
for Codex and other compatible hosts. In Codex, ask naturally or explicitly use
skills such as `$git-ship`, `$task-context`, or `$pr-feedback`.

## Commands

### `/context [guidance]`

Switch context and get up to speed with a task. Accepts a ticket reference, branch name, or general guidance. Orients its summary toward next steps based on what you give it.

### `/commit [guidance]`

Create a git commit with an auto-generated message.

- Analyzes current changes
- Matches your repository's commit style
- Handles pre-commit hooks automatically
- Optional: Provide guidance text to influence the commit message

**Example:**
```bash
/commit
/commit "focus on the bug fix, not the refactoring"
```

### `/commit-push-pr [guidance]`

Create a commit, push to remote, and open a pull request.

- Creates a branch if you're on main/master
- Commits changes with verification
- Pushes to remote
- Opens a PR with auto-generated description
- If a draft PR already exists, re-writes its description from scratch and marks it ready for review
- Optional: Provide guidance for commit/PR messages

**Example:**
```bash
/commit-push-pr
/commit-push-pr "this is a breaking change"
```

### `/commit-push-draft [guidance]`

Same as `/commit-push-pr` but creates a draft PR. If a PR already exists for the branch, updates it in place instead (leaving its draft/ready state alone).

**Example:**
```bash
/commit-push-draft
/commit-push-draft "WIP - needs more testing"
```

### `/bg <task>`

Spin off a task to a background agent. The argument becomes the agent's prompt.

**Example:**
```bash
/bg refactor the auth module to use the new middleware
/bg investigate why the billing tests are flaky
```

### `/remember [instruction]`

Append a convention, fact, or instruction to the project's shared `AGENTS.md` or `CLAUDE.md`. Also auto-activates when conventions or corrections come up in conversation.

**Example:**
```bash
/remember always run make lint before committing
/remember API handlers must return structured errors using pkg/apierror
```

### `/ready-for-review [PR number or URL]`

Take a draft PR whose description has gone stale, rewrite the title and body from scratch against what the branch actually contains, and mark it ready for review. Stops if you have uncommitted or unpushed work, then hands off to the review agent.

**Example:**
```bash
/ready-for-review
/ready-for-review 42
```

### `/pr-feedback [PR number or URL]`

Triage and act on PR review feedback. Fetches all comments, categorises each as implement/acknowledge/decline, plans changes, and implements approved fixes.

**Example:**
```bash
/pr-feedback
/pr-feedback 42
```

### `/pr-comments [PR number or URL]`

Fetch all PR comments, reviews, and review threads via a single GraphQL call.

**Example:**
```bash
/pr-comments
/pr-comments https://github.com/org/repo/pull/42
```

### `/tourguide [commit range, branch, PR, or plan]`

Walk through code changes or a plan in a logical, grouped sequence — one group at a time, pausing after each for questions or feedback. Instead of dumping a raw diff, organises related pieces together and presents them incrementally.

**Example:**
```bash
/tourguide
/tourguide feature/auth-refactor
/tourguide 42
```

### `/what [what was unclear]`

Re-explain the previous message in plain English — reconnect it to the thread, define only what you introduced, bottom line first. Use it when a reply didn't land.

**Example:**
```bash
/what
/what "the bit about the migration"
```

### `/deslop [target]`

Rewrite words for one-pass comprehension — code comments, user-facing copy, commit messages, PR titles and bodies, ticket titles and bodies. Plain English, short sentences, no filler or AI tells, no personification, no agent working memory in comments. Only the words change; logic, markup, and variables stay put.

**Example:**
```bash
/deslop                       # comments and strings in the branch diff
/deslop src/forms.py          # whole-file pass
/deslop commit                # amend HEAD's message (if unpushed)
/deslop 42                    # PR title and body
/deslop ABC-123               # ticket title and description
/deslop "Oops! Something went wrong. Please try again later!"
```

### `/slack [draft|send] [to <person or #channel>] [what to say]`

Write a Slack message from what the session just did. By default the reply is the bare message, nothing else, so `/copy` grabs it and it pastes cleanly into Slack's composer. Say `draft` or `send` with a recipient to go through the Slack tool instead. The message is written in whichever Slack formatting dialect matches the delivery path; the rules, verified by round-tripping real messages, are in `skills/slack/references/slack-formatting.md`.

**Example:**
```bash
/slack
/slack draft to Pete: migration is done, needs a sign-off on the flag
```

### `/write [topic, draft file path, or guidance]`

Write or improve a substantial document through a structured process: fix the goals, outline the key points, map the audience, design the structure, draft it, then run two independent review passes (a cold-read for clarity and a style pass for LLM-isms and British English).

**Example:**
```bash
/write proposal to move billing onto the new pipeline
/write docs/rfc-auth.md
/write "make this readable for the leadership team"
```

## Features

- **Fast**: Minimal overhead, executes quickly
- **Step verification**: Checks each operation before proceeding
- **Pre-commit hook handling**: Automatically retries if hooks modify files
- **Style matching**: Analyzes your repo's commit history to match existing style
- **Clean messages**: Short, actionable commit and PR descriptions

## Installation

Install it from the repository's Claude Code or Codex marketplace. Other Agent
Skills hosts can load the `skills/` directory directly.

## Requirements

- Git
- GitHub CLI (`gh`) for PR commands
