# Maintain Registry (How-to)

**Status**: Stable
**Date**: 2026-01-13
**Purpose**: Procedure for keeping registry mappings valid.

---

## 1. When to update
- New files are created.
- Files are moved or renamed.
- Directives change or are split.
- Registry scope changes.
 - `AGENTS.md` Registry Scope is updated.

## 2. How to update
1. Add or update `@directive` annotations in code files.
2. Add or update `@implementation` entries in docs.
3. Run `just agentos::validate-registry` if it exists, or `scripts/agentos/validate_registry.py`.
4. See `docs/reference/agentos/registry.md` for the canonical format.

## 3. If validation is missing
1. Run `date +%Y-%m-%d`.
2. Create a work note at `docs/work/agentos/YYYY-MM-DD-<slug>.md` describing the missing validation command.
3. Link it to PRB-0007 in `docs/reference/agentos/problem-registry.md`.

## 4. Verification
- Validation output must not be truncated.
- Record the validation command in the task report.
