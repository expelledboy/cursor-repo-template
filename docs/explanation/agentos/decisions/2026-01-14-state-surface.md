# Decision: Local State Surface

**Status**: Accepted
**Date**: 2026-01-14
**Scope**: agentos
**Problem IDs**: PRB-0002; PRB-0001

## Context
Cursor rule loading is probabilistic and memory is opaque; active task state can drift across multi-step work and reduce reproducibility. The system needs a local, explicit state surface for active tasks without turning it into an audit artifact.

## Decision
Introduce a local, gitignored state surface at `docs/local/state/` for active task state.

Constraints:
- The state surface is non-authoritative and non-evidence.
- Promotion is limited to:
- Decision summaries that affect future work (process/tooling/constraints).
- Gaps that require contract/process changes.

See `docs/reference/agentos/state-surface.md` and `docs/how-to/agentos/local-state.md`.

## Alternatives
- No state surface (rejected: leaves context drift unresolved).
- Commit state surface to git (rejected: high-churn artifacts and audit burden).
- Promote all task state to work notes (rejected: excessive noise).

## Consequences
- Operational: stable local workspace reduces reliance on opaque memory.
- Governance: promotion limited to durable decisions and gaps only.

## Why this worked
It addresses PRB-0002 (context instability) and reduces PRB-0001 risk while keeping the audit surface minimal and aligned with stated preferences.

## Artifacts
- `docs/reference/agentos/state-surface.md`
- `docs/how-to/agentos/local-state.md`
- `docs/reference/agentos/self-improvement.md`
- `docs/how-to/agentos/capture-gaps.md`
- `docs/how-to/agentos/run-self-improvement-cycle.md`
- `docs/reference/agentos/data-model.md`
- `docs/reference/agentos/truth-surface.md`
- `docs/how-to/agentos/cursor-adapter.md`
