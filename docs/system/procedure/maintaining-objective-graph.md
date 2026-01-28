---
doc_status: stable
purpose: Define how to create and update the objective graph.
intent: procedure
governed_by:
  docs/system/model/procedure-doc.md: Load if you need the contract for procedure docs
related:
  docs/system/model/objective-graph.md: Load if you need the objective graph contract
  docs/system/decision/introduce-objective-graph.md: Load if you need the decision that mandates objective graphs
  docs/system/procedure/objective-graph-realignment.md: Load if you need the realignment procedure
  docs/system/procedure/objective-graph-behavior-guide.md: Load if you need behavioral guidance for fields
---

# Maintaining Objective Graphs

## Purpose
Create and update objective graphs to keep tasks aligned.

## Inputs
- Current task objective.
- Known sub-objectives and dependencies.
- Required and optional context sources.

## Procedure
1) Create or update `docs/work/objective-graph.yaml`.
2) Add or update objective nodes with required fields.
3) Link parent and child objectives explicitly.
4) Define `entry_check`, `definition_of_done`, and `evaluation_framework` for each objective.
5) Populate context links using the schema in the objective graph contract.
6) Set `current_step` and `next_action` for the active objective.
7) Save the graph after each significant subtask.
8) Do not treat the YAML as canonical documentation.

## Validation
- All objective nodes include required fields.
- Entry checks include expected outcomes and objective restatement.
- Evaluation frameworks include evidence and pass criteria.
- Required context links include authority and load conditions.
- Active objective includes `current_step` and `next_action`.

## Failure Modes
- Objective graph omitted from a long-running task.
- Required context links missing load conditions.
- Entry checks not executed before subtasks.
