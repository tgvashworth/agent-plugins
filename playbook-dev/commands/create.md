---
name: create
description: Create a new analysis playbook with guided wizard
argument-hint: [domain description]
allowed-tools:
  - Skill
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash(mkdir:*)
  - AskUserQuestion
  - TodoWrite
  - Task
---

# Create Analysis Playbook

Create a new multi-stage analysis playbook using the guided wizard.

## User Guidance

$1

## Instructions

1. **Load the playbook-wizard skill** immediately:
   ```
   Skill: playbook-wizard
   ```

2. **Follow the wizard workflow** defined in the skill:
   - Phase 1: Discovery - understand the analysis domain
   - Phase 2: Structure Design - create directory scaffold
   - Phase 3: Stage Definition - define each analysis stage
   - Phase 4: Reference Materials - create taxonomies, templates, glossary
   - Phase 5: Quality Framework - define gates and validation
   - Phase 6: Advanced Patterns - optional advanced features
   - Phase 7: Orchestration - create master instructions

3. **Track progress with TodoWrite** throughout the wizard process.

4. **Ask clarifying questions** using AskUserQuestion when:
   - Analysis domain is unclear
   - Multiple valid approaches exist
   - User input is needed for domain-specific decisions

5. **Load additional skills as needed**:
   - `playbook-scaffold` for directory structure
   - `setup-stage`, `per-item-stage`, etc. for stage design
   - `taxonomy-builder`, `template-designer` for reference materials
   - `quality-gates`, `verification-script` for quality framework

6. **After completion**, invoke the playbook-validator agent to check quality.

## Usage Examples

```
/playbook create code review analysis for pull request quality
/playbook create security audit for vulnerability assessment
/playbook create customer feedback analysis for support tickets
/playbook create operational review for production event postmortems
```

## Notes

- The wizard is interactive - it will ask questions to understand your domain
- Output is created in the current directory under `playbook/`
- Each skill provides specialized guidance for its area
- The full pattern reference is at `${CLAUDE_PLUGIN_ROOT}/references/playbook-pattern.md`
