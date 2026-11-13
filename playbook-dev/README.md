# playbook-dev

Skills for designing analysis playbooks in Claude Code, Codex, and other Agent
Skills hosts.

## What is a playbook?

A playbook is a set of Markdown instructions that agents follow to analyse a
dataset. It defines the work, stage order, outputs, and checks for completion.

The standard playbook has five stages: setup, individual analysis, aggregation,
synthesis, and finalisation. Stages can use parallel agents where the work is
independent. Shared templates and definitions keep outputs consistent.

## Features

### Guided creation

Start with `create` or `playbook-wizard` to design a complete playbook.
Use the other skills to write or improve individual parts.

### Skills by category

**Creating a playbook**

- [create](skills/create/README.md): Start the guided process for creating an analysis playbook.
- [playbook-wizard](skills/playbook-wizard/README.md): Design an analysis playbook through a guided conversation.

**Directories and instructions**

- [playbook-scaffold](skills/playbook-scaffold/README.md): Create the directories and placeholder files for a five-stage analysis playbook.
- [master-instructions](skills/master-instructions/README.md): Write instructions.md, the main entry point for running a playbook.

**Stages**

- [stage-document](skills/stage-document/README.md): Write a stage README or analysis document using the playbook format.
- [setup-stage](skills/setup-stage/README.md): Design Stage 0, which checks the environment and data before analysis starts.
- [per-item-stage](skills/per-item-stage/README.md): Design Stage 1, where agents analyse individual records in parallel.
- [aggregation-stage](skills/aggregation-stage/README.md): Design Stage 2 to group individual results and find patterns across the dataset.
- [synthesis-stage](skills/synthesis-stage/README.md): Design Stage 3 to turn patterns into recommendations.
- [finalization-stage](skills/finalization-stage/README.md): Design Stage 4 to summarise findings and save reusable knowledge.

**References and templates**

- [taxonomy-builder](skills/taxonomy-builder/README.md): Create categories for classifying analysis results.
- [template-designer](skills/template-designer/README.md): Design templates for playbook outputs.
- [glossary-creator](skills/glossary-creator/README.md): Define the terms and metrics used in an analysis.
- [architecture-doc](skills/architecture-doc/README.md): Document the system being analysed.

**Quality and validation**

- [quality-gates](skills/quality-gates/README.md): Define the checks required before, during, and after each stage.
- [verification-script](skills/verification-script/README.md): Generate scripts that check playbook outputs.
- [impact-estimation](skills/impact-estimation/README.md): Define how to estimate the effect of proposed improvements.
- [playbook-validator](skills/playbook-validator/README.md): Check a playbook's directory structure, stage documents, templates, references, quality checks, and main instructions.

**Analysis methods**

- [attribution-framework](skills/attribution-framework/README.md): Define how to connect a change to altered behaviour and measured outcomes.
- [clustering-strategy](skills/clustering-strategy/README.md): Define how to group analysis results across several dimensions.
- [bi-directional-enrichment](skills/bi-directional-enrichment/README.md): Design updates that carry later findings back into earlier analysis outputs.
- [meta-analysis](skills/meta-analysis/README.md): Assess how well the playbook and analysis process worked.

### Validation

The `playbook-validator` workflow checks directory structure, documents,
templates, references, and quality criteria. It reports problems without editing
the playbook. Claude Code also provides it as a validator agent.

## Usage

Describe the analysis you need:

> Create a playbook for analysing customer support tickets. Find recurring
> causes of escalation and recommend improvements.

Or invoke the guided process explicitly in Claude Code:

```text
/playbook-dev:create customer feedback analysis for support tickets
```

In Codex:

```text
$playbook-wizard customer feedback analysis for support tickets
```

For a specific task, name the skill in Claude Code or Codex:

```text
/playbook-dev:quality-gates define completion criteria for Stage 1
$quality-gates define completion criteria for Stage 1
```

Each skill's README includes examples for both hosts. The
[repository README](../README.md#installation) covers installation.

## Playbook structure

```text
playbook/
├── instructions.md          # Stage order and execution rules
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

See [playbook-pattern.md](references/playbook-pattern.md) for the full playbook
format and execution model.
