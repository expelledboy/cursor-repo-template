# Decision: Safety Policy Contract

**Status**: Accepted
**Date**: 2026-01-13
**Scope**: agentos
**Problem IDs**: PRB-0008

## Context
Destructive or unsafe actions reduce trust and can cause irreversible damage.

## Decision
Define a safety policy as a core reference contract.
See `docs/reference/agentos/safety-policy.md`.

## Alternatives
- Rely on ad-hoc safety warnings.
- Limit safety to destructive confirmation only.

## Consequences
- Adds explicit safety constraints to the core.
- Requires manual fallbacks and secret handling rules.

## Why this worked
Explicit constraints prevent unsafe autonomy and reduce PRB-0008 risk.

## Artifacts
- `docs/reference/agentos/safety-policy.md`
