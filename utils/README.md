# Utils

`/u`: useful Claude commands.

## Commands

### `/context [guidance]`

Get up to speed with the current task by reviewing git state, recent commits, modified files, and any external references.

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
