# Capture Gaps During Execution (How-to)

**Status**: Stable
**Date**: 2026-01-13
**Purpose**: Procedure for turning task gaps into durable AgentOS improvements.

---

## 1. When to capture a gap
- A task fails due to missing or incorrect directives.
- A required step is unclear or missing from the task lifecycle.
- Verification gates are missing, stale, or unclear.
- Ambiguity is resolved but not yet documented.

## 2. Create a work note
1. Run `date +%Y-%m-%d`.
2. Create `docs/work/agentos/gaps/YYYY-MM-DD-<slug>.md` with **Status**: Draft.
   - Create the `docs/work/agentos/gaps/` folder as needed.
   - If notes start in scratch (`docs/local/`), promote them here before validation.

## 3. Use the gap template
```markdown
# Gap: <short title>

**Status**: Draft
**Date**: YYYY-MM-DD
**Task**: <link or summary>

## Symptom
## Evidence
## Impact
## Proposed direction
```

## 4. Promote when validated
- If the gap defines a new problem, create a problem draft under `docs/work/agentos/problems/`.
- If the gap changes behavior, create or update an ADR.
- Update `docs/reference/agentos/traceability.md`.
- Promote only gaps that affect future work or require contract/process changes; keep local-only gaps in `docs/local/state/` (see `docs/how-to/agentos/local-state.md`).

## 5. Archive the gap
- When superseded, add a banner and move to `docs/archive/`.
