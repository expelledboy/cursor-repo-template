# Problem: Rationale Loss Across Evolution

**Status**: Draft
**Date**: 2026-01-13
**Scope**: system

## Statement
Rationale for the core design is lost over time, causing future changes to remove critical constraints.

## Evidence
- User requirement: preserve why the core exists so future evolution does not forget (2026-01-13).
- User report: prior agent interactions lost fidelity, indicating rationale must live in durable docs (2026-01-13).

## Impact
Core behavior drifts or regresses when changes are made without the original reasoning.

## Detection signals
- Changes that remove constraints without replacing rationale.
- Inconsistent behavior across similar tasks.
- Repeated debates about why a rule exists.

## Notes
- Require an ADR for any core behavioral change.
- Validation evidence: at least one core change made without an ADR that led to re-litigation or regression.
