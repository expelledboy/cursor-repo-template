---
status: stable
purpose: Define global rules for doc structure and precedence.
governed_by:
  docs/reference/docs/core-values.md: System core values
governs:
  docs/reference/docs/doc-relationships.md: Relationship semantics
  docs/reference/docs/docs-index.md: Docs index contract
  docs/reference/docs/rules-system.md: Rules system reference
  docs/domains/dev.md: Dev domain governance
  docs/domains/docs.md: Docs domain governance
  docs/how-to/docs/content-aware-restructuring.md: Restructuring procedure
  docs/explanation/docs/system-rationale.md: System rationale
  docs/tutorials/getting-started.md: System onboarding
---

# System Governance

## Governance Scope
This document defines the global rules for how the documentation system is structured,
linked, and maintained.

## Precedence Mechanics
- Precedence is inferred from the `governs` and `governed_by` graph.
- A document that `governs` another is higher precedence.
- If two documents conflict, follow the `governed_by` chain upward.

## Default Escalation Rule
If a conflict appears at a lower level (procedure, rationale, tutorial),
escalate to the nearest governing document and resolve the mismatch there.

## Conflict Resolution Protocol
1) Identify the conflict.
2) Trace the `governed_by` chain.
3) Fix at the lowest governing document that can resolve it.
4) Propagate changes downward to governed docs.

## Domain Requirements
- Every domain must have `docs/domains/{domain}.md`.
- Domain docs govern all canonical docs in that domain.

## Doc Bucket Rules
- `reference`: stable facts and constraints
- `how-to`: procedures that implement `reference`
- `explanation`: rationale, tradeoffs, architecture
- `tutorials`: learning only, lowest authority
- `work` and `archive`: optional and non-authoritative

## Update Protocol
- Change facts in reference first.
- Then update how-to and explanation.
- Tutorials update last.

## `AGENTS.md` Role
`AGENTS.md` is implementation-layer alignment. It does not govern canonicals.
