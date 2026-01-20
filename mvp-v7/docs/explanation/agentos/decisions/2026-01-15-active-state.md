# Decision: Active-state as resumability substrate

Status: Proposed
Date: 2026-01-15
Scope: mvp-v7
Problem IDs: V7-PRB-0002
Discovery refs: V7-DIS-0001, V7-DIS-0003

## Context
- Context decays across summarization/session boundaries unless stored as an artifact.
- We want jump-back navigation and nested objectives without copying large excerpts.

## Decision
- Use `.agentos/active-state.yaml` as a resumability artifact (summaries + anchors only).
- Frames form a graph; manual insertions/objective shifts default to a new branch frame.

## Consequences
- Pros: resumable reasoning; objective shifts are explicit; history is preserved.
- Cons: requires maintaining a small state file and frame links.

## Artifacts
- `docs/reference/agentos/spec-active-state.md`
- `schemas/active-state.yaml`
- `.agentos/active-state.example.yaml`
- `.cursor/commands/checkpoint.md`
- `.cursor/commands/resume.md`

