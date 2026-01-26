---
doc_status: stable
purpose: Record the decision to enforce doc contracts with automated validation.
intent: decision
decision_status: accepted
decision_date: 2026-01-26
governed_by:
  docs/system/model/decision-doc.md: Load if you need the required fields for decision docs
related:
  docs/system/problem/context-limits-break-correctness.md: Load if you need the motivating problem for this decision
  docs/system/loading-policy.md: Load if you need the procedure that consumes this output
  docs/system/procedure/validating-doc-contracts.md: Load if you need the procedure that enforces this decision
---

# Decision: Enforce Doc Contracts

## Decision Statement
Enforce doc contracts with automated validation.

## Context and Drivers
- Manual validation misses contract drift.
- Authority rules must be enforced consistently.

## Alternatives Considered
- Manual checks only.
- Optional validation on demand.

## Outcome and Implications
- Maintain `scripts/docs/docs_validate.py` as the enforcement tool.
- Use `just docs-validate` during doc changes.

## Related Problems
- Context limits break correctness.
