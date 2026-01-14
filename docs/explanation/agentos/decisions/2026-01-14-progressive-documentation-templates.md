# Decision: Progressive Documentation Templates for Design Decisions

**Status**: Accepted
**Date**: 2026-01-14
**Scope**: agentos
**Problem IDs**: PRB-0005
**Ratified**: 2026-01-14
**Supersedes**: (none)

## Context
Design-decision checkpoints lack scaled templates; simple tasks are over-documented and complex tasks under-structured. The batch-2 research (progressive docs) proposes complexity-scaled templates to preserve rationale efficiently.

## Decision
Adopt Level 1–4 design-decision templates with minimum required fields (selected approach, rationale, tradeoffs) and tabular tradeoff standard. Template level is chosen by complexity; task plan header records the level. Validation will enforce template use and completeness.

## Alternatives
- Single comprehensive template for all decisions (rejected: overhead for simple tasks).
- Unstructured/freeform checkpoints (rejected: rationale loss, inconsistency).
- Two-level (simple/complex) templates (rejected: insufficient granularity for Level 3–4).

## Consequences
- Positive: Right-sized documentation, better rationale preservation, consistent tradeoff capture.
- Negative: Template maintenance and validation required.
- Neutral: ADRs remain comprehensive; templates feed ADRs when behavior changes.

## Why this worked
Scaling templates by complexity aligns effort to task scope, preserving rationale without bloating small tasks. Tabular tradeoffs compress tokens while keeping comparisons explicit.

## Artifacts
- `docs/reference/agentos/design-decision-templates.md` (new)
- `docs/reference/agentos/behavior-spec.md` (design checkpoint requirements referencing templates)
- `docs/how-to/agentos/design-decision-checkpoint.md` (usage guide)
- `scripts/agentos/validate_design_decisions.py` (new)
- `docs/reference/agentos/validation-scripts.md` (list validator)
- `.cursor/rules/20-agentos.topic.mdc`, `docs/reference/agentos/components.md` (core list sync)
