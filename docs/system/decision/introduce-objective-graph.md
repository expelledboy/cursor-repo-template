---
doc_status: stable
purpose: Record the decision to use an objective graph with realignment.
intent: decision
decision_status: accepted
decision_date: 2026-01-28
governed_by:
  docs/system/model/decision-doc.md: Load if you need the required fields for decision docs
related:
  docs/system/problem/context-loss-breaks-alignment.md: Load if you need the motivating problem for this decision
  docs/system/model/objective-graph.md: Load if you need the objective graph contract
  docs/system/procedure/maintaining-objective-graph.md: Load if you need steps to maintain the objective graph
  docs/system/procedure/objective-graph-realignment.md: Load if you need the realignment procedure
  docs/system/procedure/defining-evaluation-frameworks.md: Load if you need evaluation framework guidance
  docs/system/examples/objective-graph.example.md: Load if you need a full example of the objective graph
---

# Decision: Introduce Objective Graph

## Decision Statement
Use an objective graph as the authoritative task hierarchy and require realignment after context loss.

## Context and Drivers
- Agents forget objectives during long or nested tasks.
- Compaction and new sessions create inconsistent outcomes.

## Alternatives Considered
- Rely on ad-hoc task notes.
- Keep only a simple todo list.

## Outcome and Implications
- Objective graph lives in `docs/work/` and is not committed.
- Subtasks must re-load the objective graph and run entry checks.
- Realignment is required after compaction, new sessions, or sub-agent starts.

## Non-Negotiables
- Entry checks must include objective restatement and scope confirmation.
- Subtasks must not proceed without objective graph re-load.

## Related Problems
- Context loss breaks alignment.
