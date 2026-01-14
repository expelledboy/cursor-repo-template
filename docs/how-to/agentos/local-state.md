# How-to: Local State Surface

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Use the local state surface for active tasks without promoting unnecessary artifacts.

---

## 1. When to use
Use local state for in-progress tasks when you need a lightweight, disposable workspace.

## 2. Where it lives
- `docs/local/state/` (gitignored)

## 3. Suggested files
- `task.md`: current task summary
- `plan.md`: working plan draft
- `decisions.md`: task-local decisions
- `gaps.md`: task-local gaps

## 4. Promotion rule (minimal)
Promote only:
- Decision summaries that affect future work (process/tooling/constraints).
- Gaps that require contract/process changes.

All other content stays local and is discarded after the task completes.

## 5. Promotion path
Local state → `docs/work/**` (decision/gap only) → canonical docs if required.

## 6. Related docs
- `docs/reference/agentos/state-surface.md`
- `docs/how-to/agentos/capture-gaps.md`
- `docs/how-to/agentos/run-self-improvement-cycle.md`
