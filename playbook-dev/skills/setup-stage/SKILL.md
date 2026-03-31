---
name: setup-stage
description: This skill should be used when the user asks to "design Stage 0", "create preflight checks", "define environment validation", "create scope document", "set up data validation", or needs to author the interactive setup stage of a playbook.
version: 0.1.0
---

# Setup Stage Design

Design Stage 0 (Setup/Preflight) with environment validation, data validation, scope creation, and exit criteria.

## Purpose of Stage 0

Stage 0 ensures the analysis environment is correctly configured before autonomous execution begins. This stage is:
- **Interactive** - Requires user confirmation
- **Sequential** - Checks run in order
- **Blocking** - All checks must pass before Stage 1

## Stage 0 Components

### 1. Environment Validation

Verify the execution environment is ready:

```markdown
# Check: Environment Validation

## Purpose
Ensure working directory and required tools are available.

## Steps
1. Verify working directory is playbook root
2. Check required directories exist
3. Validate symlinks resolve correctly
4. Confirm required tools are available

## Pass Criteria
- Working directory is correct
- All required directories exist
- Symlinks resolve to valid paths
- Required tools respond to version checks

## Failure Handling
Report missing requirements with installation instructions.
```

### 2. Data Validation

Verify input data is present and correctly structured:

```markdown
# Check: Data Validation

## Purpose
Ensure input data is available and correctly formatted.

## Steps
1. Verify input directory exists
2. Check required files are present
3. Validate file formats/schemas
4. Count items to be analyzed

## Pass Criteria
- Input directory exists
- Required files present
- Files pass format validation
- Item count > 0

## Failure Handling
Report missing or malformed files with expected format.
```

### 3. Baseline Configuration (Optional)

For comparison-based analysis:

```markdown
# Check: Baseline Configuration

## Purpose
Verify baseline data is available for comparison analysis.

## Steps
1. Check baseline directory/symlinks exist
2. Verify baseline files are accessible
3. Validate baseline format matches current

## Pass Criteria
- Baseline data accessible
- Formats are compatible
- Comparison scope is clear

## Failure Handling
Offer to proceed without baseline comparison.
```

### 4. Scope Creation

Create the scope.md document that configures the analysis:

```markdown
# Check: Scope Creation

## Purpose
Establish analysis scope with user confirmation.

## Scope Document Fields

| Field | Description | Source |
|-------|-------------|--------|
| Execution Mode | Interactive or Non-interactive | User choice |
| Focus | What questions to answer | User input |
| Data Bounds | What to analyze, filters | User input |
| Comparison | Baseline for comparison | User input |
| Confirmation | User approval timestamp | System |

## Steps
1. Ask user about execution mode
2. Ask about analysis focus/goals
3. Determine data bounds
4. Configure comparison (if applicable)
5. Present scope summary
6. Get explicit user confirmation
7. Write scope.md

## Pass Criteria
- All required fields populated
- User explicitly confirmed
- scope.md written successfully
```

## Stage README Template

```markdown
# Stage 0: Setup

{Brief description}

---

## Execution Context

| Aspect | Details |
|--------|---------|
| **Execution** | Sequential, interactive |
| **Agent** | Main agent (not sub-agents) |
| **User interaction** | Required (scope confirmation) |
| **Outputs** | `scope.md` in analysis directory |

---

## Preflight Checklist

Run each check in order. All checks must pass before proceeding to Stage 1.

| # | Check | File | Pass Criteria |
|---|-------|------|---------------|
| 1 | Environment | `environment.md` | Working directory valid |
| 2 | Data Validation | `data-validation.md` | Input data present and valid |
| 3 | Baseline (if applicable) | `baseline.md` | Comparison configured |
| 4 | Scope Creation | `scope-creation.md` | scope.md created, user confirmed |

---

## Exit Criteria

Preflight is complete when:

- [ ] Environment validated
- [ ] Data validated
- [ ] Baseline configured (if applicable)
- [ ] scope.md created with all required fields
- [ ] User has explicitly confirmed scope
- [ ] Context compaction requested (for long setups)

---

## Failure Handling

If any check fails:

1. **Stop immediately** - do not proceed to Stage 1
2. **Report the failure** clearly:
   ```
   PREFLIGHT CHECK FAILED

   Check: [check name]
   Issue: [what went wrong]

   Required action: [how to fix]
   ```
3. **Wait for user** to resolve
4. **Re-run the failed check** before continuing
```

## Scope Document Template

```markdown
# Analysis Scope

## Execution Configuration

| Setting | Value |
|---------|-------|
| **Mode** | {Interactive/Non-interactive} |
| **Created** | {timestamp} |
| **Confirmed by** | {user confirmation} |

## Analysis Focus

**Goal:** {What the user wants to learn}

**Key Questions:**
1. {Question 1}
2. {Question 2}
3. {Question 3}

## Data Bounds

**Input Path:** `{path}`
**Item Count:** {N} items
**Filters:** {Any filters applied}

## Comparison Configuration

**Baseline:** {path or "None"}
**Comparison Type:** {Full/Partial/None}

## Confirmation

User confirmed scope on {timestamp}.

---

*This scope document is read by all subsequent stages.*
```

## Context Compaction

After scope confirmation, compact conversation context:

**Why compact:**
- Setup accumulates exploration artifacts
- Long context slows sub-agent execution
- Sub-agents need focused context

**Compaction protocol:**
1. Inform user setup is complete
2. Request context compaction
3. After compaction, reload essential documents:
   - `playbook/instructions.md`
   - `{analysis_path}/scope.md`
   - `playbook/stages/1-{name}/README.md`
   - `playbook/reference/autonomous-operation.md` (if exists)

## Common Patterns

### Multi-Source Data Validation

When data comes from multiple sources:

```markdown
## Data Sources

| Source | Check | Required |
|--------|-------|----------|
| Primary data | Exists, valid format | Yes |
| Comparison baseline | Exists, compatible | No |
| External context | Accessible | No |
```

### Conditional Checks

Skip checks based on configuration:

```markdown
| # | Check | Condition | File |
|---|-------|-----------|------|
| 1 | Environment | Always | `environment.md` |
| 2 | Data | Always | `data-validation.md` |
| 3 | Baseline | If comparison requested | `baseline.md` |
```

## Additional Resources

For complete setup stage patterns:
- **`${CLAUDE_PLUGIN_ROOT}/references/playbook-pattern.md`** - Section 5: Stage 0
