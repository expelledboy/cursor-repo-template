# Decision: Hybrid Rationale System

**Status**: Accepted
**Date**: 2026-01-13
**Scope**: agentos
**Problem IDs**: PRB-0005

## Context
Future agents must understand why the core exists and how it should evolve without relying on hidden memory.

## Decision
Use a hybrid system: Problem Registry + ADRs + Traceability Map.

## Alternatives
- ADRs only
- Single rationale ledger
- Inline rationale in the core spec

## Consequences
- Extra maintenance overhead
- Clear separation of what vs why vs where

## Why this worked
Matches the requirement for durable, explicit rationale and supports self-improvement.

## Artifacts
- `docs/reference/agentos/problem-registry.md`
- `docs/reference/agentos/decision-record-format.md`
- `docs/reference/agentos/traceability.md`
