---
title: "Decision: Dual Documentation Architecture"
status: accepted
created_date: 2026-01-16
purpose: "Implement dual documentation architecture with Diátaxis buckets and development tiers"
domain: docs
related:
  - docs/work/problems/2026-01-16-doc-management.md
  - docs/work/discoveries/2026-01-16-doc-lifecycle.md
---

# Decision: Dual Documentation Architecture

## Decision
Addresses [Documentation Context Management](docs/work/problems/2026-01-16-doc-management.md) using insights from [Dual Documentation Architecture](docs/work/discoveries/2026-01-16-doc-lifecycle.md).
Implement dual documentation architecture: Diátaxis buckets for canonical structure + Development tiers for lifecycle management. Integrate hierarchical loading patterns and progressive documentation scaling.

## Architecture
- **Diátaxis Buckets** (authoritative documentation):
  - `reference/`: Stable facts, APIs, schemas (always loaded core)
  - `how-to/`: Procedures, workflows (task-type specific)
  - `explanation/`: Rationale, decisions (complexity-based)
  - `tutorial/`: Learning guides (on-demand)
  - `work/`: Drafts, research (phase-specific)
  - `archive/`: Superseded content (lazy-loaded)

- **Development Tiers** (content lifecycle):
  - `work/`: Active development and research
  - `local/`: Temporary workspace (gitignored)
  - `archive/`: Historical content

## Trade-offs
- **Gained**: Scalable organization, efficient loading, lifecycle management, context efficiency
- **Gained**: Progressive documentation scaling, hierarchical access patterns
- **Lost**: Additional organizational complexity, tier management overhead
- **Lost**: Initial setup complexity vs simple flat structure
- **Risk**: Tier assignment consistency, loading plan complexity
- **Risk**: Migration overhead from flat to hierarchical structure

## Implementation
- Directory structure follows Diátaxis + domain pattern (`docs/reference/agentos/`)
- Loading tiers integrated with Cursor rules and context compass
- Progressive templates scale documentation by complexity level
- Validation ensures tier assignments and required sections

## Rationale
Dual architecture enables efficient documentation management at scale. Diátaxis provides semantic structure, development tiers manage evolution. Hierarchical loading reduces context pressure while maintaining explicit declaration. Progressive scaling ensures appropriate documentation depth without overhead.

## Validation Criteria
- All documentation fits Diátaxis + domain structure
- Context loading follows tier hierarchy (core → task-type → complexity → phase)
- Documentation scales with complexity levels (1-4)
- Migration paths work: work → reference, local → discard/promote
- Cross-references validate across all tiers

## See Also
- [Documentation Authority](docs/reference/docs/doc-authority.md) - Complete Diátaxis structure and authority rules
- [Documentation System Rationale](docs/explanation/architecture/doc-system-rationale.md) - Architectural design principles
- [Migration Guide](docs/explanation/architecture/migration-guide.md) - Content migration between buckets and tiers