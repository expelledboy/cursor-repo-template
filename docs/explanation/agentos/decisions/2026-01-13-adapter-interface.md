# Decision: Adapter Interface

**Status**: Accepted
**Date**: 2026-01-13
**Scope**: agentos
**Problem IDs**: PRB-0002

## Context
Adapters can introduce hidden behavior if they override core rules.

## Decision
Allow adapters to load context, but require them to map outputs into the task plan header and forbid overriding core behavior.
See definitions in `docs/reference/agentos/behavior-spec.md`.

## Alternatives
- Allow adapters to override core rules.
- Disallow adapters entirely.

## Consequences
- Preserves IDE flexibility without changing core constraints.
- Requires explicit mapping from adapter output to core declarations.

## Why this worked
Keeps core behavior stable while reducing opaque context effects, addressing PRB-0002.
Evidence: adapter behavior must be transparent because memory and routing are opaque to the agent.

## Artifacts
- `docs/reference/agentos/behavior-spec.md`
