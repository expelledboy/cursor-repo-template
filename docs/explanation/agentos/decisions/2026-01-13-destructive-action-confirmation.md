# Decision: Destructive Action Confirmation

**Status**: Accepted
**Date**: 2026-01-13
**Scope**: agentos
**Problem IDs**: PRB-0008

## Context
Destructive actions can be attempted without explicit user confirmation.

## Decision
Require explicit user confirmation before any destructive action.
See definitions in `docs/reference/agentos/behavior-spec.md`.

## Alternatives
- Implicit confirmation via task request.
- Confirmation only for high-impact deletions.

## Consequences
- Adds confirmation prompts before destructive steps.
- Reduces accidental data loss.

## Why this worked
Forces a user checkpoint that prevents PRB-0008 failures.
Evidence: explicit confirmation prevents irreversible actions without consent.

## Artifacts
- `docs/reference/agentos/behavior-spec.md`
