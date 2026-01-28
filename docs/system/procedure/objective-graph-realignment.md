---
doc_status: stable
purpose: Define how to realign after context loss.
intent: procedure
governed_by:
  docs/system/model/procedure-doc.md: Load if you need the contract for procedure docs
related:
  docs/system/model/objective-graph.md: Load if you need the objective graph contract
  docs/system/procedure/maintaining-objective-graph.md: Load if you need the maintenance procedure
  docs/system/decision/introduce-objective-graph.md: Load if you need the decision that mandates realignment
  docs/system/loading-policy.md: Load if you need the loading rules that invoke realignment
  docs/system/examples/objective-graph.example.md: Load if you need a full example of the objective graph
  docs/system/procedure/objective-graph-behavior-guide.md: Load if you need behavioral guidance for fields
  docs/system/procedure/agent-bootup.md: Load if you need the bootup procedure that invokes realignment
---

# Objective Graph Realignment

## Purpose
Realign the current task after compaction, new sessions, or sub-agent starts.

## Inputs
- `docs/work/objective-graph.yaml`.
- Current task context (if available).

## Active Objective Summary
- Active objective id and parent chain.
- Definition of done and evaluation framework.
- Required context list and load conditions.
- Current step and next action.

## Procedure
1) Load `docs/work/objective-graph.yaml`.
2) Identify the active objective and its parent chain.
3) Load all required context links for the active objective.
4) Re-establish the evaluation framework and definition of done.
5) Resume at `current_step` and `next_action`.

## Validation
- Required context for the active objective is loaded.
- `current_step` and `next_action` are aligned with the objective.

## Failure Modes
- Subtasks begin without loading the objective graph.
- Required context is skipped after compaction.
