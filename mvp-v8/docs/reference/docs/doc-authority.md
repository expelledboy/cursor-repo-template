---
title: "Doc authority + structure (v8, Reference)"
status: stable
created_date: 2026-01-16
purpose: "Deterministically route documentation changes using Hybrid Diátaxis + Domain"
domain: docs
---

# Doc authority + structure (v8, Reference)

Status: Stable
Date: 2026-01-16
Purpose: Complete canonical reference for documentation system structure, authority rules, and content organization.

## Authority Order (Conflict Resolver)
**[reference → how-to → explanation → tutorials → work → archive](docs/reference/docs/glossary.md#authority-order)**

When documentation conflicts, defer to higher authority sources. This ensures stable facts override temporary guidance.

## Diátaxis Framework

The documentation system uses **[Diátaxis](docs/reference/docs/glossary.md#diátaxis)** principles with [domain-based organization](docs/reference/docs/glossary.md#domain-organization):

### Reference (`docs/reference/**`)
**Purpose**: Stable facts, contracts, schemas, invariants - "What is X?"

**Content**: Complete specifications, API definitions, data models, invariants that change infrequently.
**Audience**: Developers needing authoritative technical details.
**Stability**: High - represents current system truth.

**Examples**:
- `docs/reference/agentos/` - AgentOS specifications and schemas
- `docs/reference/docs/` - Documentation system specifications

### How-to (`docs/how-to/**`)
**Purpose**: Step-by-step procedures - "How do I do X?"

**Content**: Installation guides, configuration steps, workflows, troubleshooting procedures.
**Audience**: Users performing specific tasks.
**Stability**: Medium - may change with process updates.

**Examples**:
- `docs/how-to/agentos/` - AgentOS usage procedures
- `docs/how-to/docs/` - Documentation creation procedures

### Explanation (`docs/explanation/**`)
**Purpose**: Design rationale and architecture - "Why is X this way?"

**Content**: Design decisions, architectural reasoning, historical context, trade-off analysis.
**Audience**: Architects and engineers understanding system design.
**Stability**: Medium-High - evolves with system understanding.

**Examples**:
- `docs/explanation/agentos/` - AgentOS design rationale
- `docs/explanation/architecture/` - System architecture rationale
- `docs/explanation/decisions/` - Design decisions linking problems to solutions

### Tutorials (`docs/tutorials/**`)
**Purpose**: Learning-oriented guides - "How do I learn X?"

**Content**: Getting started guides, conceptual overviews, learning walkthroughs.
**Audience**: New users learning the system.
**Stability**: Medium - may evolve with onboarding improvements.

**Examples**:
- `docs/tutorials/agentos/` - AgentOS getting started guides

### Work (`docs/work/<category>/YYYY-MM-DD-<slug>.md`)
**Purpose**: Drafts and research becoming canonical - "What might X become?"

**Content**: Research findings, experimental features, problem analysis, emerging patterns.
**Audience**: Contributors developing new capabilities.
**Stability**: Low - active development and research.

**Required**: Include **Status** field (active/draft) and **Date**.

**Examples**:
- `docs/work/research/` - Research findings and analysis
- `docs/work/problems/` - Current problems registry and analysis
- `docs/work/discoveries/` - System discoveries and insights

### Local (`docs/local/`)
**Purpose**: Temporary development files - not committed.

**Content**: Current work-in-progress, scratch notes, short-term experiments.
**Audience**: Individual developers.
**Stability**: Ephemeral - not version controlled.

### Archive (`docs/archive/**`)
**Purpose**: Superseded material with historical record.

**Content**: Old specifications, deprecated features, historical documentation.
**Required**: 
1. `original_path: <path>` in frontmatter to preserve provenance.
2. Frontmatter supersede status:
```yaml
status: superseded
superseded_by: docs/reference/agentos/cursor-integration-specs.md
superseded_date: 2026-01-18
superseded_reason: Distilled into Reference
```

**Note**: Work files (problems, discoveries) should generally NOT be archived when they are promoted. They should remain in `docs/work/` as permanent records of the research phase, linked from the canonical documentation. Only archive Work files if they are factually incorrect or actively confusing.

## Content Type Selection Criteria

### Is This Reference?
- Contains stable, authoritative facts
- Changes infrequently (version-level changes)
- Multiple systems depend on its accuracy
- Represents current system truth

### Is This How-to?
- Provides step-by-step task execution
- Focuses on immediate user goals
- May reference multiple systems/tools
- Changes with process improvements

### Is This Explanation?
- Explains why design decisions were made
- Includes trade-off analysis and rationale
- Connects problems to solutions
- Documents architectural reasoning

### Is This Tutorial?
- Teaches concepts through guided learning
- Includes conceptual overviews and examples
- Focuses on understanding over task completion
- May be ignored during execution tasks (context efficiency)

### Is This Work?
- Contains research, analysis, or experimental content
- Has potential to become canonical reference
- Includes Status field indicating development stage
- May be temporary or evolve into formal documentation

## Domain Organization Rule
Within each Diátaxis bucket, group by **domain** to maintain routing determinism:

- `agentos/` - Core AgentOS functionality
- `docs/` - Documentation system itself
- `dev/` - Development tools and processes

## Decision Documentation Criteria
Only document as decisions when ALL criteria apply:
- Requires active choice between meaningful alternatives
- Involves analysis of trade-offs and consequences
- Could have been implemented differently with different benefits
- Has clear criteria for validating correct implementation
- Represents a policy or architectural choice affecting multiple components

## Writing Guidelines
See `docs/how-to/docs/writing-effective-docs.md` for comprehensive guidance on creating effective documentation that follows these structural principles.