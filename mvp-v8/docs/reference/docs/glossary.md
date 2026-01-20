---
title: "Documentation System Glossary"
status: stable
created_date: 2026-01-17
purpose: "Core concepts and terminology for the documentation system"
domain: docs
---

# Documentation System Glossary

This glossary defines key concepts and terminology used throughout the documentation system. All technical terms are linked to their definitions for consistent understanding.

## Core Framework

### Diátaxis
A content organization framework that structures documentation by user intent:
- **Reference**: Stable facts and specifications ("What is X?")
- **How-to**: Step-by-step procedures ("How do I do X?")
- **Explanation**: Design rationale and architecture ("Why is X this way?")
- **Tutorial**: Learning-oriented guides ("How do I learn X?")
- **Work**: Drafts and research becoming canonical
- **Archive**: Superseded material with historical record

### Authority Order
Conflict resolution hierarchy for documentation: **reference → how-to → explanation → tutorials → work → archive**. When docs conflict, defer to higher authority sources to ensure stable facts override temporary guidance.

### Domain Organization
Content grouping by functional area within Diátaxis buckets (e.g., `agentos/`, `docs/`, `dev/`). Enables deterministic routing and context-aware loading.

## Restructuring Concepts

### 6-Phase Restructuring
Systematic documentation improvement process:
1. **Inventory**: Assess current documentation landscape
2. **Batching**: Group related content respecting cognitive limits
3. **Analysis**: Evaluate consolidation opportunities
4. **Decision**: Select restructuring strategies
5. **Execution**: Apply approved changes
6. **Validation**: Quality assurance and cleanup

### Consolidation Criteria
Standards for merging documentation files:
- **Content Overlap**: >70% shared content between files
- **Purpose Alignment**: Files serve the same user intent
- **Authority Clarity**: One file is clearly more authoritative/complete
- **Maintenance Burden**: Consolidation reduces future upkeep overhead

### Cognitive Limits
Human processing constraints in documentation work:
- **Working Memory**: 7±2 items for simultaneous consideration
- **Context Windows**: ~20-30 files for coherent analysis
- **Attention Span**: Focused phases prevent cognitive overload
- **Batch Boundaries**: Respect limits for effective restructuring

## Distillation & Compression

### Distillation
The semantic compression of documentation by separating "Scaffolding" from "Structure." The goal is to retain 100% of the functional directives while reducing token count by 50-80%.

### Scaffolding (Documentation)
Content required to *create* the knowledge but not to *use* it. Includes historical debates, failed attempts, temporal context ("yesterday"), and author narrative ("I think").

### Structure (Documentation)
The load-bearing knowledge required for execution. Includes final decisions, invariants, configuration schemas, and strict directives.

### Compression Strategies
Methods for distilling specific content types:
- **Extractor**: For research (Work → Reference). Removes rejected alternatives.
- **Operator**: For drafts (Local → How-to). Removes narrative, extracts steps.
- **Cryogenics**: For theory (Explanation → Reference). Extracts invariants from obsolescence.
- **Partitioning**: Separation of content into Fact (Reference), Procedure (How-to), and Rationale (Explanation).

## Metacognitive Loop

### Metacognitive Loop
The continuous cycle of Observation (`/learn`) → Adaptation (`/evolve`) that allows the system to debug and improve its own instructions.

### Discovery
A validated observation of a successful pattern or insight that warrants integration into the system.

### System Evolution
The process of modifying the system's "Behavioral Core" (Rules and Commands) to incorporate a validated lesson or discovery.

## Decision & State Management

### Decision Tree
Active reasoning state representation showing:
- Current decision paths and nodes
- Reasoning context across processing contexts
- Active decision graph for transparency
- Complete state for understanding agent actions

### PR-Style Review
Structured change proposal format for documentation restructuring:
- **Change Summary**: Files affected and consolidation strategy
- **Authority Analysis**: Diátaxis compliance and authority order application
- **Quality Impact**: Link integrity and maintenance implications
- **Rollback Plan**: Recovery options for failed changes

### Active State
Resumable conversation context with:
- **Frames**: Context snapshots with titles and summaries
- **Focus**: Current working frame
- **Links**: Navigation between conversation states
- **Persistence**: Automatic state saving across sessions

## Technical Infrastructure

### File Patterns
Glob expressions for rule triggering and content matching:
- `docs/**/*.md`: All documentation files
- `docs/reference/**/*.md`: Reference documentation only
- `docs/explanation/**/*.md`: Explanation content

### Evidence Anchoring
Provenance tracking for decision validation:
- **Command Anchors**: Tool execution records with timestamps and hashes
- **Mention Anchors**: Explicit context injections with file references
- **Search Anchors**: Query results with confidence scores
- **Rule Anchors**: Configuration-driven content injections

### Cursor Mechanics Constraints
Evidence-based decision tracking principles:
- **Provenance Tracking**: Record source and context for all decisions
- **Evidence Anchoring**: Link decisions to supporting information
- **Decision Transparency**: Make reasoning processes visible
- **State Consistency**: Maintain resumable workflow contexts

## Quality Standards

### Link Resolution
All cross-references and internal links must resolve to valid targets. Broken links indicate documentation integrity issues requiring immediate correction.

### Content Integrity
Documentation must maintain required sections, follow Diátaxis principles, and preserve relationship accuracy during restructuring operations.

### Functional Completeness
All restructuring goals achieved with no information loss, clear navigation paths, and improved long-term maintainability.

## Workflow States

### Resumability
Ability to interrupt and resume complex operations:
- **State Persistence**: Progress saved across sessions
- **Incremental Progress**: Partial work preserved
- **Quality Tracking**: Validation prevents incomplete operations
- **Rollback Capability**: Failed attempts safely reversible

### Batch Processing
Strategic content grouping for efficient analysis:
- **Relationship Grouping**: Dependent files processed together
- **Size Optimization**: Respect cognitive processing limits
- **Context Coherence**: Maintain analytical focus within batches
- **Progress Tracking**: Monitor advancement through phases