---
doc_status: stable
purpose: Define the problem of context limits breaking correctness.
intent: problem
governed_by:
  docs/domains/system.md: Load if you need domain constraints for this problem
  docs/system/model/problem-doc.md: Load if you need the required fields for problem docs
related:
  docs/system/decision/separate-intent-from-authority.md: Load if you need the decision that resolves this problem
  docs/system/decision/domain-first-organization.md: Load if you need the decision that resolves this problem
  docs/system/decision/automate-governed-by-graph.md: Load if you need the decision that provides graph visibility
  docs/system/decision/enforce-doc-contracts.md: Load if you need the decision that enforces doc contracts
  docs/system/procedure/creating-decision-docs.md: Load if you need the procedure that turns this problem into a decision
---

# Problem: Context Limits Break Correctness

## Problem Statement
Context limits cause missing constraints and inconsistent behavior.

## Scope and Boundaries
- Applies to agent workflows that load docs.
- Excludes cases where all governing docs are already loaded.

## Consequences
- Actions can violate constraints.
- Decisions can be made on partial information.

## Related Decisions
- Separate `intent` from authority.
- Use domain first organization.
