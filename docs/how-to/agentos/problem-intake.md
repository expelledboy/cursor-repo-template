# Propose and Validate Problems (How-to)

**Status**: Stable
**Date**: 2026-01-13
**Purpose**: Procedure for adding or superseding entries in the AgentOS Problem Registry.

---

## 1. Create a draft
1. Run `date +%Y-%m-%d` and capture the output.
2. Create `docs/work/agentos/problems/YYYY-MM-DD-<slug>.md` with **Status**: Draft.
3. Do not assign a problem ID in the draft.

## 2. Use the draft template
```markdown
# Problem: <short title>

**Status**: Draft
**Date**: YYYY-MM-DD
**Scope**: <system|domain>

## Statement
## Evidence
## Impact
## Detection signals
## Notes
```

## 3. Validate with a human
1. Review the draft with the maintainer.
2. If accepted, assign the next ID in `docs/reference/agentos/problem-registry.md`.
3. If rejected, keep the draft and record the reason in **Notes**.

## 4. Update the registry
1. Add the problem as a new row in `docs/reference/agentos/problem-registry.md`.
2. Set **Status** to Validated.
3. If superseding, mark the old entry Superseded and reference the new ID.

## 5. Update traceability
1. Add or update the mapping in `docs/reference/agentos/traceability.md`.
2. If the problem requires a behavior change, create an ADR using `docs/reference/agentos/decision-record-format.md`.
