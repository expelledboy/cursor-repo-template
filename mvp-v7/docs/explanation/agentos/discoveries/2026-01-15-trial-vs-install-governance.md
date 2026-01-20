# Discovery: Trial vs install governance is required for safe reactivity

Status: Draft
Date: 2026-01-15
Scope: mvp-v7
Cursor features: Rules, Commands, Tools/MCP
Discovery ID: V7-DIS-0002

## Observation
- Without an auditable backlog, “scientific validation” is performative; we still need improvement.
- Cursor work is interactive; users can approve/deny persistent behavior changes.
- Commands and rules can enforce consistent gates for persistence.

## Implication
- Support Trial-by-default (session-local), Install-by-approval (explicit user approval) as a stable constraint.
- Encode install gates as graphs and expose them via commands when needed.

## Artifacts
- `docs/reference/agentos/kernel.md`
- `docs/reference/agentos/reactive-coherence-loop.md`
- `docs/reference/agentos/decision-graphs/trial-install-gate.md`
