# AgentOS Components Inventory

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Enumerates the concrete components that make up AgentOS.

---

## 1. Core contracts
This section is the authoritative list of AgentOS core contracts. Other lists must mirror it. Adapter rules may load a minimal core via `.cursor/rules/agentos/core.mdc` for isolation; the full list remains canonical here and in `docs/index.md`.
- `docs/reference/agentos/behavior-spec.md`
- `docs/reference/agentos/architecture.md`
- `docs/reference/agentos/components.md`
- `docs/reference/agentos/problem-registry.md`
- `docs/reference/agentos/routing.md`
- `docs/reference/agentos/context-compass.md`
- `docs/reference/agentos/safety-policy.md`
- `docs/reference/agentos/registry.md`
- `docs/reference/agentos/truth-surface.md`
- `docs/reference/agentos/verification-contract.md`
- `docs/reference/agentos/verification-gates.md`
- `docs/reference/agentos/meta-questions.md`
- `docs/reference/agentos/bootstrap-gates.md`
- `docs/reference/agentos/cursor-mechanics.md`
- `docs/reference/agentos/validation-scripts.md`
- `docs/reference/agentos/self-improvement.md`
- `docs/reference/agentos/self-model.md`
- `docs/reference/agentos/self-awareness-framework.md`
- `docs/reference/agentos/meta-analysis.md`
- `docs/reference/agentos/directive-tiers.md`
- `docs/reference/agentos/design-decision-templates.md`
- `docs/reference/agentos/complexity-determination.md`
- `docs/reference/agentos/workflow-variations.md`
- `docs/reference/agentos/decision-record-format.md`
- `docs/reference/agentos/data-model.md`
- `docs/reference/agentos/traceability.md`
- `docs/reference/agentos/state-surface.md`

## 2. Governance artifacts
- `docs/explanation/agentos/decisions/` (ADRs)
- `docs/explanation/agentos/design-highlights.md`
 - `docs/reference/agentos/meta-questions.md`

## 3. Directive system
- `docs/index.md` (documentation map)
- `docs/reference/**` (facts and contracts)
- `docs/how-to/**` (procedures)
- `docs/explanation/**` (rationale)
- `docs/tutorials/**` (learning)
- `docs/work/**` (drafts and notes)
- `docs/archive/**` (superseded material)

## 4. Routing and adapters
- `.cursor/rules/00-global.mdc` (global guardrails)
- `.cursor/rules/10-docs-routing.mdc` (docs routing discipline)
- `.cursor/rules/20-agentos.topic.mdc` (AgentOS adapter rule)
- Adapter guidance: `docs/how-to/agentos/cursor-adapter.md`
 - Cursor mechanics: `docs/reference/agentos/cursor-mechanics.md`
 - Routing validation: `docs/how-to/agentos/validate-routing.md`

## 5. Bootstrap
- Bootstrap gates: `docs/reference/agentos/bootstrap-gates.md`
- Bootstrap runbook: `docs/how-to/agentos/bootstrap-repo.md`
- Porting runbook: `docs/how-to/agentos/porting-to-new-repo.md`

## 6. Verification and execution
- Execution API: task runner recipes, scripts, CI workflows
- Verification gates: defined per task in plans and aligned with CI
- Verification contract: `docs/reference/agentos/verification-contract.md`
- Validation scripts: `docs/reference/agentos/validation-scripts.md`
- Visual process maps (supplementary): `docs/reference/agentos/visual-maps-standards.md` with diagrams in core reference docs

## 7. Evidence hierarchy
- Truth surface: `docs/reference/agentos/truth-surface.md`

## 8. Registry and mapping
- Registry contract: `docs/reference/agentos/behavior-spec.md` (mapping requirement)
- Traceability map: `docs/reference/agentos/traceability.md`
- Registry specification: `docs/reference/agentos/registry.md`
 - Registry maintenance: `docs/how-to/agentos/maintain-registry.md`

## 9. Self-improvement loop
- Gap capture: `docs/how-to/agentos/capture-gaps.md`
- Self-improvement system: `docs/reference/agentos/self-improvement.md`
- Improvement runbook: `docs/how-to/agentos/run-self-improvement-cycle.md`
- Problem registry: `docs/reference/agentos/problem-registry.md`
- ADRs and traceability: `docs/explanation/agentos/decisions/` and `docs/reference/agentos/traceability.md`
 - Alignment runbook: `docs/how-to/agentos/maintain-alignment.md`
