# Spec: Active State (agentos.active-state/v1)

Status: Draft
Date: 2026-01-15
Purpose: Persist resumable context across summarization via a file artifact (not memory).

## Core requirements
- Summaries + anchors only (no copied excerpts).
- Frames form a **graph** (jumpable), not a stack.
- Objectives can be nested and can be paused/abandoned without losing history.
- Frames reference decision traces (by id) for review.

## Field reference
For a field-by-field breakdown of the schema, see:
- `docs/reference/agentos/schema-active-state.md`

## Important v7.1 hardening notes
- Prefer `anchor_registry` to avoid dangling anchor IDs in frames.
- Use `rehydration.trace_store_path` + `rehydration.trace_filename_template` to make persisted traces discoverable.

## Minimal shape (conceptual)
```yaml
spec_version: agentos.active-state/v1
state_id: AST-...
updated_at: ISO-8601

focus: { frame_id: F-ROOT, objective_id: OBJ-ROOT, phase: DISCOVER, mode: trial }

objectives:
  - id: OBJ-ROOT
    parent_id: null
    title: "..."
    status: active|paused|done|abandoned
    exit_reason: deprioritized|blocked|not_worth_it|superseded|null
    children: []

frames:
  - id: F-ROOT
    title: "..."
    summary: "1-3 sentences"
    anchors: [A-1]
    decision_trace_ids: [DT-1]
    links:
      - to: F-2
        kind: branch|resume|shift_context|supersede|depends_on
        note: "why"

navigation:
  recent_focus: [{ frame_id: F-ROOT, at: ISO-8601 }]

rehydration:
  required_rules: ["..."]
  required_docs: ["docs/reference/agentos/kernel.md"]
  state_file_path: ".agentos/active-state.yaml"
```

