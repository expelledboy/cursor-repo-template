# Decision: Registry Protocol Baseline

**Status**: Accepted
**Date**: 2026-01-13
**Scope**: agentos
**Problem IDs**: PRB-0007

## Context
Registry drift occurs when doc and code links are missing or inconsistent.

## Decision
Define a registry specification with a default bidirectional annotation strategy and deterministic validation rules.
See `docs/reference/agentos/registry.md`.

## Alternatives
- Best-effort mapping without validation.
- A generated map as the default strategy.

## Consequences
- Requires annotation discipline for in-scope files.
- Requires a validation command or a documented gap.

## Why this worked
Explicit mapping and validation make drift detectable and correctable.

## Artifacts
- `docs/reference/agentos/registry.md`
