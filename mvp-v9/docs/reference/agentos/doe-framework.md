---
title: "DOE Framework: Directive-Orchestration-Execution"
status: stable
created_date: 2026-01-18
purpose: "Definitive DOE framework specification establishing layer consciousness and precedence"
domain: agentos
type: doe_framework
authority_level: framework
doe_layer: directive
doe_responsibility: "Define DOE operating model and layer responsibilities"
doe_governance: "Highest authority - governs all other specifications"
doe_precedence: 0
importance_factors:
  authority_weight: 1.0
  criticality: "system_foundation"
  connectivity_impact: "governs_all_layers"
governs: ["docs/reference/agentos/directive-layer.md", "docs/reference/agentos/orchestration-layer.md", "docs/reference/agentos/execution-layer.md", "docs/reference/agentos/architecture.md", "docs/reference/agentos/behavior-spec.md", "docs/reference/agentos/learning-system.md", "docs/reference/agentos/relationship-orchestration.md", "docs/reference/agentos/state-management.md", "docs/how-to/agentos/usage.md"]
---

# DOE Framework: Directive-Orchestration-Execution

## Operating Model Consciousness

AgentOS v9 operates on the **Directive-Orchestration-Execution (DOE)** framework, establishing clear consciousness and responsibility boundaries between layers.

## Layer Definitions and Consciousness

### D Layer (Directive): Source of Truth
**Consciousness**: Defines WHAT should be done and HOW the system works
**Authority**: Highest precedence - immutable specifications
**Artifacts**: Reference documentation with authority hierarchies
**Responsibilities**:
- Define behavioral specifications
- Establish authority relationships
- Create governance chains
- Provide immutable contracts

### O Layer (Orchestration): Cognitive Processing
**Consciousness**: Analyzes directives, plans execution, makes decisions
**Authority**: High precedence - enables intelligent operation
**Artifacts**: AI agent analysis, task planning, decision frameworks
**Responsibilities**:
- Analyze D layer directives for execution planning
- Make context-aware decisions and adaptations
- Handle ambiguity and complex reasoning
- Coordinate multi-step task execution

### E Layer (Execution): Deterministic Operations
**Consciousness**: Performs simple, predictable operations with evidence production
**Authority**: Operational precedence - enables reliable execution
**Artifacts**: CLI commands, scripts, validation tools, evidence outputs
**Responsibilities**:
- Execute deterministic file system operations
- Collect and structure data for O layer analysis
- Produce evidence meeting DOE standards
- Maintain operational safety and reliability

## Layer Interaction Consciousness

### D → O Flow: Specification to Analysis
- D layer provides authoritative specifications
- O layer analyzes specifications for execution planning
- O layer requests clarification from D layer when needed
- D layer remains immutable source of truth

### O → E Flow: Planning to Execution
- O layer provides execution plans and context
- E layer executes plans deterministically
- E layer produces evidence for O layer verification
- O layer validates execution against D layer specifications

### E → O Feedback: Evidence to Analysis
- E layer provides structured evidence of execution
- O layer analyzes evidence for DOE compliance
- O layer identifies gaps requiring D layer updates
- Continuous improvement cycle maintained

## Precedence Hierarchy Consciousness

### Authority Precedence (Hierarchical)
```
DOE Framework (Level 1) - Highest authority
├── Layer Specifications (Level 2) - Framework governance
├── Component Specifications (Level 3) - Feature governance
└── Implementation Details (Level 4+) - Operational governance
```

### Operational Precedence (Execution Order)
1. **Directive Loading**: D layer specifications loaded first
2. **Orchestration Planning**: O layer analyzes and plans
3. **Execution Validation**: E layer checks preconditions
4. **Safe Execution**: E layer performs operations
5. **Evidence Verification**: O layer validates against D layer
6. **Completion Assessment**: O layer determines success/failure

## Consciousness Validation Requirements

### D Layer Consciousness Validation
- All specifications must declare `doe_layer: directive`
- Authority hierarchies must be properly established
- Governance relationships must be explicitly defined
- Precedence levels must be clearly articulated

### O Layer Consciousness Validation
- All analysis components must declare `doe_layer: orchestration`
- Decision processes must reference governing directives
- Context awareness must be demonstrable
- Analysis quality must meet DOE standards

### E Layer Consciousness Validation
- All execution components must declare `doe_layer: execution`
- Operations must be demonstrably deterministic
- Evidence production must meet DOE standards
- Safety mechanisms must be verifiable

## Implementation Consciousness

### Documentation Layer Awareness
All AgentOS documentation must include DOE consciousness:

```yaml
# Required frontmatter for DOE awareness
doe_layer: "directive"  # or "orchestration" or "execution"
doe_responsibility: "Define system behavior specifications"
doe_governance: "Governed by doe-framework.md"
doe_precedence: 1
```

### Component Layer Awareness
All AgentOS components must declare their DOE layer:

```python
# Required constants in all scripts
DOE_LAYER = "execution"
DOE_RESPONSIBILITY = "Collect file system evidence"
DOE_GOVERNANCE = "docs/reference/agentos/execution-layer.md"
```

### Validation Layer Awareness
DOE consciousness must be continuously validated:

```python
# Validation ensures DOE awareness
def validate_doe_layer_awareness():
    """Ensure all components declare DOE consciousness."""
    # Verify documentation DOE declarations
    # Verify component DOE declarations
    # Validate governance relationships
    # Check precedence hierarchies
```

## Evolution and Adaptation Consciousness

### Framework Evolution
DOE framework evolution must maintain backward compatibility:
- Layer responsibilities remain stable
- Precedence hierarchies preserved
- Consciousness requirements maintained
- Validation standards upheld

### Component Evolution
Component changes must respect DOE boundaries:
- D layer changes require authority approval
- O layer changes maintain analysis integrity
- E layer changes preserve determinism
- All changes validated against DOE consciousness

## Success Metrics

### Consciousness Achievement Metrics
- **100% Documentation DOE Awareness**: All docs declare DOE layer and responsibilities
- **100% Component DOE Awareness**: All scripts declare DOE layer and governance
- **100% Precedence Compliance**: Authority hierarchies properly established
- **100% Validation Coverage**: DOE consciousness continuously verified

### Operational Effectiveness Metrics
- **Deterministic Execution**: E layer operations produce consistent results
- **Evidence Quality**: E layer outputs meet DOE standards
- **Analysis Integrity**: O layer decisions traceable to D layer directives
- **Safety Compliance**: E layer operations prevent harm and unauthorized actions

This DOE framework establishes the consciousness foundation for authentic AgentOS operation, ensuring clear layer responsibilities, proper precedence relationships, and continuous validation of DOE awareness throughout the system.