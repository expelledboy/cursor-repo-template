# Decision: Verification Contract Reference

**Status**: Accepted
**Date**: 2026-01-13
**Scope**: agentos
**Problem IDs**: PRB-0004

## Context
Verification gates decay when they are not explicitly defined and maintained.

## Decision
Define a verification contract reference that anchors gate expectations.
See `docs/reference/agentos/verification-contract.md`.

## Alternatives
- Keep verification guidance only in behavior spec.
- Rely on CI without explicit gates per task.

## Consequences
- Adds a single contract location for gate rules.
- Requires gate updates when CI changes.

## Why this worked
Explicit gate contracts reduce PRB-0004 by preventing silent drift.

## Artifacts
- `docs/reference/agentos/verification-contract.md`
