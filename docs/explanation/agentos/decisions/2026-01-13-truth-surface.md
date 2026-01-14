# Decision: Truth Surface Contract

**Status**: Accepted
**Date**: 2026-01-13
**Scope**: agentos
**Problem IDs**: PRB-0002; PRB-0003

## Context
Conflicting sources cause ambiguity and inconsistent decisions.

## Decision
Define a truth surface hierarchy for resolving conflicts.
See `docs/reference/agentos/truth-surface.md`.

## Alternatives
- Treat all sources as equal.
- Rely on implicit preference rules.

## Consequences
- Adds explicit evidence ordering to task planning.
- Forces provisional labeling when evidence is missing.

## Why this worked
Explicit evidence ordering reduces ambiguity and misrouting.

## Artifacts
- `docs/reference/agentos/truth-surface.md`
