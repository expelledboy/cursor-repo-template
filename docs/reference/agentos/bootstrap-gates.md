# Bootstrap Exit Criteria (Reference)

**Status**: Stable
**Date**: 2026-01-13
**Purpose**: Defines the conditions required to exit bootstrap mode.

---

## 1. Exit criteria
Bootstrap is complete only when all of the following are true:
1. Inventory exists for CI, task runner, config, and repo structure.
2. Minimal workflows exist (install, test, build, deploy if relevant).
3. Draft directives exist for critical domains.
4. Routing exists (`docs/index.md` and domain rules).
5. Registry scope is defined and initial mapping exists.
6. A bootstrap analysis summary is produced for human validation.

## 2. Ratification
A human must confirm:
- Safety constraints and risk tolerance.
- Production workflows and definitions of done.
- Any remaining gaps or provisional items.

## 3. Related docs
- `docs/how-to/agentos/bootstrap-repo.md`
