---
name: bi-directional-enrichment
description: This skill should be used when the user asks to "design cross-stage enrichment", "create bi-directional updates", "enrich earlier outputs", "link later findings to earlier analysis", "update Stage 1 from Stage 3", or needs patterns for later stages to enrich earlier stage outputs.
version: 0.1.0
---

# Bi-Directional Enrichment

Design patterns for later stages to enrich earlier outputs, creating a connected knowledge graph.

## What is Bi-Directional Enrichment?

Traditional pipelines flow forward only:

```
Stage 1 → Stage 2 → Stage 3 → Stage 4
```

Bi-directional enrichment adds backward connections:

```
Stage 1 outputs ←── Enriched by ──→ Stage 3 findings
     ↑                                    │
     └─────────── Validated by ───────────┘
```

## Why Enrich Earlier Outputs?

1. **Context preservation** - Later insights appear alongside original analysis
2. **Navigation** - Users can find related information from any entry point
3. **Validation** - Later findings validate or refute earlier hypotheses
4. **Completeness** - Items have full context in one place

## Enrichment Patterns

### Pattern 1: Placeholder Sections

Reserve sections in early stage outputs for later stages to populate:

```markdown
# Stage 1 Template

## Original Analysis
{Stage 1 content}

## Code Bug Analysis (Enriched by Stage 3)

> **Note:** This section is initially empty. Stage 3 will add details.

**Bug identified:** [To be added by Stage 3]
**Location:** [File:line to be added by Stage 3]
**Problem:** [Description to be added by Stage 3]
**Fix:** [Recommendation to be added by Stage 3]
**Expected impact:** [Estimate to be added by Stage 3]
```

### Pattern 2: Attribution Tagging

Add attribution confidence from later analysis:

```markdown
# Stage 1: Comparison Analysis

## Performance Delta
Current: 75%
Baseline: 60%
Delta: +15 points

## Attribution (Added by Stage 3)

> **Note:** Added by Stage 3 Change Impact Analysis

**Primary attribution:** Change X (Strong confidence)
**Evidence:** {Trace marker found in artifacts}
**Secondary factors:** {Other contributing changes}
```

### Pattern 3: Cross-Reference Links

Add links to related later-stage analysis:

```markdown
# Stage 1: Capability Gaps

## Gap: Missing database inspection

...

## Related Analysis (Added by Stage 3)

**Opportunity:** See `opportunity-analysis/1-tool-capabilities.md#database-inspection`
**Impact estimate:** +12 points across 8 items
**Priority:** P1
```

### Pattern 4: Validation Status

Mark whether hypotheses were validated:

```markdown
# Stage 1: Diagnosis

## Failure Hypothesis
Suspected code bug in error handling.

## Validation Status (Added by Stage 3)

**Status:** ✅ Confirmed
**Evidence:** Code inspection found bug at `handler.go:245`
**Fix PR:** #1234
```

## Enrichment Process

### Step 1: Define Enrichment Points

Identify where later stages add value to earlier outputs:

```markdown
## Enrichment Map

| Stage 1 File | Enriched By | Section Added |
|--------------|-------------|---------------|
| diagnosis.md | Stage 3 | Code bug details |
| capability-gaps.md | Stage 3 | Validation status, priority |
| comparison-analysis.md | Stage 3 | Attribution confidence |
```

### Step 2: Create Placeholder Sections

Add placeholder sections in Stage 1 templates:

```markdown
## {Section Name} (Enriched by Stage {N})

> **Note:** This section is initially empty. Stage {N} ({Name}) will add {what}.

**Field 1:** [To be added by Stage {N}]
**Field 2:** [To be added by Stage {N}]
```

### Step 3: Document Enrichment Instructions

In Stage 3 instructions, specify how to enrich:

```markdown
## Stage 1 Enrichment

After completing {analysis}, enrich Stage 1 files:

### diagnosis.md Enrichment

**When:** After Vector 3 (Code Fixes) identifies code bugs

**Add to "Code Bug Analysis" section:**
- Bug identified: {from Vector 3 analysis}
- Location: {file:line from code inspection}
- Problem: {description of the bug}
- Fix: {recommended fix}
- Expected impact: {from impact estimation}

**Process:**
1. For each item with identified code bug
2. Read item's diagnosis.md
3. Fill in the Code Bug Analysis section
4. Write updated file
```

### Step 4: Verify Enrichment

Check that enrichment occurred:

```bash
# Verify enrichment sections populated
grep -l "To be added by Stage" items/*/analysis/*.md
# Should return empty if all enriched
```

## Enrichment Templates

### Code Bug Enrichment

```markdown
## Code Bug Analysis (Enriched by Stage 3)

**Bug identified:** Yes
**Location:** `{file}:{line}`
**Problem:** {Description of the bug}
**Fix:** {How to fix it}
**Expected impact:** +{N} points on quality score

**Reference:** See `opportunity-analysis/3-check-improvements.md#{anchor}`
```

### Attribution Enrichment

```markdown
## Change Attribution (Added by Stage 3)

**Attribution confidence:** {Strong/Moderate/Weak/None}

**Primary change:** {Change name}
- Commit: {hash}
- Evidence: {What trace markers found}

**Secondary factors:**
- {Factor 1}
- {Factor 2}

**Reference:** See `change-impact-analysis/investigation-impact.md#{item-id}`
```

### Validation Enrichment

```markdown
## Validation Status (Added by Stage 3)

**Hypothesis:** {Original Stage 1 hypothesis}

**Status:** {✅ Confirmed / ❌ Refuted / ⚠️ Partially confirmed}

**Evidence:**
- {Evidence point 1}
- {Evidence point 2}

**Updated assessment:** {Revised conclusion if needed}
```

### Priority Enrichment

```markdown
## Priority Assessment (Added by Stage 3)

**Aggregate priority:** P{1/2/3}

**Reasoning:**
- Impact: +{N} points
- Items affected: {count}
- Effort: {Low/Medium/High}

**Roadmap placement:** {Quarter/Phase}

**Reference:** See `opportunity-analysis/cross-vector-analysis.md#roadmap`
```

## Best Practices

### Clear Section Markers

Always mark enrichment sections clearly:

```markdown
## {Section} (Enriched by Stage N)

> **Note:** {Explanation of what this section contains and who adds it}
```

### Reference Back to Source

Include references to where the enrichment came from:

```markdown
**Reference:** See `{path-to-source}#{anchor}`
```

### Preserve Original Content

Never modify original Stage 1 content - only add to enrichment sections.

### Handle Missing Enrichment

If Stage 3 doesn't have relevant information:

```markdown
## Code Bug Analysis (Enriched by Stage 3)

**Bug identified:** No code bug identified
**Notes:** Issue appears to be reasoning/synthesis related, not code bug.
```

## Validation Checklist

Before finalizing enrichment design:

- [ ] Enrichment points identified for all relevant files
- [ ] Placeholder sections in Stage 1 templates
- [ ] Enrichment instructions in Stage 3
- [ ] References link correctly
- [ ] Verification method defined

## Additional Resources

For enrichment patterns:
- **`${CLAUDE_PLUGIN_ROOT}/references/playbook-pattern.md`** - Section 2.6
