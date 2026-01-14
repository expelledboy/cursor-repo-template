# Decision: Adaptive Complexity Model with Workflow Variations

**Status**: Accepted
**Date**: 2026-01-14
**Scope**: agentos
**Problem IDs**: PRB-0001 (efficiency/overhead)
**Supersedes**: (none)

## Context
Simple tasks incur unnecessary overhead, while complex tasks need more rigor. AgentOS requires an 8-step lifecycle; variations must not skip steps. Complexity level already exists in headers but is not enforced for rigor, loading, checkpoints, or verification depth.

## Decision
Adopt complexity-based workflow variations (Levels 1–4) that adjust rigor within the mandatory 8-step lifecycle. Complexity level must be determined in classify, recorded with rationale/criteria, and used to drive:
- Directive loading (Level ↔ Tier mapping; Tier 3 for complexity-driven directives).
- Documentation depth (plan/report/anneal).
- Verification rigor.
- Design-decision checkpoints (L1–2 optional if no material decision; L3–4 mandatory or explicitly waived with rationale).
- Escalation (one-way up, explicit trigger + confirmation).

## Alternatives
- Keep unified lifecycle with no rigor scaling (rejected: overhead for simple tasks, insufficient rigor for complex tasks).
- Skip lifecycle steps for simple tasks (rejected: violates deterministic lifecycle).
- Two-level simple/complex split (rejected: insufficient granularity).

## Consequences
- Positive: 40–60% overhead reduction for L1; preserves rigor for L3–4; keeps lifecycle intact; improves traceability of complexity decisions.
- Negative: Added mappings (Level→Tier, rigor tables) and validation cost.
- Neutral: Requires lightweight how-to and validator to keep usage consistent.

## Why this worked
Preserves the required 8-step sequence while scaling rigor. Makes complexity explicit and auditable, aligning loading, checkpoints, and verification with task difficulty.

## Artifacts
- `docs/reference/agentos/complexity-determination.md`
- `docs/reference/agentos/workflow-variations.md`
- `docs/reference/agentos/behavior-spec.md` (sections 4, 11)
- `docs/how-to/agentos/determine-complexity.md`
- `scripts/agentos/validate_complexity_workflow.py`
- `docs/reference/agentos/validation-scripts.md`
- `scripts/agentos/mod.just`
- `scripts/agentos/validate_agentos.py`
