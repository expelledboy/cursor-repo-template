---
title: "Decision: Mandatory Schema Compliance Enforcement"
status: accepted
created_date: 2026-01-18
purpose: "Ensure consistent adherence to system schemas and patterns"
domain: agentos
related:
  - docs/archive/2026-01-18-inconsistent-schema-adherence.md
  - docs/reference/docs/frontmatter-schema.md
implementations:
  - scripts/docs/index.py
---

# Decision: Mandatory Schema Compliance Enforcement

## Decision
We mandate strict adherence to all system schemas and patterns for all documentation operations. This includes frontmatter completeness, implementations fields, @directive annotations, and registry validation.

## Rationale
Inconsistent schema adherence has led to broken traceability, maintenance burden, and trust erosion. By enforcing compliance as a mandatory step in all document operations, we ensure the system remains coherent and maintainable.

## Implications
- **Higher Quality**: All documents follow established patterns
- **Better Traceability**: Registry links work correctly
- **Reduced Maintenance**: Fewer manual fixes needed
- **System Reliability**: Operations follow predictable patterns

## Implementation
- **Core Rule**: Added `Document Schema Compliance` to `.cursor/rules/core.mdc`
- **Validation**: All document operations must pass `just docs::validate` and `just docs::validate-registry`
- **Checklist Enforcement**: Schema requirements must be verified before operation completion