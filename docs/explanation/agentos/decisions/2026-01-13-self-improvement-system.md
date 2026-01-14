# Decision: Self-Improvement System

**Status**: Accepted
**Date**: 2026-01-13
**Scope**: agentos
**Problem IDs**: PRB-0005

## Context
The current loop captures gaps but does not define the improvement events, outputs, and trigger rules needed to prevent rationale loss and drift.

## Decision
Define a self-improvement system with explicit events (micro-AAR, retrospective, postmortem), loop selection rules, and mandatory outputs that promote gaps to validated artifacts.

## Alternatives
- Rely on ad-hoc reflection in chat.
- Capture gaps without required events or action items.

## Consequences
- Adds lightweight overhead after tasks.
- Improves repeatability and preserves rationale over time.

## Why this worked
Codifies the improvement behaviors that already proved effective during iterative refinement and makes them durable.

## Artifacts
- `docs/reference/agentos/self-improvement.md`
- `docs/how-to/agentos/run-self-improvement-cycle.md`
- `docs/reference/agentos/behavior-spec.md`
- `docs/reference/agentos/components.md`
- `docs/reference/agentos/traceability.md`
