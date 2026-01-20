# AgentOS v7 Problem Registry

Status: Draft
Date: 2026-01-15
Purpose: Self-contained list of problems that motivate design in this fork. Problems are stable and additive.

## ID format
V7-PRB-0001 (zero-padded, monotonic)

## Status
Proposed | Accepted | Superseded

## Registry (lean)
| ID | Title | Status | Statement | Evidence (lean) | Detection signals |
|---|---|---|---|---|---|
| V7-PRB-0001 | Uninspectable decision path | Proposed | Agent decisions are not consistently reviewable as a structured graph path with concrete anchors. | User report: rationale is lost when chat closes (2026-01-15). | User asks “why”; agent can’t show evaluated path/anchors. |
| V7-PRB-0002 | Context decay across summarization | Proposed | Without an artifact, context/state is lost across summarization/session boundaries. | User report: need resumable active state (2026-01-15). | Repeated re-explaining; inability to resume prior frame/objective. |
| V7-PRB-0003 | Implicit context usage | Proposed | Graphs can accidentally rely on undefined `context` fields. | User request: graphs declare `context_contract` (2026-01-15). | Graph evaluation depends on missing fields; inconsistent branching. |

