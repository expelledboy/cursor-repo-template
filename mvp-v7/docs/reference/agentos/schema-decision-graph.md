# Schema: Decision Graph (agentos.decision-graph/v1)

Status: Draft
Date: 2026-01-15
Purpose: Field-by-field reference for `schemas/decision-graph.yaml`.

## Contract summary
- Graphs are deterministic data.
- Graph introduction is auditable via `provenance`.
- Graph evaluation is reviewable via decision traces + `anchors_used`.
- Graphs should declare `context_contract` to prevent implicit context dependencies.

## Rationale
See: `docs/explanation/agentos/schema-rationale-decision-graph.md`

## Top-level fields
| Field | Type | Required | Meaning | Notes / constraints |
|---|---|---:|---|---|
| `spec_version` | string | yes | Schema/version discriminator | Must be `agentos.decision-graph/v1`. |
| `name` | string | yes | Graph identifier | Used in traces (`graph_stack.name`, `graphs[].name`). |
| `description` | string | yes | What the graph decides | Keep short; “what output means”. |
| `expression_language` | string | no | Condition language | v1 supports `"string"` only (human-evaluated / engine-defined). |
| `trace` | object | no | Trace preference | `display_policy` should align with v7 kernel (auto-display on ask). |
| `context_contract` | object | no | Declares expected `context.*` fields | Prevents hidden coupling to injected context. |
| `nodes` | array | yes | Graph nodes | Nodes form a control flow graph by `then/else`. |

## `context_contract`
| Field | Type | Required | Meaning | Notes |
|---|---|---:|---|---|
| `required[]` | array | no | Required dot-paths | If missing at runtime, graph should deterministically ask user or take a fallback. |
| `optional[]` | array | no | Optional dot-paths | For fields that refine decisions when present. |
| `notes` | string | no | Human guidance | Keep short. |

Each entry supports:
`path` (required), optional `description`, `type` (hint), `enum`, `example`.

## Nodes
All nodes share:
| Field | Type | Meaning |
|---|---|---|
| `id` | string | Node identifier used by edges (`then/else`). |
| `type` | enum | `decision`, `decision_table`, `ask`, `terminal`. |
| `anchors_used[]` | string[] | Anchor IDs to cite in traces (concrete artifacts). |
| `provenance` | object | Why this node/graph was introduced (Cursor feature linkage). |

### Node type: `decision`
| Field | Meaning |
|---|---|
| `when` | Condition evaluated against `context`. |
| `then` / `else` | Next node ids (true/false). |
| `question` | Human-readable prompt for traces/UI. |

### Node type: `decision_table`
| Field | Meaning |
|---|---|
| `hit_policy` | `first` (default), `collect`, `priority`. v1 typically uses `first`. |
| `rules[]` | Ordered rules; the first matching `when` usually determines `output`. |

`rules[].output` supports: `route`, `load[]`, `confidence`, `mode`.

### Node type: `ask`
| Field | Meaning |
|---|---|
| `ask.prompt` | Why we are asking. |
| `ask.questions[]` | Structured user gate (id/text/options). |
| `ask.questions[].branch_default` | v7 default: `new_branch` (preserve history). |

### Node type: `terminal`
May include `output` for a final mode/route.

## Provenance (`provenance.source_kind`)
Must be consistent with `docs/reference/agentos/cursor-feature-mapping.md`:
`kernel_default`, `rule`, `user_mention`, `manual_insert`, `search_suggested`, `command`, `skill`.

