---
name: architecture-doc
description: This skill should be used when the user asks to "document system architecture", "describe domain structure", "map system components", "create architecture reference", or needs to document the domain system being analyzed by the playbook.
version: 0.1.0
---

# Architecture Documentation

Document domain system structure for complex system analysis in playbooks.

## Purpose of Architecture Docs

Architecture documentation helps analysts understand:
- System components and their relationships
- Data flow through the system
- Key code locations and file patterns
- Integration points and dependencies

## When to Create

Create architecture documentation when:
- Playbook analyzes a technical system
- Multiple components interact
- Code inspection is part of analysis
- Domain knowledge is required for diagnosis

## Architecture Document Format

```markdown
# {System} Architecture

## Overview

{2-3 paragraph description of what the system does and its main components}

## System Diagram

```
[Component A] ─────> [Component B] ─────> [Component C]
      │                    │                    │
      ↓                    ↓                    ↓
[Data Store]         [External API]       [Output]
```

## Components

### Component A: {Name}

**Purpose:** {What this component does}

**Location:** `{path/to/code}`

**Key files:**
- `{file1.ext}` - {Purpose}
- `{file2.ext}` - {Purpose}

**Interfaces:**
- Input: {What it receives}
- Output: {What it produces}

**Dependencies:**
- {Dependency 1}
- {Dependency 2}

### Component B: {Name}

...

## Data Flow

### {Flow Name}

```
1. {Step 1} ──> [Component]
2. {Step 2} ──> [Component]
3. {Step 3} ──> [Component]
4. {Step 4} ──> [Output]
```

**Key transformation points:**
- At step 2: {What happens}
- At step 3: {What happens}

## Code Patterns

### {Pattern Name}

**Files:** `{pattern}*.ext`

**Purpose:** {What these files do}

**Example:**
```{language}
// Typical structure
{code example}
```

## Integration Points

### External Service: {Name}

**Purpose:** {What this integration does}

**Endpoint:** `{URL or path}`

**Data exchanged:**
- Request: {Format}
- Response: {Format}

**Failure modes:**
- {Failure 1}: {Impact}
- {Failure 2}: {Impact}

## Key Concepts

### {Concept 1}

{Explanation of domain concept relevant to analysis}

### {Concept 2}

{Explanation of domain concept relevant to analysis}

## Common Issues

| Issue | Symptoms | Typical Cause |
|-------|----------|---------------|
| {Issue 1} | {What you see} | {Root cause} |
| {Issue 2} | {What you see} | {Root cause} |

## Relevant Code Locations

For analysis purposes, key code is at:

| Purpose | Location |
|---------|----------|
| {Purpose 1} | `{path}` |
| {Purpose 2} | `{path}` |
| {Purpose 3} | `{path}` |
```

## Component Documentation

### Required Information

For each component:

| Field | Description |
|-------|-------------|
| Purpose | What it does in 1-2 sentences |
| Location | Path to source code |
| Key files | Most important files |
| Interfaces | What goes in/out |
| Dependencies | What it relies on |

### Optional Information

| Field | When to Include |
|-------|-----------------|
| Configuration | If configurable behavior |
| State | If maintains state |
| Concurrency | If parallel execution |
| Error handling | If complex failure modes |

## Data Flow Documentation

### Flow Diagrams

Use ASCII art for simplicity:

```
[Input] ──> [Process A] ──> [Process B] ──> [Output]
                │
                ↓
           [Side Effect]
```

### Sequence Diagrams

For temporal flows:

```
Client    Server    Database
   │         │          │
   │──req──> │          │
   │         │──query──>│
   │         │<─result──│
   │<─resp───│          │
```

## Code Pattern Documentation

### Pattern Format

```markdown
### {Pattern Name}

**Files matching:** `{glob pattern}`

**Purpose:** {What these files do}

**Typical structure:**
- {Section 1}: {Purpose}
- {Section 2}: {Purpose}

**Analysis focus:**
- Look for: {What to examine}
- Common issues: {What goes wrong}
```

### Common Patterns to Document

| Pattern | Example | Purpose |
|---------|---------|---------|
| Handlers | `handle_*.go` | Request processing |
| Models | `model_*.py` | Data structures |
| Services | `*_service.ts` | Business logic |
| Tests | `*_test.*` | Test coverage |

## Integration Documentation

### External Services

Document each external dependency:

```markdown
### {Service Name}

**Type:** {API/Database/Queue/etc}

**Purpose:** {Why we integrate}

**Access pattern:**
- Protocol: {HTTP/gRPC/etc}
- Authentication: {Method}
- Rate limits: {If any}

**Data format:**
- Request: {Schema/format}
- Response: {Schema/format}

**Failure handling:**
- Timeout: {Behavior}
- Error: {Behavior}
- Retry: {Policy}
```

## Validation Checklist

Before finalizing:

- [ ] All major components documented
- [ ] Data flows are traceable
- [ ] Key code locations specified
- [ ] Integration points covered
- [ ] Common issues listed
- [ ] Diagrams are accurate

## Additional Resources

For architecture documentation patterns:
- **`${CLAUDE_PLUGIN_ROOT}/references/playbook-pattern.md`** - Section 4.2
