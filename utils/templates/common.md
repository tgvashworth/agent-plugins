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
- First line: Clear, concise summary of the change
- Bullet points: Only if there are multiple important details
- Next steps: Only if there are obvious follow-up tasks
- No attribution footers
- Match the existing commit style in the repository

## Step-by-step Verification

Always verify at each step:
1. Before committing: Check `git status` and `git diff`
2. After committing: Verify commit was created successfully
3. Before pushing: Confirm branch and remote are correct
4. After pushing: Verify push succeeded
5. After PR creation: Confirm PR URL is returned
