---
name: template-designer
description: This skill should be used when the user asks to "create output template", "design analysis template", "define output format", "build document template", "structure output with placeholders", or needs to author standardized templates for playbook outputs.
version: 0.1.0
---

# Template Designer

Author output templates with proper headers, placeholders, required/optional sections, and examples.

## Purpose of Templates

Templates ensure consistent output format across:
- Different items in Stage 1
- Different analysts running the playbook
- Different playbook executions

## Template Requirements

### Clear Section Headers

Use consistent markdown heading levels:

```markdown
# {Document Title}: {ID}

## Section 1
{Content}

### Subsection 1.1
{Content}

## Section 2
{Content}
```

### Placeholder Syntax

Use clear, distinguishable placeholders:

| Placeholder | Meaning |
|-------------|---------|
| `{Description}` | Text to fill in |
| `X%` | Numeric percentage |
| `N` | Count/number |
| `[List]` | Multiple items |
| `{ID}` | Identifier |

### Required vs Optional

Mark optional sections clearly:

```markdown
## Required Section
{Content}

## Optional Section (if applicable)
> Include this section only if {condition}

{Content}
```

### Examples of Good Output

Include concrete examples showing completed templates.

## Template Document Format

```markdown
# Template: {name}.md

**Purpose:** {What this template captures}

---

## Template

```markdown
# {Title}: {ID}

## Section 1
**Field 1:** {Description}
**Field 2:** X% ({qualifier})

## Section 2

### Subsection
{Content with [list] placeholder}

| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| {Value} | X% | {Note} |

## Optional Section (if applicable)

> **Note:** Include only if {condition}

{Placeholder content}

## Section (Enriched by Stage N)

> **Note:** Initially empty. Stage N will add details.

**Field:** [To be added by Stage N]
```

---

## Guidance

### Section 1 Guidelines
{How to fill this section}

### Section 2 Guidelines
{How to fill this section}

---

## Example

{Complete example showing filled-in template}
```

## Template Types

### Analysis Output Template

For Stage 1 per-item analysis:

```markdown
# Template: diagnosis.md

## Template

```markdown
# {Analysis Name}: {ID}

## Ground Truth
**Source:** {From which file}
**Key facts:** {What to extract}

## Analysis Result
**Finding:** {Main conclusion}
**Confidence:** {High/Medium/Low}

## Evidence

| Evidence | Source | Supports |
|----------|--------|----------|
| {Item} | {File} | {Conclusion} |

## Classification
- [ ] Tag 1
- [ ] Tag 2
- [ ] Tag 3

## Verdict
**Overall:** {Pass/Partial/Fail}
**Reasoning:** {1-2 sentences}
```
```

### Cluster Output Template

For Stage 2 aggregation:

```markdown
# Template: {axis}-clusters.md

## Template

```markdown
# {Axis} Clusters

## Overview

| Cluster | Count | % | Characteristic |
|---------|-------|---|----------------|
| {Name} | N | X% | {Brief} |

## Cluster: {Name}

### Items
| ID | Score | Notes |
|----|-------|-------|
| {ID} | X% | {Note} |

### Patterns
- {Pattern 1}
- {Pattern 2}

### Representative Example
{ID}: {Why representative}
```
```

### Summary Output Template

For Stage 4 executive summary:

```markdown
# Template: SUMMARY.md

## Template

```markdown
# Analysis Summary: {Title}

**Date:** {YYYY-MM-DD}
**Items:** N
**Baseline:** {Info or "None"}

## Key Metrics

| Metric | Value | Target |
|--------|-------|--------|
| {Name} | X% | Y% |

## Top Findings
1. {Finding with impact}
2. {Finding with impact}

## Recommendations
1. **{Action}**: {Expected impact}
2. **{Action}**: {Expected impact}

## Navigation
| Goal | Location |
|------|----------|
| {Use case} | `{path}` |
```
```

## Placeholder Guidelines

### Text Placeholders

```markdown
**Key Finding:** {From source_data.md - the primary finding}
```

Be specific about what goes in the placeholder.

### Numeric Placeholders

```markdown
**Score:** X% ({Bullseye/Strong/Partial/Weak})
```

Include qualifiers where relevant.

### List Placeholders

```markdown
**Missing observations:**
[List top 5 from scorecard - most critical first]
```

Specify count and ordering.

### Conditional Placeholders

```markdown
**Baseline comparison:** {Delta vs baseline, or "N/A" if no baseline}
```

Handle missing data cases.

## Section Patterns

### Enrichment Sections

Mark sections populated by later stages:

```markdown
## Code Bug Details (Enriched by Stage 3)

> **Note:** This section is initially empty. Stage 3 (Opportunity Analysis) will add code bug details if applicable.

**Bug identified:** [To be added by Stage 3]
**Location:** [File:line to be added by Stage 3]
**Problem:** [To be added by Stage 3]
**Fix:** [To be added by Stage 3]
```

### Conditional Sections

Mark sections that may not apply:

```markdown
## Baseline Comparison (if applicable)

> Include this section only if `comparison/` directory exists.

| Metric | Baseline | Current | Delta |
|--------|----------|---------|-------|
| {Name} | X% | Y% | {+/-}Z% |
```

### Checklist Sections

For classification:

```markdown
## Failure Classification
- [ ] Misattributed blame (blamed wrong component)
- [ ] Shallow analysis (saw evidence but didn't analyze)
- [ ] Evidence synthesis failure (had pieces, didn't connect)
- [ ] Other: [specify]
```

## Validation Checklist

Before finalizing template:

- [ ] All sections have clear headers
- [ ] Placeholders are specific and distinguishable
- [ ] Required vs optional clearly marked
- [ ] Enrichment sections noted
- [ ] Example of completed template included
- [ ] Guidance for each section provided

## Additional Resources

For template design patterns:
- **`${CLAUDE_PLUGIN_ROOT}/references/playbook-pattern.md`** - Section 4.3
