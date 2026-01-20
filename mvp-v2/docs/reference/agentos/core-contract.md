# AgentOS Core Contract

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Core invariants and principles for AgentOS MVP-v2.

---

## Core Principle

**AgentOS maintains coherence across three surfaces:**
1. **Documentation** - What the system says it does
2. **Implementation** - What the system actually does
3. **Behavior** - What the system does in practice

---

## Invariants

1. **Structured Requirements**: All requirements must be structured (YAML schema)
2. **Documentation-Driven**: Behavior is defined in documentation, not code
3. **Deterministic Routing**: Same requirement → same route → same outcome
4. **Validation at Boundaries**: Validate structure at intake, coherence at execution
5. **Single Source of Truth**: Each fact lives in one canonical location

---

## Authority Order

When sources conflict, defer to:
1. **Schemas** (requirement.yaml, decision-graph.yaml)
2. **Core Contract** (this document)
3. **Workflow Documentation** (docs/reference/agentos/workflows/)
4. **Decision Graphs** (docs/reference/agentos/decisions/)

---

## Task Plan Header

Every task must include:

```yaml
plan:
  task_id: TASK-20260114-ABC123
  type: execution | coordination | architecture | meta
  objective: Clear single sentence
  workflow: workflow-name
  steps:
    - id: step-1
      action: description
      validation: validation-method
  success_criteria:
    - measurable outcome
  loaded_docs:
    - docs/reference/agentos/workflows/execution.md
```

---

## Safety Policy

1. **Destructive Actions**: Require explicit confirmation
2. **Schema Validation**: Validate all structured data
3. **Coherence Checks**: Run validation before committing changes
4. **Rollback Plan**: Document how to undo changes

---

## Validation Contract

1. **Structure Validation**: Validate requirement/plan structure (JSON Schema)
2. **Coherence Validation**: Check documentation ↔ implementation alignment
3. **Outcome Validation**: Verify success criteria met

---

## Evolution

Changes to this contract require:
1. Problem identification (structured)
2. Decision record (ADR)
3. Schema update (if structural change)
4. Validation update (if validation change)
