# Decision: Verification Contract

**Status**: Accepted
**Date**: 2026-01-13
**Scope**: agentos
**Problem IDs**: PRB-0004

## Context
Verification gates can be missing or stale, allowing regressions.

## Decision
Require explicit verification gates aligned with CI, and require command lists when gates cannot be run.
See definitions in `docs/reference/agentos/behavior-spec.md`.

## Alternatives
- Best-effort verification without explicit gates.
- Rely solely on CI after changes.

## Consequences
- More explicit definition of verification per task.
- Less risk of regressions due to missing checks.

## Why this worked
Links correctness to explicit, auditable gates and CI alignment, addressing PRB-0004.
Evidence: SWE-bench Verified emphasizes fail-to-pass and pass-to-pass verification rigor.

## Artifacts
- `docs/reference/agentos/behavior-spec.md`
