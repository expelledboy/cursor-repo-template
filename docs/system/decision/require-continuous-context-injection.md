---
doc_status: stable
purpose: Require that governance constraints survive context loss via continuous injection.
intent: decision
decision_status: accepted
decision_date: 2026-01-28
governed_by:
  docs/system/model/decision-doc.md: Load for structural requirements and validation rules
implemented_by:
  .cursor/rules/governance-enforcement.mdc: Load for Cursor-specific injection of governance
  .cursor/rules/objective-state.mdc: Load for Cursor-specific injection of state
  .cursor/rules/cursor-mechanics.mdc: Load for Cursor-specific injection of mechanics
related:
  docs/system/problem/context-loss-breaks-governance-executability.md: The problem this decision resolves
---

# Decision: Require Continuous Context Injection

## Decision Statement
Any critical governance behavior must be continuously re-injected by the runtime environment. We will use runtime-specific mechanisms (like `.cursor/rules`) to actively force awareness of the Governance DAG and Objective Graph.

## Context and Drivers
- **Physics of Context:** Agents inevitably lose context. Relying on initial instructions or user discipline is a point of failure.
- **Executability:** A rule that isn't present in the context window is effectively repealed.
- **SSOT Principle:** Injection layers must be pointers only. They cannot redefine the rules, only point to the canonical docs.

## Alternatives Considered
- **Honor System:** Rely on users/agents to manually check rules. Rejected due to high failure rate under pressure.
- **Hard CI Gates:** Essential for final validation, but too slow for interactive guidance.
- **System Prompt Stuffing:** Loading all rules constantly is token-prohibitive and degrades reasoning.

## Outcome and Implications
- We will implement "active rules" in `.cursor/rules/` as the enforcement layer.
- These rules will be strictly "pointer layers" to avoid SSOT violations.
- Governance docs remain the single source of truth; rules are the delivery mechanism.

## Related Problems
- Context loss breaks governance executability.
