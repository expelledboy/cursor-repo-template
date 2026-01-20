---
title: "Self-Awareness Framework"
status: stable
created_date: 2026-01-18
purpose: "Defines self-awareness mechanisms for continuous monitoring during AgentOS task execution"
domain: agentos
---

# Self-Awareness Framework (Reference)

## Purpose
Defines self-awareness mechanisms that enable AgentOS to continuously monitor its own state, compliance, and performance during task execution. Self-awareness complements the `/retrospect` command's one-time audits with ongoing validation throughout the task lifecycle.

## Architectural Foundation

**Cognitive-First Design**: Self-awareness is fundamentally a cognitive capability that cannot be fully automated. While scripts provide guidance frameworks and checklists, the actual analysis and judgment must be performed by the AI agent within reasoning phases.

**Guidance vs Intelligence Boundaries**:
- **Guidance (Scripts/Automation)**: Structure, checklists, process frameworks, validation rules
- **Intelligence (AI Agent)**: Cognitive judgment, pattern recognition, authentic evaluation, meta-reasoning

## Self-Awareness Dimensions

### 1. State Awareness
**What**: Understanding current operational state and context
**Monitors**:
- Current task phase (intake, classify, route, plan, execute, verify, report, anneal)
- Loaded directives and their authority levels
- Routing decisions and allowed domains
- Evidence sources in use and their quality
- Verification gates defined and their status

**Implementation**: Tracked throughout task execution, reported in `/retrospect` self-monitoring checkpoint

### 2. Contract Awareness
**What**: Compliance with behavioral contracts and safety policies
**Monitors**:
- DOE (Directive-Orchestration-Execution) flow adherence
- Task lifecycle sequence completion
- Safety policy compliance (destructive action confirmations)
- Verification contract fulfillment
- Registry mapping validity

**Implementation**: Continuous validation during execution, hard blocks for critical violations

### 3. Objective Awareness
**What**: Alignment between current actions and primary objective
**Monitors**:
- Primary objective clarity and measurability
- Current task actions' contribution to objective
- Objective drift indicators (scope expansion, requirement changes)
- Progress toward measurable completion criteria

**Implementation**: Checkpoint validation at phase transitions, early warning for drift

### 4. Evidence Awareness
**What**: Quality and authority of evidence sources used
**Monitors**:
- Evidence source authority hierarchy compliance
- Evidence completeness for decision type
- Evidence freshness and applicability
- Source accessibility and integrity

**Implementation**: Integrated into `/retrospect` evidence quality checks, warning thresholds for low-authority sources

### 5. Performance Awareness
**What**: Task execution quality and outcomes
**Monitors**:
- Primary objective completion status
- Verification gate pass/fail rates
- Gap capture completeness
- User correction frequency (alignment indicators)
- Execution efficiency and resource usage

**Implementation**: Post-execution assessment, performance trend analysis

### 6. Gap Awareness
**What**: Identification and capture of missing capabilities or knowledge
**Monitors**:
- Missing directives or tools for task requirements
- Knowledge gaps in domain understanding
- Process gaps in task execution
- Tool capability limitations
- Documentation completeness gaps

**Implementation**: Continuous monitoring with `/learn` command integration for gap capture

## Self-Monitoring Checkpoints

### Pre-Execution Checkpoint
**When**: After planning, before execution begins
**Validates**:
- ✅ Task plan header complete and valid
- ✅ Required directives loaded and accessible
- ✅ Primary objective clear and measurable
- ✅ Verification gates defined for task type
- ✅ Evidence sources identified with appropriate authority
- ✅ Destructive actions confirmed (if any)
- ✅ Safety compliance verified

**Implementation**: Built into `/retrospect` as primary audit function

### Mid-Execution Checkpoint
**When**: At natural breakpoints during execution
**Validates**:
- ✅ Objective alignment maintained
- ✅ Required directives still relevant
- ✅ Evidence sources remain authoritative
- ✅ Contract compliance sustained
- ✅ New gaps captured and addressed

**Implementation**: Optional checkpoint, can be triggered manually or automatically

### Post-Execution Checkpoint
**When**: After execution, before reporting
**Validates**:
- ✅ Primary objective achieved (yes/no/partial)
- ✅ Verification gates passed/deferred
- ✅ All gaps captured in work notes
- ✅ Contract compliance maintained throughout
- ✅ Evidence sources used documented
- ✅ Performance metrics captured

**Implementation**: Automatic assessment, feeds into improvement processes

## Self-Reflection Practices

### Decision Reflection
**When**: After significant decisions or actions
**Questions**:
- What evidence supported this action?
- What alternatives were considered?
- How does this align with primary objective?
- What assumptions were made?
- What risks were identified?

### Outcome Reflection
**When**: After task phase completion
**Questions**:
- Was the phase objective met?
- What worked well in this phase?
- What could be improved?
- What new gaps emerged?
- What would be done differently?

### Contract Reflection
**When**: When contract compliance is uncertain
**Questions**:
- Which contract applies to this situation?
- What does the contract require?
- Is compliance being maintained?
- What evidence shows compliance?
- What corrective action is needed?

## Self-Awareness Integration

### With `/retrospect` Command
- Self-awareness dimensions reported in monitoring checkpoint
- Contract compliance status displayed
- Gap awareness triggers improvement suggestions

### With `/learn` Command
- Gap awareness automatically proposes `/learn` stubs
- Self-reflection outputs feed into gap documentation
- Performance awareness informs improvement prioritization

### With `/evolve` Command
- Self-assessment results guide improvement implementation
- Contract reflection identifies needed rule changes
- Outcome reflection validates improvement effectiveness

## Self-Awareness Limitations

### Boundaries
- **No External Validation**: Self-awareness enhances but doesn't replace external verification
- **Observable Evidence Only**: Cannot validate based on hidden memory or inaccessible information
- **Tool Enhancement**: Self-awareness improves agent behavior but doesn't guarantee correctness

### Enhancement Opportunities
- **Meta-Analysis Integration**: Self-awareness feeds MAM with context for deeper audits
- **Continuous Learning**: Self-awareness data improves future task execution
- **Performance Trending**: Historical self-awareness data identifies systemic issues

## Implementation Status

### Currently Implemented
- ✅ State awareness in `/retrospect` checklist
- ✅ Contract awareness with hard blocks for violations
- ✅ Evidence awareness with authority validation
- ✅ Gap awareness with automatic `/learn` suggestions
- ✅ Self-monitoring checkpoint in `/retrospect` output

### Future Enhancements (Phase 3)
- Mid-execution automatic checkpoints
- Self-awareness data persistence
- Performance trending and prediction
- Advanced gap detection algorithms

## Related
- `docs/reference/agentos/architecture.md#doe-integrated-flow`
- `docs/reference/agentos/task-plan-spec.md`
- `docs/reference/agentos/evidence-authority.md`
- `.cursor/commands/retrospect.md`