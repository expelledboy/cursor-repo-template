# Decision: Context Loading Contract

**Status**: Accepted
**Date**: 2026-01-13
**Scope**: agentos
**Problem IDs**: PRB-0002

## Context
Context selection can be unstable and opaque, leading to inconsistent directives.

## Decision
Require explicit declaration and loading of required directives, and treat opaque memories as non-authoritative.
See definitions in `docs/reference/agentos/behavior-spec.md`.

## Alternatives
- Rely on IDE routing rules alone.
- Allow opaque memories as authoritative sources.

## Consequences
- Requires explicit declarations in the task plan.
- Reduces unexpected context variance.

## Why this worked
Makes directive use explicit and auditable, reducing the PRB-0002 failure mode.
Evidence: Cursor memories are opaque; explicit directives reduce reliance on hidden context.

## Artifacts
- `docs/reference/agentos/behavior-spec.md`
