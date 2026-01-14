# Validate Routing (How-to)

**Status**: Stable
**Date**: 2026-01-13
**Purpose**: Manual procedure for checking routing drift.

---

## 1. What to check
- Rules reference existing docs.
- `docs/index.md` lists every domain rule.
- Every domain in `docs/index.md` has a rule file.

## 2. Manual steps
1. List rules in `.cursor/rules/`.
2. Open each rule and confirm referenced doc paths exist.
3. Open `docs/index.md` and confirm each domain lists a rule.
4. If mismatches exist, run `date +%Y-%m-%d` and create a work note under `docs/work/agentos/`.
5. Fix mismatches before execution.

## 3. Related contract
- `docs/reference/agentos/routing.md`

## 4. If a task runner exists
- Run `just agentos::validate-routing` when available.
- The default implementation is `scripts/agentos/validate_routing.py`.
