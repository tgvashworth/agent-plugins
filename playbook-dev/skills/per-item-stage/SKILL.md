---
name: per-item-stage
description: This skill should be used when the user asks to "design Stage 1", "create per-item analysis", "define parallel analysis", "configure sub-agent prompts", "set up rolling pipeline", or needs to author the parallel per-item analysis stage.
version: 0.1.0
---

# Per-Item Stage Design

Design Stage 1 (Per-Item Analysis) with parallel sub-agent execution and rolling pipeline configuration.

## Purpose of Stage 1

Stage 1 performs deep-dive analysis on each item using parallel sub-agents. Each agent processes one item completely before the next item is assigned.

## Execution Model

### Rolling Pipeline

Instead of batch processing, maintain constant agent utilization:

```
Start: Launch N agents for items 1-N
Item 3 completes → immediately launch agent for item N+1
Item 7 completes → immediately launch agent for item N+2
Continue until all items processed
```

**Benefits:**
- No idle time waiting for slowest agent
- Constant resource utilization
- Faster overall completion

### Agent Count Guidelines

| Item Count | Recommended Agents | Reasoning |
|------------|-------------------|-----------|
| <20 | 10-15 | Lower parallelism, faster per-item |
| 20-50 | 15-25 | Balance parallelism and stability |
| 50-100 | 20-30 | Higher throughput |
| >100 | 25-35 | Maximum reasonable parallelism |

**Rule of thumb:** Target 2x agent count = 2 full cycles through queue.

## Stage Structure

```
stages/1-per-item/
├── README.md                    # Stage overview
├── diagnosis.md                 # Analysis type 1
├── evidence-assessment.md       # Analysis type 2
├── capability-gaps.md           # Analysis type 3
├── comparison-analysis.md       # Conditional analysis
└── ...
```

## Stage README Template

```markdown
# Stage 1: Per-{Item} Analysis

Deep-dive analysis of each {item} to {purpose}.

---

## Execution Context

| Aspect | Details |
|--------|---------|
| **Execution** | Parallel sub-agents |
| **Agent count** | {N} concurrent |
| **Strategy** | Rolling pipeline |
| **User interaction** | None |
| **Outputs** | `{items}/*/analysis/` |

---

## Inputs per {Item}

Each sub-agent receives:
- `{item}/source-file-1.md` - {Description}
- `{item}/source-file-2.md` - {Description}
- `{item}/source-file-3.md` - {Description}
- `comparison/` - Baseline data (if exists)

## Outputs per {Item}

Each sub-agent produces in `{item}/analysis/`:

| # | Analysis | File | Purpose |
|---|----------|------|---------|
| 1 | Diagnosis | `diagnosis.md` | {Purpose} |
| 2 | Evidence | `evidence-assessment.md` | {Purpose} |
| 3 | Gaps | `capability-gaps.md` | {Purpose} |
| 4 | Comparison | `comparison-analysis.md` | {Purpose} (conditional) |

---

## Parallelization Strategy

### Rolling Pipeline

```
Launch {N} agents for items 1-{N}
As each completes, launch next item
Maintain constant {N}-agent utilization
```

### Error Handling

- Track failed items separately
- Re-launch failed items after initial pass
- Kill stuck agents after {timeout} minutes
- Maintain retry count per item

---

## Sub-Agent Instructions

Each sub-agent:

1. **Read** the stage README and analysis files
2. **Process** their assigned item:
   - Read all input files for the item
   - Execute each analysis in sequence
   - Write output files
3. **Verify** outputs are complete
4. **Report** completion or failure

---

## Exit Criteria

Stage 1 is complete when:

- [ ] All items have `analysis/` directory
- [ ] All required files exist per item
- [ ] Files are non-trivial (>500 bytes)
- [ ] Verification script shows 100% complete
```

## Analysis Document Patterns

### Common Analysis Types

| Analysis | Purpose | Key Outputs |
|----------|---------|-------------|
| Diagnosis | Classify success/failure | Classification tags, verdict |
| Evidence Assessment | Map information flow | Gap categories, reach score |
| Capability Gaps | Identify missing capabilities | Impact estimates, priorities |
| Comparison | Delta vs baseline | Metric changes, attribution |

### Analysis Template

```markdown
# Analysis: {Name}

## Purpose

{What this analysis captures - enables Stage 2 aggregation by {dimension}}

## Output

**File:** `analysis/{name}.md`

## Instructions

### What to Analyze

1. **{Source 1}** from `{file}`
   - Extract: {what}
   - Classify: {how}

2. **{Source 2}** from `{file}`
   - Extract: {what}
   - Map to: {what}

### How to Perform Analysis

**Step 1: Read source files**
- `{file1}` - {purpose}
- `{file2}` - {purpose}

**Step 2: {Analysis step}**
{Instructions}

**Step 3: Classify using tags**
{Tag checklist}

**Step 4: Write output**
{Template reference}

## Template

[Include full output template]

## Guidance

### Classification Tags

| Tag | Definition | When to Use |
|-----|------------|-------------|
| {Tag 1} | {Definition} | {Criteria} |
| {Tag 2} | {Definition} | {Criteria} |

### Example

[Concrete example of good output]

## Common Pitfalls

**Don't:**
- Skip classification tags (needed for Stage 2)
- Write vague assessments
- Miss conditional sections

**Do:**
- Use explicit tags
- Provide specific evidence
- Note items for cross-reference
```

## Cross-Reference Support

Enable Stage 2 aggregation by:

### Consistent Classification Tags

```markdown
### Failure Classification
- [ ] Misattributed blame
- [ ] Shallow analysis
- [ ] Pattern matching over primary analysis
- [ ] Evidence synthesis failure
```

### Cross-Item References

```markdown
**Similar patterns in other items:**
- ITEM-123: Similar {pattern}
- ITEM-456: Related {issue}
```

### Machine-Readable Sections

```markdown
## Metrics Summary

| Metric | Value |
|--------|-------|
| Primary Score | X% |
| Secondary Score | Y% |
| Classification | {Tag} |
```

## Conditional Analyses

Some analyses only run under certain conditions:

```markdown
## comparison-analysis.md (Conditional)

**Condition:** Only if `comparison/` symlink exists

**Purpose:** Delta analysis vs baseline

**Skip when:** No baseline configured in scope.md
```

## Verification

After Stage 1, verify completion:

```bash
# Check each item has analysis directory
# Check required files exist
# Check file sizes > 500 bytes
# Report completion percentage
```

## Additional Resources

For complete per-item stage patterns:
- **`${CLAUDE_PLUGIN_ROOT}/references/playbook-pattern.md`** - Section 5: Stage 1
