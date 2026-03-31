---
name: impact-estimation
description: This skill should be used when the user asks to "estimate impact", "design confidence framework", "create impact scoring", "define confidence levels", "build ROI analysis", or needs frameworks for estimating improvement impact in playbook analysis.
version: 0.1.0
---

# Impact Estimation

Design confidence frameworks with clear criteria for estimating improvement impact.

## Purpose

Impact estimation provides:
- Quantified improvement potential
- Confidence levels for estimates
- Prioritization criteria
- ROI analysis framework

## Confidence Framework

### Standard Confidence Levels

| Level | Confidence | Variance | Criteria |
|-------|------------|----------|----------|
| High | 90%+ | ±10 points | Direct evidence, clear causal mechanism |
| Medium | 70-89% | ±20 points | Logical connection, some uncertainty |
| Low | <70% | ±30 points | Speculative benefit |

### Confidence Criteria

**High Confidence (90%+):**
- Direct trace linking cause to effect
- Mechanism is well understood
- Similar fixes have proven impact
- Evidence is unambiguous

**Medium Confidence (70-89%):**
- Logical connection exists
- Mechanism is plausible
- Some uncertainty in scope
- Evidence supports but doesn't prove

**Low Confidence (<70%):**
- Speculative benefit
- Mechanism unclear
- Limited evidence
- Many assumptions required

## Impact Estimation Format

### Per-Item Impact

```markdown
## Impact Analysis

### Item: {ID}

**Current state:** X%
**With fix:** Y%
**Estimated lift:** +Z points

**Confidence:** {High/Medium/Low}

**Reasoning:**
{Why this estimate is credible}

**Evidence:**
- {Evidence point 1}
- {Evidence point 2}
```

### Aggregate Impact

```markdown
## Aggregate Impact Summary

| Improvement | Items | Avg Lift | Total Points | Confidence |
|-------------|-------|----------|--------------|------------|
| {Fix 1} | N | +X | +N×X | High |
| {Fix 2} | N | +Y | +N×Y | Medium |
| {Fix 3} | N | +Z | +N×Z | Low |

**Total estimated improvement:** +{sum} points
**Weighted by confidence:** +{adjusted} points
```

### Impact Table Format

```markdown
## Impact Analysis: {Opportunity}

| Item | Current | With Fix | Lift | Confidence |
|------|---------|----------|------|------------|
| {ID1} | 45% | 75% | +30 | High |
| {ID2} | 60% | 80% | +20 | Medium |
| {ID3} | 55% | 70% | +15 | Low |

**Summary:**
- Total items: 3
- Average lift: +21.7 points
- Confidence-weighted lift: +18.5 points
```

## Estimation Methods

### Direct Evidence Method

When you have clear causal links:

```markdown
### Estimation Method: Direct Evidence

**Applicable when:**
- Fix addresses root cause directly
- Similar fixes have known outcomes
- Trace shows clear mechanism

**Process:**
1. Identify items with this root cause
2. Calculate current score
3. Estimate score if root cause removed
4. Assign High confidence
```

### Comparative Method

When you can compare similar cases:

```markdown
### Estimation Method: Comparative

**Applicable when:**
- Similar items have different outcomes
- Difference attributable to specific factor
- Pattern is consistent

**Process:**
1. Find similar items with/without factor
2. Calculate average scores for each group
3. Difference = estimated impact
4. Assign Medium confidence
```

### Extrapolation Method

When direct evidence is limited:

```markdown
### Estimation Method: Extrapolation

**Applicable when:**
- Limited direct evidence
- Logical mechanism exists
- Must estimate from principles

**Process:**
1. Identify affected items
2. Estimate mechanism impact
3. Apply conservative estimate
4. Assign Low confidence
```

## Priority Scoring

### Priority Formula

```
Priority = (Items Affected × Quality Improvement) / (Effort × Risk)
```

### Factor Definitions

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

### Priority Table

```markdown
## Priority Analysis

| Opportunity | Items | Lift | Effort | Risk | Score | Priority |
|-------------|-------|------|--------|------|-------|----------|
| {Opp 1} | 15 | +20 | 2 | 1 | 150 | P1 |
| {Opp 2} | 10 | +15 | 3 | 2 | 25 | P2 |
| {Opp 3} | 5 | +10 | 4 | 2 | 6 | P3 |
```

## ROI Analysis

### Simple ROI

```markdown
## ROI Analysis

### Investment
- Development: {hours/cost}
- Testing: {hours/cost}
- Deployment: {hours/cost}
- **Total:** {total}

### Return
- Items improved: N
- Average lift: +X points
- Total improvement: +N×X points

### ROI
- Improvement per unit effort: {points/hour}
- Payback: {timeframe}
```

### Effort/Impact Matrix

```
         High Impact
              │
    Quick Wins│ Major Projects
    (Do first)│ (Plan carefully)
              │
──────────────┼──────────────
              │
    Fill-ins  │ Reconsider
    (If time) │ (Maybe don't)
              │
         Low Impact

        Low Effort ──> High Effort
```

## Estimation Guidelines

### Be Conservative

- Use lower bound of confidence range
- Round down, not up
- Prefer underestimate to overestimate

### Document Assumptions

```markdown
**Assumptions:**
1. {Assumption 1}
2. {Assumption 2}

**If assumption invalid:**
- Impact could be: {range}
```

### Show Your Work

```markdown
**Calculation:**
- Current score: 45%
- Missing 3 key observations worth ~10 points each
- Fix addresses 2 of 3 observations
- Expected improvement: +20 points (2 × 10)
- Confidence: Medium (mechanism clear, but observation value estimated)
```

## Validation Checklist

Before finalizing estimates:

- [ ] Confidence levels have clear criteria
- [ ] Each estimate has documented reasoning
- [ ] Assumptions are explicit
- [ ] Priority formula is defined
- [ ] Conservative approach used
- [ ] Aggregate impact calculated

## Additional Resources

For impact estimation patterns:
- **`${CLAUDE_PLUGIN_ROOT}/references/playbook-pattern.md`** - Section 4.8
