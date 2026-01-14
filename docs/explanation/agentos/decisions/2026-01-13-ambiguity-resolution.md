# Decision: Ambiguity Resolution Rule

**Status**: Accepted
**Date**: 2026-01-13
**Scope**: agentos
**Problem IDs**: PRB-0003

## Context
Ambiguous requirements lead to inconsistent outcomes if not resolved immediately.

## Decision
Require Primary vs Derived classification, and require user confirmation when uncertain. Record resolved ambiguities in canonical docs.
See definitions in `docs/reference/agentos/behavior-spec.md`.

## Alternatives
- Allow the agent to infer ambiguous requirements.
- Defer ambiguity resolution until after implementation.

## Consequences
- More questions before execution.
- Reduced divergence between intent and implementation.

## Why this worked
Forces clarification at the point of uncertainty and preserves decisions, addressing PRB-0003.
Evidence: requirement classification reduces ambiguity when primary and derived requirements are unclear.

## Artifacts
- `docs/reference/agentos/behavior-spec.md`
