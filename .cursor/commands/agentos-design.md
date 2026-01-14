# /agentos-design - Design-Decision Checkpoint

## Purpose
Design checkpoint phase. Behavior is defined in canonical docs below.

## Lifecycle Entrypoint
- Covers: design-decision checkpoint
- Handoff: execute phase

## Canonical entrypoints (must read)
- docs/reference/agentos/behavior-spec.md#11-1-design-decision-checkpoint-requirements
- docs/reference/agentos/design-decision-templates.md
- docs/reference/agentos/structured-exploration.md
- .cursor/rules/agentos/core.mdc
- .cursor/rules/agentos/phase/design.mdc
- .cursor/rules/agentos/complexity/level3.mdc
- .cursor/rules/agentos/complexity/level4.mdc

## Cursor rule loading
- If phase rules do not auto-load, explicitly open `.cursor/rules/agentos/phase/design.mdc`.

## Adapter boundary
Commands are optional UI entrypoints. Core contracts live in docs/reference and must be followed.

## Next command
/agentos-execute
