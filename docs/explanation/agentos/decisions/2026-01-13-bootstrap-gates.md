# Decision: Bootstrap Exit Criteria

**Status**: Accepted
**Date**: 2026-01-13
**Scope**: agentos
**Problem IDs**: PRB-0011

## Context
Portability fails when a repo lacks routing and directives, and the agent guesses.

## Decision
Define explicit exit criteria and a bootstrap runbook.
See `docs/reference/agentos/bootstrap-gates.md` and `docs/how-to/agentos/bootstrap-repo.md`.

## Alternatives
- Rely on ad-hoc bootstrapping without exit gates.
- Exit bootstrap when any docs exist.

## Consequences
- Adds a formal bootstrap lifecycle.
- Requires human ratification before normal operation.

## Why this worked
Explicit exit gates prevent premature assumptions and improve portability.

## Artifacts
- `docs/reference/agentos/bootstrap-gates.md`
- `docs/how-to/agentos/bootstrap-repo.md`
