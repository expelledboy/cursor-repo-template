# Decision: Improvement Template Requirements

**Status**: Accepted
**Date**: 2026-01-14
**Scope**: agentos
**Problem IDs**: PRB-0005

## Context
Self-improvement notes are required outputs, but the template did not capture evidence or affected artifacts.

## Decision
Require improvement notes to include Evidence and Affected artifacts fields.
See `docs/reference/agentos/self-improvement.md` and `docs/how-to/agentos/run-self-improvement-cycle.md`.

## Alternatives
- Keep the template minimal without evidence or artifact fields.
- Capture evidence only in ADRs.

## Consequences
- Adds minor overhead to improvement notes.
- Makes improvement outputs auditable and traceable.

## Why this worked
Explicit evidence and artifact fields strengthen the improvement loop and reduce rationale loss.

## Artifacts
- `docs/reference/agentos/self-improvement.md`
- `docs/how-to/agentos/run-self-improvement-cycle.md`
