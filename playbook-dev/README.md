# playbook-dev

A Claude Code plugin for creating structured, multi-stage analysis playbooks that guide LLM agents through complex analytical workflows.

## What is a Playbook?

A playbook is an **executable specification** encoded as markdown documents that:
- Defines repeatable processes agents can follow autonomously
- Encodes domain expertise in machine-readable format
- Enables parallel execution through clear stage boundaries
- Produces consistent, high-quality outputs

## Features

### Guided Creation
Use `/playbook create` to walk through the full playbook creation process with interactive guidance.

### Skills by Category

**Scaffolding & Structure**
- `playbook-scaffold` - Create directory structure with placeholder files
- `master-instructions` - Author the orchestration document

**Stage Authoring**
- `stage-document` - Write stage README files
- `setup-stage` - Design Stage 0 (environment validation, scope)
- `per-item-stage` - Define parallel analysis with sub-agents
- `aggregation-stage` - Design clustering and synthesis
- `synthesis-stage` - Create opportunity and impact analysis
- `finalization-stage` - Design summaries and institutional memory

**Reference & Templates**
- `taxonomy-builder` - Create classification systems
- `template-designer` - Author output templates
- `glossary-creator` - Build term definitions
- `architecture-doc` - Document domain systems

**Quality & Validation**
- `quality-gates` - Define stage prerequisites and exit criteria
- `verification-script` - Generate completion check scripts
- `impact-estimation` - Design confidence frameworks

**Advanced Patterns**
- `attribution-framework` - Build causal attribution chains
- `clustering-strategy` - Define multi-axis clustering
- `bi-directional-enrichment` - Cross-stage enrichment patterns
- `meta-analysis` - Self-assessment structures

### Proactive Validation
The `playbook-validator` agent automatically checks your playbook at key milestones.

## Usage

```bash
# Start the guided wizard
/playbook create

# Or invoke skills directly as you build
# Claude will activate relevant skills based on context
```

## Playbook Structure

```
playbook/
├── instructions.md          # Master orchestration
├── stages/
│   ├── 0-setup/
│   ├── 1-per-item/
│   ├── 2-aggregation/
│   ├── 3-synthesis/
│   └── 4-finalization/
├── templates/
└── reference/
```

## Reference

See `references/playbook-pattern.md` for the complete playbook pattern documentation.
