# AgentOS Architectural Patterns (Reference)

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Defines the core architectural patterns that implement the coherence engine.

---

## 1. DOE Pattern Implementation

The Directive-Orchestration-Execution pattern provides the fundamental architecture for coherence maintenance.

### 1.1. Pattern Structure
**Directive (D)**: Authoritative documentation provides source of truth
**Orchestration (O)**: Task routing and directive selection logic
**Execution (E)**: Deterministic tools with evidence production

### 1.2. Pattern Flow
```
Directive → Orchestration → Execution → Evidence → Validation → Coherence
```

### 1.3. Pattern Invariants
- Directives are immutable during task execution
- Orchestration is deterministic based on task classification
- Execution produces verifiable evidence
- Pattern maintains coherence across all surfaces

## 2. Context Compass Pattern

The Context Compass constrains documentation loading by task intent to prevent context bloat, enhanced with Cursor's deterministic loading mechanics.

### 2.1. Intent-Based Loading
| Task Intent | Allowed Doc Types | Loading Constraint |
|-------------|-------------------|-------------------|
| Execution | reference + how-to | Apply existing knowledge |
| Learning | tutorials | Acquire new knowledge |
| Architecture | explanation + reference | Understand design rationale |
| Meta-Maintenance | reference + how-to + explanation | Evolve the system |

### 2.2. Cursor-Enhanced Loading System

#### 2.2.1. alwaysApply Rules (Core Reasoning)
Loaded at Cursor startup, provide foundational reasoning structures:
- **Decision Trees**: Pre-computed routing logic for common scenarios
- **Invariant Checks**: Core coherence validation rules
- **Authority Maps**: Truth surface hierarchy definitions
- **Safety Guards**: Destructive action confirmation protocols

#### 2.2.2. description Rules (Semantic Matching)
Keyword-triggered loading of specialized reasoning aids:
- **Routing Instructions**: "When you see X, route to Y with reasoning Z"
- **Pre-reasoning Steps**: Structured analysis frameworks for complex decisions
- **Context Enrichment**: Domain-specific reasoning patterns
- **Validation Templates**: Automated checking procedures

#### 2.2.3. globs Rules (Path-Based Loading)
File pattern matching loads contextual reasoning supports:
- **Directory Reasoning**: Project structure analysis patterns
- **File Type Logic**: Language/framework-specific decision trees
- **Module Boundaries**: Import/dependency reasoning rules
- **Change Pattern Analysis**: Modification impact assessment frameworks

### 2.3. Hierarchical Tier Loading
Directives load in 5 tiers with explicit triggers, now enhanced with reasoning aids:
1. **Tier 1 (Core)**: Load first if intent allows reference docs + alwaysApply reasoning
2. **Tier 2 (Task-Type)**: Load after Tier 1 based on routing + description-matched reasoning
3. **Tier 3 (Complexity)**: Load based on complexity level + complexity-specific decision trees
4. **Tier 4 (Phase)**: Load only on lifecycle triggers + phase-appropriate reasoning frameworks
5. **Tier 5 (Specialized)**: Load only on rare explicit triggers + specialized analysis tools

### 2.4. Reasoning Aid Integration
Each loaded context includes structured reasoning support:
- **Decision Trees**: Binary/logic trees for complex routing decisions
- **Validation Checklists**: Automated verification steps
- **Impact Analysis**: Change consequence prediction frameworks
- **Escalation Protocols**: When to involve human judgment

### 2.5. Deferral Protocol
Directives defer loading when:
- Intent constraints prevent loading
- Phase triggers not yet reached
- Context constraints require minimal mode
- Reasoning aids not yet needed for current decision

## 3. Registry Mapping Pattern

Bidirectional documentation-implementation mapping prevents surface drift.

### 3.1. Mapping Annotations
**Code to Docs**: `# @directive docs/path.md`
**Docs to Code**: `@implementation code/path.py`

### 3.2. Mapping Scope
- Source code, configuration, scripts, tests
- Excludes generated files, vendor code, local state
- Defined in AGENTS.md registry scope

### 3.3. Mapping Maintenance
- Add mappings on file creation
- Update mappings on file moves
- Validate mappings regularly
- Fix breaks immediately

## 4. State Surface Management Pattern

Manages authoritative vs local state to maintain coherence boundaries.

### 4.1. State Types
**Authoritative State**: Permanent, validated, evidence-bearing
- Location: `docs/reference/`, `docs/how-to/`, `docs/explanation/`
- Characteristics: Version controlled, validated, traceable

**Local State**: Ephemeral, working, non-evidence
- Location: `docs/local/state/`
- Characteristics: Gitignored, task-scoped, disposable

### 4.2. State Transitions
- Promote local to authoritative only for decision summaries and gaps
- Never promote local state as primary evidence
- Discard local state after task completion

### 4.3. State Boundaries
- Task scope: Local state per task
- Evidence boundary: Local state non-authoritative
- Validation boundary: Local state not validated
- Persistence boundary: Local state may be lost

## 5. Truth Surface Hierarchy Pattern

Resolves conflicts through evidence ordering when surfaces disagree.

### 5.1. Evidence Hierarchy
1. **CI Workflows**: Automated, deterministic validation
2. **Task Runner Commands**: Executable scripts and recipes
3. **Runtime Configuration**: Deployed system state
4. **Tests**: Automated verification of behavior
5. **Implementation Artifacts**: Code and configuration files
6. **Documentation**: reference > how-to > explanation > tutorials > work > archive
7. **Local State**: Non-authoritative working notes

### 5.2. Conflict Resolution
1. Identify conflicting evidence sources
2. Determine higher-authority source
3. Align lower-authority sources with higher
4. Document resolution rationale
5. Update traceability if systemic

## 6. Pattern Composition

### 6.1. Pattern Relationships
- **DOE** orchestrates all other patterns
- **Context Compass** constrains DOE directive loading
- **Registry Mapping** maintains DOE surface alignment
- **State Surface** manages DOE evidence boundaries
- **Truth Surface** resolves DOE conflicts

### 6.2. Pattern Evolution
Patterns evolve through the evolution framework:
- Gap detection when patterns fail
- Problem validation for pattern issues
- ADR creation for pattern changes
- Implementation through alignment mechanisms

## 7. Pattern Validation

### 7.1. Pattern Compliance
- DOE pattern: Task lifecycle adherence
- Context Compass: Intent-based loading verification
- Registry Mapping: Bidirectional link validation
- State Surface: Boundary enforcement
- Truth Surface: Conflict resolution tracking

### 7.2. Pattern Metrics
- Pattern adherence rate
- Surface alignment quality
- Conflict resolution time
- Evolution success rate

## 8. Implementation Requirements

To implement these patterns:
- Follow DOE flow for all tasks
- Respect Context Compass constraints
- Maintain registry mappings
- Enforce state boundaries
- Apply truth hierarchy for conflicts

## 9. Behavior-Deterministic Documentation Reduction

The enhanced context loading system enables significant documentation reduction through deterministic behavioral guidance.

### 9.1. Reasoning Aid Replacement
**Before**: Verbose documentation with manual reasoning steps
**After**: Pre-loaded decision trees and automated reasoning frameworks

**Examples**:
- **Routing Logic**: 500-word explanation → 50-line decision tree
- **Validation Procedures**: 300-word checklist → 20-rule automated validator
- **Impact Analysis**: 400-word methodology → 15-pattern recognition framework

### 9.2. Contextual Intelligence Amplification
**Pattern Recognition**: Cursor's semantic matching loads exactly the right reasoning aids
**Structural Awareness**: File path patterns trigger project-specific logic
**Temporal Adaptation**: Phase-based loading provides just-in-time reasoning support

### 9.3. Documentation Reduction Metrics
- **Procedural Documentation**: 70-80% reduction through automated reasoning
- **Validation Documentation**: 60-70% reduction through automated checking
- **Routing Documentation**: 80-90% reduction through decision trees

### 9.4. Quality Assurance
- **Deterministic Loading**: Same inputs always load same reasoning aids
- **Version Consistency**: Reasoning frameworks versioned with contracts
- **Fallback Mechanisms**: When reasoning aids insufficient, load full documentation

### 9.5. Evolution Compatibility
- **Reasoning Framework Updates**: New patterns can be deployed without changing contracts
- **Backward Compatibility**: Legacy documentation remains accessible
- **Progressive Enhancement**: System improves reasoning without breaking existing behavior

## 10. Related Contracts

- `coherence-contract.md`: Defines pattern invariants
- `evolution-framework.md`: Governs pattern evolution
- `validation-contract.md`: Validates pattern compliance
- `alignment-mechanisms.md`: Implements pattern operations