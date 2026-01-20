---
title: "Decision: Documentation Registry System"
status: accepted
created_date: 2026-01-16
purpose: "Implement bidirectional traceability between documentation and code"
domain: docs
related:
  - docs/reference/docs/frontmatter-schema.md
  - docs/work/problems/2026-01-16-doc-management.md
implementations:
  - scripts/docs/index.py
---

# Decision: Documentation Registry System

## Problem

Addresses [Documentation Context Management](docs/work/problems/2026-01-16-doc-management.md).

Agent chat windows have limited context capacity, requiring careful management of documentation lifecycle. Without proper organization, documentation becomes overwhelming and loses relevance over time.

## Discovery

No separate discovery document referenced. The need for bidirectional traceability emerged from the documentation management problem.

## Decision

Implement registry system with:
- `implementations:` field in YAML frontmatter for structured code references
- `@directive` inline annotations in code files for immediate traceability
- Registry generation and validation commands for automated maintenance

## Trade-offs
- **Gained**: Bidirectional traceability, automated validation, living documentation, discoverable relationships
- **Gained**: Registry generation for complete system visibility
- **Lost**: Additional annotation overhead in code files
- **Lost**: Complexity in maintaining bidirectional links
- **Risk**: Registry maintenance burden if not automated
- **Risk**: Annotation drift if code moves without updating references

## Implementation
- **Frontmatter**: Add `implementations` array field to schema
- **Annotations**: Use `@directive docs/path/to/doc.md` in code files
- **Commands**: `just docs::registry` generates registry, `just docs::validate-registry` validates linkages
- **Validation**: Automated checks for broken links and missing annotations
- **Generation**: Dynamic registry output showing doc-code relationships

## Rationale
Registry system enables living documentation where code and specs maintain traceable relationships. Bidirectional linking prevents documentation drift while enabling automated validation and discovery.

## Validation Criteria
- Registry generation shows complete doc-code relationships
- Validation catches broken linkages before they cause issues
- @directive annotations survive code refactoring
- New implementations automatically registered in docs
- Registry provides actionable navigation between specs and code

## See Also
- [Frontmatter Schema](docs/reference/docs/frontmatter-schema.md) - `implementations` field specification and `@directive` annotation rules
- [Writing Effective Docs](docs/how-to/docs/writing-effective-docs.md) - Usage guidance for registry system
- [Documentation Tools](scripts/docs/index.py) - Registry generation and validation implementation