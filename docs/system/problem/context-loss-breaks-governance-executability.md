---
doc_status: stable
purpose: Define why governance and operational state fail under agent context limits.
intent: problem
governed_by:
  docs/system/model/problem-doc.md: Load for structural requirements and validation rules
related:
  docs/system/decision/require-continuous-context-injection.md: Decision that addresses this problem
  docs/system/problem/context-loss-breaks-alignment.md: Related problem focused on objective drift
  docs/system/problem/injection-doesnt-guarantee-internalization.md: Related problem extending injection verification
  docs/system/problem/awareness-degrades-without-recovery.md: Related problem extending awareness maintenance
  docs/system/decision/require-bootup-and-awareness-maintenance.md: Decision extending injection with bootup/maintenance
---

# Problem: Context Loss Breaks Governance Executability

## Problem Statement
Governance structures (DAGs) and operational state (Objective Graphs) rely on the agent's awareness of them. However, agents operate under finite context windows. As tasks progress, compaction removes these critical constraints from active memory, making them "non-executable" at the moment of decision.

## Scope and Boundaries
- Applies to all agent runtimes (Cursor, Codex, etc.) with finite context.
- Covers both static authority (DAG) and dynamic state (Objective Graph).
- Distinct from "user discipline" issues; this is a system physics failure.

## Consequences
- Governance becomes purely advisory/theoretical.
- Operational state drifts as agents "forget" to check the graph.
- Compliance relies on chance rather than system guarantees.

## Related Decisions
- Require continuous context injection.
