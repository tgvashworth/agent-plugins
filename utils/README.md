# Utils

`/u`: useful Claude commands.

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
- Optional: Provide guidance for commit/PR messages

**Example:**
```bash
/commit-push-pr
/commit-push-pr "this is a breaking change"
```

### `/commit-push-draft [guidance]`

Same as `/commit-push-pr` but creates a draft PR.

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

## Skills (auto-activated)

### `pr-feedback`

Triage and act on PR review feedback. Fetches all comments, categorises each as implement/acknowledge/decline, plans changes, and implements approved fixes.

### `pr-comments`

Fetch all PR comments, reviews, and review threads via a single GraphQL call. Used by `pr-feedback` and available for direct use.

## Features

- **Fast**: Minimal overhead, executes quickly
- **Step verification**: Checks each operation before proceeding
- **Pre-commit hook handling**: Automatically retries if hooks modify files
- **Style matching**: Analyzes your repo's commit history to match existing style
- **Clean messages**: Short, actionable commit and PR descriptions

## Installation

Copy this plugin to your Claude Code plugins directory or install via the marketplace.

## Requirements

- Git
- GitHub CLI (`gh`) for PR commands
