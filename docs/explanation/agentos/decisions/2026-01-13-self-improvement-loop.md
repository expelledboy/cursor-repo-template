# Decision: Self-Improvement Loop

**Status**: Accepted
**Date**: 2026-01-13
**Scope**: agentos
**Problem IDs**: PRB-0005

## Context
Rationale is lost when gaps are not captured and promoted through a durable workflow.

## Decision
Require gaps to become work notes, validated problems, ADRs, and traceability updates.
See definitions in `docs/reference/agentos/behavior-spec.md`.

## Alternatives
- Capture gaps informally in chat only.
- Update the core without problems or ADRs.

## Consequences
- Adds process overhead for changes.
- Preserves rationale and enables auditable evolution.

## Why this worked
Creates a durable promotion path and prevents rationale loss, addressing PRB-0005.
Evidence: Reflexion highlights durable reflection artifacts that improve future attempts.

## Artifacts
- `docs/reference/agentos/behavior-spec.md`
- `docs/reference/agentos/problem-registry.md`
- `docs/reference/agentos/decision-record-format.md`
- `docs/reference/agentos/traceability.md`
