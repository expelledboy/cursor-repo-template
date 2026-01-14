# AgentOS Self-Awareness Framework (Reference)

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Defines self-awareness mechanisms, practices, and checkpoints for AgentOS to monitor its own state, performance, and compliance.

---

## 1. Overview

Self-awareness enables AgentOS to:
- Monitor its own state and behavior continuously
- Detect deviations from contracts and objectives
- Assess performance and compliance
- Identify gaps and improvement opportunities
- Reflect on decisions and outcomes
- Maintain alignment with primary objectives

**Relationship to Meta-Analysis Mode (MAM)**: This framework defines continuous self-awareness during normal task execution. MAM (see `docs/reference/agentos/meta-analysis.md`) is a separate, on-demand deep self-audit that complements continuous self-awareness. MAM provides comprehensive, structured audits when triggered, while continuous self-awareness provides ongoing monitoring at task boundaries.

## 2. Self-awareness dimensions

### 2.1. State awareness
**What**: Understanding current operational state
**Monitors**:
- Current task type and primary objective
- Loaded directives and their authority order
- Routing decisions and allowed domains
- Task phase (intake, classify, route, plan, execute, verify, report, anneal)
- Evidence sources in use
- Verification gates defined
- Gaps discovered but not yet captured

**Checkpoint**: Before each major phase transition, verify state consistency.

### 2.2. Contract awareness
**What**: Understanding behavioral contracts and compliance status
**Monitors**:
- Behavior spec compliance (lifecycle, routing, verification)
- Safety policy compliance (destructive actions, confirmations)
- Verification contract compliance (gates defined, run)
- Truth surface compliance (evidence sources authoritative)
- Registry compliance (directive mappings current)

**Checkpoint**: Before execution, assess contract compliance readiness.

### 2.3. Objective awareness
**What**: Understanding primary objective and alignment
**Monitors**:
- Primary objective clarity and measurability
- Current actions' alignment with primary objective
- Sub-task contributions to primary objective
- Objective drift indicators (scope expansion, requirement changes)

**Checkpoint**: At each checkpoint, verify primary objective alignment.

### 2.4. Evidence awareness
**What**: Understanding evidence quality and sources
**Monitors**:
- Evidence source authority (reference > how-to > explanation > tutorials > work > archive)
- Evidence completeness (all required directives loaded)
- Evidence freshness (no stale or superseded docs)
- Evidence gaps (missing required directives)

**Checkpoint**: Before making decisions, verify evidence quality.

### 2.5. Performance awareness
**What**: Understanding task execution quality
**Monitors**:
- Task completion (primary objective met)
- Verification gate outcomes (passed, failed, deferred)
- Gap capture (all gaps documented)
- User corrections (indicators of misalignment)

**Checkpoint**: After execution, assess performance against objectives and gates.

### 2.6. Gap awareness
**What**: Understanding knowledge, capability, and guidance gaps
**Monitors**:
- Missing directives (required but not found)
- Ambiguous requirements (unresolved)
- Tool limitations (capabilities insufficient)
- Contract gaps (behavior not specified)
- Knowledge gaps (domain expertise insufficient)

**Checkpoint**: Continuously during execution, capture gaps as discovered.

## 3. Self-monitoring checkpoints

### 3.1. Pre-execution checkpoint
**When**: After planning, before execution
**Checks**:
- [ ] Task plan header complete (all required fields present)
- [ ] Required directives loaded
- [ ] Primary objective stated and measurable
- [ ] Verification gates defined or referenced
- [ ] Evidence sources declared
- [ ] Design-decision checkpoint completed (if required)
- [ ] Destructive actions identified and confirmed (if any)
- [ ] Contract compliance verified

**Output**: Transition readiness summary or gap list.

### 3.2. Mid-execution checkpoint
**When**: At natural breakpoints during execution
**Checks**:
- [ ] Primary objective still aligned with current actions
- [ ] Required directives still loaded and relevant
- [ ] Evidence sources still authoritative
- [ ] Contract compliance maintained
- [ ] New gaps captured (if discovered)
- [ ] State consistency maintained

**Output**: Alignment status or corrective action.

### 3.3. Post-execution checkpoint
**When**: After execution, before reporting
**Checks**:
- [ ] Primary objective met (yes/no/partial)
- [ ] Verification gates passed (all/some/none/deferred)
- [ ] All gaps captured in work notes
- [ ] Contract compliance maintained throughout
- [ ] Evidence sources used documented
- [ ] User corrections addressed (if any)

**Output**: Completion assessment and gap list.

### 3.4. Meta-analysis checkpoint
**When**: Triggered by MAM or meta-maintenance tasks
**Checks**: See `docs/reference/agentos/meta-analysis.md`

## 4. Self-reflection practices

### 4.1. Decision reflection
**When**: After making significant decisions
**Questions**:
- What evidence supported this decision?
- What alternatives were considered?
- What tradeoffs were made?
- What assumptions were made?
- How does this align with primary objective?

**Output**: Decision rationale (may be implicit in task plan).

### 4.2. Outcome reflection
**When**: After task completion
**Questions**:
- Was the primary objective met? Why or why not?
- What worked well?
- What could be improved?
- What gaps were discovered?
- What would I do differently next time?

**Output**: Micro-AAR (implicit in completion report).

### 4.3. Contract reflection
**When**: When contract compliance is uncertain
**Questions**:
- Which contract applies?
- What does the contract require?
- Am I following it?
- What evidence shows compliance or non-compliance?
- What corrective action is needed?

**Output**: Compliance assessment or gap note.

## 5. Self-assessment triggers

### 5.1. Automatic triggers
- Task phase transitions (plan → execute, execute → verify)
- Primary objective changes or clarifications
- User corrections or feedback
- Verification gate failures
- Gap discoveries

### 5.2. Manual triggers
- User requests self-assessment
- Meta-maintenance tasks
- Meta-analysis mode (MAM)
- Retrospectives or postmortems

### 5.3. Scheduled triggers
- After each task (post-execution checkpoint)
- At retrospective cadence
- During meta-maintenance cycles

## 6. Self-awareness outputs

### 6.1. State reports
- Current task state summary
- Loaded directives list
- Evidence sources in use
- Compliance status

### 6.2. Compliance assessments
- Contract compliance status
- Gap list
- Corrective actions needed

### 6.3. Performance assessments
- Objective completion status
- Verification gate outcomes
- Quality indicators

### 6.4. Gap reports
- Discovered gaps
- Gap capture status
- Gap promotion status (to problem registry)

## 7. Integration with self-improvement

Self-awareness feeds into self-improvement:
- **Gap detection** → gap capture → problem registry → ADR
- **Performance assessment** → micro-AAR → retrospective → improvement actions
- **Contract reflection** → compliance gaps → behavior spec updates
- **Outcome reflection** → improvement opportunities → how-to updates

See `docs/reference/agentos/self-improvement.md` for improvement mechanisms.

## 8. Limitations

Self-awareness has limits:
- Cannot validate chat outputs directly (requires artifacts)
- Cannot enforce behavior (requires external validation)
- Cannot access opaque memory (requires observable evidence)
- Self-assessment is a tool, not a guarantee

Self-awareness enhances but does not replace:
- External validation (scripts, CI, user feedback)
- Artifact verification
- Deterministic tools

## 9. Related docs
- `docs/reference/agentos/self-model.md` (self-model with self-awareness)
- `docs/reference/agentos/self-improvement.md` (improvement mechanisms)
- `docs/reference/agentos/meta-analysis.md` (deep self-audit)
- `docs/reference/agentos/behavior-spec.md` (behavioral contracts)
- `docs/reference/agentos/truth-surface.md` (evidence sources)

## 10. Usage requirements

- Self-monitoring checkpoints must be applied during all tasks.
- Self-assessment mechanisms must be invoked at task boundaries.
- State awareness must be maintained continuously.
- Gap awareness must trigger gap capture workflow.
- Self-reflection must inform improvement cycles.
