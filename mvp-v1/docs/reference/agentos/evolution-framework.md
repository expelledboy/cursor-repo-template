# AgentOS Evolution Framework (Reference)

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Defines the immutable contracts governing AgentOS evolution.

---

## 1. Evolution Principles

AgentOS evolution must maintain coherence across all surfaces while enabling improvement. The evolution framework ensures:

- **Rationale Preservation**: Design decisions retain their underlying reasoning
- **Structured Change**: Modifications follow defined processes
- **Traceability**: Changes are linked to the problems they solve
- **Validation**: Evolution outcomes are verified for coherence
- **Self-Sustainability**: The system can improve itself without external intervention

## 2. Evolution Lifecycle

Changes to AgentOS follow this structured lifecycle:

```
Gap Detection → Work Note → Problem Validation → ADR Creation → Implementation → Traceability Update → Validation
```

### 2.1. Gap Detection
**Trigger**: Incoherence detected during execution or validation
**Output**: Initial work note capturing the gap
**Requirements**:
- Document what is incoherent
- Note when and how it was detected
- Record immediate impact

### 2.2. Work Note Creation
**Location**: `docs/work/agentos/YYYY-MM-DD-<slug>.md`
**Format**:
```markdown
# Work Note: <Title>

**Status**: Draft
**Date**: YYYY-MM-DD
**Type**: gap | improvement | research
**Detected During**: <task or validation>

## Description
[What incoherence or opportunity was found]

## Evidence
[Links to artifacts, logs, or observations]

## Impact
[Why this matters for coherence]

## Initial Assessment
[Potential solutions or next steps]
```

### 2.3. Problem Validation
**Trigger**: Work note indicates systemic issue
**Process**:
1. Assess if gap represents validated problem
2. Check against existing problem registry
3. If new problem, assign PRB-XXXX ID
4. Update problem registry with new entry

**Problem Registry Entry Format**:
| ID | Title | Status | Scope | Statement | Evidence | Impact | Detection Signals |
|----|-------|--------|-------|-----------|----------|--------|------------------|

### 2.4. ADR Creation
**Trigger**: Problem requires system change
**Location**: `docs/explanation/agentos/decisions/YYYY-MM-DD-<slug>.md`
**Format**:
```markdown
# Decision: <Title>

**Status**: Proposed
**Date**: YYYY-MM-DD
**Scope**: agentos
**Problem IDs**: PRB-XXXX

## Context
[Why this decision is needed]

## Decision
[What was decided]

## Alternatives
[Other options considered]

## Consequences
[Impact of this decision]

## Why this worked
[Evidence and reasoning]

## Artifacts
[Files/docs affected]
```

### 2.5. Implementation
**Process**:
1. Update canonical documentation first
2. Modify implementation to match documentation
3. Update registry mappings
4. Run validation to confirm alignment

### 2.6. Traceability Update
**Location**: `docs/reference/agentos/traceability.md`
**Format**: Add row linking problem to decision and affected artifacts
```
| PRB-XXXX | YYYY-MM-DD-decision-slug.md | docs/affected/file.md, docs/another/file.md |
```

### 2.7. Validation
**Checks**:
- Registry validation passes
- Traceability validation passes
- Behavior validation confirms coherence
- No new gaps introduced

## 3. Problem Registry

Current validated problems AgentOS addresses:

| ID | Title | Status | Scope | Statement | Evidence | Impact | Detection Signals |
|----|-------|--------|-------|-----------|----------|--------|------------------|
| PRB-0001 | Goal Drift | Validated | system | Agents lose primary objectives during multi-step work | User reports | Primary requirements missed, rework | Plan lacks primary objective, sub-task changes without closing requirements |
| PRB-0002 | Context Instability | Validated | system | Context selection unstable or opaque | User reports | Inconsistent directives, ambiguous decisions | Same task produces different outputs, missing canonical docs |
| PRB-0003 | Ambiguity Resolution | Validated | system | Unresolved requirements lead to inconsistent outcomes | User reports | Behavior diverges from intent | No clarifying questions, intent corrections after implementation |
| PRB-0004 | Verification Gaps | Validated | system | Changes ship without adequate validation | User reports | Regressions slip through | Tasks complete without verification step, gates diverge from CI |
| PRB-0005 | Rationale Loss | Validated | system | Design decisions lose their underlying reasoning | User reports | Core behavior drifts, repeated debates | Constraints removed without rationale, core changes without ADRs |
| PRB-0006 | Routing Drift | Validated | system | Routing fails, causing wrong domain execution | User reports | Incorrect constraints, wasted effort | Task uses directives from wrong domain, canonical docs not loaded |
| PRB-0007 | Registry Drift | Validated | system | Docs and code become unsynchronized | User reports | Deterministic lookup fails | New/changed files lack directive mapping, docs updated without implementation links |
| PRB-0008 | Unsafe Autonomy | Validated | system | Destructive actions without confirmation | User reports | Unintended deletions, reduced trust | Destructive actions without confirmation prompt |
| PRB-0009 | Non-Deterministic Execution | Validated | system | Same inputs produce different outcomes | User reports | Unreliable verification and maintenance | Similar tasks use different commands, steps not captured in deterministic tools |
| PRB-0010 | Taxonomy Drift | Validated | system | Task types evolve without updating contracts | User reports | Inconsistent task handling | New task types appear without behavior spec or traceability updates |
| PRB-0011 | Bootstrap Failures | Validated | system | New repos lack coherent starting state | User reports | Early tasks misrouted/incomplete | Missing docs/index.md or routing rules, tasks proceed without canonicals |

## 4. ADR Examples

### ADR Template Example
```markdown
# Decision: Core Purpose and Non-Goals

**Status**: Accepted
**Date**: 2026-01-13
**Scope**: agentos
**Problem IDs**: PRB-0005

## Context
Rationale loss makes it easy to remove or weaken core constraints during evolution.

## Decision
Define core purpose and non-goals as contract constraints.

## Alternatives
- Leave purpose implicit
- Define purpose in explanation docs only

## Consequences
- Adds explicit scope boundaries
- Reduces future drift in core intent

## Why this worked
Preserves core intent over time, addressing PRB-0005.

## Artifacts
- docs/reference/agentos/behavior-spec.md
```

### ADR Status Progression
- **Proposed**: Initial decision record, awaiting ratification
- **Accepted**: Ratified and implemented or scheduled
- **Superseded**: Replaced by another ADR (must link to replacement)

## 5. Traceability Map Structure

Links problems to decisions and affected artifacts:

| Problem ID | Decision Record | Artifacts |
|------------|-----------------|-----------|
| PRB-0001 | 2026-01-13-primary-objective-control.md | docs/reference/agentos/behavior-spec.md |
| PRB-0005 | 2026-01-13-rationale-preservation-system.md | docs/reference/agentos/problem-registry.md, docs/explanation/agentos/decisions/ |

## 6. Loop Selection Rules

Evolution follows two types of improvement loops:

### 6.1. Single-Loop Changes
**When to use**: Fix within existing coherence contracts
**Examples**:
- Update validation script for better coverage
- Improve documentation clarity
- Add missing registry mappings
- Refine work note templates

**Process**: Direct implementation without ADR requirement

### 6.2. Double-Loop Changes
**When to use**: Change the coherence contracts themselves
**Examples**:
- Modify core invariants
- Add new coherence mechanisms
- Change evolution protocols
- Update authority order

**Process**: Full ADR lifecycle required

## 7. Design Decision Framework

### 7.1. Design-Decision Checkpoint Requirements

Design-decision checkpoints are required documentation of options, tradeoffs, and rationale when design or architecture decisions are material.

**When Required**:
- **Level 1-2**: Optional (only if material design/architecture decision exists)
- **Level 3-4**: Mandatory (document decision or explain rationale for skipping)

**Integration with Task Lifecycle**:
- Checkpoints occur during planning phase before execution
- Must use structured exploration phases (1-5) from design-decision-templates.md
- All phases must produce documented outputs preserved in checkpoint document
- Phase outputs integrate with complexity-scaled templates

**Level-Specific Requirements**:
- **Level 1-2 (Optional Structured Exploration)**: If decision exists, use brief structured exploration. Phases 1-4 recommended (brief), Phase 5 optional. Phase outputs may be concise.
- **Level 3-4 (Mandatory Structured Exploration)**: All 5 phases mandatory when material decision exists. Phase 1: Component Breakdown (required), Phase 2: Option Exploration (required, 2-4 options), Phase 3: Trade-off Analysis (required, tabular format), Phase 4: Decision Documentation (required), Phase 5: Decision Verification (required). If no material decision exists, document rationale for skipping structured exploration.

### 7.2. Structured Exploration (5 Phases)
**Phase 1**: Component Breakdown - Functional requirements, technical constraints, integration points, dependencies
**Phase 2**: Option Exploration - 2-4 viable options with brief descriptions and preliminary pros/cons
**Phase 3**: Trade-off Analysis - Tabular comparison (options × criteria) with risk assessment
**Phase 4**: Decision Documentation - Selected approach, rationale, discarded alternatives, implementation guidance
**Phase 5**: Decision Verification - Validate against requirements/constraints with checklists

### 7.3. Complexity-Scaled Templates

#### Level 1 (Brief)
```
Decision: [name]

## Phase 1: Component Breakdown (brief)
Requirements/constraints: [key items only]

## Phase 2: Option Exploration (brief)
Options: [2-3 short bullets]

## Phase 3: Trade-off Analysis
Tradeoffs (table): options × 3-4 criteria

## Phase 4: Decision Documentation (brief)
Selected: [1-2 sentences]
Rationale: [1-2 sentences]
```

#### Level 2 (Basic)
```
Decision: [name]

## Phase 1: Component Breakdown (brief)
Requirements/constraints: [brief]

## Phase 2: Option Exploration (brief)
Options: [2-3 options, 1-2 sentences each]

## Phase 3: Trade-off Analysis
Tradeoffs (table): options × 4-5 criteria

## Phase 4: Decision Documentation (brief)
Selected + rationale: [2-3 sentences]
Implementation notes: [brief]
```

#### Level 3 (Comprehensive)
```
Decision: [name]

## Phase 1: Component Breakdown
Requirements/constraints/integration points: [bullets]
Dependencies: [list]

## Phase 2: Option Exploration
Options: [3-4 options, short description each]

## Phase 3: Trade-off Analysis
Tradeoffs (table): options × criteria (add weights if useful)
Risk assessment: [brief per option]

## Phase 4: Decision Documentation
Selected approach: [paragraph]
Rationale and evidence: [paragraph]
Discarded alternatives: [brief reasons]
Implementation guidance: [key steps/risks]

## Phase 5: Decision Verification (mandatory)
Verification against requirements: [checklist]
Verification against constraints: [checklist]
Verification against integration points: [checklist]
Risk assessment validation: [brief]
```

#### Level 4 (Enterprise)
```
Decision: [name]

## Phase 1: Component Breakdown
Requirements/constraints/integration points: [bullets]
Dependencies: [comprehensive list]

## Phase 2: Option Exploration
Options: [4+ options, concise descriptions]

## Phase 3: Trade-off Analysis
Tradeoffs (table): options × criteria (weighted)
Risk assessment: [detailed per option]

## Phase 4: Decision Documentation
Selected approach: [short paragraph]
Rationale and evidence: [short paragraph]
Discarded alternatives: [reasons]
Risks/mitigations: [bullets]
Implementation guidance: [bullets]

## Phase 5: Decision Verification (mandatory)
Verification against requirements: [comprehensive checklist]
Verification against constraints: [comprehensive checklist]
Verification against integration points: [comprehensive checklist]
Risk assessment validation: [detailed]
```

### 7.4. Tradeoff Table Standards
- Markdown table format with pipes
- First column: Option name
- Subsequent columns: Decision criteria
- Left-align text, center-align numeric
- 3-6 criteria based on complexity
- Include risk assessment for Level 3-4

### 7.5. Evolution Governance
- **Single-loop**: Direct implementation with validation
- **Double-loop**: ADR + traceability required
- **Core changes**: Problem registry validation first
- **Validation**: Registry, traceability, behavior, rationale checks
- **Rollback**: Immediate reversion + gap capture if coherence broken

## 8. Evolution Boundaries

### 8.1. Allowed Changes
- Add new coherence mechanisms
- Refine existing protocols
- Improve validation coverage
- Update documentation for clarity
- Add new problem types to registry

### 8.2. Prohibited Changes
- Remove core coherence invariants without ADR
- Break existing registry mappings
- Eliminate traceability requirements
- Disable validation without replacement
- Lose rationale for existing constraints

## 9. Self-Evolution Capabilities

AgentOS can evolve itself through:

- **Automated validation**: Scripts detect coherence issues
- **Gap promotion**: Work notes automatically become problems when validated
- **ADR templates**: Structured decision capture
- **Traceability automation**: Links maintained through validation
- **Self-monitoring**: Continuous coherence assessment

## 10. Evolution Documentation

All evolution is documented through:

- **Work notes**: Initial gap capture
- **Problem registry**: Validated systemic issues
- **ADRs**: Decision records with rationale
- **Traceability map**: Problem-to-solution links
- **Validation reports**: Automated coherence checks

## 11. Evolution Validation

Evolution outcomes are validated by:

- **Pre-change validation**: Confirm starting coherence
- **Post-change validation**: Verify maintained coherence
- **Regression testing**: Ensure no existing coherence broken
- **Gap analysis**: Confirm no new incoherence introduced
- **Rationale review**: Verify reasoning is preserved and accessible

## 12. Implementation Requirements

Evolution framework compliance requires:

- **Gap capture**: All incoherence documented as work notes
- **Problem validation**: Systemic issues added to registry
- **ADR discipline**: Core changes require decision records
- **Traceability maintenance**: All links kept current
- **Validation execution**: Automated checks run after changes
- **Rationale preservation**: Reasoning documented and accessible

## 13. Related Contracts

- `coherence-contract.md`: Defines what evolution must preserve
- `architectural-patterns.md`: Implementation patterns for evolution
- `validation-contract.md`: Validation invariants for evolution
- `alignment-mechanisms.md`: Operational evolution implementations