---
name: taxonomy-builder
description: This skill should be used when the user asks to "create classification system", "build taxonomy", "define failure tags", "design classification tags", "create mutually exclusive categories", or needs to build machine-readable classification systems for playbook analysis.
version: 0.1.0
---

# Taxonomy Builder

Create classification systems that are mutually exclusive, collectively exhaustive, and actionable.

## What is a Taxonomy?

A taxonomy is a standardized classification system that enables:
- Machine-readable aggregation in Stage 2
- Consistent tagging across items
- Pattern recognition across analyses
- Actionable categorization

## Taxonomy Requirements

### MECE Principle

**M**utually **E**xclusive, **C**ollectively **E**xhaustive:

- **Mutually Exclusive**: Each item fits in exactly one category
- **Collectively Exhaustive**: All items can be classified

### Actionable

Each category should inform what action to take:

```markdown
| Tag | Definition | System Fix |
|-----|------------|------------|
| {Tag} | {What it means} | {How to address} |
```

### Machine-Readable

Use consistent formats for aggregation:

```markdown
### Classification
- [ ] Tag 1
- [ ] Tag 2
- [ ] Tag 3
```

## Taxonomy Design Process

### Step 1: Identify Classification Need

Determine what dimension needs classification:
- Failure modes
- Item types
- Quality levels
- Gap categories
- Impact levels

### Step 2: Analyze Sample Items

Review 10-20 sample items to identify natural groupings:
- What patterns emerge?
- How do items differ?
- What categories would be actionable?

### Step 3: Define Categories

For each category, specify:

| Field | Description |
|-------|-------------|
| Tag | Short, consistent identifier |
| Definition | Precise description |
| When to Use | Specific criteria |
| Examples | Concrete cases |
| System Fix | What action it implies |

### Step 4: Test for MECE

Validate against samples:
- Can every item be classified?
- Does any item fit multiple categories?
- Is "Other" needed? (Should be <10% of items)

### Step 5: Document Edge Cases

Specify how to handle ambiguous items:

```markdown
## Edge Case Guidelines

### When item could be Tag A or Tag B

If {condition}, use Tag A.
If {condition}, use Tag B.
If both equally apply, prefer Tag A because {reason}.
```

## Taxonomy Document Format

```markdown
# Taxonomy: {Name}

## Purpose

{Why this taxonomy exists and how it's used}

## Categories

| Tag | Definition | When to Use | System Fix |
|-----|------------|-------------|------------|
| {Tag 1} | {Definition} | {Criteria} | {Action} |
| {Tag 2} | {Definition} | {Criteria} | {Action} |
| {Tag 3} | {Definition} | {Criteria} | {Action} |

## Usage in Analysis

Include this checklist in analysis documents:

```markdown
### {Taxonomy Name} Classification
- [ ] {Tag 1} ({Brief definition})
- [ ] {Tag 2} ({Brief definition})
- [ ] {Tag 3} ({Brief definition})
- [ ] Other: [specify]
```

## Decision Tree

```
Start
  │
  ├─ Is {condition A}? → Tag 1
  │
  ├─ Is {condition B}? → Tag 2
  │
  ├─ Is {condition C}? → Tag 3
  │
  └─ None of above → Other (specify)
```

## Edge Cases

### {Edge Case 1}
{Guidance}

### {Edge Case 2}
{Guidance}

## Examples

### Tag 1 Example
**Item:** {ID}
**Classification:** Tag 1
**Reasoning:** {Why this tag applies}

### Tag 2 Example
**Item:** {ID}
**Classification:** Tag 2
**Reasoning:** {Why this tag applies}
```

## Common Taxonomy Types

### Failure Mode Taxonomy

Classifies how analyses fail:

| Tag | Definition | System Fix |
|-----|------------|------------|
| Misattributed Blame | Blamed wrong component | Causal reasoning improvements |
| Shallow Analysis | Saw evidence but didn't analyze deeply | Depth requirements |
| Pattern Matching | Copied without verification | Add verification step |
| Symptom vs Cause | Treated symptom as cause | Guidance in prompts |
| Missing Evidence | Qualitative when numbers available | Better data extraction |
| Synthesis Failure | Had pieces, didn't connect | Add synthesis phase |
| Gave Up Early | Concluded "unable" too soon | Dynamic iteration |

### Item Type Taxonomy

Classifies items by category:

| Tag | Definition | Characteristics |
|-----|------------|-----------------|
| Type A | {Definition} | {Typical traits} |
| Type B | {Definition} | {Typical traits} |
| Type C | {Definition} | {Typical traits} |
| Multi-type | Multiple types involved | {How to handle} |

### Impact Level Taxonomy

Classifies by severity:

| Tag | Definition | Threshold |
|-----|------------|-----------|
| Critical | {Definition} | {Metric > X} |
| High | {Definition} | {Metric Y-X} |
| Medium | {Definition} | {Metric Z-Y} |
| Low | {Definition} | {Metric < Z} |

### Gap Category Taxonomy

Classifies missing capabilities:

| Tag | Definition | Fix Type |
|-----|------------|----------|
| Data Collection | Evidence doesn't exist | Build integration |
| Query/Access | Evidence exists, not queried | Fix access logic |
| Analysis | Evidence found, not used | Improve reasoning |

## Validation Checklist

Before finalizing taxonomy:

- [ ] Every sample item can be classified
- [ ] No item fits multiple categories
- [ ] "Other" category is <10% of items
- [ ] Each category has clear system fix
- [ ] Edge cases are documented
- [ ] Decision tree is unambiguous

## Additional Resources

For taxonomy best practices:
- **`${CLAUDE_PLUGIN_ROOT}/references/playbook-pattern.md`** - Section 4.8
