# Decision: Task Plan Header Authorship

**Status**: Accepted
**Date**: 2026-01-14
**Scope**: agentos
**Problem IDs**: PRB-0001; PRB-0003

## Context
Users should not be required to draft the task plan header, but the core contract did not assign authorship.

## Decision
The agent drafts the task plan header and only asks the user to confirm missing or ambiguous fields.
See `docs/reference/agentos/behavior-spec.md`.

## Alternatives
- Require the user to provide the task plan header.
- Allow either the user or the agent to author it.

## Consequences
- Reduces user friction.
- Makes header consistency the agent's responsibility.

## Why this worked
Keeps alignment friction low while preserving explicit intent and ambiguity resolution.

## Artifacts
- `docs/reference/agentos/behavior-spec.md`
- `.cursor/rules/20-agentos.topic.mdc`
- `docs/how-to/agentos/cursor-adapter.md`
