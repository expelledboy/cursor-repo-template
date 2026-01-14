# /agentos-start - Intake + Classify + Route

## Purpose
Start this phase. Behavior is defined in canonical docs below.

## Lifecycle Entrypoint
- Covers: intake → classify → route → complexity
- Handoff: plan phase

## Canonical entrypoints (must read)
- docs/reference/agentos/behavior-spec.md#4-task-lifecycle
- docs/reference/agentos/behavior-spec.md#6-task-taxonomy
- docs/reference/agentos/behavior-spec.md#10-context-loading-contract
- docs/reference/agentos/behavior-spec.md#11-task-plan-header-requirements
- docs/reference/agentos/complexity-determination.md
- docs/reference/agentos/routing.md
- .cursor/rules/agentos/core.mdc
- .cursor/rules/agentos/phase/init.mdc
- docs/reference/agentos/state-surface.md

## Cursor rule loading
- If phase rules do not auto-load, explicitly open `.cursor/rules/agentos/phase/init.mdc`.

## Adapter boundary
Commands are optional UI entrypoints. Core contracts live in docs/reference and must be followed.

## Next command
/agentos-plan
