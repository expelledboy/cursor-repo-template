# Architecture Rationale (Explanation)

**Status**: Stable
**Date**: 2026-01-13
**Purpose**: Explains why the AgentOS architecture is structured around DOE and scoped routing.

---

## 1. Why DOE
- **Directive** anchors behavior to explicit, versioned truth (reduces drift).
- **Orchestration** keeps the agent focused on routing and planning (reduces goal drift).
- **Execution** shifts reliability to deterministic tools (reduces stochastic outcomes).

## 2. Why virtual sub-agents
- Context windows are limited and unstable.
- Routing to a single domain reduces misrouting and overload.
- Scoped execution lowers the chance of cross-domain mistakes.

## 3. Why the supporting contracts
- **Registry** makes doc updates deterministic and prevents silent drift.
- **Verification gates** make correctness auditable and repeatable.
- **Safety constraints** prevent destructive or unsafe actions.
- **Bootstrap** makes the system portable to new repos.

## 4. Tradeoffs
- More up-front structure and documentation.
- Slower starts, fewer regressions.
- Requires discipline to keep rules and docs in sync.

## 5. Related contracts
- `docs/reference/agentos/behavior-spec.md`
- `docs/reference/agentos/problem-registry.md`
- `docs/reference/agentos/traceability.md`
