---
title: "Decision: YAML State Representation"
status: accepted
created_date: 2026-01-16
purpose: "Use YAML for state representation to maintain reasoning consistency"
domain: agentos
related:
  - docs/work/problems/2026-01-16-context-drift.md
  - docs/work/discoveries/2026-01-16-yaml-efficiency.md
implementations:
  - schemas/active-state.yaml
  - validate.py
  - scripts/docs/index.py
---

# Decision: YAML State Representation

## Decision
Use YAML for state representation to maintain reasoning consistency across multi-step tasks. State files will use `.yaml` extension and follow structured schemas defined in `schemas/`.

## Trade-offs
- **Gained**: Structured consistency, character efficiency, auditability, evolution safety
- **Gained**: Human-readable format for debugging and manual inspection
- **Gained**: Schema validation prevents silent corruption
- **Lost**: Slightly more complex than plain text or JSON for simple cases
- **Lost**: YAML parsing overhead vs raw performance
- **Risk**: Schema evolution requires coordinated updates across components
- **Risk**: Learning curve for team members unfamiliar with YAML syntax

## Implementation
- State files use `.yaml` extension with schemas in `schemas/` directory
- Validation via `python3 validate.py <schema> <file>` before loading
- Loading via `yaml.safe_load()` with error handling
- Character limit monitoring to prevent context window overflow
- State persistence in `docs/local/` for active tasks, promoted to authoritative docs when stable

## Rationale
YAML bridges the gap between human auditability and machine processing, enabling durable reasoning artifacts that survive system evolution. Unlike opaque memory systems or unstructured text, YAML provides explicit contracts that prevent rationale loss while maintaining the flexibility needed for complex reasoning tasks.

## Validation Criteria
- State files load within 500ms without errors
- Multi-step reasoning maintains 95%+ consistency across 10+ steps
- Context window usage reduced by 30% vs unstructured approaches
- State validation catches 100% of schema violations
- Manual inspection possible for all active state files

## See Also
- [Active State Specification](docs/reference/agentos/spec-active-state.md) - Implementation specification for YAML state representation
- [YAML Character Efficiency](docs/work/discoveries/2026-01-16-yaml-efficiency.md) - Technical grounding for YAML choice