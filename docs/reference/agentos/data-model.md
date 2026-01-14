# AgentOS Data Model (Reference)

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Defines the canonical data model for AgentOS artifacts and their required relationships.

---

## 1. Scope
AgentOS is a doc-native system. The data model is defined by Markdown artifacts and enforced by deterministic validation where available.

## 2. Core entities
- **Task**: work item governed by the task lifecycle in `behavior-spec.md`.
- **Task plan header**: required fields declared in the task plan (not a separate file).
- **Directive**: canonical docs that define behavior or facts.
- **Domain**: bounded scope with its own directives and routing rule.
- **Routing decision**: selection of required directives and allowed domains for a task.
- **Evidence source**: artifacts used to justify decisions, ordered by truth surface.
- **Verification gate**: deterministic check that defines pass or fail for a task.
- **Problem**: validated issue in the problem registry.
- **Decision record (ADR)**: accepted decision with rationale and artifacts.
- **Traceability entry**: mapping from problems to ADRs and artifacts.
- **Improvement note**: work note that captures improvement events and action items.
- **Gap note**: work note that captures missing or incorrect guidance.
- **Validation script**: deterministic validator for AgentOS contracts.

## 3. Storage locations
- Task plan header: task plan output (not a standalone artifact).
- Directives: `docs/reference/**`, `docs/how-to/**`, `docs/explanation/**`.
- Domains and routing: `docs/index.md` and `.cursor/rules/*.mdc`.
- Problems: `docs/reference/agentos/problem-registry.md`.
- ADRs: `docs/explanation/agentos/decisions/`.
- Traceability: `docs/reference/agentos/traceability.md`.
- Improvement notes: `docs/work/agentos/improvement/`.
- Gap notes: `docs/work/agentos/gaps/` (create folder as needed).
- Validation scripts: `scripts/agentos/` with index in `validation-scripts.md`.
- Local scratch (non-authoritative, gitignored): `docs/local/` and `docs/local/state/`.
- Local state surface definition: `docs/reference/agentos/state-surface.md`.

## 4. Required relationships
- Every validated problem appears in traceability.
- Every ADR appears in traceability.
- Directives and implementation files are linked via the registry.
- Tasks must declare a task plan header and verification gates.

## 5. Invariants
- Evidence sources follow the truth surface order.
- Routing must align to declared domains and context compass intent.
- Improvement notes must include evidence and affected artifacts.

## 6. Related docs
- `docs/reference/agentos/behavior-spec.md`
- `docs/reference/agentos/routing.md`
- `docs/reference/agentos/context-compass.md`
- `docs/reference/agentos/truth-surface.md`
- `docs/reference/agentos/verification-contract.md`
- `docs/reference/agentos/verification-gates.md`
- `docs/reference/agentos/registry.md`
- `docs/reference/agentos/problem-registry.md`
- `docs/reference/agentos/decision-record-format.md`
- `docs/reference/agentos/traceability.md`
- `docs/reference/agentos/self-improvement.md`
- `docs/reference/agentos/validation-scripts.md`
- `docs/reference/agentos/meta-analysis.md`
- `docs/reference/agentos/state-surface.md`

## 7. Validator coverage map
| Invariant | Validator |
| --- | --- |
| Registry mapping completeness and bidirectional links | `scripts/agentos/validate_registry.py` |
| Routing rule and index alignment | `scripts/agentos/validate_routing.py` |
| Core list sync across components, index, and rule | `scripts/agentos/validate_core_list_sync.py` |
| Traceability coverage for problems and ADRs | `scripts/agentos/validate_traceability.py` |
| ADR format compliance | `scripts/agentos/validate_adr_format.py` |
| Improvement note evidence fields | `scripts/agentos/validate_improvement_notes.py` |
| Verification gates coverage and command existence | `scripts/agentos/validate_verification_gates.py` |
