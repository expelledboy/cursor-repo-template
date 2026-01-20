# AgentOS Validation Contract (Reference)

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Defines the validation invariants that ensure AgentOS coherence.

---

## 1. Validation Principles

The validation contract provides deterministic, automated checks that coherence is maintained across all surfaces. Validation is:

- **Deterministic**: Same inputs always produce same results
- **Automated**: Runs without human intervention where possible
- **Comprehensive**: Covers all coherence invariants
- **Actionable**: Provides clear pass/fail with remediation guidance
- **Integrated**: Runs at appropriate points in task and evolution lifecycles

## 2. Validation Types

### 2.1. Static Validation
Checks that can run without execution:
- Registry completeness and accuracy
- Traceability link validity
- Documentation structure compliance
- Configuration consistency

### 2.2. Dynamic Validation
Checks that require execution or observation:
- Behavior contract compliance
- Verification gate execution
- Self-awareness checkpoint completion
- Evolution protocol adherence

### 2.3. Continuous Validation
Ongoing checks during operation:
- Coherence metric monitoring
- Gap detection and capture
- Self-assessment execution
- Authority order enforcement

## 3. Validation Triggers

### 3.1. Task-Based Triggers
- **Pre-execution**: Validate task plan coherence
- **Mid-execution**: Check behavior alignment
- **Post-execution**: Verify outcomes and capture gaps
- **Gate execution**: Run verification checks

### 3.2. Evolution-Based Triggers
- **Pre-change**: Validate starting coherence
- **Post-change**: Confirm maintained coherence
- **ADR creation**: Validate decision completeness
- **Traceability updates**: Check link accuracy

### 3.3. Scheduled Triggers
- **Daily**: Registry and traceability validation
- **Weekly**: Comprehensive coherence assessment
- **Milestone**: Full system validation

## 4. Evolution Events

### 4.1. Micro-AAR (After Action Review)
**Trigger**: After every task completion
**Purpose**: Capture task-level insights and coherence gaps
**Process**:
- Review task execution against coherence invariants
- Document any detected gaps
- Assess improvement opportunities
- Update work notes with findings

### 4.2. Retrospective
**Trigger**: Scheduled cadence (weekly/monthly) or milestone completion
**Purpose**: Review patterns across multiple tasks
**Process**:
- Analyze coherence metrics trends
- Identify systemic gaps or opportunities
- Validate problem hypotheses
- Plan improvement initiatives

### 4.3. Postmortem
**Trigger**: High-impact failures or repeated issues
**Purpose**: Deep analysis of significant coherence breakdowns
**Process**:
- Root cause analysis of failure
- Impact assessment across all surfaces
- Prevention strategy development
- ADR creation for systemic fixes

### 4.4. Meta-Analysis Mode (MAM)
**Trigger**: AgentOS validation failures or destructive action requests
**Purpose**: Comprehensive self-audit using visible context only
**Process**:
- Checklist-based coherence assessment
- Gap identification and documentation
- Self-improvement recommendations

## 5. Validation Output Standards

All validation must provide:

- **Clear Pass/Fail Status**: Binary determination
- **Detailed Error Messages**: Specific violations identified
- **Remediation Guidance**: How to fix issues
- **Evidence Links**: References to failing artifacts
- **Severity Levels**: Critical, Warning, Info
- **Execution Metadata**: Runtime, scope, version

## 6. Validation Integration

### 6.1. Task Lifecycle Integration
- **Intake**: Validate task type and scope coherence
- **Classify**: Check taxonomy alignment
- **Route**: Validate domain and directive selection
- **Plan**: Verify plan completeness and coherence
- **Execute**: Monitor behavior contract compliance
- **Verify**: Run verification gates
- **Report**: Validate outcome documentation
- **Anneal**: Check gap capture completeness

### 6.2. Evolution Integration
- **Gap Detection**: Validate gap documentation completeness
- **Work Note Creation**: Check required fields and evidence
- **Problem Validation**: Verify registry entry completeness
- **ADR Creation**: Validate format and completeness
- **Implementation**: Check coherence maintenance
- **Traceability Update**: Validate link accuracy
- **Validation**: Run comprehensive checks

### 6.3. Self-Monitoring Integration
- **Pre-execution**: Validate readiness against coherence contracts
- **Mid-execution**: Check ongoing alignment
- **Post-execution**: Assess outcome coherence
- **Meta-analysis**: Comprehensive self-audit

## 7. Evolution Metrics

Track evolution effectiveness through:

- **Gap Resolution Rate**: Percentage of detected gaps that are resolved
- **Evolution Cycle Time**: Time from gap detection to validation
- **Coherence Drift**: Rate of coherence metric degradation
- **Rationale Preservation**: Percentage of constraints with current reasoning
- **Validation Coverage**: Percentage of evolution events with validation

## 8. Validation Boundaries

### 8.1. Validation Scope
- Documentation structure and content
- Implementation↔documentation mapping
- Behavior contract compliance
- Evolution protocol adherence
- Self-monitoring effectiveness

### 8.2. Validation Limits
- Cannot validate unobservable behavior
- Cannot enforce compliance without artifacts
- Cannot detect all coherence issues automatically
- Requires human judgment for complex coherence calls

## 9. Validation Dependencies

Validation relies on:

- **Registry**: For scope definition and mapping
- **Traceability**: For problem-decision-artifact links
- **Truth Surfaces**: For evidence hierarchy
- **Self-Awareness**: For runtime coherence monitoring
- **Evolution Framework**: For validation system improvement

## 10. Implementation Requirements

To implement validation:

- **Contract Adherence**: Follow validation invariants
- **Output Standardization**: Consistent error formats
- **Documentation**: Clear scope and remediation guidance
- **Testing**: Validation of validation systems themselves
- **Maintenance**: Evolution through improvement protocol

## 11. Validation Assurance

Validation quality is assured through:

- **Self-Validation**: Systems that validate other systems
- **Cross-Validation**: Multiple checks for same invariants
- **Human Oversight**: Review of validation outputs
- **Evolution Tracking**: Validation improvements tracked
- **Failure Analysis**: Root cause analysis of validation misses

## 12. Related Contracts

- `coherence-contract.md`: Defines what validation must enforce
- `evolution-framework.md`: Governs validation system evolution
- `architectural-patterns.md`: Implementation patterns for validation
- `alignment-mechanisms.md`: Operational validation implementations