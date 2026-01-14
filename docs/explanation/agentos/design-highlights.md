# AgentOS Design Highlights

**Status**: Stable
**Date**: 2026-01-13
**Purpose**: Curated explanation of core design decisions and their rationale.

---

## 1. Design goals
- Reduce goal drift in multi-step tasks.
- Make context loading explicit and auditable.
- Resolve requirement ambiguity before execution.
- Tie verification to explicit gates aligned with CI.
- Preserve rationale through durable artifacts.
- Enable portability with explicit bootstrap gates.

## 2. Core mechanisms
- Task lifecycle sequence with required outputs.
- Routing model that declares required directives and allowed domains.
- Context compass that constrains doc types by task intent.
- Primary vs Derived requirement classification with user confirmation on ambiguity.
- Truth surface ordering for evidence and conflict resolution.
- Verification contract with explicit gate listing and non-truncated outputs.
- Self-improvement loop that promotes gaps to problems, ADRs, and traceability.
- Safety policy with destructive confirmation and least privilege.
- Registry mapping with deterministic validation expectations.
- Bootstrap runbook and exit criteria for new repos.
- Meta-questions for alignment and conscience checks.

## 3. Tradeoffs
- More up-front planning and documentation.
- More explicit structure per task.
- Slower starts, fewer regressions.

## 4. Decision links
- PRB-0001: `2026-01-13-task-lifecycle.md`; `2026-01-13-primary-objective-control.md`
- PRB-0002: `2026-01-13-context-loading-contract.md`; `2026-01-13-routing-model.md`; `2026-01-13-routing-spec.md`; `2026-01-13-truth-surface.md`; `2026-01-13-cursor-mechanics.md`; `2026-01-13-adapter-interface.md`
- PRB-0003: `2026-01-13-ambiguity-resolution.md`; `2026-01-13-truth-surface.md`
- PRB-0004: `2026-01-13-verification-contract.md`; `2026-01-13-verification-contract-ref.md`
- PRB-0005: `2026-01-13-self-improvement-loop.md`; `2026-01-13-core-purpose-scope.md`; `2026-01-13-hybrid-rationale-system.md`; `2026-01-13-architecture-model.md`; `2026-01-13-meta-questions.md`
- PRB-0006: `2026-01-13-routing-drift-controls.md`
- PRB-0007: `2026-01-13-registry-mapping-requirement.md`; `2026-01-13-registry-spec.md`; `2026-01-13-registry-enforcement.md`
- PRB-0008: `2026-01-13-destructive-action-confirmation.md`; `2026-01-13-safety-policy.md`
- PRB-0009: `2026-01-13-deterministic-execution.md`
- PRB-0010: `2026-01-13-taxonomy-drift-controls.md`
- PRB-0011: `2026-01-13-bootstrap-gates.md`
