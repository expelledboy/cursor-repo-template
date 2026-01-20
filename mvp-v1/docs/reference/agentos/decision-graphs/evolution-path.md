# Evolution Path Decision Graph

**Purpose**: Route AgentOS meta-maintenance and evolution tasks to appropriate processes.

**Status**: Initial Version
**Date**: 2026-01-14

---

## Decision Tree

### Step 1: Check for Gap Detection
**Question**: Does this describe an incoherence gap or system limitation?

**If YES** → Route to: **Gap Capture Process**
- Create work note in `docs/work/agentos/YYYY-MM-DD-<slug>.md`
- Load: `docs/reference/agentos/evolution-framework.md` (gap detection section)
- Follow: Gap → Work Note → Problem Validation → ADR lifecycle
- Confidence: 0.95
- **Stop here**

**If NO** → Proceed to Step 2

---

### Step 2: Check for Problem Validation
**Question**: Is this a validated systemic problem requiring registry entry?

**If YES** → Route to: **Problem Registry Process**
- Check if problem already exists in registry
- If new, assign PRB-XXXX ID
- Update problem registry
- Load: `docs/reference/agentos/evolution-framework.md` (problem registry section)
- Confidence: 0.90
- **Stop here**

**If NO** → Proceed to Step 3

---

### Step 3: Check for Improvement Idea
**Question**: Does this propose a system improvement or enhancement?

**If YES** → Route to: **ADR Creation Process**
- Create ADR in `docs/explanation/agentos/decisions/YYYY-MM-DD-<slug>.md`
- Follow structured exploration (if Level 3-4)
- Load: `docs/reference/agentos/evolution-framework.md` (ADR format section)
- Confidence: 0.85
- **Stop here**

**If NO** → Proceed to Step 4

---

### Step 4: Check for Single-Loop Change
**Question**: Is this a fix within existing coherence contracts?

**If YES** → Route to: **Direct Implementation**
- Implement directly without ADR requirement
- Update documentation if needed
- Run validation to confirm coherence maintained
- Load: `docs/reference/agentos/evolution-framework.md` (single-loop changes section)
- Confidence: 0.90
- **Stop here**

**If NO** → Proceed to Step 5

---

### Step 5: Check for Double-Loop Change
**Question**: Does this change the coherence contracts themselves?

**If YES** → Route to: **Full ADR Lifecycle**
- Requires full ADR lifecycle (mandatory)
- Problem validation first
- Structured exploration (Level 3-4)
- Traceability update required
- Load: `docs/reference/agentos/evolution-framework.md` (double-loop changes section)
- Confidence: 0.95
- **Stop here**

**If NO** → Route to: **General AgentOS Work**
- Treat as general AgentOS maintenance
- Follow standard task workflow
- Load: `docs/reference/agentos/alignment-mechanisms.md`
- Confidence: 0.70

---

## Evolution Lifecycle Reference

```
Gap Detection → Work Note → Problem Validation → ADR Creation → Implementation → Traceability Update → Validation
```

### Gap Detection
- **Trigger**: Incoherence detected
- **Output**: Work note with gap description
- **Location**: `docs/work/agentos/`

### Problem Validation
- **Trigger**: Gap represents systemic issue
- **Output**: Problem registry entry (PRB-XXXX)
- **Location**: Problem registry in `docs/reference/agentos/evolution-framework.md`

### ADR Creation
- **Trigger**: Problem requires system change
- **Output**: Decision record with rationale
- **Location**: `docs/explanation/agentos/decisions/`

### Implementation
- **Process**: Update docs first, then implementation, then registry
- **Validation**: Run coherence checks

### Traceability Update
- **Process**: Link problem → decision → artifacts
- **Location**: Traceability map

---

## Single-Loop vs Double-Loop

### Single-Loop Changes (No ADR Required)
- Fix within existing contracts
- Examples:
  - Update validation script for better coverage
  - Improve documentation clarity
  - Add missing registry mappings
  - Refine work note templates

### Double-Loop Changes (ADR Required)
- Change the coherence contracts themselves
- Examples:
  - Modify core invariants
  - Add new coherence mechanisms
  - Change evolution protocols
  - Update authority order

---

## Examples

**Example 1**: "The task classification graph doesn't handle edge case X"
- **Route**: Gap Capture Process
- **Action**: Create work note describing the gap
- **Next**: Validate if systemic problem

**Example 2**: "We need to add a new validation type"
- **Route**: ADR Creation Process
- **Action**: Create ADR with structured exploration
- **Next**: Implement after ADR accepted

**Example 3**: "Fix typo in coherence contract"
- **Route**: Direct Implementation (single-loop)
- **Action**: Fix typo, no ADR needed
- **Next**: Validate change

**Example 4**: "Change authority order hierarchy"
- **Route**: Full ADR Lifecycle (double-loop)
- **Action**: Problem validation → ADR → implementation
- **Next**: Update traceability

---

## Integration with Task Classification

Evolution tasks are typically:
- **Task Type**: Meta-Maintenance
- **Complexity**: Usually Level 2-4 (system changes)
- **Workflow**: Enhanced rigor (comprehensive documentation)

---

## Related Decision Graphs

- **Task Classification**: Determines if task is evolution-related
- **Complexity Assessment**: Determines rigor level for evolution
- **Validation Strategy**: Determines how to validate evolution changes
