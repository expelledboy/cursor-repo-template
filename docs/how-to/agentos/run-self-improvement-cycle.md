# Run the Self-Improvement Cycle (How-to)

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Execute the required improvement events and promote outcomes to canonical artifacts.

---

## 1. Choose the improvement event
- **Micro-AAR**: after each task.
- **Retrospective**: scheduled cadence or milestone.
- **Postmortem**: triggers in `docs/reference/agentos/self-improvement.md`.
- **Meta Analysis Mode (MAM)**: triggered by `docs/reference/agentos/self-improvement.md`.
- If the task type is **AgentOS Meta-Maintenance**, load `docs/reference/agentos/self-model.md`.

## 2. Select the loop
- **Single-loop**: fix steps, docs, or gates inside existing rules.
- **Double-loop**: change rules or assumptions when they cause repeated failure.

## 3. Create the improvement note
1. Run `date +%Y-%m-%d`.
2. Create `docs/work/agentos/improvement/YYYY-MM-DD-<slug>.md` with **Status**: Draft.
3. Use the minimal template:
```markdown
# Improvement: <short title>

**Status**: Draft
**Date**: YYYY-MM-DD
**Event**: micro-aar | retrospective | postmortem
**Task**: <link or summary>
**Evidence**: <links or references>
**Affected artifacts**: <paths>

## Planned
## Observed
## Why it happened
## Action items
```

## 4. Promote outcomes
- If a new problem is confirmed, follow `docs/how-to/agentos/problem-intake.md`.
- If core behavior changes, create an ADR using `docs/reference/agentos/decision-record-format.md`.
- Update `docs/reference/agentos/traceability.md`.
- Scratch notes in `docs/local/` must be promoted into `docs/work/**` before they are considered evidence.
- Promote only decision summaries that affect future work and gaps that require contract/process changes; other state remains local (see `docs/how-to/agentos/local-state.md`).

## 5. Implement and verify
- Update the canonical docs first, then how-to and explanation.
- Add or update verification gates when behavior changes.
- Run required validation commands (see `docs/reference/agentos/validation-scripts.md`).

## 6. Close action items
- Mark each action item complete with evidence.
- Supersede or archive the improvement note if replaced.
