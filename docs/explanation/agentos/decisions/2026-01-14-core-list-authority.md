# Decision: Core List Authority

**Status**: Accepted
**Date**: 2026-01-14
**Scope**: agentos
**Problem IDs**: PRB-0005

## Context
Multiple documents list the AgentOS core, and they can drift.

## Decision
Declare `docs/reference/agentos/components.md` as the authoritative core list.
All other core lists must mirror it.

## Alternatives
- Treat `docs/index.md` as the authoritative core list.
- Treat the adapter rule as the authoritative core list.

## Consequences
- Core list changes must update `components.md` first.
- Adapter rules and doc maps must follow the authoritative list.

## Why this worked
Centralizes the authoritative core list in a reference contract, reducing rationale loss and drift.

## Artifacts
- `docs/reference/agentos/components.md`
- `docs/index.md`
- `.cursor/rules/20-agentos.topic.mdc`
