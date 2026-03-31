---
name: glossary-creator
description: This skill should be used when the user asks to "create glossary", "define metrics", "document terminology", "build term definitions", "define domain concepts", or needs to create standardized definitions for playbook analysis.
version: 0.1.0
---

# Glossary Creator

Build term definitions and metrics glossaries for domain concepts.

## Purpose of Glossaries

Glossaries ensure consistent interpretation of:
- Domain-specific terminology
- Metrics and their calculation methods
- Quality thresholds and targets
- Classification criteria

## Glossary Types

### Metrics Glossary

Define quantitative measures:

```markdown
# Metrics Glossary

## Overview

| Metric | Target | Formula |
|--------|--------|---------|
| {Name} | X% | {How calculated} |

## Metric Definitions

### {Metric Name}

**Definition:** {What it measures}

**Formula:**
```
{Metric} = {formula}
```

**Target:** {Target value with rationale}

**Interpretation:**
| Value | Meaning |
|-------|---------|
| ≥X% | {Interpretation} |
| Y-X% | {Interpretation} |
| <Y% | {Interpretation} |

**Data source:** {Where data comes from}

**Common issues:**
- {Issue 1}: {How to handle}
- {Issue 2}: {How to handle}
```

### Term Glossary

Define domain concepts:

```markdown
# Term Glossary

## Terms

### {Term}

**Definition:** {Clear, unambiguous definition}

**Context:** {When/where this term is used}

**Related terms:** {Links to related terms}

**Example:** {Concrete example of usage}

**Not to be confused with:** {Similar but different concepts}
```

### Quality Level Glossary

Define quality gradations:

```markdown
# Quality Levels

## Levels

| Level | Definition | Criteria |
|-------|------------|----------|
| Bullseye | {Definition} | {Specific criteria} |
| Strong | {Definition} | {Specific criteria} |
| Partial | {Definition} | {Specific criteria} |
| Weak | {Definition} | {Specific criteria} |
| Wrong | {Definition} | {Specific criteria} |

## Detailed Definitions

### Bullseye

**Definition:** {Precise definition}

**Criteria:**
- {Criterion 1}
- {Criterion 2}
- {Criterion 3}

**Example:** {What bullseye looks like}

### Strong

**Definition:** {Precise definition}
...
```

## Glossary Document Format

```markdown
# {Domain} Glossary

## Overview

This glossary defines key terms and metrics used in {domain} analysis.

## Quick Reference

| Term/Metric | Definition | Target/Threshold |
|-------------|------------|------------------|
| {Item 1} | {Brief} | {Value} |
| {Item 2} | {Brief} | {Value} |

---

## Detailed Definitions

### {Term/Metric 1}

**Definition:** {Full definition}

**Formula/Calculation:** {If metric}
```
{formula}
```

**Target:** {Target value}

**Interpretation:**
| Range | Meaning |
|-------|---------|
| ≥X | {Interpretation} |
| Y-X | {Interpretation} |
| <Y | {Interpretation} |

**Usage context:** {When this is used}

**Example:**
{Concrete example}

**Notes:**
- {Important consideration 1}
- {Important consideration 2}

---

### {Term/Metric 2}

...

---

## Common Confusions

### {Term A} vs {Term B}

| {Term A} | {Term B} |
|----------|----------|
| {Characteristic} | {Characteristic} |
| {When to use} | {When to use} |

---

## Appendix: Calculation Methods

### {Metric} Calculation

**Input data:**
- {Data source 1}
- {Data source 2}

**Steps:**
1. {Step 1}
2. {Step 2}
3. {Step 3}

**Edge cases:**
- {Edge case}: {How to handle}
```

## Writing Clear Definitions

### Be Specific

**Vague:** "A measure of quality"
**Specific:** "The percentage of correct observations divided by total observations made"

### Include Boundaries

**Unclear:** "High quality"
**Clear:** "Quality score ≥80% with no critical errors"

### Provide Context

```markdown
**Overall Quality Score**

**Definition:** Composite score combining accuracy and completeness metrics.

**Context:** Used as the primary metric for analysis quality assessment. A score ≥70% indicates production-ready performance.
```

### Show Calculations

```markdown
**F1 Score**

**Formula:**
```
F1 = 2 × (Precision × Recall) / (Precision + Recall)
```

**Where:**
- Precision = Correct observations / Total observations
- Recall = Found observations / Expected observations
```

## Metrics Table Format

Standard format for quick reference:

```markdown
## Metrics Summary

| Metric | Target | Definition |
|--------|--------|------------|
| Quality Score | 70%+ | Overall analysis quality |
| Accuracy | 75%+ | Correctness of primary findings |
| Precision | 90%+ | Accuracy of claims |
| Recall | 70%+ | Completeness of observations |
| F1 | 70%+ | Harmonic mean of precision/recall |
| Coverage | 90%+ | Evidence accessibility |
```

## Validation Checklist

Before finalizing glossary:

- [ ] All terms used in playbook are defined
- [ ] Definitions are unambiguous
- [ ] Metric formulas are explicit
- [ ] Targets/thresholds are specified
- [ ] Interpretation guides included
- [ ] Examples provided for complex concepts
- [ ] Related/confusing terms distinguished

## Additional Resources

For glossary best practices:
- **`${CLAUDE_PLUGIN_ROOT}/references/playbook-pattern.md`** - Section 4.2
