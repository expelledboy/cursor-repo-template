# Agent Instructions

This repository uses a governed documentation system.

## Bootup

At session start, run `just status` as a health check.
If you cannot produce accurate status, investigate before proceeding.
If an objective exists, load `docs/work/objective-graph.yaml` and state your understanding before proceeding.

## Awareness Maintenance

- Before editing any governed doc, report: "Editing X, governed by Y"
- On task transitions, report the new task type
- If context is compacted, re-run `just status` and reload kernel files if awareness is degraded

## Governance

Authority and constraints are defined in `docs/system/`. Use `just docs-index`
to trace the `governed_by` DAG.

## Discovery

- `just docs-index` — Governance DAG
- `just docs-domains` — Domain scopes
- `just docs-skills` — Available skills

## State Management

For multi-step or complex tasks, use `docs/work/objective-graph.yaml` per
`docs/system/model/objective-graph.md`.

## Constraint

This file is implementation-layer alignment and does not govern canonicals.
