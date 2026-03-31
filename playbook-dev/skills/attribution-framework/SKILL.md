---
name: attribution-framework
description: This skill should be used when the user asks to "build attribution framework", "establish causal attribution", "design change impact analysis", "create attribution chains", "trace cause to effect", or needs to establish causal links between changes and outcomes in playbook analysis.
version: 0.1.0
---

# Attribution Framework

Build change-to-behavior-to-performance attribution chains with confidence levels.

## The Attribution Challenge

**Correlation ≠ Causation**

- Correlation: "Quality improved between runs"
- Causation: "Quality improved BECAUSE of change X"

Attribution establishes the causal chain:

```
Code/Config Change → Behavior Change → Performance Change
       ↓                    ↓                   ↓
  (What changed)     (How it behaved)    (What metrics show)
```

## Attribution Process

### Step 1: Catalog Changes

Document all changes between comparison points:

```markdown
## Change Catalog

### Change 1: {Description}

**Type:** {Code/Config/Process}
**Commit/Date:** {Reference}
**Files affected:** {List}

**Expected mechanism:**
{How this change should affect outcomes}

**Expected scope:**
{Which items should be affected}
```

### Step 2: Map Changes to Items

Determine which items each change should affect:

```markdown
## Change-Item Mapping

| Change | Should Affect | Criteria |
|--------|---------------|----------|
| Change 1 | Items with {trait} | {Why} |
| Change 2 | Items of {type} | {Why} |
| Change 3 | All items | {Why} |
```

### Step 3: Validate Attribution

For each change-item pair, look for evidence:

```markdown
## Attribution Validation

### Change 1 → Item A

**Expected effect:** {What should have happened}

**Observed effect:** {What actually happened}

**Evidence:**
- Trace marker: {Specific evidence in artifacts}
- Behavioral change: {How behavior differed}
- Metric change: {Before vs after}

**Attribution confidence:** {Strong/Moderate/Weak/None}

**Reasoning:** {Why this confidence level}
```

### Step 4: Assign Confidence

| Level | Confidence | Criteria |
|-------|------------|----------|
| Strong | 90%+ | Clear trace, mechanism links change to outcome |
| Moderate | 60-89% | Evidence of change, likely caused improvement |
| Weak | 30-59% | Correlation but unclear mechanism |
| None | <30% | Not evident or likely other factors |

### Step 5: Synthesize Patterns

```markdown
## Attribution Synthesis

### What Worked

| Change | Items | Improvement | Confidence |
|--------|-------|-------------|------------|
| {Name} | N | +X% | Strong |

### What Didn't Work

| Change | Items | Expected | Observed | Gap |
|--------|-------|----------|----------|-----|
| {Name} | N | +Y% | +0% | -Y% |

### What Wasn't Tested

| Change | Reason | Items Needed |
|--------|--------|--------------|
| {Name} | {Why not testable} | N |

### Recommendations

Based on attribution:
1. **Double down on:** {What worked}
2. **Investigate:** {Unexpected results}
3. **Test next cycle:** {Untested changes}
```

## Attribution Document Format

```markdown
# Change Impact Analysis

## Overview

Analysis period: {start} to {end}
Changes analyzed: N
Items in scope: M

## Change Catalog

### Change 1: {Title}

**Reference:** {commit/PR/etc}
**Date:** {when}
**Type:** {Code/Config/Process}

**Description:**
{What changed}

**Mechanism:**
{How it should affect outcomes}

**Expected impact:**
- Affected items: {criteria}
- Expected improvement: +{N} points

---

## Attribution Analysis

### Change 1 Impact

**Items potentially affected:** N

**Items with evidence:** M

**Impact Summary:**
| Item | Before | After | Delta | Confidence |
|------|--------|-------|-------|------------|
| {ID} | X% | Y% | +Z | {Level} |

**Overall attribution:**
- Confidence: {Strong/Moderate/Weak/None}
- Average improvement: +{N} points
- Evidence quality: {Assessment}

**Key evidence:**
1. {Trace marker/behavioral evidence}
2. {Trace marker/behavioral evidence}

---

## Synthesis

### Effectiveness Summary

| Change | Attribution | Improvement | ROI |
|--------|-------------|-------------|-----|
| {Name} | Strong | +X% | High |
| {Name} | Moderate | +Y% | Medium |
| {Name} | None | - | Low |

### Recommendations

**Continue:**
- {Change with strong attribution}

**Investigate:**
- {Change with unexpected results}

**Next cycle:**
- {Untested or inconclusive changes}
```

## Evidence Types

### Trace Markers

Direct evidence in artifacts:

```markdown
**Trace markers to look for:**
- Log entries mentioning the change
- Artifact content reflecting new behavior
- Error patterns that should disappear
- New data that wasn't available before
```

### Behavioral Evidence

Changes in system behavior:

```markdown
**Behavioral indicators:**
- Different code paths executed
- New queries/calls made
- Changed output format
- Different error handling
```

### Metric Evidence

Quantitative changes:

```markdown
**Metric indicators:**
- Score improvement in affected items
- Error rate changes
- Coverage changes
- Performance timing changes
```

## Common Attribution Patterns

### Clear Attribution

```markdown
**Pattern:** Single change, clear mechanism, strong evidence

**Example:**
- Change: Added query for missing data
- Mechanism: Data now available for analysis
- Evidence: Query appears in artifacts, data used in conclusions
- Attribution: Strong (90%+)
```

### Confounded Attribution

```markdown
**Pattern:** Multiple concurrent changes, hard to isolate

**Approach:**
- Analyze each change independently
- Look for items affected by only one change
- Use regression analysis if sample large enough
- Note uncertainty in conclusions
```

### Indirect Attribution

```markdown
**Pattern:** Change enables improvement but doesn't directly cause it

**Example:**
- Change: Improved data collection
- Mechanism: Better data enables better analysis
- Evidence: Data quality improved, but analysis improvement depends on reasoning
- Attribution: Moderate (reasoning improvement not guaranteed)
```

## Statistical Validation

For large samples (20+ items), consider statistical methods:

### A/B Comparison

```markdown
**Treatment group:** Items where change applies
**Control group:** Items where change doesn't apply

**Analysis:**
- Treatment mean: X%
- Control mean: Y%
- Difference: Z%
- P-value: {significance}
```

### Regression Analysis

```markdown
**Model:** Outcome ~ Change1 + Change2 + Change3

**Results:**
| Change | Coefficient | P-value | Significant |
|--------|-------------|---------|-------------|
| Change1 | +15 | 0.01 | Yes |
| Change2 | +8 | 0.12 | No |
| Change3 | +3 | 0.45 | No |
```

### When NOT to Use Statistics

- Single clear change (simple comparison sufficient)
- Obvious causation (statistics add little)
- Small samples <15 (power too low)
- Time pressure (qualitative faster)

## Validation Checklist

Before finalizing attribution:

- [ ] All changes cataloged
- [ ] Change-item mapping complete
- [ ] Evidence documented for each attribution
- [ ] Confidence levels assigned with reasoning
- [ ] Synthesis includes what worked/didn't/untested
- [ ] Recommendations are actionable

## Additional Resources

For attribution patterns:
- **`${CLAUDE_PLUGIN_ROOT}/references/playbook-pattern.md`** - Section 4.10
