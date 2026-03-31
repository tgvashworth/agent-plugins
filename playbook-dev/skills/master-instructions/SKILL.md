---
name: master-instructions
description: This skill should be used when the user asks to "write instructions.md", "create master orchestration", "define stage sequencing", "configure agent counts", "set operational constraints", or needs to author the main playbook instructions file.
version: 0.1.0
---

# Master Instructions Authoring

Create the `instructions.md` file that orchestrates the entire playbook execution.

## Purpose of instructions.md

The master instructions document is the single entry point that:
- Defines stage sequencing and dependencies
- Specifies agent counts for parallel stages
- Sets operational constraints for autonomous execution
- Documents file dependencies and data flow
- Provides navigation for different execution modes

## Document Structure

```markdown
# {Playbook Name} Instructions

## Overview

{1-2 paragraphs describing playbook purpose and scope}

## Quick Start

{Minimal steps to run the playbook}

## Stage Sequencing

| Stage | Name | Execution | Agent Count | Inputs | Outputs |
|-------|------|-----------|-------------|--------|---------|
| 0 | Setup | Sequential, Interactive | 1 | User input | scope.md |
| 1 | Per-Item | Parallel | N | scope.md, items/ | items/*/analysis/ |
| 2 | Aggregation | Sequential | 1 | Stage 1 outputs | cohort-analysis/ |
| 3 | Synthesis | Parallel (optional) | 3 | Stages 1-2 | synthesis/ |
| 4 | Finalization | Sequential | 1 | All prior | SUMMARY.md |

## Stage Details

### Stage 0: {Setup Name}

**Entry point:** `stages/0-{name}/README.md`

**Purpose:** {What this stage accomplishes}

**Execution:**
- Mode: Interactive (requires user confirmation)
- Agent: Main agent
- Duration: 5-10 minutes

**Outputs:**
- `scope.md` - Analysis scope and configuration

**Exit to Stage 1 when:**
- [ ] All preflight checks pass
- [ ] scope.md created
- [ ] User confirmed

### Stage 1: {Per-Item Name}

**Entry point:** `stages/1-{name}/README.md`

**Purpose:** {What this stage accomplishes}

**Execution:**
- Mode: Parallel sub-agents
- Agent count: {N} concurrent
- Strategy: Rolling pipeline

**Parallelization:**
```
Launch {N} agents for items 1-{N}
As each completes, launch next item
Maintain constant {N}-agent utilization
```

**Outputs per item:**
- `analysis/diagnosis.md`
- `analysis/evidence-assessment.md`
- `analysis/{other}.md`

**Exit to Stage 2 when:**
- [ ] All items processed
- [ ] Verification script shows 100% complete

### Stage 2: {Aggregation Name}

...

## File Dependencies

```
User input
    ↓
scope.md (Stage 0)
    ↓
items/*/analysis/*.md (Stage 1)
    ↓
cohort-analysis/*.md (Stage 2)
    ↓
synthesis/*.md (Stage 3)
    ↓
SUMMARY.md (Stage 4)
```

## Operational Constraints

### Autonomous Operation

Stages 1-4 run without user interaction. Follow these rules:

| Operation | Tool | Autonomous? |
|-----------|------|-------------|
| Create files | Write tool | Yes |
| Read files | Read tool | Yes |
| Edit files | Edit tool | Yes |
| Create directories | Write tool (auto-creates) | Yes |
| Shell file operations | cat >, echo > | NO - breaks workflow |

### Context Management

After Stage 0, request context compaction then reload:
1. `playbook/instructions.md`
2. `scope.md`
3. `stages/1-{name}/README.md`
4. `reference/autonomous-operation.md` (if exists)

### Error Handling

**Stage-level failures:**
- Stop immediately on preflight failures
- Report clearly: check name, issue, required action
- Wait for user resolution

**Item-level failures:**
- Track failed items separately
- Re-launch failed items only
- Kill stuck agents after timeout

## Execution Modes

### Interactive Mode

```
Stage 0 → Review → Stage 1 → Review → Stage 2 → Review → ...
```

Pause after each stage for user review.

### Non-Interactive Mode

```
Stage 0 → Stage 1 → Stage 2 → Stage 3 → Stage 4
```

Run all stages autonomously after initial setup.

## Reference Documents

- `reference/taxonomy.md` - Classification systems
- `reference/glossary.md` - Term definitions
- `reference/architecture.md` - Domain system structure
```

## Key Sections

### Stage Sequencing Table

Define clear dependencies:

```markdown
| Stage | Depends On | Blocks |
|-------|------------|--------|
| 0 | None | 1, 2, 3, 4 |
| 1 | 0 | 2, 3 |
| 2 | 1 | 3, 4 |
| 3 | 1, 2 | 4 |
| 4 | 1, 2, 3 | None |
```

### Agent Count Configuration

Balance parallelism with stability:

| Workload Size | Recommended Agents |
|---------------|--------------------|
| <20 items | 10-15 agents |
| 20-50 items | 15-25 agents |
| 50-100 items | 20-30 agents |
| >100 items | 25-35 agents |

Target: 2x agent count = 2 full cycles through item queue.

### Operational Constraints

Critical for autonomous execution:

1. **File operations** - Use Write/Read/Edit tools only
2. **No shell writes** - Avoid cat >, echo >, heredocs
3. **Relative paths** - From playbook root
4. **Context compaction** - After Stage 0 setup

### File Dependencies Diagram

Show data flow clearly:

```
[Input] → Stage 0 → [scope.md]
                         ↓
[Items] → Stage 1 → [item/*/analysis/*.md]
                         ↓
              Stage 2 → [cohort-analysis/*.md]
                         ↓
              Stage 3 → [synthesis/*.md]
                         ↓
              Stage 4 → [SUMMARY.md]
```

## Writing Guidelines

### Be Explicit

Specify exact file paths, not general descriptions:
- Good: `stages/1-per-investigation/README.md`
- Bad: "the stage 1 readme"

### Define Exit Criteria

Every stage needs checkable exit conditions:
```markdown
**Exit to Stage N+1 when:**
- [ ] All outputs exist
- [ ] Verification passes
- [ ] (Interactive only) User confirmed
```

### Document Agent Handoffs

Specify what each agent receives and produces:
```markdown
**Agent receives:**
- scope.md
- stages/1-{name}/README.md
- item/{id}/ directory

**Agent produces:**
- item/{id}/analysis/diagnosis.md
- item/{id}/analysis/evidence-assessment.md
```

## Additional Resources

For complete orchestration patterns:
- **`${CLAUDE_PLUGIN_ROOT}/references/playbook-pattern.md`** - Sections 4-5
