# /agentos-verify - Verification

## Purpose
Verify phase. Behavior is defined in canonical docs below.

## Lifecycle Entrypoint
- Covers: verify
- Handoff: report + anneal

## Canonical entrypoints (must read)
- docs/reference/agentos/verification-contract.md
- docs/reference/agentos/verification-gates.md
- .cursor/rules/agentos/core.mdc
- .cursor/rules/agentos/phase/verify.mdc

## Cursor rule loading
- If phase rules do not auto-load, explicitly open `.cursor/rules/agentos/phase/verify.mdc`.

## Adapter boundary
Commands are optional UI entrypoints. Core contracts live in docs/reference and must be followed.

## Next command
/agentos-complete
