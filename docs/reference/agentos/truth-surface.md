# Truth Surface (Reference)

**Status**: Stable
**Date**: 2026-01-13
**Purpose**: Defines the evidence hierarchy used to resolve conflicts.

---

## 1. Evidence order
- CI workflows
- Task runner recipes
- Tests
- Runtime and deploy config
- Docs
- Scratch (docs/local/*) is non-evidence and must not be cited
- Everything else is provisional
See `docs/reference/agentos/state-surface.md` for local state rules.

## 2. Conflict rule
When sources conflict, the higher evidence source wins.
If the conflict affects behavior or safety, ask the user and record the outcome.

## 3. Use in tasks
- The task plan must cite the evidence sources used.
- When evidence is missing, mark assumptions as provisional.
