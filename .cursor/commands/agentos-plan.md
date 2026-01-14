# /agentos-plan - Planning

## Purpose
Plan this phase. Behavior is defined in canonical docs below.

## Lifecycle Entrypoint
- Covers: plan checkpoint
- Handoff: design checkpoint (if required) or execute

## Canonical entrypoints (must read)
- docs/reference/agentos/behavior-spec.md#4-task-lifecycle
- docs/reference/agentos/behavior-spec.md#11-task-plan-header-requirements
- docs/reference/agentos/workflow-variations.md
- docs/reference/agentos/verification-contract.md
- docs/reference/agentos/verification-gates.md
- .cursor/rules/agentos/core.mdc
- .cursor/rules/agentos/phase/plan.mdc
- .cursor/rules/agentos/complexity/level1.mdc
- .cursor/rules/agentos/complexity/level2.mdc
- .cursor/rules/agentos/complexity/level3.mdc
- .cursor/rules/agentos/complexity/level4.mdc
- docs/reference/agentos/state-surface.md

## Cursor rule loading
- If phase rules do not auto-load, explicitly open `.cursor/rules/agentos/phase/plan.mdc`.

## Adapter boundary
Commands are optional UI entrypoints. Core contracts live in docs/reference and must be followed.

## Next command
/agentos-design (if required) or /agentos-execute
