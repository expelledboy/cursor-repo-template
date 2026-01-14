# Problem: Routing Drift and Misrouting

**Status**: Draft
**Date**: 2026-01-13
**Scope**: system

## Statement
Routing selection fails or drifts, causing the agent to load directives from the wrong domain.

## Evidence
User requirement: routing and route management are critical (2026-01-13).

## Impact
The agent uses incorrect constraints and procedures, leading to incorrect outcomes or wasted effort.

## Detection signals
- Task uses directives from a different domain than the task type.
- Canonical docs for the task type are not loaded before execution.
- Repeated user corrections about domain or scope.

## Notes
- Validation evidence: at least two cases where routing selected the wrong domain or missed required directives.
