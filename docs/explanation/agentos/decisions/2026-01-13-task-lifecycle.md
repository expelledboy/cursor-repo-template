# Decision: Task Lifecycle Sequence

**Status**: Accepted
**Date**: 2026-01-13
**Scope**: agentos
**Problem IDs**: PRB-0001

## Context
Goal drift and partial completion occur when tasks skip required steps or execute out of order.

## Decision
Require a fixed task lifecycle sequence and minimal outputs for each step.
See definitions in `docs/reference/agentos/behavior-spec.md`.

## Alternatives
- Allow free-form ordering of steps.
- Allow execution before planning or routing.

## Consequences
- Adds explicit structure to every task.
- Reduces drift by enforcing ordered checkpoints.

## Why this worked
Directly constrains the PRB-0001 failure mode by enforcing a consistent sequence.
Evidence: ReAct and Plan-and-Solve emphasize explicit sequencing to reduce missing-step errors.

## Artifacts
- `docs/reference/agentos/behavior-spec.md`
