---
name: stage-document
description: This skill should be used when the user asks to "write a stage README", "create analysis document", "follow stage document format", "structure stage instructions", or needs guidance on the standard format for stage and analysis documents.
version: 0.1.0
---

# Stage Document Format

Write stage README files and analysis documents following the standard playbook format.

## Stage README Format

Every stage directory contains a README.md that defines:

```markdown
# Stage N: {Name}

{Brief description of stage purpose - 1-2 sentences}

---

## Execution Context

| Aspect | Details |
|--------|---------|
| **Execution** | {Sequential/Parallel} |
| **Agent** | {Main agent/Sub-agents} |
| **User interaction** | {Required/None} |
| **Outputs** | {Output directory or files} |

---

## Analyses in This Stage

| # | Analysis | File | Output |
|---|----------|------|--------|
| 1 | {Name} | `{file}.md` | `{output-path}` |
| 2 | {Name} | `{file}.md` | `{output-path}` |

---

## Inputs

- **{Input type}**: {Description}
- **{Input type}**: {Description}

## Outputs

- **{Output file}**: {Description}
- **{Output file}**: {Description}

---

## How to Run

```
1. Read this README.md
2. For each analysis in the table:
   a. Read the analysis file
   b. Execute the instructions
   c. Write the output file
3. Verify all outputs exist
4. Proceed to next stage
```

---

## Exit Criteria

Stage N is complete when:

- [ ] {Criterion 1}
- [ ] {Criterion 2}
- [ ] All outputs exist and are non-trivial (>500 bytes)

---

## Adding New Analyses

To add a new analysis to this stage:

1. Create new `.md` file in this directory
2. Follow the standard analysis format
3. Add to the analyses table above
4. Create corresponding template if needed
5. Update instructions.md if analysis produces new outputs
```

## Analysis Document Format

Each analysis within a stage follows this structure:

```markdown
# Analysis: {Name}

## Purpose

{What this analysis captures and why it matters - 2-3 sentences}

## Output

**File:** `{output path relative to item}`

## Instructions

### What to Analyze

{List of things to examine}

1. **{Category 1}**
   - {Detail}
   - {Detail}

2. **{Category 2}**
   - {Detail}
   - {Detail}

### How to Perform Analysis

**Step 1: {Action}**
{Detailed instructions}

**Step 2: {Action}**
{Detailed instructions}

**Step 3: {Action}**
{Detailed instructions}

## Template

```markdown
# {Output Title}: {ID}

## Section 1
{Content description}

## Section 2
{Content description}

## Section 3 (Enriched by Stage N)

> **Note:** This section is initially empty. Stage N will add details.

{Placeholder content}
```

## Guidance

### {Topic 1}

{Guidance content}

### {Topic 2}

| Condition | Action |
|-----------|--------|
| {When X} | {Do Y} |
| {When A} | {Do B} |

### Example

{Concrete example showing good output}

## Common Pitfalls

**Don't:**
- {Anti-pattern 1}
- {Anti-pattern 2}

**Do:**
- {Best practice 1}
- {Best practice 2}
```

## Key Principles

### Self-Contained Instructions

Each analysis document should be readable in isolation:
- Include all necessary context
- Reference source files explicitly
- Provide complete templates
- Give concrete examples

### Machine-Readable Tags

Use consistent, enumerable tags for aggregation:

```markdown
### Classification Tags
- [ ] Tag 1 (definition)
- [ ] Tag 2 (definition)
- [ ] Tag 3 (definition)
```

This enables Stage 2 to aggregate by tag.

### Bi-Directional Enrichment

Mark sections that later stages will populate:

```markdown
## Code Bug Analysis (Enriched by Stage 3)

> **Note:** This section is initially empty. Stage 3 will add code bug details if applicable.

**Bug identified:** [To be added by Stage 3]
**Location:** [File:line to be added by Stage 3]
```

### Clear Input/Output Mapping

Specify exact files to read and write:

```markdown
## Instructions

**Read these files:**
- `item/source_data.md` - Ground truth
- `item/analysis_output.md` - System conclusion
- `item/scorecard.md` - Metrics

**Write this file:**
- `item/analysis/findings.md`
```

## Execution Context Table

### Execution Types

| Type | Description |
|------|-------------|
| Sequential | One step at a time, main agent |
| Parallel | Multiple sub-agents concurrently |
| Sequential, Interactive | Main agent, requires user input |

### Agent Types

| Type | Description |
|------|-------------|
| Main agent | The orchestrating agent |
| Sub-agents | Spawned agents for parallel work |
| N concurrent | Specific count of parallel agents |

### User Interaction Types

| Type | Description |
|------|-------------|
| Required | Must get user confirmation |
| Optional | May ask questions |
| None | Fully autonomous |

## Stage-Specific Patterns

### Stage 0 (Setup)

- Always Sequential, Interactive
- Checklist format for preflight checks
- Must end with user confirmation

### Stage 1 (Per-Item)

- Typically Parallel with N sub-agents
- One README + multiple analysis files
- Clear per-item input/output paths

### Stage 2 (Aggregation)

- Typically Sequential, single agent
- Reads all Stage 1 outputs
- Produces cluster/pattern files

### Stage 3 (Synthesis)

- Can be Parallel (independent syntheses)
- Cross-cutting analysis
- May enrich Stage 1 outputs

### Stage 4 (Finalization)

- Always Sequential
- No new analysis
- Summary and knowledge capture

## Additional Resources

For complete stage document examples:
- **`${CLAUDE_PLUGIN_ROOT}/references/playbook-pattern.md`** - Section 4
