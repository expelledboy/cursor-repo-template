# Problem: Goal Drift Across Multi-Step Tasks

**Status**: Draft
**Date**: 2026-01-13
**Scope**: system

## Statement
Agents lose the primary objective during multi-step work and optimize local sub-tasks instead.

## Evidence
- User report: agent workflows forget overarching objectives during sub-tasks (2026-01-13).
- User report: reference material needed to finish a refactor can fall outside the context window (2026-01-13).

## Impact
Primary requirements are missed or only partially met, causing rework and intent mismatch.

## Detection signals
- The plan or checkpoints do not restate the primary objective.
- Changes address local sub-tasks without closing the primary requirement.
- User corrections indicate scope or intent drift.

## Notes
- Validate whether the task plan includes an explicit primary objective before execution.
- Validation evidence: at least two tasks where subtasks were completed but the primary objective was not met.
