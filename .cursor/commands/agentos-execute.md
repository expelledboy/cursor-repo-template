# /agentos-execute - Execution

## Purpose
Execute phase. Behavior is defined in canonical docs below.

## Lifecycle Entrypoint
- Covers: execute
- Handoff: verify phase

## Canonical entrypoints (must read)
- docs/reference/agentos/behavior-spec.md#13-execution-discipline
- docs/reference/agentos/safety-policy.md
- .cursor/rules/agentos/core.mdc
- .cursor/rules/agentos/phase/execute.mdc

## Cursor rule loading
- If phase rules do not auto-load, explicitly open `.cursor/rules/agentos/phase/execute.mdc`.

## Adapter boundary
Commands are optional UI entrypoints. Core contracts live in docs/reference and must be followed.

## Next command
/agentos-verify
