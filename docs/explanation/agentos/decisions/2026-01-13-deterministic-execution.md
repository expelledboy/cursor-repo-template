# Decision: Deterministic Execution Rule

**Status**: Accepted
**Date**: 2026-01-13
**Scope**: agentos
**Problem IDs**: PRB-0009

## Context
Ad-hoc execution produces non-repeatable outcomes across runs.

## Decision
Require deterministic tools when available and promote repeated ad-hoc commands.
See definitions in `docs/reference/agentos/behavior-spec.md`.

## Alternatives
- Allow ad-hoc commands without promotion.
- Rely on manual recollection of steps.

## Consequences
- Adds process overhead for tool promotion.
- Reduces variance across executions.

## Why this worked
Enforces repeatable execution steps that address PRB-0009.
Evidence: deterministic tools reduce variance compared to ad-hoc commands.

## Artifacts
- `docs/reference/agentos/behavior-spec.md`
