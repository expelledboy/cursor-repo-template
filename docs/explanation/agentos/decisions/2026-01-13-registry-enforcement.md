# Decision: Registry Enforcement Baseline

**Status**: Accepted
**Date**: 2026-01-13
**Scope**: agentos
**Problem IDs**: PRB-0007

## Context
Registry drift persists if validation is optional or undefined.

## Decision
Require a deterministic registry validation command and treat its absence as a documented gap.
See `docs/reference/agentos/registry.md`.

## Alternatives
- Best-effort mapping without validation.
- Manual checklist only.

## Consequences
- Adds a required validation expectation for mapped files.
- Requires a work note when enforcement is missing.

## Why this worked
Deterministic validation makes registry drift detectable and correctable.

## Artifacts
- `docs/reference/agentos/registry.md`
