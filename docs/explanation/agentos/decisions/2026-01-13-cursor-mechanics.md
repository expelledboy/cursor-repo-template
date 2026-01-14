# Decision: Cursor Mechanics as Adapter Constraints

**Status**: Accepted
**Date**: 2026-01-13
**Scope**: agentos
**Problem IDs**: PRB-0002

## Context
Cursor rule matching and memories are opaque and can shift behavior.

## Decision
Document Cursor mechanics as adapter constraints and keep them out of core contracts.
See `docs/reference/agentos/cursor-mechanics.md` and `docs/explanation/agentos/cursor-adapter-notes.md`.

## Alternatives
- Treat Cursor behavior as core truth.
- Ignore Cursor constraints entirely.

## Consequences
- Adapter is explicit without contaminating the core.
- Routing and loading remain auditable.

## Why this worked
Explicit adapter constraints reduce context instability and PRB-0002 drift.

## Artifacts
- `docs/reference/agentos/cursor-mechanics.md`
- `docs/explanation/agentos/cursor-adapter-notes.md`
- `docs/how-to/agentos/validate-routing.md`
