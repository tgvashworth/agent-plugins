---
name: aggregation-stage
description: This skill should be used when the user asks to "design Stage 2", "create clustering analysis", "define aggregation axes", "build cohort analysis", "design cross-cluster synthesis", or needs to author the pattern identification stage.
version: 0.1.0
---

# Aggregation Stage Design

Design Stage 2 (Aggregation) with clustering axes, cross-cluster synthesis, and priority frameworks.

## Purpose of Stage 2

Stage 2 reads all Stage 1 outputs and clusters items to identify patterns across multiple dimensions. A single agent processes all items to maintain consistency.

## Execution Model

```
Stage 2: Single Agent
├── Read all Stage 1 outputs
├── Define clustering criteria per axis
├── Assign items to clusters
├── Identify patterns per cluster
├── Synthesize cross-cluster insights
└── Write aggregation outputs
```

## Clustering Axes

Define multiple independent clustering dimensions:

| Axis Type | Purpose | Example Categories |
|-----------|---------|-------------------|
| Performance | Group by outcome quality | High / Medium / Low |
| Failure Mode | Group by how things fail | Taxonomy tags |
| Item Type | Group by category | Type A / Type B / Type C |
| Pipeline Stage | Group by where it fails | Collection / Analysis / Synthesis |
| Gap Type | Group by what's missing | Capability categories |
| Evolution | Group by change | Improved / Stable / Regressed |

### Defining Clustering Criteria

For each axis, specify clear boundaries:

```markdown
## Performance Clustering

| Cluster | Criteria | Characteristics |
|---------|----------|-----------------|
| High | Score ≥80% | Reliable, minimal gaps |
| Medium | Score 60-79% | Partial success, specific gaps |
| Low | Score <60% | Significant issues |
```

## Stage Structure

```
stages/2-aggregation/
├── README.md                        # Stage overview
├── performance-clusters.md          # Cluster by outcome
├── failure-mode-clusters.md         # Cluster by how things fail
├── item-type-clusters.md            # Cluster by category
├── gap-clusters.md                  # Cluster by missing capabilities
├── evolution-clusters.md            # Cluster by change (if baseline)
└── cross-cluster-analysis.md        # Multi-axis synthesis
```

## Stage README Template

```markdown
# Stage 2: Cohort Clustering

Cluster items to identify patterns across {N} dimensions.

---

## Execution Context

| Aspect | Details |
|--------|---------|
| **Execution** | Sequential |
| **Agent** | Single agent |
| **User interaction** | None |
| **Outputs** | `cohort-analysis/` |

---

## Clustering Axes

| # | Axis | File | Grouping |
|---|------|------|----------|
| 1 | Performance | `performance-clusters.md` | High/Medium/Low |
| 2 | Failure Mode | `failure-mode-clusters.md` | By taxonomy tags |
| 3 | Item Type | `item-type-clusters.md` | By category |
| 4 | Gaps | `gap-clusters.md` | By capability |
| 5 | Evolution | `evolution-clusters.md` | Improved/Regressed |
| 6 | Cross-Cluster | `cross-cluster-analysis.md` | Multi-axis |

---

## Inputs

- All Stage 1 outputs: `{items}/*/analysis/*.md`
- Classification tags from diagnosis files
- Metrics from summary sections

## Outputs

- `cohort-analysis/{axis}-clusters.md` for each axis
- `cohort-analysis/cross-cluster-analysis.md`

---

## Exit Criteria

Stage 2 is complete when:

- [ ] All cluster files created
- [ ] Each item assigned to clusters
- [ ] Cross-cluster analysis complete
- [ ] Priority framework defined
```

## Cluster Document Template

```markdown
# {Axis} Clusters

## Overview

{Items} clustered by {axis criterion}.

| Cluster | Count | % of Total | Key Characteristic |
|---------|-------|------------|-------------------|
| {Name} | N | X% | {Description} |
| {Name} | N | X% | {Description} |
| {Name} | N | X% | {Description} |

---

## Cluster: {Name}

### Items

| ID | {Key Metric} | {Secondary} | Notes |
|----|--------------|-------------|-------|
| {ID} | X% | {Value} | {Note} |

### Common Characteristics

- {Pattern 1}
- {Pattern 2}
- {Pattern 3}

### Distinguishing Factors

What makes this cluster different:
- {Factor 1}
- {Factor 2}

### Representative Example

**{Item ID}**: {Brief description of why it's representative}

### Treatment Recommendations

{What to do with items in this cluster}
```

## Cross-Cluster Analysis

The most valuable aggregation synthesizes across all axes:

```markdown
# Cross-Cluster Analysis

## Multi-Axis Insights

### Correlation: {Axis A} × {Axis B}

| {Axis A} | {Axis B High} | {Axis B Med} | {Axis B Low} |
|----------|---------------|--------------|--------------|
| High | N items | N items | N items |
| Medium | N items | N items | N items |
| Low | N items | N items | N items |

**Insight:** {What the correlation reveals}

### Pattern: {Description}

When {condition A} is true, {condition B} tends to be true.

**Evidence:** {N} of {M} items with {A} also have {B}

**Implication:** {What this means for action}

---

## Cohort Segmentation

| Segment | Profile | Count | Treatment |
|---------|---------|-------|-----------|
| Ready | High perf, minimal gaps | N | Deploy now |
| Needs X | Medium perf, specific gap | N | Add capability |
| Needs Y | Low perf, structural issue | N | Architecture change |

---

## Priority Framework

```
Priority = (Items Affected × Quality Improvement) / (Effort × Risk)
```

| Opportunity | Items | Improvement | Effort | Priority |
|-------------|-------|-------------|--------|----------|
| {Opp 1} | N | +X points | Low | P1 |
| {Opp 2} | N | +Y points | Medium | P2 |
| {Opp 3} | N | +Z points | High | P3 |
```

## Aggregation Techniques

### Counting and Grouping

```markdown
## Failure Mode Distribution

| Tag | Count | % |
|-----|-------|---|
| Misattributed blame | 12 | 24% |
| Shallow analysis | 8 | 16% |
| Evidence synthesis | 15 | 30% |
| Other | 15 | 30% |
```

### Metric Aggregation

```markdown
## Performance by Item Type

| Type | Avg Score | Min | Max | Std Dev |
|------|-----------|-----|-----|---------|
| Type A | 75% | 45% | 95% | 12% |
| Type B | 62% | 30% | 85% | 18% |
| Type C | 81% | 70% | 92% | 8% |
```

### Pattern Detection

```markdown
## Recurring Patterns

### Pattern: {Name}

**Frequency:** {N} items ({X}%)

**Characteristics:**
- {Trait 1}
- {Trait 2}

**Example items:** {ID1}, {ID2}, {ID3}

**Root cause hypothesis:** {Explanation}
```

## Priority Framework

Define how to prioritize findings:

```markdown
## Priority Calculation

Priority Score = (Items × Improvement) / (Effort × Risk)

### Factors

| Factor | Scale | Description |
|--------|-------|-------------|
| Items Affected | 1-50 | Count of items this addresses |
| Quality Improvement | 1-30 | Expected point improvement |
| Effort | 1-5 | Implementation difficulty |
| Risk | 1-3 | Potential for negative impact |

### Priority Tiers

| Tier | Score Range | Action |
|------|-------------|--------|
| P1 | >50 | Implement immediately |
| P2 | 20-50 | Plan for next cycle |
| P3 | <20 | Consider for backlog |
```

## Additional Resources

For complete aggregation patterns:
- **`${CLAUDE_PLUGIN_ROOT}/references/playbook-pattern.md`** - Section 5: Stage 2
