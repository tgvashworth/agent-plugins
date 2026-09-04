---
name: bg
description: >
  Run a task in a background agent. Use when the user invokes /bg with a task
  description to spin off an autonomous sub-agent.
argument-hint: <task description>
---

# Background Agent

Launch a background agent to handle a task autonomously.

## Instructions

If the user did not provide a task, tell them: "Usage: `/bg <task description>`" and stop.

Otherwise, launch an Agent with:
- **prompt**: the task from the user's request
- **run_in_background**: `true`
- **description**: a 3-5 word summary of the task

Then tell the user the agent has been launched.
