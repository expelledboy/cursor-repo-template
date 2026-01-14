# /agentos-complete - Report + Anneal

## Purpose
Complete phase. Behavior is defined in canonical docs below.

## Lifecycle Entrypoint
- Covers: report → anneal
- Handoff: next task

## Canonical entrypoints (must read)
- docs/reference/agentos/behavior-spec.md#4-task-lifecycle
- docs/reference/agentos/self-improvement.md
- docs/reference/agentos/self-awareness-framework.md
- .cursor/rules/agentos/core.mdc
- .cursor/rules/agentos/phase/complete.mdc
- docs/reference/agentos/state-surface.md

## Cursor rule loading
- If phase rules do not auto-load, explicitly open `.cursor/rules/agentos/phase/complete.mdc`.

## Adapter boundary
Commands are optional UI entrypoints. Core contracts live in docs/reference and must be followed.

## Next command
/agentos-start
