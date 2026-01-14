# Improvement: State Surface Adoption (Micro-AAR)

**Status**: Complete
**Date**: 2026-01-14
**Event**: micro-aar
**Task**: Introduce local state surface with minimal promotion policy
**Evidence**: ADR created and traceability updated
**Affected artifacts**: `docs/reference/agentos/state-surface.md`, `docs/how-to/agentos/local-state.md`, `docs/explanation/agentos/decisions/2026-01-14-state-surface.md`, `docs/reference/agentos/traceability.md`, `docs/reference/agentos/self-improvement.md`, `docs/how-to/agentos/capture-gaps.md`, `docs/how-to/agentos/run-self-improvement-cycle.md`, `docs/reference/agentos/data-model.md`, `docs/reference/agentos/truth-surface.md`, `docs/how-to/agentos/cursor-adapter.md`

## Planned
Define a local, gitignored state surface for active tasks and codify a minimal promotion policy (decision summaries + gaps only).

## Observed
State surface definition and usage guidance were added, and promotion rules were limited to future-impact decisions and contract/process gaps.

## Why it happened
Context instability and goal drift require a stable local workspace without introducing audit overhead.

## Action items
- Validate adoption in practice using the new commands and isolated rules.
- Revisit promotion thresholds if local state grows uncontrolled.
