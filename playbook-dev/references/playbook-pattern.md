# The Playbook Pattern: A Framework for LLM-Driven Analysis Pipelines

This document describes a generalized pattern for creating systematic, reproducible analysis workflows using LLM agents. The pattern applies broadly to any domain requiring structured multi-stage analysis.

---

# 1. What is a Playbook?

A **playbook** is a structured methodology encoded as markdown documents that guide LLM agents through complex, multi-stage analysis tasks.

## Definition

A playbook is NOT just documentation. It is an **executable specification** that:
- Defines a repeatable process that agents can follow autonomously
- Encodes domain expertise in a machine-readable format
- Enables parallel execution through clear stage boundaries
- Produces consistent, high-quality outputs regardless of who runs it

## Core Components

| Component | Purpose | Example |
|-----------|---------|---------|
| **Process documentation** | Step-by-step instructions for each stage | Stage READMEs |
| **Output templates** | Standardized formats for analysis artifacts | Diagnosis template |
| **Reference materials** | Domain knowledge, taxonomies, glossaries | Metrics glossary |
| **Quality gates** | Validation checklists between stages | Exit criteria |

## What Playbooks Solve

1. **Consistency** - Same analysis approach regardless of who/what runs it
2. **Reproducibility** - Results can be verified and repeated
3. **Scalability** - Parallelization through sub-agents
4. **Quality** - Built-in validation and cross-checking
5. **Extensibility** - New analyses added without restructuring
6. **Institutional memory** - Knowledge captured in documents, not heads

## When to Use a Playbook

Use playbooks when you have:
- Complex analysis requiring multiple passes over data
- Tasks benefiting from parallel processing
- Domains with established taxonomies and metrics
- Workflows requiring human oversight at key points
- Analysis that will be repeated regularly

---

# 2. General Principles

## 2.1 Progressive Refinement

Each stage builds on previous outputs, becoming more abstract and actionable:

```
Raw data → Item analysis → Patterns → Insights → Recommendations
```

Never skip stages. Each layer adds value.

## 2.2 Separation of Concerns

Keep different types of knowledge separate:

| Document Type | Defines |
|---------------|---------|
| Stage documents | WHAT to do |
| Templates | WHAT to output |
| Reference docs | HOW to interpret domain concepts |
| Master instructions | HOW to orchestrate |

This separation enables independent evolution and maintenance.

## 2.3 Autonomous Execution

After initial setup, the pipeline runs without intervention:
- Use approved tools (Write/Read/Edit) that don't prompt for permission
- Avoid shell operations that trigger permission requests
- Design for multi-hour unattended execution
- Handle errors gracefully within the pipeline

## 2.4 Standardized Taxonomies

Define classification systems upfront:
- Enable machine-readable aggregation
- Allow pattern recognition across items
- Support consistent metrics tracking
- Use tags that are mutually exclusive and collectively exhaustive

## 2.5 Explicit Quality Gates

Each stage must have:
- **Prerequisites:** What must exist before starting
- **Validation steps:** What to check during execution
- **Exit criteria:** What must be true before proceeding

Never allow a stage to "complete" without meeting exit criteria.

## 2.6 Bi-Directional Enrichment

Later stages should enrich earlier outputs:

```
Stage 1 outputs ←── Enriched by ──→ Stage 3 findings
     ↑                                    │
     └─────────── Validated by ───────────┘
```

This creates a connected knowledge graph, not isolated documents.

---

# 3. Architecture of a Playbook

## 3.1 Directory Structure

```
playbook/
├── instructions.md          ← Master orchestration document
├── stages/                  ← Per-stage instructions
│   ├── 0-{setup}/          ← Interactive setup phase
│   ├── 1-{per-item}/       ← Parallel item-level analysis
│   ├── 2-{aggregation}/    ← Pattern identification
│   ├── 3-{synthesis}/      ← Cross-cutting insights
│   └── 4-{finalization}/   ← Summary and output
├── templates/              ← Output format templates
└── reference/              ← Domain knowledge documents
```

## 3.2 Stage Types

| Stage Type | Execution Model | Purpose |
|------------|-----------------|---------|
| **Setup** | Interactive, sequential | Validate environment, establish scope |
| **Per-Item** | Parallel sub-agents | Deep analysis of individual items |
| **Aggregation** | Single agent | Pattern recognition across items |
| **Synthesis** | Parallel optional | Cross-cutting insights, recommendations |
| **Finalization** | Sequential | Summary generation, knowledge capture |

## 3.3 Document Hierarchy

```
instructions.md (master)
    ↓
stages/N-{name}/README.md (stage overview)
    ↓
stages/N-{name}/{analysis}.md (individual analyses)
    ↓
templates/{stage}/{file}.md (output templates)
    ↓
reference/{topic}.md (supporting knowledge)
```

## 3.4 Data Flow

```
[Input Data]
     ↓
Stage 0: Scope + Validation ─────→ scope.md
     ↓
Stage 1: Per-Item Analysis  ─────→ items/*/analysis/*.md
     ↓
Stage 2: Aggregation        ─────→ cohort-analysis/*.md
     ↓
Stage 3: Synthesis          ─────→ opportunity-analysis/*.md
     ↓                             change-impact-analysis/*.md
Stage 4: Finalization       ─────→ SUMMARY.md
                                   institutional-memory.md
```

---

# 4. Implementation Approaches and Details

## 4.1 Stage Document Format

Each analysis within a stage follows a standard format:

```markdown
# Analysis: [Name]

## Purpose
[What this analysis captures and why it matters]

## Output
**File:** `[output path]`

## Instructions
[Step-by-step guide for performing analysis]

## Template
[Output format to follow]

## Guidance
[Tips, examples, common pitfalls]
```

This format ensures:
- Self-contained instructions (agent doesn't need to read multiple files)
- Clear output expectations
- Reproducible methodology

## 4.2 Reference Document Types

| Type | Purpose | When to Create |
|------|---------|----------------|
| **Architecture** | Domain system structure | When analyzing complex systems |
| **Taxonomy** | Classification systems | When standardized tags needed |
| **Glossary** | Term definitions | When metrics/terms might be ambiguous |
| **Checklists** | Validation patterns | When quality gates are complex |
| **Operational** | Execution constraints | When autonomous operation needed |

## 4.3 Template Design

Templates should:
- Have clear section headers with `##` formatting
- Include placeholder syntax: `[Description]` or `X%`
- Define required vs optional sections (mark optional with "if applicable")
- Provide examples of good output
- Be directly copy-paste usable by agents

## 4.4 Parallelization Strategy

### Rolling Pipeline (Preferred)

Instead of batches, maintain constant agent count:

```
Start: Launch N agents for items 1-N
Item 3 completes → immediately launch agent for item N+1
Item 7 completes → immediately launch agent for item N+2
Continue until all items processed
```

**Benefits:**
- No idle time waiting for slowest agent
- Constant resource utilization
- Faster overall completion

### Optimal Agent Count

Balance between:
- **Parallelism benefit:** More agents = faster
- **System resources:** Too many = instability
- **Typical workload:** Target 2x agent count = 2 cycles through queue

## 4.5 Error Handling

### Stage-Level Failures
- Stop immediately on preflight failures
- Report clearly what failed and how to fix
- Require resolution before continuing

### Item-Level Failures
- Track failed items separately
- Re-launch failed items only
- Kill stuck agents after timeout
- Maintain retry list

### Validation Failures
- Cross-check outputs for consistency
- Flag contradictions for review
- Require minimum content thresholds (e.g., >500 bytes)

## 4.6 Scope Establishment

Create a scope document that captures:

| Category | Information |
|----------|-------------|
| **Execution mode** | Interactive (pause) vs Non-interactive (autonomous) |
| **Focus** | What questions to answer |
| **Data bounds** | What to analyze, time ranges, filters |
| **Comparison** | Baseline for comparison if applicable |
| **External context** | Code commits, config changes in scope |
| **Confirmation** | User approval timestamp |

## 4.7 Context Compaction

After setup completes, compact conversation context:

**Why compact:**
- Setup accumulates exploration artifacts
- Long context slows sub-agent execution
- Sub-agents need focused context

**Compaction protocol:**
1. Inform user setup is complete
2. Request context compaction
3. After compaction, reload essential documents:
   - Master instructions
   - Scope document
   - Next stage instructions
   - Operational constraints

## 4.8 Taxonomies and Classification

### Building Effective Taxonomies

**Characteristics of good classification tags:**
- Mutually exclusive (item fits in exactly one category)
- Collectively exhaustive (all items can be classified)
- Actionable (classification informs what to do)
- Machine-readable (consistent format for aggregation)

**Example taxonomy structure:**
```markdown
| Tag | Definition | When to Use | System Fix |
|-----|------------|-------------|------------|
| [Tag 1] | [Clear definition] | [Criteria] | [How to address] |
```

### Impact Estimation

Provide specific estimates with reasoning:

| Confidence | Variance | Criteria |
|------------|----------|----------|
| High | ±10 points | Direct evidence, clear causal mechanism |
| Medium | ±20 points | Logical connection, some uncertainty |
| Low | ±30 points | Speculative benefit |

## 4.9 Clustering and Aggregation

### Clustering Axes

Define multiple independent clustering dimensions:

| Axis Type | Purpose | Example |
|-----------|---------|---------|
| Performance | Group by outcome quality | High/Medium/Low |
| Failure Mode | Group by how things fail | Taxonomy tags |
| Item Type | Group by category | Code bugs vs External |
| Pipeline Stage | Group by where it fails | Collection vs Synthesis |
| Gap Type | Group by what's missing | Capability categories |
| Time/Evolution | Group by change | Improved vs Regressed |

### Cross-Cluster Analysis

The most valuable aggregation synthesizes across all axes:

**Multi-Axis Insights:**
- "When X is true, Y tends to be true"
- Correlation patterns across dimensions
- Interaction effects between axes

**Cohort Segmentation:**
| Segment | Multi-Axis Profile | Treatment |
|---------|-------------------|-----------|
| Ready | High perf, minimal gaps | Deploy now |
| Needs X | Medium perf, specific gap | Add capability |
| Needs Y | Low perf, structural issue | Architecture change |

### Priority Framework

```
Priority = (Items affected × Quality improvement) / (Effort × Risk)
```

## 4.10 Change Impact and Attribution

### The Attribution Challenge

Correlation ≠ Causation
- Correlation: "Quality improved between runs"
- Causation: "Quality improved BECAUSE of change X"

### Attribution Framework

```
Code/Config Change → Behavior Change → Performance Change
      ↓                    ↓                   ↓
 (What changed)      (How it behaved)    (What metrics show)
```

### Attribution Process

1. **Catalog changes** - What changed between runs?
2. **Map to items** - Which items should each change affect?
3. **Validate attribution** - Compare artifacts, find trace markers
4. **Assign confidence:**
   - Strong (90%+): Clear trace, mechanism links change to outcome
   - Moderate (60-89%): Evidence of change, likely caused improvement
   - Weak (30-59%): Correlation but unclear mechanism
   - None (<30%): Not evident or likely other factors
5. **Synthesize** - What worked, what didn't, what wasn't tested

## 4.11 Statistical Validation

For larger datasets (20+ items), statistical methods strengthen claims:

**A/B Testing:**
- Treatment: Items where change applies
- Control: Items where it shouldn't
- T-test or Mann-Whitney U for significance

**Regression Analysis:**
- Use when multiple changes occurred simultaneously
- Isolates independent contributions
- Coefficients show per-change impact

**When NOT to use:**
- Single clear change (simple comparison sufficient)
- Obvious causation (statistics add little)
- Small samples <15 (power too low)
- Time pressure (qualitative is faster)

## 4.12 Self-Assessment (Meta-Analysis)

Include meta-analysis of the analysis process itself.

**What to Track:**
| Category | Examples |
|----------|----------|
| Configuration errors | Setup mistakes |
| Playbook issues | Instructions unclear |
| Analysis gaps | Steps skipped |
| Attribution errors | Wrong conclusions |
| Tool problems | Scripts that failed |

**What NOT to Include:**
- Subject domain issues (go in item analysis)
- System improvements (go in opportunity analysis)

**Theme-Based Structure:**
1. Create initial themes after 3-5 items
2. Add item IDs to existing themes
3. Periodically consolidate

## 4.13 Verification Scripts

Build helper scripts to validate completion:

**Checks:**
1. Output directory exists
2. Required files exist
3. Files are non-trivial (>500 bytes)
4. Optional files present when expected

**Modes:**
- Detailed: Full report with issues
- Progress: Simple DONE/TODO list

**Exit codes:**
- 0: Complete
- 1: Incomplete

---

# 5. Key Stages for Implementation

## Stage 0: Setup (Interactive)

**Purpose:** Validate environment and establish scope before autonomous execution.

**Components:**
1. Environment validation (working directory, dependencies)
2. Data validation (required files exist, structure correct)
3. Baseline configuration (comparison setup if applicable)
4. Scope creation (execution mode, focus, bounds)
5. User confirmation
6. Context compaction

**Exit Criteria:**
- All validation checks pass
- Scope document created
- User confirmed
- Context compacted

## Stage 1: Per-Item Analysis (Parallel)

**Purpose:** Deep analysis of each item using multiple analysis types.

**Common Analysis Types:**
- **Diagnosis:** Compare outcome to expectation, classify failures
- **Evidence Flow:** Trace information through pipeline, identify gaps
- **Gap Identification:** Catalog missing capabilities with impact estimates
- **Comparison:** Delta analysis vs baseline (if exists)

**Execution:**
- Rolling pipeline with N concurrent agents
- Each agent processes one item completely
- As agents complete, launch new ones

**Cross-Reference Support:**
- Use consistent classification tags
- Note similar patterns in other items
- Track item IDs for clustering

## Stage 2: Aggregation (Single Agent)

**Purpose:** Cluster items to identify patterns across multiple dimensions.

**Clustering Process:**
1. Define clustering criteria per axis
2. Assign each item to clusters
3. Identify common characteristics per cluster
4. Find what distinguishes clusters
5. Select prototype examples
6. Calculate aggregate metrics

**Cross-Cluster Synthesis:**
- Multi-axis insights
- Cohort segmentation
- Priority framework

## Stage 3: Synthesis (Parallel Optional)

**Purpose:** Cross-cutting insights and actionable recommendations.

**Synthesis Types:**

### Opportunity Analysis
Examine failures through multiple vectors (lenses):
- Define question each vector answers
- Aggregate from earlier stages
- Specify solutions with impact estimates
- Create cross-vector roadmap

### Change Impact Analysis
Establish causal attribution:
- Catalog changes
- Map to items
- Validate attribution
- Synthesize patterns

### Bi-Directional Enrichment
Enrich Stage 1 outputs with Stage 3 findings:
- Add code bug locations to diagnosis files
- Add attribution confidence to comparison files
- Add validation status to gap files

## Stage 4: Finalization (Sequential)

**Purpose:** Administrative tasks - no new analysis, only synthesis and knowledge capture.

**Tasks:**

### Institutional Memory
Update persistent log with validated findings:
- Entry criteria: High confidence (90%+), significant impact
- Structure: What changed, impact, evidence, lessons

### Executive Summary
Create primary summary document:
- Scannable in 5-10 minutes
- Links to detailed files
- Navigation guide for different personas
- Key findings, opportunities, recommendations

**Success Criteria:**
- Memory updated (if applicable)
- Summary contains all sections
- All links valid
- Different personas can find relevant info

---

# 6. Anti-Patterns to Avoid

| Anti-Pattern | Problem | Alternative |
|--------------|---------|-------------|
| Monolithic instructions | Hard to maintain, agents get lost | Stage-specific documents |
| Implicit knowledge | Inconsistent analysis | Explicit taxonomies |
| No templates | Output format varies | Standardized templates |
| Batch parallelization | Idle time, slower completion | Rolling pipeline |
| Shell file operations | Permission prompts break autonomy | Use Write/Read/Edit tools |
| Vague guidance | Inconsistent interpretation | Specific examples |
| No validation | Errors propagate | Stage exit criteria |
| Per-item self-assessment | Duplication, hard to see patterns | Theme-based structure |
| Correlation as causation | Wrong conclusions | Attribution framework |

---

# 7. Generalization

This pattern applies to any domain where:

1. **Items** need individual deep analysis
2. **Patterns** emerge across items
3. **Synthesis** produces actionable insights
4. **Execution** benefits from parallelization
5. **Quality** requires systematic validation

**Example Domains:**
- Code review analysis
- Security audit workflows
- Research literature review
- Customer feedback analysis
- Performance evaluation
- Operational postmortem analysis
- Competitive intelligence gathering
- Compliance verification

---

# 8. Getting Started

To create a playbook for your domain:

1. **Define stages** - What are the major phases of your analysis?
2. **Create taxonomies** - What classification systems do you need?
3. **Design templates** - What should each output look like?
4. **Write instructions** - How should each analysis be performed?
5. **Add reference docs** - What domain knowledge is needed?
6. **Build validation** - How do you verify completion and quality?
7. **Test incrementally** - Run on a small sample, refine, expand

Start simple. A playbook doesn't need to be complete to be useful. Begin with the most critical analyses and expand over time.
