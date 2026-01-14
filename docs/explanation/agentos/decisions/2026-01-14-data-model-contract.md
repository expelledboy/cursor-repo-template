# Decision: Data Model Contract

**Status**: Accepted
**Date**: 2026-01-14
**Scope**: agentos
**Problem IDs**: PRB-0005

## Context
AgentOS relies on doc-native artifacts, but the data model was implicit and spread across multiple contracts.

## Decision
Define a canonical data model reference for AgentOS artifacts and relationships.
See `docs/reference/agentos/data-model.md`.

## Alternatives
- Keep the data model implicit in other contracts.
- Capture the data model only in a work note.

## Consequences
- Adds a new core reference that must be maintained.
- Clarifies required relationships for validation and traceability.

## Why this worked
Explicit data model definitions reduce ambiguity and preserve rationale as the system evolves.

## Artifacts
- `docs/reference/agentos/data-model.md`
- `docs/reference/agentos/components.md`
