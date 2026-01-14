# AgentOS Research Notes

**Status**: Draft
**Date**: 2026-01-13
**Purpose**: Capture non-authoritative research and context that informed AgentOS decisions.

---

## 1. Sources (summary only)
- ReAct: reasoning and action interleaving improves task reliability and interpretability.
- Plan-and-Solve: explicit planning before execution reduces missing-step errors.
- Reflexion: explicit reflection notes improve subsequent attempts without retraining.
- Tree of Thoughts: branching exploration can help complex tasks but increases cost.
- SWE-bench Verified: fail-to-pass and pass-to-pass testing highlight verification rigor.
- Cursor rules and memories: rule-based context loading exists; memories are opaque and not controllable by the agent.

## 2. Extracted lessons
- Explicit plan -> act -> verify sequencing reduces goal drift.
- Deterministic execution and explicit gates reduce variance and regressions.
- Rationale must be written into durable artifacts, not stored in hidden memory.
- Branching should be optional and user-approved for cost and clarity.
- Context must be explicit and auditable; opaque memories are not authoritative.

## 3. Mapping to problems
- PRB-0001: lifecycle sequencing and objective checkpoints address goal drift.
- PRB-0002: explicit directive loading and routing address context instability.
- PRB-0003: ambiguity checks and user confirmation reduce misinterpretation.
- PRB-0004: verification gates aligned with CI address gate decay.
- PRB-0005: ADRs and traceability preserve rationale across evolution.

## 4. Mapping to ADRs
- 2026-01-13-task-lifecycle.md -> ReAct, Plan-and-Solve.
- 2026-01-13-context-loading-contract.md -> Cursor rules and memory opacity.
- 2026-01-13-ambiguity-resolution.md -> requirement classification discipline.
- 2026-01-13-verification-contract.md -> SWE-bench Verified gate rigor.
- 2026-01-13-self-improvement-loop.md -> Reflexion and durable artifacts.
- 2026-01-13-adapter-interface.md -> Cursor adapter constraints.
- 2026-01-13-core-purpose-scope.md -> scope clarity to reduce rationale loss.

## 5. Notes
- This note is non-authoritative and must not be treated as a contract.
- New problems discovered here require separate drafts under `docs/work/agentos/problems/`.
