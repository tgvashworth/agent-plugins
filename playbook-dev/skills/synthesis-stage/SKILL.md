---
name: synthesis-stage
description: This skill should be used when the user asks to "design Stage 3", "create opportunity analysis", "define synthesis vectors", "build change impact analysis", "design improvement recommendations", or needs to author the cross-cutting insights stage.
version: 0.1.0
---

# Synthesis Stage Design

Design Stage 3 (Synthesis) with opportunity analysis vectors, change impact attribution, and actionable recommendations.

## Purpose of Stage 3

Stage 3 performs cross-cutting analysis to generate actionable recommendations. Multiple independent synthesis types can run in parallel.

## Execution Model

```
Stage 3: Parallel (Optional)
├── Opportunity Analysis (can parallelize by vector)
├── Change Impact Analysis (if baseline exists)
├── Telemetry Analysis (domain-specific)
└── [Other synthesis types]
```

## Synthesis Types

### 1. Opportunity Analysis

Examine failures through multiple improvement vectors:

| Vector | Question | Scope |
|--------|----------|-------|
| Capabilities | What new tools/data would help? | External APIs, data access |
| Reasoning | What logic improvements help? | Prompts, orchestration |
| Fixes | What specific bugs should we fix? | Individual code fixes |
| Observability | How do we measure better? | Metrics, monitoring |
| Prevention | How do we prevent failures? | Guardrails, validation |

### 2. Change Impact Analysis

Establish causal attribution for performance changes:

```
Code Change → Behavior Change → Performance Change
    ↓              ↓                  ↓
(What changed) (How it behaved) (What metrics show)
```

### 3. Domain-Specific Synthesis

Custom synthesis for the analysis domain (e.g., telemetry analysis for system monitoring).

## Stage Structure

```
stages/3-synthesis/
├── README.md                    # Stage overview
├── opportunity-analysis.md      # Improvement opportunities
├── change-impact.md             # Attribution analysis
└── {domain-specific}.md         # Domain-specific synthesis
```

## Opportunity Analysis Format

```markdown
# Opportunity Analysis

## Overview

{N} improvement opportunities identified across {M} vectors.

---

## Vector 1: {Name}

**Question:** {What this vector answers}

### Opportunities

#### Opportunity 1.1: {Name}

**Problem Statement**
- Failure mode: {Description}
- Investigations affected: {List}
- Example: {Specific case}

**Solution Specification**
- What to build: {Description}
- Implementation details: {Technical approach}
- Integration points: {Where it connects}

**Impact Analysis**

| Item | Current | With Fix | Lift | Confidence |
|------|---------|----------|------|------------|
| {ID} | X% | Y% | +Z | High/Med/Low |

**Total impact:** +{N} points across {M} items

**Implementation Plan**
1. Phase 1: {Description}
2. Phase 2: {Description}

**ROI Analysis**
- Effort: {Low/Medium/High}
- Priority: P{1/2/3}

---

## Cross-Vector Analysis

### Dependencies

```
Vector 1 ──enables──> Vector 3
Vector 2 ──blocks───> Vector 4
```

### Sequencing

| Phase | Vectors | Rationale |
|-------|---------|-----------|
| 1 | {List} | {Why first} |
| 2 | {List} | {Why second} |
| 3 | {List} | {Why third} |

### Effort/Impact Matrix

```
         High Impact
              │
    Quick Wins│ Major Projects
              │
──────────────┼──────────────
              │
    Fill-ins  │ Consider Later
              │
         Low Impact

        Low Effort ──> High Effort
```
```

## Change Impact Analysis Format

```markdown
# Change Impact Analysis

## Purpose

Establish causal attribution: Did code changes CAUSE observed performance deltas?

**Key principle:** Correlation ≠ Causation

---

## Code Changes Catalog

### Change 1: {Description}

**Commit:** {hash}
**Date:** {date}
**Files changed:** {list}

**Expected impact:**
- Should affect items with: {criteria}
- Mechanism: {how it should help}

**Observed impact:**
- Items affected: {list}
- Metric change: {before} → {after}

**Attribution confidence:** {Strong/Moderate/Weak/None}

**Evidence:**
- {Trace marker 1}
- {Trace marker 2}

---

## Attribution Summary

### What Worked

| Change | Items | Avg Improvement | Confidence |
|--------|-------|-----------------|------------|
| {Name} | N | +X% | Strong |

### What Didn't Work

| Change | Items | Observed | Expected | Gap |
|--------|-------|----------|----------|-----|
| {Name} | N | +X% | +Y% | -Z% |

### What Wasn't Tested

| Change | Reason | Items Needed |
|--------|--------|--------------|
| {Name} | {Why not tested} | N |

---

## Recommendations

Based on attribution analysis:

1. **Double down on:** {What worked}
2. **Investigate:** {Unexpected results}
3. **Next cycle:** {What to test}
```

## Attribution Confidence Levels

| Level | Confidence | Criteria |
|-------|------------|----------|
| Strong | 90%+ | Clear trace in artifacts, mechanism links change to outcome |
| Moderate | 60-89% | Evidence of change, likely caused improvement |
| Weak | 30-59% | Correlation but unclear mechanism |
| None | <30% | Change not evident or likely other factors |

## Attribution Process

1. **Catalog changes** - What changed between runs?
2. **Map to items** - Which items should each change affect?
3. **Validate attribution** - Compare artifacts, find trace markers
4. **Assign confidence** - Based on evidence strength
5. **Synthesize** - What worked, what didn't, what wasn't tested

## Stage 1 Enrichment

Stage 3 should enrich Stage 1 outputs with findings:

```markdown
## Bi-Directional Enrichment

After Vector 3 (Code Fixes), enrich:
- `diagnosis.md` - Add code bug locations
- `capability-gaps.md` - Add validation status

After Change Impact Analysis, enrich:
- `comparison-analysis.md` - Add attribution confidence
- `diagnosis.md` - Add validated bug confirmation
```

## Enrichment Pattern

```markdown
# In Stage 1 file (diagnosis.md)

## Code Bug Analysis (Enriched by Stage 3)

> **Note:** This section is initially empty. Stage 3 will add details.

**Bug identified:** {Added by Stage 3}
**Location:** {File:line added by Stage 3}
**Problem:** {Description added by Stage 3}
**Fix:** {Recommendation added by Stage 3}
**Expected impact:** +{N}% quality score
```

## Additional Resources

For complete synthesis patterns:
- **`${CLAUDE_PLUGIN_ROOT}/references/playbook-pattern.md`** - Section 5: Stage 3
