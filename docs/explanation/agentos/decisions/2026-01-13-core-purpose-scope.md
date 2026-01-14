# Decision: Core Purpose and Non-Goals

**Status**: Accepted
**Date**: 2026-01-13
**Scope**: agentos
**Problem IDs**: PRB-0005

## Context
Rationale loss is more likely when the core purpose is not explicit.

## Decision
Define the core purpose and non-goals as contract constraints.
See definitions in `docs/reference/agentos/behavior-spec.md`.

## Alternatives
- Leave purpose implicit.
- Define purpose in explanation docs only.

## Consequences
- Adds explicit scope boundaries to the core.
- Reduces future drift in core intent.

## Why this worked
Preserves core intent over time and reduces rationale loss, addressing PRB-0005.
Evidence: explicit scope reduces drift when adapting to new tools or workflows.

## Artifacts
- `docs/reference/agentos/behavior-spec.md`
