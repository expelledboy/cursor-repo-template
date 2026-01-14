# Decision: Meta-Maintenance Context Intent

**Status**: Accepted
**Date**: 2026-01-14
**Scope**: agentos
**Problem IDs**: PRB-0002; PRB-0005

## Context
AgentOS Meta-Maintenance tasks require reference, how-to, and explanation docs, but the context compass did not define this intent.

## Decision
Add an explicit AgentOS Meta-Maintenance intent that allows reference + how-to + explanation docs.
See `docs/reference/agentos/context-compass.md`.

## Alternatives
- Treat meta-maintenance as Architecture intent only.
- Allow any doc type without an explicit intent rule.

## Consequences
- Removes ambiguity about allowed doc types during meta-maintenance.
- Keeps the context compass aligned with core maintenance needs.

## Why this worked
Defines a clear intent boundary for meta-maintenance without weakening execution or learning constraints.

## Artifacts
- `docs/reference/agentos/context-compass.md`
- `docs/reference/agentos/behavior-spec.md`
