---
name: quality-gates
description: This skill should be used when the user asks to "define quality gates", "create exit criteria", "design validation steps", "set up stage prerequisites", "define completion criteria", or needs to establish quality checkpoints between playbook stages.
version: 0.1.0
---

# Quality Gates

Define prerequisites, validation steps, and exit criteria for each playbook stage.

## What are Quality Gates?

Quality gates are checkpoints that ensure:
- Prerequisites are met before starting
- Validation occurs during execution
- Exit criteria are satisfied before proceeding

## Gate Components

### Prerequisites

What must exist before starting a stage:

```markdown
## Prerequisites

Before starting Stage N:

- [ ] Stage N-1 complete
- [ ] Required files exist:
  - `{file1}`
  - `{file2}`
- [ ] Configuration valid:
  - `scope.md` has required fields
  - Paths resolve correctly
- [ ] Resources available:
  - {Resource 1}
  - {Resource 2}
```

### Validation Steps

What to check during execution:

```markdown
## Validation Steps

During Stage N execution:

1. **Input validation**
   - Verify file formats
   - Check data completeness
   - Validate schema compliance

2. **Process validation**
   - Monitor for errors
   - Check intermediate outputs
   - Verify expected behavior

3. **Output validation**
   - Confirm files created
   - Check minimum content thresholds
   - Validate cross-references
```

### Exit Criteria

What must be true before proceeding:

```markdown
## Exit Criteria

Stage N is complete when:

- [ ] All required outputs exist
- [ ] Outputs are non-trivial (>500 bytes)
- [ ] Verification script passes
- [ ] No unresolved errors
- [ ] (Interactive only) User confirmed
```

## Gate Design Patterns

### Stage 0 Gates (Setup)

```markdown
## Stage 0: Prerequisites
- Working directory is correct
- Required tools available

## Stage 0: Validation
- Environment checks pass
- Data validation succeeds
- Scope document created

## Stage 0: Exit Criteria
- [ ] All preflight checks pass
- [ ] scope.md created with required fields
- [ ] User explicitly confirmed
- [ ] Context compacted (if lengthy setup)
```

### Stage 1 Gates (Per-Item)

```markdown
## Stage 1: Prerequisites
- Stage 0 complete
- scope.md exists
- Items directory populated

## Stage 1: Validation
- Each item has required inputs
- Sub-agents complete successfully
- Outputs meet format requirements

## Stage 1: Exit Criteria
- [ ] All items processed
- [ ] Each item has analysis/ directory
- [ ] Required files exist per item:
  - diagnosis.md
  - evidence-assessment.md
  - {other}.md
- [ ] Files are non-trivial (>500 bytes)
- [ ] Verification script shows 100%
```

### Stage 2 Gates (Aggregation)

```markdown
## Stage 2: Prerequisites
- Stage 1 complete (100%)
- All analysis files accessible

## Stage 2: Validation
- Can read all Stage 1 outputs
- Clustering assignments valid
- Cross-references resolve

## Stage 2: Exit Criteria
- [ ] All cluster files created
- [ ] Each item assigned to clusters
- [ ] Cross-cluster analysis complete
- [ ] Priority framework defined
```

### Stage 3 Gates (Synthesis)

```markdown
## Stage 3: Prerequisites
- Stage 2 complete
- Cluster analysis accessible
- (If applicable) Codebase accessible

## Stage 3: Validation
- Opportunity analysis covers all vectors
- Attribution confidence levels assigned
- Stage 1 enrichment applied

## Stage 3: Exit Criteria
- [ ] Opportunity analysis complete
- [ ] (If baseline) Change impact complete
- [ ] Stage 1 files enriched
- [ ] Cross-vector analysis done
```

### Stage 4 Gates (Finalization)

```markdown
## Stage 4: Prerequisites
- Stages 1-3 complete
- All analysis files accessible

## Stage 4: Validation
- Summary references valid files
- Metrics consistent across documents
- Navigation links resolve

## Stage 4: Exit Criteria
- [ ] Institutional memory updated (if applicable)
- [ ] Executive summary complete
- [ ] All links valid
- [ ] Navigation guide covers use cases
```

## Validation Techniques

### File Existence Checks

```bash
# Check required files exist
[ -f "item/analysis/diagnosis.md" ] && echo "OK" || echo "MISSING"
```

### Content Threshold Checks

```bash
# Check file is non-trivial (>500 bytes)
size=$(wc -c < "item/analysis/diagnosis.md")
[ "$size" -gt 500 ] && echo "OK" || echo "TOO SMALL"
```

### Format Validation

```markdown
## Format Checks

For each output file:
- [ ] Has expected heading structure
- [ ] Contains required sections
- [ ] Placeholders are filled
- [ ] Classification tags present
```

### Cross-Reference Validation

```markdown
## Cross-Reference Checks

- [ ] File references in summary point to existing files
- [ ] Item IDs in clusters match actual items
- [ ] Stage references are internally consistent
```

## Quality Gate Document Format

```markdown
# Quality Gates: {Playbook Name}

## Overview

| Stage | Prerequisites | Validation | Exit Criteria |
|-------|---------------|------------|---------------|
| 0 | {Count} | {Count} | {Count} |
| 1 | {Count} | {Count} | {Count} |
| 2 | {Count} | {Count} | {Count} |
| 3 | {Count} | {Count} | {Count} |
| 4 | {Count} | {Count} | {Count} |

---

## Stage 0: Setup

### Prerequisites
- [ ] {Prerequisite 1}
- [ ] {Prerequisite 2}

### Validation Steps
1. {Validation 1}
2. {Validation 2}

### Exit Criteria
- [ ] {Criterion 1}
- [ ] {Criterion 2}

---

## Stage 1: Per-Item

...
```

## Failure Handling

### Stage-Level Failures

```markdown
## Stage Failure Protocol

If stage cannot complete:

1. **Stop immediately**
2. **Report clearly:**
   ```
   STAGE {N} FAILED

   Check: {What failed}
   Issue: {Description}

   Required action: {How to fix}
   ```
3. **Wait for resolution**
4. **Re-run failed stage**
```

### Item-Level Failures

```markdown
## Item Failure Protocol

If individual item fails:

1. **Track in failed list**
2. **Continue with other items**
3. **After initial pass:**
   - Review failed items
   - Re-launch failed items only
4. **Kill stuck items after timeout**
5. **Report final failed count**
```

### Validation Failures

```markdown
## Validation Failure Protocol

If validation finds issues:

1. **Flag for review** (don't auto-fix)
2. **Document inconsistencies**
3. **Require human decision** for:
   - Missing critical data
   - Contradictory information
   - Below-threshold outputs
```

## Validation Checklist

Before finalizing gates:

- [ ] Every stage has prerequisites defined
- [ ] Validation steps are concrete and checkable
- [ ] Exit criteria are binary (pass/fail)
- [ ] Failure handling is specified
- [ ] Gates are proportionate (not excessive)

## Additional Resources

For quality gate patterns:
- **`${CLAUDE_PLUGIN_ROOT}/references/playbook-pattern.md`** - Section 2.5
