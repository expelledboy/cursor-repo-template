# Spec: Decision Graph (agentos.decision-graph/v1)

Status: Draft
Date: 2026-01-15
Purpose: Deterministic decision graphs with provenance + anchors to support reviewable traces.

## Core requirements
- Graphs are data (YAML) and evaluated deterministically.
- Conditions are string expressions (v1) evaluated against `context`.
- Graphs should declare the `context` fields they depend on (see `context_contract`) to avoid implicit/undefined context usage.
- Graphs must be traceable: nodes/steps should reference anchors when relevant.
- Graph introduction must record provenance (rules/mentions/commands/search/tools).

## Important v7.1 hardening notes
- Node types are now structurally validated (e.g., `decision_table` requires `rules`; `decision` requires `when/then/else`; `ask` requires `questions`).
- `expression_language` is extensible (`string`, `cel`, `json_logic`), but v7 still treats non-`string` as opt-in.

## Minimal shape (conceptual)
```yaml
spec_version: agentos.decision-graph/v1
name: graph_name
description: what it decides
expression_language: string
nodes:
  - id: start
    type: decision
    when: "true"
    then: route
    else: ask
  - id: ask
    type: ask
    ask:
      questions:
        - id: q1
          text: "..."
          branch_default: new_branch
  - id: route
    type: decision_table
    hit_policy: first
    rules:
      - id: r1
        when: "context.task.type == 'execution'"
        output: { route: ACT, confidence: 0.9 }
```

## Node types
- decision: boolean guard → then/else
- decision_table: ordered rules → output
- ask: terminates in a user gate (question/options) and must auto-display trace
- terminal: end

## Provenance + anchors
Each node may carry:
- `provenance`: why it exists/was introduced (rule, user_mention, manual_insert, search_suggested, command, kernel_default)
- `anchors_used`: references to evidence anchors (file/rule/doc/search/tool)

## Field reference
For a field-by-field breakdown of the schema, see:
- `docs/reference/agentos/schema-decision-graph.md`
