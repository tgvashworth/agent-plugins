---
name: playbook-wizard
description: This skill should be used when the user asks to "create a playbook", "build an analysis playbook", "design a multi-stage workflow", "set up an LLM analysis pipeline", or uses the /playbook create command. Provides guided, step-by-step playbook creation orchestrating all other playbook-dev skills.
version: 0.1.0
---

# Playbook Creation Wizard

Guide users through creating a complete analysis playbook by orchestrating all playbook-dev skills in sequence.

## What is a Playbook?

A playbook is an **executable specification** encoded as markdown that guides LLM agents through complex, multi-stage analysis tasks. Unlike documentation, playbooks are machine-readable instructions that enable:

- Repeatable processes agents can follow autonomously
- Parallel execution through clear stage boundaries
- Consistent, high-quality outputs regardless of who runs it
- Institutional knowledge capture in documents, not heads

## Wizard Workflow

### Phase 1: Discovery

Understand the analysis domain and goals:

1. **Identify the analysis domain**
   - What items need individual deep analysis?
   - What patterns emerge across items?
   - What actionable insights should result?

2. **Define success criteria**
   - What questions should the playbook answer?
   - What outputs do stakeholders need?
   - How will quality be measured?

3. **Map existing knowledge**
   - What taxonomies or classification systems exist?
   - What domain expertise should be encoded?
   - What reference materials are available?

Ask clarifying questions using AskUserQuestion to understand the domain before proceeding.

### Phase 2: Structure Design

Load the `playbook-scaffold` skill to create the directory structure:

```
playbook/
├── instructions.md          # Master orchestration
├── stages/
│   ├── 0-{setup}/          # Interactive setup
│   ├── 1-{per-item}/       # Parallel item analysis
│   ├── 2-{aggregation}/    # Pattern identification
│   ├── 3-{synthesis}/      # Cross-cutting insights
│   └── 4-{finalization}/   # Summary and output
├── templates/              # Output format templates
└── reference/              # Domain knowledge
```

Customize stage names based on the domain (e.g., `1-per-document/`, `1-per-entry/`, `1-per-record/`).

### Phase 3: Stage Definition

For each stage, load the appropriate skill:

| Stage | Skill to Load | Purpose |
|-------|---------------|---------|
| Stage 0 | `setup-stage` | Environment validation, scope creation |
| Stage 1 | `per-item-stage` | Parallel item-level analysis |
| Stage 2 | `aggregation-stage` | Clustering and pattern recognition |
| Stage 3 | `synthesis-stage` | Opportunity and impact analysis |
| Stage 4 | `finalization-stage` | Summary and institutional memory |

Each stage skill guides creating:
- Stage README with execution context
- Individual analysis documents
- Exit criteria and quality gates

### Phase 4: Reference Materials

Load these skills to create supporting documents:

| Need | Skill | Output |
|------|-------|--------|
| Classification system | `taxonomy-builder` | Mutually exclusive, actionable tags |
| Output formats | `template-designer` | Standardized templates with placeholders |
| Term definitions | `glossary-creator` | Metrics and domain concept definitions |
| System documentation | `architecture-doc` | Domain system structure |

### Phase 5: Quality Framework

Load these skills to establish quality controls:

| Need | Skill | Output |
|------|-------|--------|
| Stage gates | `quality-gates` | Prerequisites, validation, exit criteria |
| Completion checks | `verification-script` | Scripts to validate outputs |
| Impact estimation | `impact-estimation` | Confidence frameworks |

### Phase 6: Advanced Patterns (Optional)

For complex playbooks, load:

| Need | Skill | Purpose |
|------|-------|---------|
| Causal analysis | `attribution-framework` | Change-to-outcome attribution |
| Multi-axis grouping | `clustering-strategy` | Performance, failure mode, etc. |
| Cross-stage enrichment | `bi-directional-enrichment` | Later stages enrich earlier outputs |
| Self-assessment | `meta-analysis` | Theme-based playbook issue tracking |

### Phase 7: Orchestration

Load `master-instructions` skill to create the instructions.md file that:
- Defines stage sequencing
- Specifies agent counts for parallel stages
- Sets operational constraints
- Documents file dependencies

## Execution Model

### Interactive vs Non-Interactive

Playbooks support two execution modes:

| Mode | When to Use |
|------|-------------|
| **Interactive** | Initial runs, debugging, user wants review points |
| **Non-interactive** | Overnight runs, established playbooks, automation |

Stage 0 is always interactive. Subsequent stages can run autonomously.

### Parallelization

Stage 1 (per-item) typically uses parallel sub-agents:

```
Rolling Pipeline:
- Launch N agents for items 1-N
- As each completes, launch next item
- Maintains constant N-agent utilization
- No idle time waiting for slowest agent
```

Recommended: 15-25 concurrent agents depending on system resources.

## Progress Tracking

Use TodoWrite throughout to track:
- [ ] Phase 1: Discovery complete
- [ ] Phase 2: Structure created
- [ ] Phase 3: All stages defined
- [ ] Phase 4: Reference materials created
- [ ] Phase 5: Quality framework established
- [ ] Phase 6: Advanced patterns (if needed)
- [ ] Phase 7: Master instructions complete

## Validation

After completing the wizard, invoke the `playbook-validator` agent to check:
- Directory structure completeness
- Stage README formats
- Template consistency
- Exit criteria coverage
- Reference document quality

## Example Domains

Playbooks work well for:

| Domain | Items | Patterns | Insights |
|--------|-------|----------|----------|
| Code review | Pull requests | Bug types, complexity | Review guidelines |
| Security audit | Vulnerabilities | Attack vectors | Remediation priorities |
| Research review | Papers | Methodologies | Knowledge synthesis |
| Customer feedback | Tickets | Complaint types | Product priorities |
| Operational review | Events | Failure modes | System improvements |

## Additional Resources

For the complete playbook pattern specification:
- **`${CLAUDE_PLUGIN_ROOT}/references/playbook-pattern.md`** - Full pattern documentation

For real-world implementation examples, ask the user if they have existing playbooks to reference.
