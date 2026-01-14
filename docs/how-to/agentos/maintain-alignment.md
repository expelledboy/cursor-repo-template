# Maintain Alignment (How-to)

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Procedure for running the meta-questions to stay aligned with the repo and constraints.

---

## 1. When to run the full set
- Bootstrap or new repo alignment.
- Major changes to routing, registry, or verification.

## 2. When to run a focused subset
- **Routing confusion**: Q3, Q4.
- **Execution failure**: Q5, Q6.
- **Drift detected**: Q7, Q8.
- **Safety concern**: Q2, Q10, Q13.

## 3. How to record answers
1. Run `date +%Y-%m-%d`.
2. Create a work note at `docs/work/agentos/<category>/YYYY-MM-DD-<slug>.md` with a Status field.
3. Record each question, answer, and evidence source.
4. Mark uncertain answers as provisional.
5. If notes start in scratch (`docs/local/`), promote them into the work note before citing as evidence.

## 4. Promotion
- Promote stable findings to reference or how-to docs.
- Update traceability if any core behavior changes.
- The canonical questions live in `docs/reference/agentos/meta-questions.md`.
- For broader improvements, use `docs/how-to/agentos/run-self-improvement-cycle.md`.
