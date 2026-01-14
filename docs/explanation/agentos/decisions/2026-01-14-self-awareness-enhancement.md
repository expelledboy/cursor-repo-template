# Decision: Self-Awareness Enhancement

**Status**: Accepted
**Date**: 2026-01-14
**Scope**: agentos
**Problem IDs**: PRB-0002, PRB-0005
**Supersedes**: (none)

## Context

AgentOS operates as a behavioral framework that the agent must choose to follow, but lacks continuous self-monitoring and self-assessment capabilities. While meta-analysis mode (MAM) provides deep self-audit, there is no continuous self-awareness during normal task execution. This limits the agent's ability to:

- Detect state inconsistencies early
- Monitor contract compliance continuously
- Assess objective alignment during execution
- Identify gaps as they emerge
- Reflect on performance and outcomes

Self-awareness would enhance the agent's ability to follow the framework and prevent issues related to context instability (PRB-0002) and rationale loss (PRB-0005).

## Decision

Enhance AgentOS with comprehensive self-awareness capabilities:

1. **Enhanced Self-Model**: Add meta-cognitive capabilities, self-monitoring checkpoints, and self-assessment mechanisms to the self-model.

2. **Self-Awareness Framework**: Create a new reference document defining self-awareness dimensions (state, contract, objective, evidence, performance, gap awareness), self-monitoring checkpoints (pre-execution, mid-execution, post-execution), self-reflection practices, and integration with self-improvement.

3. **Behavior Spec Integration**: Add self-awareness requirements to the behavior spec, requiring continuous self-monitoring and self-assessment at task boundaries.

4. **Self-Improvement Integration**: Update the self-improvement system to include continuous self-assessment as a required improvement event, with self-assessment outputs feeding into improvement cycles.

5. **Operating Model Extension**: Extend the DOE model to include Self-Awareness (SA) as a fourth dimension alongside Directive, Orchestration, and Execution.

## Alternatives

**Alternative 1: Keep MAM-only self-awareness**
- Pros: Simpler, no changes to normal task execution
- Cons: Self-awareness only available on-demand, gaps may be missed during execution

**Alternative 2: Add self-awareness only to meta-maintenance tasks**
- Pros: Focused on meta-tasks where self-awareness is most needed
- Cons: Doesn't help with normal task execution, misses opportunities for early gap detection

**Alternative 3: External monitoring only (no self-awareness)**
- Pros: No changes to agent behavior
- Cons: Relies entirely on external validation, no proactive gap detection or compliance monitoring

## Consequences

**Positive:**
- Agent can monitor its own state and compliance continuously
- Early detection of objective drift, contract violations, and gaps
- Better alignment with primary objectives through continuous assessment
- Self-assessment outputs feed into improvement cycles
- Enhanced ability to follow the AgentOS framework

**Negative:**
- Additional cognitive overhead during task execution (mitigated by structured checkpoints)
- Self-assessment is a tool, not a guarantee (must still rely on external validation)
- Requires discipline to apply checkpoints consistently

**Neutral:**
- Self-awareness enhances but does not replace external validation
- Self-assessment complements artifact verification
- No changes to core contracts, only adds monitoring capabilities

## Why this worked

Self-awareness is a natural extension of the self-improvement system and meta-analysis mode. It provides continuous monitoring that complements periodic deep audits (MAM) and improvement events (micro-AAR, retrospective, postmortem). The structured checkpoint approach ensures self-awareness is applied consistently without being overly burdensome. Self-awareness dimensions align with existing AgentOS concerns (state, contracts, objectives, evidence, performance, gaps), making integration natural.

The enhancement addresses PRB-0002 (Context Instability) by monitoring state and evidence continuously, and PRB-0005 (Rationale Loss) by ensuring contract compliance and gap capture. Self-awareness enables the agent to better choose to follow the framework, addressing the fundamental constraint that AgentOS is a framework the agent must choose to follow.

## Artifacts
- `docs/reference/agentos/self-model.md` (enhanced with self-awareness capabilities)
- `docs/reference/agentos/self-awareness-framework.md` (new reference document)
- `docs/reference/agentos/behavior-spec.md` (added self-awareness requirements)
- `docs/reference/agentos/self-improvement.md` (added continuous self-assessment)
- `docs/index.md` (added self-awareness framework reference)
- `docs/reference/agentos/traceability.md` (updated with this ADR)
