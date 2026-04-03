---
name: bg
description: >
  Run a task in a background agent. Use when the user invokes /bg with a task
  description to spin off an autonomous sub-agent.
argument-hint: <task description>
disable-model-invocation: true
---

# Background Agent

Launch a background agent to handle a task autonomously.

## Instructions

If `$ARGUMENTS` is empty, tell the user: "Usage: `/bg <task description>`" and stop.

Otherwise, launch an Agent with:
- **prompt**: `$ARGUMENTS`
- **run_in_background**: `true`
- **description**: a 3-5 word summary of `$ARGUMENTS`

Then tell the user the agent has been launched.
