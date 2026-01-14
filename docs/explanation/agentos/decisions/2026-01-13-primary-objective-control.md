# Decision: Primary Objective Control

**Status**: Accepted
**Date**: 2026-01-13
**Scope**: agentos
**Problem IDs**: PRB-0001

## Context
Goal drift occurs when multi-step work loses the primary objective.

## Decision
Require a single primary objective, restated at checkpoints, with explicit completion reporting.
See definitions in `docs/reference/agentos/behavior-spec.md`.

## Alternatives
- Allow multiple primary objectives per task.
- Allow implicit objectives without restatement.

## Consequences
- Adds planning overhead.
- Reduces drift by keeping the primary objective explicit.

## Why this worked
Directly constrains the PRB-0001 failure mode by making the objective visible throughout execution.

## Artifacts
- `docs/reference/agentos/behavior-spec.md`
