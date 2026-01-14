# AgentOS Behavior Specification

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Defines non-negotiable behavior constraints for AgentOS (Reference/Contract).

---

## 1. Normative keywords
- **Must**: mandatory requirement.
- **Must not**: prohibited action.
- **May**: permitted action that is optional.

## 2. Scope
- Applies to all agent tasks in this repository.
- Applies regardless of IDE or tool adapter.

## 3. Authority order
- reference -> how-to -> explanation -> tutorials -> work -> archive.
- If two docs in the same tier conflict, the superseding doc wins; if none exists, the newest doc wins.

## 4. Task lifecycle
- The agent must follow this sequence: intake -> classify -> route -> plan -> execute -> verify -> report -> anneal.
- Intake must capture the task request in one sentence.
- Classify must assign a task type from the taxonomy.
- Route must identify required directives and allowed domains.
- Plan must include the task plan header and checkpoints.
- The agent must draft the task plan header and only ask the user to confirm missing or ambiguous fields.
- Execute must not start until required directives are loaded.
- Execute must not start until any required design-decision checkpoint is completed.
- Verify must not be skipped; if gates cannot run, list commands and expected outcomes.
- Report must state whether the primary objective is met and whether gates passed or were deferred.
- Anneal must record any gaps as work notes when discovered.
- Local state (`docs/local/state/`) may be used for active task tracking but is non-evidence; promote only decision summaries that affect future work and gaps that require contract/process changes.
- All 8 steps must be completed for all tasks, regardless of complexity level.
- workflow variations adjust rigor/documentation by complexity level (see `docs/reference/agentos/workflow-variations.md`).
- Complexity level must be determined during classify and recorded in the task plan header.
- Workflow variations must be applied according to the mapped level (workflow-variations reference).

```mermaid
graph TD
    start[Task Request] --> intake[Intake: capture request in one sentence]
    intake --> classify[Classify: assign task type]
    classify --> route[Route: select directives and allowed domains]
    route --> plan[Plan: create task plan header and checkpoints]
    plan --> checkDD{Design decision required?}
    checkDD -->|Yes| design[Design decision checkpoint: document options and rationale]
    checkDD -->|No| checkDir{Required directives loaded?}
    design --> checkDir
    checkDir -->|No| loadDir[Load required directives]
    loadDir --> execute[Execute: implement with deterministic tools]
    checkDir -->|Yes| execute
    execute --> verify[Verify: run gates or list commands]
    verify --> report[Report: state objective met and gates passed/deferred]
    report --> anneal[Anneal: record gaps as work notes]
    anneal --> end[Task complete]
```

> **Note:** This diagram is supplementary. The authoritative contract is in Section 4: Task lifecycle above. See `docs/reference/agentos/behavior-spec.md#4-task-lifecycle` for complete requirements.

## 5. Primary objective control
- Each task must state a single primary objective before execution.
- The task plan must restate the primary objective at each checkpoint.
- The completion report must state whether the primary objective is met.
- If multiple primary objectives exist, the agent must ask the user to prioritize or split the task.

## 6. Task taxonomy
- Discovery & Requirements
- Planning & Estimation
- Design & Architecture
- Implementation / Feature Build
- Testing & Verification
- Release & Deployment
- Operations & Maintenance
- Security & Compliance
- Documentation & Knowledge
- Refactoring & Tech-Debt
- Incident Response & Debugging
- AgentOS Meta-Maintenance

## 7. Task taxonomy changes
- Additions or changes must update this file, `docs/reference/agentos/traceability.md`, and an ADR.

## 8. Routing model
- Routing must select required directives and allowed domains based on task type and primary objective.
- Routing must not include domains outside the allowed set.
- Routing decisions must be recorded in the task plan header.
- The task plan must include a routing check confirming the selected domain matches the task type.
- Routing must respect the context compass in `docs/reference/agentos/context-compass.md`.

## 9. Requirement classification
- All requirements must be labeled **Primary** or **Derived**.
- When classification is uncertain, the agent must ask the user before proceeding.
- Resolved ambiguities must be recorded in canonical docs.

## 10. Context loading contract
- Each task must declare task type, primary objective, required directives, allowed domains, and evidence sources.
- The task plan must include a header with these declarations.
- The agent must load required directives before execution.
- Directive loading plan must use tiered format (see Context Compass tiers):
  - Tier 1 (Core): list loaded
  - Tier 2 (Task-type): list loaded
  - Tier 3 (Complexity): list loaded with level (e.g., level-appropriate gates/templates)
  - Tier 4 (Phase): list loaded with trigger
  - Tier 5 (Specialized): list loaded with trigger
  - Deferred: list with explicit, auditable triggers
  - Context usage: optional estimate/status (Low/Medium/High or percentage if known)
  - Minimal mode: yes/no if minimal mode used (see `docs/reference/agentos/context-compass.md` Section 5.4)
- The agent must record which directives were used in the response.
- Opaque memories are not authoritative sources of truth and may be used only as hints.
- Evidence sources must follow `docs/reference/agentos/truth-surface.md` and be listed in the header.
- Context window monitoring is optional guidance; selective loading by tier is the primary mechanism for context efficiency.

## 11. Task plan header requirements
The task plan header must include:
- Task type.
- Primary objective.
- Complexity level (1-4) with rationale and determination criteria.
- Workflow variation (Level 1-4) with rigor level for each lifecycle step.
- Complexity escalation record (if applicable): initial level, final level, escalation trigger, escalation point, user confirmation.
- Required directives.
- Allowed domains.
- Directive loading plan (loaded vs deferred + triggers).
- Design-decision checkpoint status varies by complexity level:
  - Level 1-2: Optional (only if material design/architecture decision exists)
  - Level 3-4: Mandatory (document decision or explain why not needed with rationale)
  - All checkpoints must use structured exploration phases from `docs/reference/agentos/structured-exploration.md` and the template from `docs/reference/agentos/design-decision-templates.md` for the corresponding level.
  - See `docs/how-to/agentos/design-decision-structured-exploration.md` for step-by-step guidance.
- Transition readiness summary before execution (key decisions, dependencies, risks, verification focus).
- Evidence sources.
- Verification gates.

Example (concise):
```
Complexity Level: 2
Rationale: Multiple components, simple decision, moderate risk, effort=days, deps=few
Determination Criteria: Scope=Multiple; Decisions=Simple; Risk=Moderate; Effort=Days; Dependencies=Few
Workflow Variation: Level 2 (standard rigor across 8 steps)
Complexity Escalation: None
Design-Decision Checkpoint: Optional (no material decisions)
Directive Loading Plan:
  - Tier 1 (Core): behavior-spec, architecture, routing, context-compass
  - Tier 2 (Task-type): verification-contract
  - Tier 3 (Complexity): verification-gates (Level 2)
  - Deferred: design-decision-templates (trigger: if design decision needed)
  - Context usage: Medium
  - Minimal mode: no
```

## 11.1. Design-decision checkpoint requirements

When a design-decision checkpoint is required, use structured exploration phases from `docs/reference/agentos/structured-exploration.md`. See `docs/how-to/agentos/design-decision-structured-exploration.md` for step-by-step guidance:

**Level 1-2 (Optional Structured Exploration):**
- If design decision exists, use brief structured exploration
- Phases 1-4 recommended (brief), Phase 5 optional
- Phase outputs may be concise
- Structured exploration is optional (only if design decision exists)

**Level 3-4 (Mandatory Structured Exploration):**
- All 5 phases are mandatory when material design decision exists
- Phase 1: Component Breakdown (required)
- Phase 2: Option Exploration (required, 2-4 options)
- Phase 3: Trade-off Analysis (required, tabular format)
- Phase 4: Decision Documentation (required)
- Phase 5: Decision Verification (required)
- If no material decision exists, document rationale for skipping structured exploration

All phases must produce documented outputs that are preserved in the checkpoint document. Phase outputs integrate with design-decision templates from `docs/reference/agentos/design-decision-templates.md`.

## 12. Adapter interface
- IDE-specific routing rules may load context but must not change core behavior or override this spec.
- Adapters must map their routing or context outputs to the task plan header.

## 13. Execution discipline
- Must use deterministic tools (task runner, scripts, CI) when available.
- Rule of two: if the same ad-hoc command is needed twice for the same task type, it must be promoted to a deterministic tool.

## 14. Verification contract
- Every task must define or reference verification gates.
- Gates must align with CI as the minimum standard.
- If gates cannot be run, list exact commands and expected outcomes.
- Verification output must not be truncated.
- Verification rules are defined in `docs/reference/agentos/verification-contract.md`.
- If a gate catalog exists, use `docs/reference/agentos/verification-gates.md`.

## 15. Self-improvement loop
- When a gap is discovered, the agent must create a work note describing the gap.
- Validated gaps must be promoted to the problem registry and ADRs.
- Core updates must update traceability.
- The improvement mechanisms are defined in `docs/reference/agentos/self-improvement.md`.
- When task type is **AgentOS Meta-Maintenance**, load `docs/reference/agentos/self-model.md`.
- Bootstrap mode must follow `docs/how-to/agentos/bootstrap-repo.md` and exit criteria in `docs/reference/agentos/bootstrap-gates.md`.
- Local state remains ephemeral; promote only decision summaries that affect future work and gaps that require contract/process changes (see `docs/reference/agentos/state-surface.md`).

## 15.1. Self-awareness requirements
- The agent must continuously monitor its own state, compliance, and performance during task execution.
- Self-monitoring checkpoints must be applied at task boundaries (pre-execution, mid-execution, post-execution).
- The agent must assess state awareness (task phase, directives, evidence), contract awareness (compliance status), objective awareness (alignment), evidence awareness (quality), performance awareness (completion quality), and gap awareness (discoveries).
- Self-assessment outputs must inform improvement events and gap capture.
- Self-awareness mechanisms are defined in `docs/reference/agentos/self-awareness-framework.md`.
- The self-model defines self-awareness capabilities in `docs/reference/agentos/self-model.md`.

## 16. Destructive actions
- Destructive actions must not be executed without explicit user confirmation.
- Safety constraints are defined in `docs/reference/agentos/safety-policy.md`.

## 17. Registry mapping
- Files that require documentation must have a documented directive mapping.
- Mapping changes must be recorded in canonical docs.
- The registry protocol is defined in `docs/reference/agentos/registry.md`.

## 18. Drift and governance
- Changes to core behavior must include an ADR using `docs/reference/agentos/decision-record-format.md`.
- The traceability map must be updated for every ADR.

## 19. Core purpose and non-goals
- Purpose: enforce deterministic task behavior and preserve rationale for evolution.
- Non-goal: replace domain-specific expertise or project-specific policies.

## 20. Definitions
- Checkpoint: a named step in the task plan.
- Required directives: the minimal doc set needed to execute the task.
- Allowed domains: the domains the agent is permitted to use for the task.
- Verification gate: a runnable check that defines pass or fail for the task.
- Task plan header: the first plan section that lists required declarations.
- Evidence sources: the artifacts used to justify decisions, ordered by `docs/reference/agentos/truth-surface.md`.
- Complexity level: a 1-4 scale used to match plan rigor and verification to task scope.
- Design-decision checkpoint: required documentation of options, tradeoffs, and a chosen approach when design or architecture decisions are material. Must use structured exploration phases from `docs/reference/agentos/structured-exploration.md`.
- Transition readiness summary: concise statement of outstanding decisions, dependencies, risks, and verification focus before execution.
- Self-awareness: continuous monitoring of state, compliance, performance, and gaps during task execution.
- Self-monitoring checkpoint: a structured self-assessment at task boundaries (pre-execution, mid-execution, post-execution).
