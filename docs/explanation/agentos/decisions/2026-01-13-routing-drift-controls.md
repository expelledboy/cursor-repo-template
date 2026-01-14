# Decision: Routing Drift Controls

**Status**: Accepted
**Date**: 2026-01-13
**Scope**: agentos
**Problem IDs**: PRB-0006

## Context
Routing selection can drift or misfire, causing wrong-domain directives to load.

## Decision
Require explicit routing checks for domain alignment before execution.
See definitions in `docs/reference/agentos/behavior-spec.md`.

## Alternatives
- Rely on routing selection without checks.
- Allow cross-domain directives by default.

## Consequences
- Adds a routing validation step to the task plan.
- Reduces wrong-domain directive loading.

## Why this worked
Adds a deterministic check against PRB-0006 before execution.
Evidence: explicit routing checks reduce misrouting when context selection is unstable.

## Artifacts
- `docs/reference/agentos/behavior-spec.md`
