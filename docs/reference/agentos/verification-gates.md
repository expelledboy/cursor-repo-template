# Verification Gates Catalog (Reference)

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Canonical catalog of verification gates mapped to task types.

---

## 1. Rules
- Every task type in `docs/reference/agentos/behavior-spec.md` must appear here.
- Commands must be deterministic and runnable from the repo.
- Replace template gates with repo-specific gates as soon as real workflows exist.

## 2. Gate catalog
| Task type | Gate | Command | Evidence source | Notes |
| --- | --- | --- | --- | --- |
| Discovery & Requirements | AgentOS baseline | `just agentos::validate-agentos` | Task runner | Template baseline. Replace with repo gates. |
| Planning & Estimation | AgentOS baseline | `just agentos::validate-agentos` | Task runner | Template baseline. Replace with repo gates. |
| Design & Architecture | AgentOS baseline | `just agentos::validate-agentos` | Task runner | Template baseline. Replace with repo gates. |
| Implementation / Feature Build | Unit test baseline | `just test` | Task runner | Replace with repo-specific tests. |
| Testing & Verification | Unit test baseline | `just test` | Task runner | Replace with repo-specific tests. |
| Release & Deployment | Build baseline | `just build` | Task runner | Replace with repo-specific release gates. |
| Operations & Maintenance | Smoke baseline | `just test` | Task runner | Replace with repo-specific ops gates. |
| Security & Compliance | Lint baseline | `just lint` | Task runner | Replace with repo-specific security gates. |
| Documentation & Knowledge | AgentOS baseline | `just agentos::validate-agentos` | Task runner | Replace with repo-specific doc gates. |
| Refactoring & Tech-Debt | Unit test baseline | `just test` | Task runner | Replace with repo-specific tests. |
| Incident Response & Debugging | Smoke baseline | `just test` | Task runner | Replace with repo-specific incident gates. |
| AgentOS Meta-Maintenance | AgentOS baseline | `just agentos::validate-agentos` | Task runner | Required for AgentOS changes. |

## 3. Related docs
- `docs/reference/agentos/verification-contract.md`
- `docs/reference/agentos/behavior-spec.md`
- `docs/reference/agentos/validation-scripts.md`
