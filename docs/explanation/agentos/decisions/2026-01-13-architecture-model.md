# Decision: Architecture Model (DOE + Scoped Routing)

**Status**: Accepted
**Date**: 2026-01-13
**Scope**: agentos
**Problem IDs**: PRB-0005

## Context
Rationale loss makes it easy to remove or weaken core constraints during evolution.

## Decision
Define the AgentOS architecture model as a core reference contract.
The model is DOE with scoped routing and explicit interfaces.
See `docs/reference/agentos/architecture.md`.

## Alternatives
- Keep the architecture implicit in scattered docs.
- Capture only behavior rules without a formal model.

## Consequences
- Adds one more core reference doc to maintain.
- Makes the system model explicit and durable.

## Why this worked
A durable architecture model reduces rationale loss by preserving why the core exists.

## Artifacts
- `docs/reference/agentos/architecture.md`
- `docs/explanation/agentos/architecture-rationale.md`
