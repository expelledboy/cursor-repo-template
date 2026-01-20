# Decision: Decision traces (graph path + anchors)

Status: Proposed
Date: 2026-01-15
Scope: mvp-v7
Problem IDs: V7-PRB-0001
Discovery refs: V7-DIS-0001, V7-DIS-0002

## Context
- “Why” is lost when chat closes.
- SIG_* labels are too vague to review; we need concrete anchors.

## Decision
- Record decisions as structured traces: evaluated graphs + path + anchors.
- Auto-display trace when asking the user a question; otherwise show on `/trace`.

## Consequences
- Pros: reviewable, diffable reasoning; easier to propose deterministic improvements.
- Cons: small overhead to keep traces/anchors consistent.

## Artifacts
- `docs/reference/agentos/spec-decision-trace.md`
- `schemas/decision-trace.yaml`
- `.cursor/commands/trace.md`

