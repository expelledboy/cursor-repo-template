# AgentOS Architecture (Reference)

**Status**: Stable
**Date**: 2026-01-13
**Purpose**: Defines the core architecture model and interfaces for AgentOS.

---

## 1. Architecture model (DOE)
- **Directive (D)**: Canonical docs are the source of truth.
- **Orchestration (O)**: The agent routes and plans work against directives.
- **Execution (E)**: Deterministic tools perform actions and produce evidence.

## 2. Supporting contracts
These are required for a stable DOE system but are not separate orchestration layers.
- **Registry**: Doc <-> code mapping to prevent drift.
- **Verification**: Explicit gates aligned with CI.
- **Safety**: Least privilege and destructive action confirmation.
- **Bootstrap**: Day-0 learning when directives are missing.

## 3. Roles
- **Root Orchestrator**: Routes tasks, selects domains, enforces lifecycle, and escalates ambiguity.
- **Domain Sub-Agent (virtual)**: Executes within a single domain scope using that domain's directives and tools.

## 4. Interfaces
- **Directives**: `docs/reference/**` and `docs/how-to/**` (authority order applies).
- **Routers**: `docs/index.md` plus adapter rules (for example, `.cursor/rules/*.mdc`).
- **Execution API**: Task runner recipes, scripts, and CI workflows.
- **Registry**: Bidirectional mapping between directives and implementation files.
- **Verification gates**: Commands that define pass or fail for the task.

## 5. Task flow alignment
The architecture must align to the task lifecycle in `docs/reference/agentos/behavior-spec.md`:
intake -> classify -> route -> plan -> execute -> verify -> report -> anneal.

## 6. Portability boundaries
- **Repo-specific**: Domains, registry scope, execution API, and gates.
- **Repo-agnostic**: Lifecycle, authority order, requirement classification, safety, and deterministic execution.

## 7. Adapter boundary
Adapters may load context but must not override the core architecture or behavior constraints.
