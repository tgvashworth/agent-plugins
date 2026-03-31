---
name: meta-analysis
description: This skill should be used when the user asks to "create self-assessment", "build meta-analysis", "track playbook issues", "design theme-based analysis", "identify analysis process problems", or needs structures for analyzing the analysis process itself.
version: 0.1.0
---

# Meta-Analysis

Create theme-based self-assessment structures for tracking playbook issues.

## What is Meta-Analysis?

Meta-analysis examines how well YOU performed YOUR analysis (not about the subject being analyzed).

**What belongs in meta-analysis:**
- Configuration errors in running the playbook
- Playbook instruction issues
- Analysis gaps or skipped steps
- Attribution errors in conclusions
- Tool problems during execution

**What does NOT belong:**
- Subject domain issues → Go in item analysis
- System improvements → Go in opportunity analysis
- Technical bugs in subject → Go in diagnosis

## Theme-Based Structure

### Why Theme-Based?

Per-item meta-analysis causes:
- Duplication across items
- Hard to see patterns
- Difficult to prioritize

Theme-based structure:
- Groups similar issues
- Highlights patterns
- Enables prioritization

### Theme Format

```markdown
## Theme: {Issue Category}

**Description:** {What this theme covers}

**Impact:** {How it affected analysis quality}

### Instances

| Item | Specific Issue | Impact |
|------|----------------|--------|
| {ID} | {Details} | {Effect} |
| {ID} | {Details} | {Effect} |

### Root Cause

{Why this keeps happening}

### Recommendation

{How to prevent in future}
```

## Meta-Analysis Categories

### Configuration Errors

```markdown
## Theme: Configuration Errors

Issues with playbook setup and configuration.

### Instances

| Item | Issue | Impact |
|------|-------|--------|
| All | Symlinks misconfigured | Had to reconfigure mid-analysis |
| Batch 2 | Wrong baseline selected | Comparison invalid for 10 items |

### Root Cause
Preflight checks didn't catch configuration issues.

### Recommendation
Add explicit symlink validation to Stage 0.
```

### Playbook Issues

```markdown
## Theme: Playbook Instructions

Issues with playbook documentation or guidance.

### Instances

| Stage | Issue | Impact |
|-------|-------|--------|
| 1 | Unclear criteria for classification | Inconsistent tagging |
| 2 | Missing guidance on edge cases | Had to improvise |

### Root Cause
Instructions written for ideal cases, not edge cases.

### Recommendation
Add edge case guidance to Stage 1 and 2 instructions.
```

### Analysis Gaps

```markdown
## Theme: Analysis Gaps

Steps skipped or incompletely executed.

### Instances

| Item | Gap | Reason | Impact |
|------|-----|--------|--------|
| {ID} | Skipped comparison | No baseline | Missing delta |
| {ID} | Incomplete evidence | Time pressure | Weak attribution |

### Root Cause
Unclear guidance on when steps can be skipped.

### Recommendation
Add explicit skip criteria to optional analyses.
```

### Attribution Errors

```markdown
## Theme: Attribution Errors

Incorrect or unsupported conclusions.

### Instances

| Item | Error | Discovered | Impact |
|------|-------|------------|--------|
| {ID} | Claimed code bug without evidence | Stage 3 | Had to revise |
| {ID} | Wrong causal attribution | Cross-check | Misleading priority |

### Root Cause
Pressure to reach conclusions without sufficient evidence.

### Recommendation
Require explicit evidence citations for all causal claims.
```

### Tool Problems

```markdown
## Theme: Tool Problems

Issues with scripts, tools, or automation.

### Instances

| Tool | Issue | Impact |
|------|-------|--------|
| verify-analysis.sh | False positives | Manual re-checks needed |
| Sub-agent launch | Timeout issues | Re-runs required |

### Root Cause
Tools not tested against all edge cases.

### Recommendation
Expand tool test coverage before next run.
```

## Contribution Workflow

### Phase 1: Initial Themes (Items 1-5)

After first 3-5 items, create initial themes:

```markdown
1. Review issues encountered
2. Group into preliminary themes
3. Create initial theme entries
4. Note items under each theme
```

### Phase 2: Theme Building (Items 6-15)

For subsequent items:

```markdown
1. Encounter issue
2. Check if existing theme applies
3. If yes: Add item to theme
4. If no: Create new theme or note for later
```

### Phase 3: Consolidation (After ~15 items)

Periodically consolidate:

```markdown
1. Review all themes
2. Merge related themes
3. Update impact estimates
4. Prioritize themes
```

### Phase 4: Final Pass (After Stage 1)

Complete meta-analysis:

```markdown
1. Review all themes
2. Add impact estimates
3. Prioritize recommendations
4. Note systemic issues
```

## Meta-Analysis Document Format

```markdown
# Self-Assessment

## Overview

Analysis of how well the playbook execution performed.

**Date:** {date}
**Items analyzed:** N
**Issues identified:** M themes, P instances

---

## Priority Issues

| Theme | Instances | Impact | Recommendation |
|-------|-----------|--------|----------------|
| {Name} | N | {High/Med/Low} | {Brief} |

---

## Theme 1: {Name}

**Category:** {Configuration/Playbook/Analysis/Attribution/Tool}

**Description:** {What this theme covers}

**Impact:** {How it affected analysis}

### Instances

| Item | Specific Issue | Impact |
|------|----------------|--------|
| {ID} | {Details} | {Effect} |

### Root Cause

{Why this keeps happening}

### Recommendation

{How to prevent}

---

## Theme 2: {Name}

...

---

## Summary

### Playbook Improvements Needed

1. {Improvement 1}
2. {Improvement 2}

### Process Improvements Needed

1. {Improvement 1}
2. {Improvement 2}

### Tool Improvements Needed

1. {Improvement 1}
2. {Improvement 2}
```

## Distinguishing Meta from Subject Analysis

### This IS Meta-Analysis

| Issue | Why It's Meta |
|-------|---------------|
| "Instructions unclear" | Playbook quality |
| "Skipped optional step" | Process execution |
| "Wrong tool output" | Tool reliability |
| "Misinterpreted guidance" | Documentation quality |

### This is NOT Meta-Analysis

| Issue | Where It Goes |
|-------|---------------|
| "System has bug" | diagnosis.md |
| "Missing capability" | capability-gaps.md |
| "Need new feature" | opportunity-analysis |
| "Code needs fix" | opportunity-analysis |

## Validation Checklist

Before finalizing meta-analysis:

- [ ] Themes are clearly categorized
- [ ] Instances reference specific items
- [ ] Root causes identified
- [ ] Recommendations are actionable
- [ ] Priorities assigned
- [ ] No subject analysis included

## Additional Resources

For meta-analysis patterns:
- **`${CLAUDE_PLUGIN_ROOT}/references/playbook-pattern.md`** - Section 4.12
