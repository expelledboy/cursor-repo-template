# Problem: Task Taxonomy Drift

**Status**: Draft
**Date**: 2026-01-13
**Scope**: system

## Statement
Task types evolve without updating routing, verification, and documentation contracts.

## Evidence
User requirement: task taxonomy should evolve by adding and refining tasks as needed (2026-01-13).

## Impact
New or changed task types are handled inconsistently and bypass required controls.

## Detection signals
- New task types appear without updates to behavior spec or traceability.
- Tasks are routed without an explicit taxonomy entry.
- Verification steps are missing for new task types.

## Notes
- Validation evidence: at least one task type used in practice without a corresponding taxonomy update.
