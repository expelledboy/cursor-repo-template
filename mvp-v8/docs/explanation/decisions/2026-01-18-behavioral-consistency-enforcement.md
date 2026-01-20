---
title: "Decision: Mandatory Behavioral Consistency Enforcement"
status: accepted
created_date: 2026-01-18
purpose: "Establish systemic mechanisms for ensuring agent follows established patterns"
domain: agentos
related:
  - docs/work/problems/2026-01-18-evolution-system-failure.md
  - docs/work/problems/2026-01-18-work-file-archiving-mistakes.md
  - docs/work/problems/2026-01-18-cumulative-migration-errors.md
implementations:
  - .cursor/rules/core.mdc
  - scripts/docs/index.py
---

# Decision: Mandatory Behavioral Consistency Enforcement

## Decision
We mandate systemic mechanisms to ensure the agent consistently follows established DOE patterns, schemas, and workflows. This addresses the root cause of multiple recent issues: behavioral inconsistency despite comprehensive documentation.

## Rationale
Recent issues (evolution system failure, work file archiving mistakes, cumulative migration errors, inconsistent schema adherence) are all symptoms of the same problem: the agent has access to all rules and schemas but doesn't consistently apply them. Documentation alone isn't sufficient - behavioral reinforcement is required.

## Issues Addressed
1. **Evolution System Failure**: Learn/evolve cycle creates documentation but doesn't change behavior
2. **Work File Archiving**: Valuable rationale incorrectly archived as superseded material
3. **Migration Errors**: Multi-step operations fail without validation gates
4. **Schema Inconsistency**: Required metadata and traceability links omitted

## Implementation
- **Behavioral Validation Gates**: All operations must pass consistency checks before completion
- **Archiving Criteria**: Work files with rationale must remain accessible, only truly obsolete canonical material gets archived
- **Process Reinforcement**: DOE cycle must be explicitly followed with validation at each step
- **Error Prevention**: Multi-step operations require intermediate validation

## Systemic Changes Required
The evolution system itself needs fundamental changes to ensure behavioral follow-through, not just documentation creation. Rules loading for docs operations appears inconsistent and needs investigation.