# Schema: Active State (agentos.active-state/v1)

Status: Draft
Date: 2026-01-15
Purpose: Field-by-field reference for `schemas/active-state.yaml`.

## Contract summary
- Active-state is a resumability artifact (not memory).
- Frames are a graph of contexts; objectives can be nested and paused/abandoned.
- Frames link to decision traces for auditability.

## Rationale
See: `docs/explanation/agentos/schema-rationale-active-state.md`

## Top-level fields
| Field | Type | Required | Meaning | Notes |
|---|---|---:|---|---|
| `spec_version` | string | yes | Schema/version discriminator | Must be `agentos.active-state/v1`. |
| `state_id` | string | yes | State identifier | Stable handle for traces (`state_ref.state_id`). |
| `updated_at` | string | yes | Timestamp | ISO-8601 recommended. |
| `focus` | object | yes | Current working pointer | `frame_id`, `objective_id`, `phase`, `mode`. |
| `objectives[]` | array | yes | Objective tree | Nested objectives; supports pause/abandon. |
| `frames[]` | array | yes | Context frames graph | Summaries + anchors only; links represent navigation/branching. |
| `navigation` | object | yes | Navigation history | `recent_focus` is a deterministic “back button”. |
| `rehydration` | object | yes | Required reload context | Which rules/docs must be loaded with this state. |

## `focus`
| Field | Meaning |
|---|---|
| `frame_id` | Current frame node. |
| `objective_id` | Current objective node. |
| `phase` | High-level phase (DISCOVER/SHAPE/ACT/CHECK/CLOSE). |
| `mode` | Governance mode (trial/installed/ask_user). |

## Objectives (`objectives[]`)
| Field | Meaning |
|---|---|
| `id` | Objective id. |
| `parent_id` | Parent objective id or null. |
| `title` | One-line objective. |
| `status` | `active`, `paused`, `done`, `abandoned`. |
| `exit_reason` | If not active/done, why (deprioritized/blocked/not_worth_it/superseded). |
| `children[]` | Child objective ids. |
| `resume_hint` | Optional: what to do if resuming later. |

## Frames (`frames[]`)
Frames are graph nodes. They must remain small.

| Field | Meaning |
|---|---|
| `id` | Frame id. |
| `title` | Short name. |
| `summary` | 1–3 sentences; no copied excerpts. |
| `anchors[]` | Anchor IDs (concrete references to files/docs/rules). |
| `decision_trace_ids[]` | Trace IDs associated with this frame. |
| `links[]` | Edges to other frames (branch/resume/shift_context/supersede/depends_on). |

### Frame links (`frames[].links[]`)
| Field | Meaning |
|---|---|
| `kind` | Edge semantic: `branch`, `resume`, `shift_context`, `supersede`, `depends_on`. |
| `note` | Why the link exists (1 line). |
| `effect` | Optional: objective change (`pause`, `abandon`, `supersede`). |

v7 constraint:
- Manual graph insertion or objective shift defaults to `kind=branch` unless explicitly a refinement.

## Navigation (`navigation.recent_focus`)
List of `{frame_id, at}` to enable deterministic “back” navigation.

## Rehydration (`rehydration`)
| Field | Meaning |
|---|---|
| `required_rules[]` | Rule names that must be loaded alongside the state. |
| `required_docs[]` | Canonical docs required for deterministic operation. |
| `state_file_path` | Path to the active-state file (usually `.agentos/active-state.yaml`). |

