---
name: playbook-scaffold
description: This skill should be used when the user asks to "create playbook directory structure", "scaffold a playbook", "set up playbook folders", "initialize playbook directories", or needs the initial file/folder layout for a new playbook.
version: 0.1.0
---

# Playbook Scaffold

Create the complete directory structure for a new analysis playbook with placeholder files.

## Directory Structure

```
playbook/
├── instructions.md              # Master orchestration document
├── scope.md                     # Analysis scope (generated at runtime)
├── stages/
│   ├── 0-{setup}/
│   │   ├── README.md           # Stage overview
│   │   ├── environment.md      # Environment validation
│   │   ├── data-validation.md  # Input data validation
│   │   └── scope-creation.md   # Scope document creation
│   ├── 1-{per-item}/
│   │   ├── README.md           # Stage overview
│   │   └── {analysis-type}.md  # One file per analysis type
│   ├── 2-{aggregation}/
│   │   ├── README.md           # Stage overview
│   │   └── {cluster-type}.md   # One file per clustering axis
│   ├── 3-{synthesis}/
│   │   ├── README.md           # Stage overview
│   │   └── {synthesis-type}.md # One file per synthesis type
│   └── 4-{finalization}/
│       ├── README.md           # Stage overview
│       ├── summary.md          # Executive summary creation
│       └── institutional-memory.md  # Knowledge capture
├── templates/
│   ├── per-item/               # Stage 1 output templates
│   ├── aggregation/            # Stage 2 output templates
│   ├── synthesis/              # Stage 3 output templates
│   └── summary/                # Stage 4 output templates
└── reference/
    ├── taxonomy.md             # Classification systems
    ├── glossary.md             # Term definitions
    └── architecture.md         # Domain system structure
```

## Naming Conventions

### Stage Directories

Use numbered prefixes with descriptive names:
- `0-preflight/` or `0-setup/` - Setup stage
- `1-per-document/`, `1-per-entry/`, `1-per-record/` - Per-item stage
- `2-cohort-clustering/`, `2-pattern-analysis/` - Aggregation stage
- `3-synthesis/`, `3-recommendations/` - Synthesis stage
- `4-finalization/`, `4-summary/` - Finalization stage

### Analysis Files

Use kebab-case with descriptive names:
- `findings.md` - Primary analysis
- `evidence-assessment.md` - Evidence flow mapping
- `gap-analysis.md` - Missing capability identification
- `performance-clusters.md` - Performance-based grouping

## Scaffold Creation Process

### Step 1: Gather Requirements

Ask the user:
1. What is the analysis domain? (e.g., incident analysis, code review)
2. What items will be analyzed? (e.g., incidents, PRs, documents)
3. What analyses per item? (e.g., diagnosis, evidence flow, gaps)
4. What clustering dimensions? (e.g., performance, failure mode, type)
5. What synthesis outputs? (e.g., opportunities, impact analysis)

### Step 2: Create Directory Structure

```bash
# Create main directories
mkdir -p playbook/stages/{0-setup,1-per-item,2-aggregation,3-synthesis,4-finalization}
mkdir -p playbook/templates/{per-item,aggregation,synthesis,summary}
mkdir -p playbook/reference
```

### Step 3: Create Placeholder Files

For each directory, create placeholder markdown files:

**Stage README Template:**
```markdown
# Stage N: {Name}

{Brief description of stage purpose}

---

## Execution Context

| Aspect | Details |
|--------|---------|
| **Execution** | {Sequential/Parallel} |
| **Agent** | {Main agent/Sub-agents} |
| **User interaction** | {Required/None} |
| **Outputs** | {Output directory/files} |

---

## Analyses in This Stage

| # | Analysis | File | Output |
|---|----------|------|--------|
| 1 | {Name} | `{file}.md` | `{output-path}` |

---

## Inputs

- {Input 1}
- {Input 2}

## Outputs

- {Output 1}
- {Output 2}

---

## Exit Criteria

- [ ] {Criterion 1}
- [ ] {Criterion 2}
```

**Analysis Document Template:**
```markdown
# Analysis: {Name}

## Purpose

{What this analysis captures and why it matters}

## Output

**File:** `{output path}`

## Instructions

{Step-by-step guide}

## Template

{Output format to follow}

## Guidance

{Tips, examples, common pitfalls}
```

### Step 4: Create Master Instructions Placeholder

Create `playbook/instructions.md` with sections for:
- Overview
- Stage sequencing
- Agent configuration
- File dependencies
- Operational constraints

## Customization Patterns

### Domain-Specific Stage Names

| Domain | Stage 1 | Stage 2 | Stage 3 |
|--------|---------|---------|---------|
| Code Review | `1-per-pr/` | `2-pattern-analysis/` | `3-recommendations/` |
| Security Audit | `1-per-finding/` | `2-vulnerability-clusters/` | `3-remediation/` |
| Research Review | `1-per-paper/` | `2-methodology-clusters/` | `3-knowledge-synthesis/` |
| Operational Review | `1-per-event/` | `2-cohort-clustering/` | `3-synthesis/` |

### Analysis Types by Domain

| Domain | Common Stage 1 Analyses |
|--------|------------------------|
| Code Review | quality-assessment, pattern-detection, impact-analysis |
| Security Audit | vulnerability-details, exploit-paths, remediation-options |
| Operational Review | findings, evidence-assessment, gap-analysis, comparison |

## File Operations

Use Write tool for all file creation (not shell commands):

```
Write tool: Create playbook/stages/0-setup/README.md
Write tool: Create playbook/stages/1-per-item/README.md
...
```

This ensures autonomous operation without permission prompts.

## Validation

After scaffolding, verify:
- [ ] All stage directories created
- [ ] Each stage has README.md
- [ ] Template directories match stages
- [ ] Reference directory exists
- [ ] instructions.md placeholder exists

## Additional Resources

For complete directory structure patterns:
- **`${CLAUDE_PLUGIN_ROOT}/references/playbook-pattern.md`** - Section 3: Architecture
