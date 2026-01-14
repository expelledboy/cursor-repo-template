# Decision: Verification Gates Catalog

**Status**: Accepted
**Date**: 2026-01-14
**Scope**: agentos
**Problem IDs**: PRB-0004; PRB-0010

## Context
Verification gates decay when they are implicit, and task taxonomy drift can bypass gate updates.

## Decision
Create a canonical verification gate catalog that maps every task type to a deterministic gate command.
See `docs/reference/agentos/verification-gates.md`.

## Alternatives
- Keep verification gates implicit in task plans.
- Rely on CI only after changes land.

## Consequences
- Requires updates to the gate catalog when task taxonomy changes.
- Adds a deterministic validator to enforce coverage and command existence.

## Why this worked
Explicit gate mapping makes verification auditable and prevents silent drift.

## Artifacts
- `docs/reference/agentos/verification-gates.md`
- `docs/reference/agentos/verification-contract.md`
- `docs/reference/agentos/behavior-spec.md`
- `docs/reference/agentos/validation-scripts.md`
