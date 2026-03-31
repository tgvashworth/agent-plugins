---
name: finalization-stage
description: This skill should be used when the user asks to "design Stage 4", "create executive summary", "define institutional memory", "build summary template", "design knowledge capture", or needs to author the finalization stage.
version: 0.1.0
---

# Finalization Stage Design

Design Stage 4 (Finalization) with summary templates and institutional memory update criteria.

## Purpose of Stage 4

Stage 4 performs administrative tasks - no new analysis, only synthesis and knowledge capture:
- Executive summary generation
- Institutional memory updates
- Navigation guides for stakeholders

## Execution Model

```
Stage 4: Sequential, Single Agent
├── Update institutional memory (if applicable)
├── Generate executive summary
├── Verify all links
└── Mark analysis complete
```

## Stage Structure

```
stages/4-finalization/
├── README.md                    # Stage overview
├── institutional-memory.md      # Knowledge capture criteria
└── executive-summary.md         # Summary generation guide
```

## Executive Summary Format

```markdown
# Analysis Summary: {Title}

**Date:** {date}
**Scope:** {N} items analyzed
**Baseline:** {comparison info or "None"}

---

## Key Findings

### Performance Overview

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| {Metric 1} | X% | Y% | {Met/Below} |
| {Metric 2} | X% | Y% | {Met/Below} |

### Critical Issues

1. **{Issue 1}**: {Brief description}
   - Impact: {N} items, -{X} points
   - Root cause: {Brief explanation}

2. **{Issue 2}**: {Brief description}
   - Impact: {N} items, -{X} points
   - Root cause: {Brief explanation}

---

## Cohort Summary

| Segment | Count | Avg Score | Treatment |
|---------|-------|-----------|-----------|
| High performers | N | X% | {Action} |
| Medium performers | N | X% | {Action} |
| Low performers | N | X% | {Action} |

---

## Top Opportunities

| # | Opportunity | Impact | Effort | Priority |
|---|-------------|--------|--------|----------|
| 1 | {Name} | +{N}pp | {L/M/H} | P1 |
| 2 | {Name} | +{N}pp | {L/M/H} | P2 |
| 3 | {Name} | +{N}pp | {L/M/H} | P3 |

---

## Change Attribution (if baseline)

### What Worked
- {Change 1}: +{N}pp (Strong confidence)

### What Didn't
- {Change 2}: No measurable impact

### Next Cycle
- {Recommendation 1}
- {Recommendation 2}

---

## Navigation Guide

| If you want to... | See... |
|-------------------|--------|
| Understand a specific item | `items/{id}/analysis/` |
| See failure patterns | `cohort-analysis/failure-mode-clusters.md` |
| Find improvement opportunities | `synthesis/opportunity-analysis.md` |
| Check change effectiveness | `synthesis/change-impact.md` |

---

## File Index

### Stage 1: Per-Item Analysis
- `items/*/analysis/diagnosis.md`
- `items/*/analysis/evidence-assessment.md`

### Stage 2: Aggregation
- `cohort-analysis/performance-clusters.md`
- `cohort-analysis/cross-cluster-analysis.md`

### Stage 3: Synthesis
- `synthesis/opportunity-analysis.md`
- `synthesis/change-impact.md`
```

## Institutional Memory Format

```markdown
# Institutional Memory Update

## Entry Criteria

Only add entries that meet ALL criteria:
- Attribution confidence ≥90%
- Significant impact (≥15pp improvement OR affects 5+ items)
- Validated through this analysis

## Entry Format

### {Date}: {Title}

**Change:** {What changed}

**Impact:**
- Metric improvement: +{N}pp
- Items affected: {list or count}

**Evidence:**
- {Specific trace marker}
- {Before/after comparison}

**Lessons:**
- {Key learning 1}
- {Key learning 2}

**References:**
- Analysis: `{path-to-analysis}`
- Code: `{commit or file}`
```

## Summary Generation Guidelines

### Be Scannable

Target: Readable in 5-10 minutes

- Use tables for data
- Use bullet points for findings
- Lead with most important information
- Include navigation guide

### Link Everything

Every claim should link to supporting analysis:

```markdown
### Finding: 30% of failures are evidence synthesis problems

See: `cohort-analysis/failure-mode-clusters.md#evidence-synthesis`
```

### Serve Multiple Personas

| Persona | Needs | Point to... |
|---------|-------|-------------|
| Executive | High-level summary | Key Findings section |
| Technical lead | Improvement roadmap | Top Opportunities |
| Individual contributor | Specific items | Navigation Guide |
| Future analyst | Historical context | Institutional Memory |

### Avoid New Analysis

Stage 4 synthesizes existing findings:

**Don't:**
- Perform new analysis
- Draw conclusions not supported by prior stages
- Add information not in earlier outputs

**Do:**
- Summarize findings from Stages 1-3
- Create navigation and cross-references
- Update institutional memory with validated learnings

## Success Criteria

Stage 4 is complete when:

- [ ] Institutional memory updated (if criteria met)
- [ ] Executive summary contains all required sections
- [ ] All links in summary point to existing files
- [ ] Navigation guide covers all major use cases
- [ ] Different personas can find relevant information

## Quality Checks

### Link Validation

Verify every file reference exists:

```bash
# Extract all file references from summary
# Check each exists
# Report broken links
```

### Completeness Check

Verify summary covers all stages:

- [ ] Stage 1 findings summarized
- [ ] Stage 2 clusters referenced
- [ ] Stage 3 opportunities listed
- [ ] Prior analysis (if baseline) attributed

### Consistency Check

Cross-validate numbers:

- [ ] Item counts match across sections
- [ ] Metric values consistent with source
- [ ] Priority rankings align with Stage 3

## Additional Resources

For complete finalization patterns:
- **`${CLAUDE_PLUGIN_ROOT}/references/playbook-pattern.md`** - Section 5: Stage 4
