# Decision: Context contract for graphs

Status: Proposed
Date: 2026-01-15
Scope: mvp-v7
Problem IDs: V7-PRB-0003
Discovery refs: V7-DIS-0001

## Context
- Graph conditions can silently depend on undefined `context` fields.
- Missing/implicit context causes inconsistent branching and brittle graphs.

## Decision
- Add optional `context_contract` to the decision-graph schema.
- Graphs should declare required/optional `context` fields (dot-paths) used by conditions.

## Consequences
- Pros: makes graphs safer, more reviewable, and easier to reuse across repos.
- Cons: small authoring overhead to declare fields.

## Artifacts
- `schemas/decision-graph.yaml`
- `docs/reference/agentos/spec-decision-graph.md`

