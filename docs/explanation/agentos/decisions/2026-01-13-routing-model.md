# Decision: Routing Model

**Status**: Accepted
**Date**: 2026-01-13
**Scope**: agentos
**Problem IDs**: PRB-0002

## Context
Context instability causes inconsistent directives without explicit routing decisions.

## Decision
Require routing to select required directives and allowed domains, recorded in the task plan header.
See definitions in `docs/reference/agentos/behavior-spec.md`.

## Alternatives
- Implicit routing without recording selections.
- Rely on adapter behavior alone.

## Consequences
- Adds explicit routing declarations to every task.
- Reduces hidden context variance.

## Why this worked
Makes routing decisions explicit and auditable, addressing PRB-0002.
Evidence: explicit routing reduces hidden context variance when adapters or rules differ.

## Artifacts
- `docs/reference/agentos/behavior-spec.md`
