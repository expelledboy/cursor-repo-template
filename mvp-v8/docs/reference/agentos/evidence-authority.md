---
title: "Evidence Authority"
status: stable
created_date: 2026-01-18
purpose: "Defines the authority hierarchy and validation rules for evidence sources in AgentOS operations"
domain: agentos
---

# Evidence Authority (Reference)

## Purpose
Establishes the authority hierarchy for evidence sources and validation rules to ensure AgentOS decisions are based on appropriate quality and reliability levels. This prevents decisions from being based on inadequate or inappropriate sources.

## Authority Hierarchy

Evidence sources are ranked by authority level, from most authoritative to least:

### 1. Reference (Highest Authority)
**Location**: `docs/reference/`
**Content**: Stable, authoritative specifications and contracts
**Use Case**: Primary source for system behavior, APIs, and requirements
**Authority Level**: 1 - Always appropriate for any decision

### 2. How-to
**Location**: `docs/how-to/`
**Content**: Procedural guides and operational instructions
**Use Case**: Step-by-step processes and implementation guidance
**Authority Level**: 2 - Appropriate for implementation decisions

### 3. Explanation
**Location**: `docs/explanation/`
**Content**: Rationale, design decisions, and architectural reasoning
**Use Case**: Understanding why decisions were made and system evolution
**Authority Level**: 3 - Appropriate for design and architectural decisions

### 4. Tutorials
**Location**: `docs/tutorials/`
**Content**: Learning materials and examples
**Use Case**: Educational content and getting started guides
**Authority Level**: 4 - Generally inappropriate for primary decisions

### 5. Work
**Location**: `docs/work/`
**Content**: Active research, problem analysis, and current development
**Use Case**: Ongoing work and research findings
**Authority Level**: 5 - May be flagged for primary decisions (use with caution)

### 6. Archive (Lowest Authority)
**Location**: `docs/archive/`
**Content**: Superseded historical content and deprecated specifications
**Use Case**: Historical reference only
**Authority Level**: 6 - Generally inappropriate for current decisions

## Authority Validation Rules

### Decision Context Matching
- **Strategic/Architectural**: Must use Reference/How-to level sources
- **Implementation**: May use How-to/Explanations with Reference backup
- **Operational**: May use How-to with appropriate higher authority
- **Research/Learning**: May use Work/Tutorials with clear caveats

### Authority Level Enforcement
- **Hard Block**: Archive sources (level 6) for any primary decision
- **Warning**: Work sources (level 5) for primary decisions
- **Acceptable**: All sources for secondary/supporting evidence

### Freshness Requirements
- **Reference**: Changes infrequently (version-level changes)
- **How-to**: Updates with process improvements
- **Explanation**: Evolves with system understanding
- **Work**: Actively changing, requires recency checks
- **Archive**: Historical only, not for current decisions

## Implementation in Validation

### `/retrospect` Authority Checks
```
4. 📋 Evidence Quality & Authority
   ✅ Evidence quality and authority acceptable

   ⚠️  Authority issues: Low authority source (work/5): research-notes.md
   💡 Use higher authority sources (reference > how-to > explanation)
```

### Validation Logic
- **Authority Mapping**: Each source path mapped to authority level
- **Context Assessment**: Decision type determines minimum required authority
- **Warning Thresholds**: Sources below appropriate level generate warnings
- **Block Thresholds**: Inappropriate sources may block execution

## Evidence Quality Requirements

### Completeness
- All required sources for decision type must be present
- Multiple authority levels should support major decisions
- Gaps in evidence chain must be identified

### Relevance
- Sources must directly support the decision being made
- Historical sources must be verified for continued applicability
- Conflicting evidence must be resolved with higher authority

### Accessibility
- Sources must be accessible to the agent at decision time
- External sources require validation of trustworthiness
- Source integrity must be verifiable

## Integration Points
- **DOE Flow**: Evidence authority validated at all execution checkpoints
- **Task Planning**: Required evidence sources specified in task plan headers
- **Command Validation**: `/retrospect` enforces authority hierarchy
- **Documentation System**: Authority levels integrated into validation scripts

## Related
- `docs/reference/agentos/architecture.md#doe-integrated-flow`
- `docs/reference/agentos/task-plan-spec.md`
- `docs/reference/agentos/verification-gates.md`
- `.cursor/commands/retrospect.md`