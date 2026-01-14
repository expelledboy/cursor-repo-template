# Decision: Task Taxonomy Drift Controls

**Status**: Accepted
**Date**: 2026-01-13
**Scope**: agentos
**Problem IDs**: PRB-0010

## Context
Task taxonomy changes can bypass routing and verification updates.

## Decision
Require taxonomy changes to update the core spec, ADRs, and traceability.
See definitions in `docs/reference/agentos/behavior-spec.md`.

## Alternatives
- Allow taxonomy changes without formal updates.
- Track taxonomy changes informally.

## Consequences
- Adds governance steps for taxonomy edits.
- Reduces drift between taxonomy and controls.

## Why this worked
Forces alignment between taxonomy changes and core contracts, addressing PRB-0010.
Evidence: explicit governance prevents silent drift in task handling.

## Artifacts
- `docs/reference/agentos/behavior-spec.md`
