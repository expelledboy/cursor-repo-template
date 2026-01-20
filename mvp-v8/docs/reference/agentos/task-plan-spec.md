---
title: "Task Plan Specification"
status: stable
created_date: 2026-01-18
purpose: "Defines the structure and requirements for task plan headers used in DOE operations"
domain: agentos
---

# Task Plan Specification (Reference)

## Purpose
Defines the structure and validation requirements for task plan headers used throughout the AgentOS DOE (Directive-Orchestration-Execution) system. Task plan headers ensure systematic, auditable, and verifiable task execution.

## Core Principles
- **Structured Planning**: All tasks follow explicit planning requirements
- **Measurable Objectives**: Primary objectives must be clear and verifiable
- **Validation Integration**: Plans connect to verification gates and safety checks
- **Complexity Awareness**: Plans adapt rigor based on task complexity

## Required Header Elements

### Task Identification
- **Task Type**: From supported taxonomy (Implementation/Feature, Documentation & Knowledge, etc.)
- **Primary Objective**: Single, measurable goal statement that can be definitively achieved

### Complexity Assessment
- **Complexity Level**: 1-4 scale with explicit rationale
  - Level 1: Simple, single component, clear path
  - Level 2: Multiple components, moderate complexity
  - Level 3: Complex interactions, significant decisions
  - Level 4: High uncertainty, architectural impact
- **Determination Criteria**: Scope, decisions, risk, effort, dependencies

### Execution Planning
- **Workflow Variation**: Level 1-4 rigor across lifecycle phases
- **Verification Gates**: Task-type specific validation commands
- **Evidence Sources**: Required documentation and artifacts with authority levels

### Safety Assessment
- **Destructive Actions**: Identification of operations requiring confirmation
- **Risk Level**: Low/Med/High impact assessment
- **Rollback Planning**: Contingency plans for critical operations

## Validation Integration

### `/retrospect` Command Checks
Task plans are validated by the `/retrospect` command for:
- **Completeness**: All required elements present
- **Consistency**: Task type matches supported taxonomy
- **Measurability**: Primary objective can be verified
- **Safety**: Destructive actions properly identified

### Example Valid Task Plan
```
Task Type: Implementation / Feature
Primary Objective: Add user authentication system with 90% test coverage
Complexity Level: 2
Rationale: Multiple components (auth logic, tests, docs) but clear requirements
Workflow Variation: Level 2 (standard validation, moderate documentation)
Verification Gates: just test, just docs::validate
Evidence Sources: auth.py, test_auth.py, docs/api-auth.md
Safety Assessment: No destructive operations, low risk
```

## Integration Points
- **Command Validation**: `/retrospect` validates plan structure pre-execution
- **Safety Enforcement**: Plans trigger appropriate confirmation protocols
- **Evidence Authority**: Sources validated against authority hierarchy
- **Complexity Scaling**: Plans determine validation rigor and checkpoint frequency

## Related
- `docs/reference/agentos/architecture.md#doe-integrated-flow`
- `docs/reference/agentos/verification-gates.md`
- `.cursor/commands/retrospect.md`