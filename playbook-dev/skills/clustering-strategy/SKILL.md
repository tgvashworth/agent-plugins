---
name: clustering-strategy
description: This skill should be used when the user asks to "define clustering strategy", "create multi-axis clustering", "design cohort segmentation", "build clustering dimensions", "group items by multiple factors", or needs to design how items should be grouped across multiple dimensions.
version: 0.1.0
---

# Clustering Strategy

Define multi-axis clustering strategies for performance, failure mode, item type, and other dimensions.

## Purpose of Multi-Axis Clustering

Single-dimension clustering misses important patterns. Multi-axis clustering reveals:
- Interaction effects between dimensions
- Cohort-based treatment strategies
- Hidden patterns in combinations
- Priority-informed segmentation

## Clustering Axes

### Standard Axes

| Axis | Groups By | Example Clusters |
|------|-----------|------------------|
| Performance | Outcome quality | High / Medium / Low |
| Failure Mode | How things fail | Taxonomy tags |
| Item Type | Category | Type A / B / C |
| Pipeline Stage | Where failure occurs | Collection / Analysis / Synthesis |
| Gap Type | What's missing | Capability categories |
| Evolution | Change over time | Improved / Stable / Regressed |
| Severity | Impact level | Critical / High / Medium / Low |

### Domain-Specific Axes

Design axes relevant to your domain:

```markdown
## Domain: {Name}

### Axis: {Custom Dimension}

**Groups by:** {What distinguishes clusters}

**Clusters:**
| Cluster | Criteria | Count |
|---------|----------|-------|
| {Name} | {Definition} | N |
| {Name} | {Definition} | N |
| {Name} | {Definition} | N |

**Why this axis matters:**
{How it informs action}
```

## Clustering Design Process

### Step 1: Identify Dimensions

List all potentially useful clustering dimensions:

```markdown
## Potential Clustering Axes

| Axis | Data Source | Actionable? |
|------|-------------|-------------|
| Performance | Scores in analysis | Yes |
| Failure mode | Classification tags | Yes |
| Item type | Item metadata | Yes |
| Complexity | Item characteristics | Maybe |
| {Other} | {Source} | {Yes/No} |
```

### Step 2: Define Cluster Boundaries

For each axis, specify clear boundaries:

```markdown
## Axis: Performance

| Cluster | Criteria | Rationale |
|---------|----------|-----------|
| High | Score ≥80% | Reliable performance |
| Medium | Score 60-79% | Needs improvement |
| Low | Score <60% | Significant issues |
```

### Step 3: Design Cross-Cluster Analysis

Plan how to analyze combinations:

```markdown
## Cross-Cluster Analysis Plan

### Correlation: Performance × Failure Mode

**Question:** Do certain failure modes dominate low performers?

**Matrix:**
| Performance | Mode A | Mode B | Mode C |
|-------------|--------|--------|--------|
| High | ? | ? | ? |
| Medium | ? | ? | ? |
| Low | ? | ? | ? |

**Expected insight:** {What pattern might emerge}
```

### Step 4: Define Cohort Segmentation

Create actionable cohorts from cluster combinations:

```markdown
## Cohort Segmentation

| Cohort | Profile | Treatment |
|--------|---------|-----------|
| Ready | High perf, minimal gaps | Deploy |
| Needs X | Medium perf, specific gap | Fix gap |
| Needs Y | Low perf, structural issue | Redesign |
```

## Cluster Document Templates

### Single-Axis Cluster

```markdown
# {Axis} Clusters

## Overview

| Cluster | Count | % | Key Characteristic |
|---------|-------|---|-------------------|
| {Name} | N | X% | {Brief} |

---

## Cluster: {Name}

### Membership

| ID | {Key Metric} | Notes |
|----|--------------|-------|
| {ID} | {Value} | {Note} |

### Common Characteristics

- {Pattern 1}
- {Pattern 2}

### Distinguishing Factors

What sets this cluster apart:
- {Factor 1}
- {Factor 2}

### Representative Example

**{ID}:** {Why representative}

### Treatment

{What to do with items in this cluster}
```

### Cross-Cluster Analysis

```markdown
# Cross-Cluster Analysis

## {Axis A} × {Axis B}

### Correlation Matrix

| {Axis A} \ {Axis B} | {B1} | {B2} | {B3} |
|---------------------|------|------|------|
| {A1} | N | N | N |
| {A2} | N | N | N |
| {A3} | N | N | N |

### Pattern: {Description}

**Observation:** When {Axis A} = {value}, {Axis B} tends to be {pattern}.

**Frequency:** N of M items (X%)

**Implication:** {What this means for action}

### Exceptions

Items that don't fit the pattern:
- {ID}: {Why different}

---

## Multi-Axis Insights

### Insight 1: {Title}

**Pattern:** {Description}

**Evidence:**
- {Supporting data}

**Action:** {What to do}

### Insight 2: {Title}

...

---

## Cohort Segmentation

| Cohort | Multi-Axis Profile | Count | Treatment |
|--------|-------------------|-------|-----------|
| Ready | High perf, Type A | N | Deploy now |
| Needs capability | Low reach, Type B | N | Build capability |
| Needs redesign | Low perf, Mode X | N | Architecture change |
```

## Priority Framework

### Priority Calculation

```
Priority = (Cluster Size × Improvement Potential) / (Effort × Risk)
```

### Priority Matrix

```markdown
## Priority by Cluster

| Cluster | Size | Improvement | Effort | Risk | Priority |
|---------|------|-------------|--------|------|----------|
| {Name} | N | +X | Low | Low | P1 |
| {Name} | N | +Y | Medium | Low | P2 |
| {Name} | N | +Z | High | Medium | P3 |
```

## Clustering Patterns

### Performance-Driven Segmentation

```markdown
Start with performance clusters:
- High performers → Understand what works
- Low performers → Diagnose issues

Then overlay:
- Failure mode → Why they fail
- Gap type → What's missing
```

### Issue-Driven Segmentation

```markdown
Start with failure mode clusters:
- Each failure mode → Different fix

Then overlay:
- Performance → Severity
- Item type → Fix applicability
```

### Evolution-Driven Segmentation

```markdown
Start with evolution clusters (vs baseline):
- Improved → What worked
- Regressed → What broke
- Stable → Baseline

Then overlay:
- Failure mode → What changed
- Change attribution → Why it changed
```

## Validation Checklist

Before finalizing clusters:

- [ ] All items assignable to each axis
- [ ] Cluster boundaries are clear
- [ ] Cross-cluster patterns identified
- [ ] Cohorts are actionable
- [ ] Priority framework defined
- [ ] Representative examples selected

## Additional Resources

For clustering strategies:
- **`${CLAUDE_PLUGIN_ROOT}/references/playbook-pattern.md`** - Section 4.9
