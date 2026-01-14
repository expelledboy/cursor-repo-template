# Decision: Routing Spec and Context Compass

**Status**: Accepted
**Date**: 2026-01-13
**Scope**: agentos
**Problem IDs**: PRB-0002; PRB-0006

## Context
Context instability and misrouting cause inconsistent directives and wrong-domain behavior.

## Decision
Define routing as a core reference contract and enforce a context compass for doc types.
See `docs/reference/agentos/routing.md` and `docs/reference/agentos/context-compass.md`.

## Alternatives
- Implicit routing with no recorded decisions.
- Allow any doc type regardless of task intent.

## Consequences
- Adds explicit routing and doc type constraints.
- Reduces misrouting and context overload.

## Why this worked
Explicit routing and doc type constraints make context selection auditable and stable.

## Artifacts
- `docs/reference/agentos/routing.md`
- `docs/reference/agentos/context-compass.md`
