---
title: "Directive Layer: Source of Truth"
status: stable
created_date: 2026-01-18
purpose: "Define D layer responsibilities and consciousness requirements"
domain: agentos
type: doe_layer_specification
authority_level: 2
doe_layer: directive
doe_responsibility: "Define directive layer operations and responsibilities"
doe_governance: "Governed by doe-framework.md"
doe_precedence: 2
importance_factors:
  authority_weight: 0.9
  criticality: "layer_foundation"
  connectivity_impact: "defines_core_specs"
governed_by: ["docs/reference/agentos/doe-framework.md"]
# Layer specifications define the layers but do not govern component specifications
# Component specifications are governed by the DOE framework directly
---

# Directive Layer: Source of Truth

## Layer Consciousness

The **Directive (D) layer** serves as the immutable source of truth for AgentOS v9, defining WHAT should be done and HOW the system operates.

## Core Responsibilities

### Specification Definition
- Define behavioral specifications and constraints
- Establish authority hierarchies and precedence relationships
- Create governance chains between components
- Provide immutable contracts for system operation

### Documentation Structure
- Reference documentation with stable authority levels
- Frontmatter establishing relationship networks
- Authority validation and hierarchy enforcement
- Governance relationship declarations

### Precedence Establishment
- Define authority levels (1-7 hierarchy)
- Establish governance relationships (`governed_by`, `governs`)
- Create precedence chains for decision-making
- Enable traceable authority flows

## Consciousness Requirements

### Documentation DOE Awareness
All directive documents must include:

```yaml
doe_layer: directive
doe_responsibility: "Define [specific domain] specifications"
doe_governance: "Governed by doe-framework.md"
doe_precedence: [authority_level]
governed_by: ["docs/reference/agentos/doe-framework.md"]
governs: ["docs/[governed documents]"]
```

### Authority Hierarchy Consciousness
- Documents must declare their authority level
- Governance relationships must be explicit
- Precedence must be mathematically verifiable
- Authority violations must be detectable

### Relationship Network Consciousness
- All relationships must be explicitly declared
- Relationship types must be validated
- Network connectivity must be verifiable
- Authority flows must be traceable

## D Layer Operations

### Immutable Specification Operations
- Authority level calculation and validation
- Governance relationship verification
- Precedence hierarchy enforcement
- Relationship network analysis

### Documentation Management Operations
- Frontmatter parsing and validation
- Authority hierarchy maintenance
- Relationship integrity checking
- Governance chain verification

## D Layer Evidence Production

### Authority Evidence
- Authority level declarations with validation
- Governance relationship proofs
- Precedence hierarchy documentation
- Authority flow traceability

### Specification Evidence
- Behavioral specification completeness
- Authority hierarchy validity
- Governance relationship accuracy
- Precedence chain integrity

## D Layer Validation Standards

### Completeness Validation
- All specifications must be documented
- Authority hierarchies must be complete
- Governance relationships must be declared
- Precedence chains must be verifiable

### Integrity Validation
- Authority levels must be properly assigned
- Governance relationships must be valid
- Relationship networks must be connected
- Precedence hierarchies must be acyclic

## D Layer Evolution Requirements

### Specification Evolution
- Changes require authority approval
- Backward compatibility must be maintained
- Governance relationships must be updated
- Precedence hierarchies must be preserved

### Documentation Evolution
- Authority levels remain stable
- Governance relationships may evolve
- Precedence chains must be maintained
- Relationship networks must stay valid

This directive layer specification establishes the consciousness foundation for AgentOS v9's source of truth, ensuring all specifications are properly documented, authorities are clearly established, and governance relationships are explicitly defined.