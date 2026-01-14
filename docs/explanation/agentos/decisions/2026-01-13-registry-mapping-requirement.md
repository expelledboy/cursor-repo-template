# Decision: Registry Mapping Requirement

**Status**: Accepted
**Date**: 2026-01-13
**Scope**: agentos
**Problem IDs**: PRB-0007

## Context
Unmapped files prevent deterministic directive lookup and cause doc drift.

## Decision
Require directive mapping for files that require documentation.
See definitions in `docs/reference/agentos/behavior-spec.md`.

## Alternatives
- Allow best-effort mapping without enforcement.
- Rely on manual documentation without mapping.

## Consequences
- Adds a mapping requirement to the core rules.
- Reduces directive lookup failures.

## Why this worked
Targets PRB-0007 by requiring explicit mapping for documented files.
Evidence: directive mapping enables deterministic linkage between code and docs.

## Artifacts
- `docs/reference/agentos/behavior-spec.md`
