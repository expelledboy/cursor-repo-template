# Problem: Unresolved Ambiguity in Requirements

**Status**: Draft
**Date**: 2026-01-13
**Scope**: system

## Statement
Ambiguous or uncertain requirements are not resolved immediately, leading to inconsistent outcomes.

## Evidence
- User report: ambiguity must be resolved with the user and captured in docs (2026-01-13).
- User report: primary vs derived requirements must be distinguished and clarified when uncertain (2026-01-13).

## Impact
Behavior diverges from intent and becomes harder to correct after implementation.

## Detection signals
- The agent proceeds without asking clarifying questions on ambiguous inputs.
- Follow-up corrections on intent after implementation.
- Conflicting interpretations of primary vs derived requirements.
- Missing documentation of resolved ambiguities.

## Notes
- Require an explicit ambiguity check before execution in tasks with unclear scope.
- Validation evidence: at least two cases where a clarifying question would have changed the outcome.
