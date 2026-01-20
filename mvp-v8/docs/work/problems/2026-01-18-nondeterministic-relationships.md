---
title: "Non-Deterministic Frontmatter Relationships"
status: active
created_date: 2026-01-18
domain: agentos
type: problem
evidence_for:
  - docs/explanation/decisions/2026-01-18-deterministic-relationships.md
informs:
  - docs/reference/docs/frontmatter-schema.md
---

# Non-Deterministic Frontmatter Relationships

## Context
Identified during analysis of documentation architecture and relationship visualization needs. The current frontmatter schema uses vague `related:` fields that don't specify relationship types, making traceability and visualization non-deterministic.

## Observation
Frontmatter relationships are currently specified as simple lists without directional or semantic meaning:

```yaml
related:
  - docs/some/other/doc.md  # Why related? What type of relationship?
```

This creates ambiguity and prevents deterministic analysis of documentation relationships.

## Impact Assessment
- **Severity**: High - Prevents proper documentation traceability and visualization
- **Scope**: Systemic - Affects all documentation relationship management
- **Cost**: Manual relationship interpretation, poor automation capabilities, maintenance overhead

## Evidence
- **Schema analysis**: Current `related:` field lacks semantic meaning
- **Visualization requirements**: Directional relationships needed for proper graph generation
- **Traceability gaps**: Cannot determine if relationships are dependencies, evidence, or implementations
- **Automation blockers**: Non-deterministic relationships prevent reliable tooling

## Root Cause Analysis
Frontmatter schema was designed for human readability but not machine processability. The simple list format prioritizes ease of authoring over semantic precision and automated analysis.

## Potential Solutions
1. **Directional relationship schema**: Implement typed relationships (`informs`, `depends_on`, etc.)
2. **Schema migration**: Gradually transition existing documents to new format
3. **Validation enhancement**: Add relationship type checking and bidirectional consistency
4. **Visualization tooling**: Build relationship graph generators using new schema

## Related Issues
- Documentation architecture needs holistic review
- Context loading orchestration requires relationship understanding
- Frontmatter schema evolution needed for better determinism