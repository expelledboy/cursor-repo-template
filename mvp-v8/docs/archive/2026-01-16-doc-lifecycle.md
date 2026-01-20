---
title: "Dual Documentation Architecture"
created_date: 2026-01-16
purpose: "Documentation requires both canonical structure and lifecycle management"
domain: docs
type: discovery
status: superseded
superseded_by: docs/explanation/decisions/2026-01-16-doc-structure.md
superseded_date: 2026-01-18
superseded_reason: Discovery incorporated into architecture decision
---

## Observation
Documentation requires both canonical structure (Diátaxis) and lifecycle management (development tiers).

## Key Insights
- **Diátaxis System**: reference/how-to/explanation/tutorial/work/archive provides authoritative documentation buckets
- **Development Tiers**: work/local/archive manages content lifecycle separate from authority
- **Archive Dual Role**: Serves both systems - Diátaxis for superseded canonical, development for historical working content
- **Migration Paths**: Content flows between systems as it matures

## Technical Grounding
- **Diátaxis Framework**: Content organization by user intent (Reference/How-to/Explanation/Tutorial)
- **Authority Order**: reference → how-to → explanation → tutorials → work → archive (defined in [Doc Authority](docs/reference/docs/doc-authority.md))
- **Directory Structure**: `docs/reference/`, `docs/how-to/`, `docs/explanation/`, `docs/work/`, `docs/archive/`
- **Domain Organization**: Within each Diátaxis bucket, content grouped by domain (e.g., `agentos/`, `docs/`)
- **Loading Strategy**: Hierarchical loading reduces token usage by 30-50% through tiered directive organization
- **Frontmatter Schema**: YAML frontmatter tracks status, domain, and lifecycle metadata (see [Frontmatter Schema](docs/reference/docs/frontmatter-schema.md))
- **Validation**: Automated validation ensures proper Diátaxis classification and required sections

## Implications
- Clear separation between authoritative docs and working content
- Appropriate lifecycle management for each content type
- Efficient context window usage through selective access
- Sustainable documentation evolution

## Used In
- [Dual Documentation Architecture](docs/explanation/decisions/2026-01-16-doc-structure.md)
