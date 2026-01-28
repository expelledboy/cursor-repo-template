---
doc_status: stable
purpose: Define behavioral guidance for objective graph fields.
intent: procedure
governed_by:
  docs/system/model/procedure-doc.md: Load if you need the contract for procedure docs
related:
  docs/system/model/objective-graph.md: Load if you need the objective graph schema
  docs/system/procedure/maintaining-objective-graph.md: Load if you need the maintenance procedure
  docs/system/procedure/objective-graph-realignment.md: Load if you need realignment steps
---

# Objective Graph Behavior Guide

## Purpose
Provide behavioral guidance for interpreting and updating objective graph fields.

## Top-Level Fields
- `objective_graph_version`: bump only when the schema changes.
- `graph_id`: stable for the life of the task.
- `updated_at`: update on every state change.
- `active_objective_id`: must point to a valid objective.
- `active_frame_id`: required only when frames are used.
- `phase`: use when a task has clear phases.
- `mode`: use to indicate trial vs installed behavior.

## Objective Status Transitions
- `proposed` → `active`: when work starts.
- `active` → `blocked`: when progress depends on external input.
- `active` → `done`: when definition of done is met.
- `blocked` → `active`: when the blocker is removed.

## Required vs Optional Context
- `required_context`: must be loaded before any subtask.
- `optional_context`: only load when the listed condition occurs.
- Use `authority` to identify the governing doc or source.

## Entry Checks
- Restate the objective in one sentence.
- Confirm scope is unchanged.
- If scope changes, stop and renegotiate.

## Evaluation Framework
- Prefer existing contract or test procedures.
- If none exist, define a task-specific check with evidence.

## Trace Links
- Use `doc` and `code` for direct doc-code links.
- Use `commit` when a requirement delta is frozen to a specific commit.

## Frames and Anchors
- Use frames to capture resumable context without copying content.
- Use anchors to point to files, rules, or external sources.
- Link frames when context shifts or branches.

## Rehydration
- List required rules and docs needed to resume deterministically.
- If unsure, include the governing doc for the active objective.
