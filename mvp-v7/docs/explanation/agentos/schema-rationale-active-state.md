# Schema rationale: Active State fields

Status: Draft
Date: 2026-01-15
Scope: mvp-v7
Purpose: Explain why the fields in `schemas/active-state.yaml` exist (not what they are).

## Key drivers
- V7-PRB-0002 + ADR: 2026-01-15-active-state.md (context decay across summarization).
- V7-DIS-0003: Default branching preserves history under manual insertion and objective shifts.

## Field rationale (lean)
| Field | Why it exists | Tied to |
|---|---|---|
| `spec_version` | Allows state format evolution without ambiguity. | (general) |
| `state_id` | Gives traces and tooling a stable handle for “which state file” produced a decision. | V7-PRB-0002 |
| `updated_at` | Enables “is this state stale?” checks and ordering across sessions. | V7-PRB-0002 |
| `focus` | A deterministic “current pointer” avoids losing the active thread when context is summarized or when multiple branches exist. | V7-PRB-0002; ADR `docs/explanation/agentos/decisions/2026-01-15-active-state.md` |
| `focus.frame_id` | Selects which frame is the current working context in a frame graph. | V7-PRB-0002 |
| `focus.objective_id` | Ensures the agent stays aligned to the intended objective when multiple exist. | V7-PRB-0001; V7-PRB-0002 |
| `focus.phase` | Makes the current “mode of work” explicit (discover/act/check) to reduce drift. | V7-PRB-0001 |
| `focus.mode` | Records trial/installed/ask_user governance as part of the active state. | V7-DIS-0002 |
| `objectives[]` | Captures nested work and allows pausing/abandoning without deleting history (matches real developer workflow). | V7-PRB-0002; v7 objective-shift requirement |
| `objectives[].id` | Stable objective handle so frames/traces can reference it. | V7-PRB-0002 |
| `objectives[].parent_id` | Enables nested objectives without losing hierarchy. | V7-PRB-0002 |
| `objectives[].title` | Human-readable objective so the state is reviewable. | V7-PRB-0001 |
| `objectives[].status` | Supports pausing/abandoning without deletion (real workflows). | V7-PRB-0002 |
| `objectives[].exit_reason` | Makes “why we stopped” explicit for future self-improvement. | V7-PRB-0002 |
| `objectives[].children[]` | Allows deterministic traversal of objective tree (not implicit). | (general) |
| `objectives[].resume_hint` | Lightweight memory substitute: what to do if resuming later, without copying long text. | V7-PRB-0002 |
| `frames[]` | Stores resumable contexts as a graph of summaries + anchors, avoiding copying large text while staying auditable. | V7-PRB-0002; v7 “anchors-only” constraint |
| `frames[].id` | Stable frame handle for navigation and trace binding. | V7-PRB-0002 |
| `frames[].title` | Human-readable frame name for review/navigation. | (general) |
| `frames[].summary` | Keeps context compact and portable; details live in anchors. | V7-PRB-0002 |
| `frames[].created_at` | Supports ordering and “what happened when” across branches. | V7-PRB-0002 |
| `frames[].anchors[]` | Replaces copied excerpts with concrete pointers to artifacts. | V7-DIS-0001 |
| `frames[].decision_trace_ids[]` | Connects “what we decided” (trace) to “where we were” (frame) so auditability survives chat closure. | V7-PRB-0001, V7-PRB-0002 |
| `frames[].links[]` | Explicitly records why we branched/resumed/shifted context; prevents rewriting history when the user inserts an out-of-band graph. | V7-DIS-0003; ADR `docs/explanation/agentos/decisions/2026-01-15-active-state.md` |
| `frames[].links[].to` | Identifies the linked frame node (graph edge target). | (general) |
| `frames[].links[].kind` | Encodes the semantic meaning of the edge (branch/resume/shift/etc). | V7-DIS-0003 |
| `frames[].links[].note` | One-line explanation of why the edge exists (auditability). | V7-PRB-0001 |
| `frames[].links[].effect` | Captures objective changes caused by context shifts, without rewriting objective history. | V7-DIS-0003 |
| `frames[].links[].effect.objective_change` | Encodes pause/abandon/supersede as data. | V7-PRB-0002 |
| `frames[].links[].effect.from_objective_id` | Points at the objective being left behind. | V7-PRB-0002 |
| `frames[].links[].effect.to_objective_id` | Points at the objective being entered. | V7-PRB-0002 |
| `navigation` | Provides deterministic “how did we get here” without relying on chat scrollback. | V7-PRB-0002 |
| `navigation.recent_focus[]` | Gives a deterministic “back button” across a frame graph. | V7-PRB-0002 |
| `navigation.recent_focus[].frame_id` | The visited frame. | (general) |
| `navigation.recent_focus[].at` | When it was focused. | (general) |
| `rehydration` | Makes the state portable by declaring which rules/docs must be loaded alongside it; avoids opaque behavior changes. | V7-DIS-0001; v7 portability goal |
| `rehydration.required_rules[]` | Ensures the same routing constraints are present when resuming. | V7-DIS-0001 |
| `rehydration.required_docs[]` | Ensures minimal canonicals are loaded for deterministic operation. | V7-DIS-0001 |
| `rehydration.state_file_path` | Declares where the state lives so tools/rules can locate it consistently. | (general) |

