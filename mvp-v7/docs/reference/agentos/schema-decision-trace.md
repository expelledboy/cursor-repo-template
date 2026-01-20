# Schema: Decision Trace (agentos.decision-trace/v1)

Status: Draft
Date: 2026-01-15
Purpose: Field-by-field reference for `schemas/decision-trace.yaml`.

## Contract summary
- A trace is a review artifact: which graphs were evaluated, what path fired, and which anchors justified it.
- Traces must be linkable to resumable state (`state_ref`).
- Graph introduction must be auditable (`graph_stack.source`).

## Rationale
See: `docs/explanation/agentos/schema-rationale-decision-trace.md`

## Top-level fields
| Field | Type | Required | Meaning | Notes |
|---|---|---:|---|---|
| `spec_version` | string | yes | Schema/version discriminator | Must be `agentos.decision-trace/v1`. |
| `trace_id` | string | yes | Trace identifier | Referenced by active-state frames via `decision_trace_ids`. |
| `created_at` | string | yes | Timestamp | ISO-8601 recommended. |
| `state_ref` | object | yes | Where this trace belongs | `state_id`, `frame_id`, `objective_id`. |
| `decision` | object | yes | The decision being recorded | Includes `kind`, `question`, and `output`. |
| `anchors[]` | array | yes | Concrete evidence pointers | Prefer file+lines; avoid copied long excerpts. |
| `graph_stack[]` | array | yes | Graph provenance chain | How each graph entered evaluation. |
| `graphs[]` | array | yes | Per-graph evaluation detail | Inputs + path + output. |
| `user_gate` | object | yes | Whether we asked the user | If `asked=true`, trace should be auto-displayed. |

## `decision`
| Field | Meaning |
|---|---|
| `id` | Links back to a decision point in a frame (human-level). |
| `kind` | `routing`, `scope`, `validation`, `install_gate`. |
| `question` | The prompt this decision answered. |
| `output.value` | The chosen value (route/mode/etc). |
| `output.confidence` | 0–1 confidence (human hint). |
| `output.mode` | `trial`, `installed`, `ask_user`. |

## Anchors (`anchors[]`)
Anchors are the replacement for vague signal labels in user-facing reasoning.

| Field | Meaning |
|---|---|
| `id` | Anchor identifier; referenced in `anchors_used`. |
| `type` | `kernel`, `user`, `rule`, `file`, `doc`, `search`, `tool`, `memory_hint`. |
| `ref.kind` | `path`, `message`, `query`, `command`. |
| `ref.value` | Path/message id/query/command string. |
| `lines` | Optional [start,end] for file/doc anchors. |
| `hash` | Optional fingerprint for tool output. |
| `note` | Why this anchor mattered (1 line). |

Constraints:
- If `type=search`, include the query in `ref.value` and include at least one `file` anchor for a top hit if possible.
- If `type=tool`, include `ref.kind=command` and set `hash` when feasible.

## Graph provenance (`graph_stack[]`)
| Field | Meaning |
|---|---|
| `name` | Graph name. |
| `source.source_kind` | Must follow `docs/reference/agentos/cursor-feature-mapping.md`. |
| `source.source_ref` | What introduced the graph (rule path, message id, command). |
| `source.anchors[]` | Anchor IDs supporting the provenance claim. |

## Graph evaluation detail (`graphs[]`)
| Field | Meaning |
|---|---|
| `name` | Graph name. |
| `source_ref` | Optional path to the graph artifact. |
| `inputs` | Minimal inputs used (enough to reproduce the branch). |
| `path[]` | Evaluated node steps (`node_id`, `condition`, `result`). |
| `path[].anchors_used[]` | Anchor IDs that justified that step. |
| `output.route/load/confidence` | The graph’s produced output. |

