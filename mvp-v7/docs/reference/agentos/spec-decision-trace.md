# Spec: Decision Trace (agentos.decision-trace/v1)

Status: Draft
Date: 2026-01-15
Purpose: Structured, reviewable record of which graphs were evaluated, what path was taken, and what anchors were used.

## Core requirements
- Must reference active-state location (state_id + frame_id + objective_id).
- Must record graph provenance (rules/mentions/commands/search/tools).
- Must include anchors that point to exact artifacts/lines when possible.
- Must record the evaluated path (node/step ids + condition + result).

## Field reference
For a field-by-field breakdown of the schema, see:
- `docs/reference/agentos/schema-decision-trace.md`

## Important v7.1 hardening notes
- Prefer `graph_stack[].source.source_anchor_ids` over `source_ref` (so provenance always points to concrete anchors).
- Prefer `graphs[].inputs_digest` for diffability; keep `graphs[].inputs` minimal and optional.
- Use `anchors[].hits` when `anchors[].type=search` to record top hits (auditability).

## Minimal shape (conceptual)
```yaml
spec_version: agentos.decision-trace/v1
trace_id: DT-...
created_at: ISO-8601

state_ref: { state_id: AST-..., frame_id: F-..., objective_id: OBJ-... }

decision:
  id: DP-...
  kind: routing|scope|validation|install_gate
  question: "..."
  output: { value: "...", confidence: 0.0, mode: trial|installed|ask_user }

anchors:
  - id: A-1
    type: rule|doc|file|user|search|tool|kernel|memory_hint
    ref: { kind: path|message|query|command, value: "..." }
    lines: [1, 10]
    note: "why it matters"

graph_stack:
  - name: routing
    source: { source_kind: rule, source_ref: ".cursor/rules/description-routing.mdc", anchors: [A-1] }

graphs:
  - name: routing
    inputs: { "task.objective": "..." }
    path:
      - node_id: start
        condition: "true"
        result: true
        anchors_used: [A-1]
    output: { route: DISCOVER, confidence: 0.8 }

user_gate:
  asked: false
  question_id: null
  options: []
```

