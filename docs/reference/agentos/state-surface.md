# AgentOS State Surface (Reference)

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Define the local, non-authoritative state surface for active tasks.

---

## 1. Definition
The state surface is a local, ephemeral workspace used to track active task state. It is not evidence and is never authoritative.

## 2. Location
- `docs/local/state/` (gitignored)
- This directory is not tracked by git.

## 3. Minimal local files (suggested)
- `task.md` (current task summary)
- `plan.md` (working plan draft)
- `decisions.md` (task-local decisions)
- `gaps.md` (task-local gaps)

## 4. Promotion rule
Only promote:
- Decision summaries that affect future work (process/tooling/constraints).
- Gaps that require contract/process changes.

All other state remains local and is discarded after task completion.

## 5. Evidence boundary
Content in `docs/local/state/` must not be cited as evidence. Promote approved items into `docs/work/**` before use.

## 6. Related docs
- `docs/reference/agentos/truth-surface.md`
- `docs/reference/agentos/self-improvement.md`
- `docs/how-to/agentos/local-state.md`
