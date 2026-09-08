---
name: create
description: >
  Create a new multi-stage analysis playbook with the guided wizard. Use when
  the user invokes /playbook-dev:create, says "create a playbook", "build an
  analysis playbook", or asks to scaffold a new LLM analysis pipeline for a
  domain.
argument-hint: "[domain description]"
---

# Create an analysis playbook

Create a new multi-stage analysis playbook using the guided wizard.

## User guidance

If the user described the analysis domain with the request (for example "code
review analysis for pull request quality"), treat it as the answer to the
wizard's first discovery questions. Otherwise the wizard asks.

## Instructions

1. **Load the `playbook-wizard` skill** immediately and follow its workflow:
   - Phase 1: Discovery. Understand the analysis domain.
   - Phase 2: Structure design. Create the directory scaffold.
   - Phase 3: Stage definition. Define each analysis stage.
   - Phase 4: Reference materials. Create taxonomies, templates, glossary.
   - Phase 5: Quality framework. Define gates and validation.
   - Phase 6: Advanced patterns. Optional advanced features.
   - Phase 7: Orchestration. Create the master instructions.

2. **Track progress** through the phases with whatever task-tracking the host
   provides, so the user can see where the wizard is.

3. **Ask clarifying questions** when the analysis domain is unclear, several
   valid approaches exist, or a domain-specific decision needs the user's
   input.

4. **Load additional skills as needed:**
   - `playbook-scaffold` for directory structure
   - `setup-stage`, `per-item-stage`, and the other stage skills for stage
     design
   - `taxonomy-builder`, `template-designer` for reference materials
   - `quality-gates`, `verification-script` for the quality framework

5. **After completion**, run the `playbook-validator` skill to check quality.

## Usage examples

```
/playbook-dev:create code review analysis for pull request quality
/playbook-dev:create security audit for vulnerability assessment
/playbook-dev:create customer feedback analysis for support tickets
/playbook-dev:create operational review for production event postmortems
```

## Notes

- The wizard is interactive. It asks questions to understand the domain.
- Output is created in the current directory under `playbook/`.
- Each skill provides specialised guidance for its area.
- The full pattern reference is in
  [playbook-pattern.md](../../references/playbook-pattern.md).
