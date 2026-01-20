---
title: "Decision: YAML Frontmatter Schema for Documentation"
status: accepted
created_date: 2026-01-16
purpose: "Standardize metadata format across all documentation for indexing and validation"
domain: docs
related:
  - docs/reference/docs/frontmatter-schema.md
  - docs/work/problems/2026-01-16-doc-management.md
  - docs/work/discoveries/2026-01-16-doc-lifecycle.md
implementations:
  - scripts/docs/index.py
---

# Decision: YAML Frontmatter Schema for Documentation

## Problem

Addresses [Documentation Context Management](docs/work/problems/2026-01-16-doc-management.md).

Agent chat windows have limited context capacity, requiring careful management of documentation lifecycle. Without proper organization, documentation becomes overwhelming and loses relevance over time.

## Discovery

Uses insights from [Dual Documentation Architecture](docs/work/discoveries/2026-01-16-doc-lifecycle.md).

Documentation requires both canonical structure (Diátaxis) and lifecycle management (development tiers). The Diátaxis system provides authoritative documentation buckets while development tiers manage content lifecycle separately from authority.

## Decision

Implement YAML frontmatter with standardized schema across all documentation files.

## Schema Overview
- **Required**: `title`, `status`, `created_date`
- **Optional**: `purpose`, `domain`, `tags`, `related`, `external_docs`
- **Validation**: Automated via `just docs::validate`
- **Indexing**: Powers dynamic `just docs::list-*` commands

## Trade-offs
- **Gained**: Automated indexing, validation, cross-references, domain filtering
- **Lost**: Minimal simplicity (small YAML syntax overhead)
- **Risk**: Schema evolution requires coordinated updates vs flexible approaches

## Implementation
- Schema defined in `docs/reference/docs/frontmatter-schema.md`
- Validation implemented in `scripts/docs/index.py`
- All existing documents migrated to new format
- Just commands provide dynamic querying: `just docs::list-decisions --domain agentos`

## Rationale
YAML frontmatter enables sophisticated documentation management while maintaining human editability. The schema is minimal but comprehensive enough for identified use cases. Structured metadata supports the dual documentation architecture (Diátaxis buckets + development tiers) without compromising authoring experience.

## Validation Criteria
- All documents pass `just docs::validate` without errors
- Index commands work correctly: `just docs::list-decisions`, `just docs::list-problems`
- Cross-references are valid and functional
- Domain filtering works: `--domain agentos`, `--domain docs`
- Advanced filtering supported: `--tag`, `--since`, `--status`

## See Also
- [Frontmatter Schema Reference](docs/reference/docs/frontmatter-schema.md) - Complete specification and validation rules
- [Documentation Tools](scripts/docs/index.py) - Implementation of validation and indexing
- [Writing Effective Docs](docs/how-to/docs/writing-effective-docs.md) - Usage guidance for frontmatter