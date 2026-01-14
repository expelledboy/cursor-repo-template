# How-to: Determine Complexity Level

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Step-by-step guide to set task complexity (1-4), record rationale, and handle escalation.

## When to determine
- During classify phase; update if complexity escalates during execution.

## Steps
1. Evaluate scope: single / multiple components / subsystem / system-wide.
2. Assess design decisions: none/simple / simple / complex / architectural.
3. Assess risk: low / moderate / high / critical.
4. Estimate effort: hours / days / weeks / months.
5. Check dependencies: none / few / many / architectural.
6. Use decision tree in `docs/reference/agentos/complexity-determination.md`.
7. Set level (1-4) and record rationale + criteria in the task plan header.
8. Update directive loading plan and verification rigor per level (Tier mapping in `workflow-variations.md`).

## Escalation
- Only escalate upward; requires explicit trigger and user confirmation.
- Update plan header (level, rationale, criteria, escalation record).
- Load additional directives per new level (Tier 3-5 as applicable).
- Document escalation in the report.

## Example
- Selected Level: 2
- Rationale: Multiple components, simple decision, moderate risk, effort=days, deps=few.
- Header: Complexity Level=2; Workflow Variation=Level 2; Escalation=None.
