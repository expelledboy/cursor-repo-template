# Decision: Self-Model Reference

**Status**: Accepted
**Date**: 2026-01-14
**Scope**: agentos
**Problem IDs**: PRB-0005

## Context
Meta-maintenance tasks require explicit self-awareness to avoid designing behavior the agent cannot enforce.

## Decision
Add a self-model reference that is required when AgentOS evolves its own operating model.
See `docs/reference/agentos/self-model.md`.

## Alternatives
- Rely on ad-hoc self-reflection in chat.
- Encode self-awareness only inside ADRs.

## Consequences
- Adds a core reference doc to maintain.
- Improves clarity about capabilities and limits during meta-maintenance.

## Why this worked
Makes self-awareness durable and explicit, reducing rationale loss during evolution.

## Artifacts
- `docs/reference/agentos/self-model.md`
- `docs/reference/agentos/behavior-spec.md`
- `docs/reference/agentos/self-improvement.md`
- `docs/how-to/agentos/run-self-improvement-cycle.md`
