---
doc_status: stable
purpose: Record the decision to organize docs by domain first.
intent: decision
decision_status: accepted
decision_date: 2026-01-26
governed_by:
  docs/domains/system.md: Load if you need domain constraints for this decision
  docs/system/model/decision-doc.md: Load if you need the required fields for decision docs
related:
  docs/system/problem/context-limits-break-correctness.md: Load if you need the motivating problem for this decision
---

# Decision: Domain First Organization

## Decision Statement
Organize canonical docs by domain and use `docs/domains/<domain>.md` as the authority anchor.

## Context and Drivers
- Domain scoped docs are easier to load precisely.
- Cross domain authority needs explicit links.

## Alternatives Considered
- Keep buckets as the primary structure.
- Use a global index file.

## Outcome and Implications
- Canonical docs live under `docs/<domain>/` and `docs/system/`.
- Domain docs govern their domain canonicals.

## Related Problems
- Context limits break correctness.
