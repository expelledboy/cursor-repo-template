---
doc_status: stable
purpose: Record the decision to separate `intent` from authority.
intent: decision
decision_status: accepted
decision_date: 2026-01-26
governed_by:
  docs/domains/system.md: Load if you need domain constraints for this decision
  docs/system/model/decision-doc.md: Load if you need the required fields for decision docs
related:
  docs/system/problem/context-limits-break-correctness.md: Load if you need the motivating problem for this decision
  docs/system/procedure/creating-problem-docs.md: Load if you need the procedure that applies this decision
---

# Decision: Separate Intent from Authority

## Decision Statement
Separate `intent` from authority and derive precedence from `governs` and `governed_by` only.

## Context and Drivers
- `intent` is needed for routing and loading.
- Authority must be deterministic for conflict resolution.

## Alternatives Considered
- Keep bucket authority by convention.
- Infer authority from directory structure.

## Outcome and Implications
- Authority resolution uses governance links only.
- Intent is used for loading, not conflict resolution.

## Related Problems
- Context limits break correctness.
