# Directive Tiers (Reference)

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Tier assignments for AgentOS directives to support hierarchical loading. Use this table to populate the directive loading plan (Section 10 of `behavior-spec.md`). Tiers must respect Context Compass intent constraints.

| Directive | Tier | Trigger / Notes |
| --- | --- | --- |
| behavior-spec.md | 1 | Core behavior (load when intent allows reference) |
| architecture.md | 1 | Core architecture (intent allows reference) |
| routing.md | 1 | Core routing (intent allows reference) |
| context-compass.md | 1 | Doc type constraints (intent allows reference) |
| components.md | 1 | Core list (intent allows reference) |
| validation-scripts.md | 1 | Validation index (intent allows reference) |
| problem-registry.md | 1 | Problems catalog (intent allows reference) |
| traceability.md | 1 | Traceability map (intent allows reference) |
| decision-record-format.md | 1 | ADR format (intent allows reference) |
| meta-questions.md | 1 | Meta prompts (intent allows reference) |
| meta-analysis.md | 1 | MAM reference (intent allows reference) |
| self-model.md | 1 | Self model (intent allows reference) |
| self-awareness-framework.md | 1 | Self-awareness (intent allows reference) |
| self-improvement.md | 2 | Improvement system (load for tasks with improvement/verification scope) |
| state-surface.md | 2 | Local state surface definition (load when using local state) |
| verification-gates.md | 3 | Select gates by complexity; load catalog when needed |
| verification-contract.md | 2 | Load for Testing/Verification tasks |
| safety-policy.md | 2 | Load when destructive actions possible |
| registry.md | 5 | Load when registry work required |
| bootstrap-gates.md | 5 | Load during bootstrap only |
| cursor-mechanics.md | 2 | Load for Cursor adapter work |
| routing (how-to/adapter) docs | 2 | Load for adapter/routing tasks |
| design-decision-templates.md | 4 | Load when design-decision checkpoint is required (by complexity) |
| design-decision-checkpoint (how-to) | 4 | Load when performing design-decision checkpoint |
| structured-exploration.md | 4 | Load when design-decision checkpoint phase is reached (structured exploration required) |
| design-decision-structured-exploration.md | 4 | Load when performing structured exploration for design-decision checkpoint |
| directive-tiers.md | 1 | This file (reference) |

Notes:
- Tier 3 (Complexity) directives are chosen per task complexity (e.g., level-appropriate gates/templates); include them in the loading plan when applicable.
- Tier 4/5 entries must include explicit triggers in the directive loading plan.
- If a directive is not listed, assign conservatively (default Tier 2 if task-type specific; Tier 5 if highly specialized with explicit trigger).
- Tiers present: Tier 1, Tier 2, Tier 3, Tier 4, Tier 5.
