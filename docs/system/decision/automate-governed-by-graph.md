---
doc_status: stable
purpose: Record the decision to provide a deterministic governed_by graph renderer.
intent: decision
decision_status: accepted
decision_date: 2026-01-26
governed_by:
  docs/system/model/decision-doc.md: Load if you need the required fields for decision docs
related:
  docs/system/problem/context-limits-break-correctness.md: Load if you need the motivating problem for this decision
  docs/system/loading-policy.md: Load if you need the procedure that consumes this output
  docs/system/model/docs-index-output.md: Load if you need the output contract this decision mandates
---

# Decision: Automate Governed By Graph Rendering

## Decision Statement
Provide a deterministic script that renders the governed_by DAG for context loading.

## Context and Drivers
- Agents need a reliable view of governing relationships.
- Manual inspection does not scale or remain consistent.

## Alternatives Considered
- Manual traversal only.
- Use a global index file maintained by hand.

## Outcome and Implications
- Maintain `scripts/docs/docs_index.py` as the canonical renderer.
- Use `just docs-index` for the governed_by DAG output.

## Related Problems
- Context limits break correctness.
