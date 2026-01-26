---
doc_status: stable
purpose: Record the decision to introduce a domain index.
intent: decision
decision_status: accepted
decision_date: 2026-01-26
governed_by:
  docs/system/model/decision-doc.md: Load if you need the required fields for decision docs
related:
  docs/system/model/domain-doc.md: Load if you need the domain doc contract
  docs/system/model/docs-domains-output.md: Load if you need the domain index output contract
  docs/system/problem/context-limits-break-correctness.md: Load if you need the motivating problem for this decision
  docs/system/procedure/creating-domain-docs.md: Load if you need the procedure that implements this decision
---

# Decision: Introduce Domain Index

## Decision Statement
Introduce a domain index based on `docs/domains/*.md`.

## Context and Drivers
- Domain scope needs to be discoverable without implying authority.
- A dedicated index avoids overloading governance links.

## Alternatives Considered
- Use domain docs as governors.
- Use a hand-maintained global list.

## Outcome and Implications
- Add `just docs-domains` as the domain index generator.
- Require domain docs to include indexable metadata.

## Related Problems
- Context limits break correctness.
