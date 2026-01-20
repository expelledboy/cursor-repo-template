# Cursor Feature Mapping (v7, stable constraints)

Status: Draft
Date: 2026-01-15
Purpose: Canonical mapping from Cursor features → allowed contributions to decision graphing (provenance + anchors).

## Core rule
Every Cursor feature must map to one (or more) of:
- Graph introduction (adds graphs or graph bundles)
- Evidence anchoring (adds concrete anchors)
- Deterministic entry (commands)

If a feature introduces a graph, the decision trace MUST record provenance and anchors.

## Mapping (contract)
| Cursor feature | Allowed contributions | Provenance `source_kind` | Anchor types to record |
|---|---|---|---|
| Rules | Graph introduction; evidence anchoring | `rule` | `rule`, `doc`, `file` |
| Mentions | Graph introduction (manual); evidence anchoring | `user_mention` or `manual_insert` | `user`, `file`, `doc`, `rule` |
| Commands | Deterministic entry; evidence anchoring | `command` | `tool` (command), `doc` (if command loads docs) |
| Semantic search | Candidate suggestion; evidence anchoring | `search_suggested` | `search` (query + hits), `file` |
| Tools/MCP | Evidence anchoring | `tool` (record as provenance where relevant) | `tool` (command + hash/excerpt) |

## Constraints
- Semantic search is never authoritative; it may suggest, but must be recorded as `search_suggested`.
- Tool outputs are evidence anchors; tie them to specific decisions via `anchors_used`.
- Manual graph insertion defaults to a new branch frame (preserve history).

