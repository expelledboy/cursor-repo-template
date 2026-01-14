# Problem: Verification Gate Gaps and Decay

**Status**: Draft
**Date**: 2026-01-13
**Scope**: system

## Statement
Verification gates are missing, stale, or not maintained, allowing regressions to slip through.

## Evidence
- User requirement: the system must learn to use, create, and maintain quality gates continuously (2026-01-13).

## Impact
Changes ship without adequate validation, increasing regressions and rework.

## Detection signals
- Tasks complete without a defined verification step.
- Gates differ from CI or are outdated.
- Regressions reappear after fixes.

## Notes
- Validate whether gate definitions exist and are mapped to CI in each task type.
- Validation evidence: at least one regression that passed local gates but failed CI due to missing or stale gates.
