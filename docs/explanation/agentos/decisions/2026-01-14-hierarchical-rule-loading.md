# Decision: Hierarchical Rule Loading for Context Efficiency

**Status**: Accepted
**Date**: 2026-01-14
**Scope**: agentos
**Problem IDs**: PRB-0002
**Ratified**: 2026-01-14
**Supersedes**: (none)

## Context
AgentOS loads many core directives at once, inflating context and token usage. The batch-2 research (hierarchical loading) shows a 5-tier approach can cut context use while keeping explicit declaration and traceability.

## Decision
Adopt a 5-tier hierarchical loading model with explicit declaration in the task plan header and validation of tier assignments and triggers:
- Tier 1 (Core): always loaded (per Context Compass allowance).
- Tier 2 (Task-type): load per task type/domains.
- Tier 3 (Complexity): load per complexity level.
- Tier 4 (Phase-specific): load on lifecycle triggers.
- Tier 5 (Specialized): load on rare, explicit triggers.
- Directive loading plan must list tiers and deferred triggers.

## Alternatives
- Load all directives always (rejected: excessive context, violates efficiency).
- Implicit/automatic loading without declaration (rejected: violates explicit declaration/traceability).
- Two-tier (core/other) split (rejected: insufficient granularity; still bloated).

## Consequences
- Positive: Reduced context usage; clearer declaration of what/when to load; auditable triggers for deferred loads.
- Negative: Added tier mapping maintenance and validation burden.
- Neutral: Requires adapter instructions but no behavioral change to lifecycle order.

## Why this worked
Explicit tiers align with existing loading-plan and routing contracts, adding structure without changing lifecycle steps. Tier granularity targets token savings while preserving traceability.

## Artifacts
- `docs/reference/agentos/context-compass.md` (add tiers section)
- `docs/reference/agentos/behavior-spec.md` (tiered loading plan format)
- `docs/reference/agentos/directive-tiers.md` (new)
- `docs/how-to/agentos/cursor-adapter.md` (adapter instructions)
- `scripts/agentos/validate_directive_loading.py` (new)
- `docs/reference/agentos/validation-scripts.md` (list validator)
- `.cursor/rules/20-agentos.topic.mdc`, `docs/reference/agentos/components.md` (core list sync)
