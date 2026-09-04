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

Only apply this workflow when the user explicitly invokes it. If it was selected
implicitly, do not delegate the task.

If the user did not provide a task, tell them: "Usage: `/bg <task description>`" and stop.

Otherwise, use the host's background-delegation capability. Give the worker the
task from the user's request, only the context it needs, a clear deliverable,
and a short 3-5 word label.

Do not expand the worker's authority beyond the user's request. If the host
cannot delegate work in the background, say so instead of silently switching
to a foreground workflow.

Then tell the user what was delegated and how the result will be returned.
