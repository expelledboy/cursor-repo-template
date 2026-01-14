# How-to: Design-Decision Checkpoint

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Run a design-decision checkpoint using complexity-scaled templates.

## When to use
- Material design/architecture decisions.
- Complexity Level 1–4 tasks when a design decision is required.

## Steps
1) Select template level (by complexity):
   - Level 1: quick fix / simple enhancement
   - Level 2: standard feature
   - Level 3: complex feature/subsystem
   - Level 4: system/architecture
2) Use the template from `docs/reference/agentos/design-decision-templates.md`.
3) Fill required fields (all levels): options (>=2), selected approach, rationale, tradeoffs (table).
4) Link in task plan header:
   - Record template level.
   - Link to the checkpoint document (or embed in plan).
5) If core behavior changes: create an ADR using the completed template as source.

## Checklist
- [ ] Template level matches task complexity.
- [ ] Options, selected approach, rationale, tradeoffs present.
- [ ] Tradeoff table uses minimal criteria (no fluff).
- [ ] Task plan header references template level and checkpoint link.
- [ ] ADR created if core behavior changes.

## Outputs
- Completed checkpoint (template-filled).
- Updated task plan header (template level + link).
- ADR (only if behavior/contract changes).

## Example (Level 2, minimal)
Tradeoff table (2 options × 3 criteria):
```
| Option | Criteria1 | Criteria2 | Criteria3 |
| A      | brief     | brief     | brief     |
| B      | brief     | brief     | brief     |
```
