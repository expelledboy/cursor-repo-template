---
doc_status: stable
purpose: Define the YAML schema for the objective graph state file.
intent: contract
governed_by:
  docs/system/governance.md: Load if you need global rules that govern objective graphs
governs:
  docs/system/examples/objective-graph.example.md: Load to verify the example follows this schema
related:
  docs/system/decision/introduce-objective-graph.md: Load if you need the decision that mandates objective graphs
  docs/system/procedure/maintaining-objective-graph.md: Load if you need steps to maintain objective graphs
  docs/system/procedure/objective-graph-realignment.md: Load if you need the realignment procedure
  docs/system/procedure/promoting-operational-findings.md: Load if you need the promotion procedure
  docs/system/procedure/defining-evaluation-frameworks.md: Load if you need evaluation framework guidance
  docs/system/examples/objective-graph.example.md: Load if you need a full example of the schema
  docs/system/procedure/objective-graph-behavior-guide.md: Load if you need behavioral guidance for fields
---

# Objective Graph Model

## Purpose
Define the YAML schema for `docs/work/objective-graph.yaml`.

## Definition
The objective graph is an operational state file that records objective hierarchy,
context pointers, and evaluation criteria. It is not an authoritative doc.

## File Location
- `docs/work/objective-graph.yaml`

## Top-Level Schema (required unless noted)
- `objective_graph_version: <string>`
- `graph_id: <string>`
- `updated_at: <ISO-8601 string>`
- `active_objective_id: <objective_id>`
- `active_frame_id: <frame_id>` (optional)
- `phase: <string>` (optional)
- `mode: <string>` (optional)
- `objectives: [<objective_node>...]`
- `frames: [<frame_node>...]` (optional)
- `rehydration: <rehydration_block>` (optional)

## Objective Node Schema
- `objective_id: <string>`
- `status: proposed|active|blocked|done`
- `parent_ids: [<objective_id>...]`
- `child_ids: [<objective_id>...]`
- `definition_of_done: <string>`
- `evaluation_framework: <evaluation_framework>`
- `entry_check: <entry_check>`
- `required_context: [<context_link>...]`
- `optional_context: [<context_link>...]`
- `current_step: <string>`
- `next_action: <string>`
- `trace_links: [<trace_link>...]`
- `operational_findings: [<string>...]`

## Context Link Schema
- `type: doc|code|mcp|external`
- `uri: <path or URL>`
- `load_condition: <task|phase|trigger>`
- `authority: <doc path or source>`
- `priority: required|conditional|optional`
- `refresh_policy: <string>` (optional)

## Entry Check Schema
- `check_type: checklist|command|manual`
- `check_steps: [<string>...]`
- `expected_outcome: <string>`
- `objective_restatement: <string>`
- `scope_confirmation: <string>`

## Evaluation Framework Schema
- `method: test|contract|manual`
- `evidence: <string>`
- `pass_criteria: <string>`
- `failure_action: <string>`

## Trace Link Schema
- `doc: <path>` (optional)
- `code: <path>` (optional)
- `commit: <sha>` (optional)

## Frame Node Schema (optional)
- `frame_id: <string>`
- `title: <string>`
- `summary: <string>`
- `anchors: [<context_link>...]`
- `links: [<frame_link>...]`

## Frame Link Schema (optional)
- `to: <frame_id>`
- `kind: branch|resume|shift_context|supersede|depends_on`
- `note: <string>` (optional)

## Rehydration Block (optional)
- `required_rules: [<rule_id>...]`
- `required_docs: [<doc_path>...]`

## Behavioral Rules
- Every subtask must re-load the objective graph and run the objective's `entry_check`.
- Entry checks must include objective restatement and scope confirmation.
- Required context must include `load_condition` and `authority`.
- Operational findings must be processed (promoted or discarded) before marking the Root Objective as done.

## Scope Rules
- Objective graphs live under `docs/work/` and are not committed.
- Objective graphs are operational state and not authoritative docs.
- Objective graphs are excluded from canonical validation.
