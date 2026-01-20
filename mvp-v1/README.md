# AgentOS MVP

This is a minimal viable product (MVP) of AgentOS, designed from first principles as a **self-sustaining coherence engine** that maintains alignment between documentation, implementation, and behavior surfaces.

## Core Identity

AgentOS is a meta-system that prevents entropy in complex socio-technical systems by ensuring three fundamental surfaces remain synchronized:

1. **Documentation Surface**: Authoritative source of truth (what should be)
2. **Implementation Surface**: Actual code and artifacts (what is built)
3. **Behavior Surface**: Runtime execution and outcomes (what actually happens)

## Architecture Overview

The MVP consists of five core reference documents organized in contract-implementation layers:

### Contracts Layer (Immutable)

#### 1. Coherence Contract (`coherence-contract.md`)
Defines the fundamental invariants and principles of coherence:
- Three surface alignment requirements
- Authority order and truth surfaces
- Coherence failure modes (11 validated problems)
- Safety policy and verification contracts

#### 2. Evolution Framework (`evolution-framework.md`)
Structured processes for coherent system evolution:
- Gap detection → work notes → problem validation → ADRs → implementation
- Single-loop vs double-loop changes
- Problem registry and ADR format
- Design decision framework and templates

#### 3. Validation Contract (`validation-contract.md`)
Validation invariants and evolution events:
- Validation principles and triggers
- Evolution events (micro-AAR, retrospective, postmortem, MAM)
- Validation integration and metrics

### Implementation Layer (Evolvable)

#### 4. Architectural Patterns (`architectural-patterns.md`)
Core patterns implementing the coherence engine:
- DOE pattern, context compass, registry mapping
- State surface management, truth surface hierarchy
- Pattern composition and validation

#### 5. Alignment Mechanisms (`alignment-mechanisms.md`)
Operational implementations maintaining surface synchronization:
- Registry mapping operations
- Context loading and routing mechanisms
- State management and synchronization processes
- Cursor adapter constraints

## Key Design Decisions

- **Self-Sustaining**: The system can detect, document, and resolve its own coherence issues
- **Deterministic**: All validation and processes produce consistent, repeatable results
- **Comprehensive**: Covers all 11 validated coherence failure modes
- **Evolvable**: Structured processes for coherent system evolution
- **Minimal**: Only the essential mechanisms for coherence maintenance

## Registry Scope

This MVP includes the following in-scope paths for registry validation:

- `docs/reference/agentos/*.md` (core contracts)
- `scripts/agentos/*.py` (validation scripts)
- `scripts/agentos/*.bats` (test scripts)
- `tests/agentos/*.bats` (validation tests)

## Validation Commands

Run these commands to validate the MVP:

```bash
# Validate registry mappings
just agentos::validate-registry

# Validate traceability links
just agentos::validate-traceability

# Run all AgentOS validations
just agentos::validate-agentos
```

## Evolution Readiness

The MVP is designed to evolve through its own mechanisms:

1. **Gap Detection**: Use validation failures to identify coherence issues
2. **Work Notes**: Document gaps in `docs/work/agentos/`
3. **Problem Validation**: Add systemic issues to problem registry
4. **ADR Creation**: Document decisions in `docs/explanation/agentos/decisions/`
5. **Implementation**: Update contracts and scripts
6. **Traceability**: Link problems to solutions in `traceability.md`

## Limitations

This MVP provides the coherence framework but requires:

- Implementation of the 14 validation scripts
- Population of the problem registry with specific domain problems
- Integration with task execution environments
- Customization of registry scope for specific projects

## Cursor Implementation

The MVP is designed for deterministic implementation through Cursor IDE's routing system:

- **Cursor Rules**: Load decision graphs and reasoning aids based on context
- **Cursor Commands**: Manual overrides and explicit graph execution
- **Cursor Subagents**: Specialized reasoning environments
- **Semantic Search**: Intelligent discovery of relevant directives
- **MCP Extensions**: External tool integration for validation

See `docs/reference/agentos/cursor-implementation-spec.md` for complete implementation details.

## Next Steps

1. Implement Cursor rules and decision graphs (see implementation spec)
2. Create MCP servers for validation automation
3. Build semantic search integration for intelligent routing
4. Implement validation scripts in `scripts/agentos/`
5. Create domain-specific adaptations
6. Populate problem registry with project-specific issues
7. Integrate with task runners and CI systems
8. Add self-awareness checkpoints to task execution

This MVP establishes the foundation for a self-sustaining, coherent system that can maintain alignment across complex software development processes through deterministic behavioral guidance.