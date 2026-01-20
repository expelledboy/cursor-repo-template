# Schema rationale: Decision Trace fields

Status: Draft
Date: 2026-01-15
Scope: mvp-v7
Purpose: Explain why the fields in `schemas/decision-trace.yaml` exist (not what they are).

## Key drivers
- V7-DIS-0001: Cursor interplay requires provenance + anchors.
- V7-PRB-0001 + ADR: 2026-01-15-decision-traces.md (uninspectable decision path).
- Cursor mapping contract: `docs/reference/agentos/cursor-feature-mapping.md`.

## Field rationale (lean)
| Field | Why it exists | Tied to |
|---|---|---|
| `spec_version` | Allows trace format evolution without ambiguity. | (general) |
| `trace_id` | Stable handle to reference a trace from active-state frames. | V7-PRB-0001 |
| `created_at` | Enables ordering and correlating traces across branches/sessions. | V7-PRB-0002 |
| `state_ref` | Traces must be resumable and navigable; tying to state/frame/objective prevents “floating reasoning” that dies with chat. | V7-PRB-0002; ADR `docs/explanation/agentos/decisions/2026-01-15-active-state.md` |
| `state_ref.state_id` | Binds a trace to a specific active-state artifact. | V7-PRB-0002 |
| `state_ref.frame_id` | Lets you jump back to the exact context frame that produced the decision. | V7-PRB-0002 |
| `state_ref.objective_id` | Keeps decisions tied to the correct objective thread when multiple exist. | V7-PRB-0002 |
| `decision` | Ensures every trace is “about a decision,” not just a log blob. | V7-PRB-0001 |
| `decision.id` | Links the trace to a decision point identifier used in state/notes. | (general) |
| `decision.kind` | Keeps trace semantics consistent across common decision types. | (general) |
| `decision.question` | Preserves the user-facing “what was being decided” for review. | V7-PRB-0001 |
| `decision.output` | Captures the final outcome as data (not prose). | V7-PRB-0001 |
| `decision.output.value` | The chosen value (route/mode/etc) that downstream actions depend on. | (general) |
| `decision.output.confidence` | Captures uncertainty in a compact way; supports “ask user” thresholds. | V7-PRB-0003 |
| `decision.output.mode` | Records Trial/Installed/Ask-user governance decisions as data. | V7-DIS-0002 |
| `anchors[]` | Human-auditable evidence pointers (rules/docs/files/search/tools) to replace vague “signals” and preserve review across sessions. | V7-DIS-0001; V7-PRB-0001 |
| `anchors[].id` | Enables nodes/path steps to cite anchors without copying them repeatedly. | (general) |
| `anchors[].type` | Makes the *kind* of evidence explicit (rule vs search vs tool). | V7-DIS-0001 |
| `anchors[].ref` | Ensures anchors point to a concrete thing (path/message/query/command). | V7-PRB-0001 |
| `anchors[].ref.kind` | Disambiguates how to interpret `ref.value`. | (general) |
| `anchors[].ref.value` | Stores the actual pointer (file path, message id, query, command). | (general) |
| `anchors[].lines` | Allows precise pointing without copying text; supports “show me where.” | V7-PRB-0001 |
| `anchors[].note` | One-line justification for why the anchor mattered. | V7-PRB-0001 |
| `anchors[].hash` | Tool outputs can be large; a hash lets you refer to evidence stably without dumping it. | V7-DIS-0001 |
| `graph_stack[]` | Records how each graph entered the chain (rule vs mention vs search vs command), which is essential given Cursor feature interplay. | V7-DIS-0001; mapping `docs/reference/agentos/cursor-feature-mapping.md` |
| `graph_stack[].name` | Names the graph so provenance is readable. | (general) |
| `graph_stack[].source` | Groups provenance fields under a stable shape. | V7-DIS-0001 |
| `graph_stack[].source.source_kind` | Makes the introducing mechanism explicit. | V7-DIS-0001 |
| `graph_stack[].source.source_ref` | Concrete pointer to the introducer (rule path/message/command). | V7-DIS-0001 |
| `graph_stack[].source.anchors[]` | Lets provenance cite the evidence anchors that justify “this is how it was introduced.” | V7-DIS-0001 |
| `graphs[]` | Captures per-graph evaluation so “why” is path-based, not narrative. | V7-PRB-0001 |
| `graphs[].name` | Links the per-graph detail to the graph stack entry. | (general) |
| `graphs[].source_ref` | Allows pointing to the concrete graph artifact that was evaluated. | V7-PRB-0001 |
| `graphs[].source_ref.kind` | Disambiguates reference type (v1 uses `path`). | (general) |
| `graphs[].source_ref.value` | Path to graph artifact for auditability. | V7-PRB-0001 |
| `graphs[].inputs` | Captures the minimum “decision surface” used so the path can be reviewed/replayed without relying on full chat history. | V7-PRB-0001 |
| `graphs[].path[]` | The actual evaluated path is the “why”; without it, traces become narrative again. | V7-PRB-0001; ADR `docs/explanation/agentos/decisions/2026-01-15-decision-traces.md` |
| `graphs[].path[].node_id` | Names the step taken (so you can point to the exact node). | V7-PRB-0001 |
| `graphs[].path[].condition` | Preserves the rule/guard that was evaluated (deterministic explanation). | V7-PRB-0001 |
| `graphs[].path[].result` | Records the boolean outcome, avoiding “hand-wavy” why. | V7-PRB-0001 |
| `graphs[].path[].anchors_used[]` | Ties a path step to concrete evidence rather than vibes. | V7-DIS-0001 |
| `graphs[].output` | Captures the graph-produced output distinct from the trace’s decision output. | (general) |
| `graphs[].output.route` | Primary result of this graph’s evaluation. | (general) |
| `graphs[].output.load[]` | Records what was loaded/should be loaded next due to this graph. | V7-DIS-0001 |
| `graphs[].output.confidence` | Captures graph-level confidence as a compact hint. | (general) |
| `user_gate` | The moment we ask is the moment review is most valuable; this field makes that explicit and machine-detectable. | V7-DIS-0001; v7 kernel trace policy |
| `user_gate.asked` | Enables automatic “show trace now” behavior only when needed. | V7-PRB-0001 |
| `user_gate.question_id` | Makes the asked question referenceable and consistent across flows. | (general) |
| `user_gate.options[]` | Ensures the choice set is explicit and reviewable (no hidden branches). | V7-PRB-0003 |

