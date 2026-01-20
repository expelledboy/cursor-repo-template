# Schema rationale: Decision Graph fields

Status: Draft
Date: 2026-01-15
Scope: mvp-v7
Purpose: Explain why the fields in `schemas/decision-graph.yaml` exist (not what they are).

## Key drivers
- V7-DIS-0001: Cursor interplay constrains schemas (provenance + anchors + context).
- V7-DIS-0002: Trial vs install governance is required for safe reactivity.
- V7-PRB-0003 + ADR: 2026-01-15-context-contract.md (implicit context usage).

## Field rationale (lean)
| Field | Why it exists | Tied to |
|---|---|---|
| `spec_version` | Makes it safe to evolve the format over time without ambiguity. | (general) |
| `name` | Stable identifier so traces and docs can refer to “which graph ran”. | (general) |
| `description` | Ensures the graph’s intent is human-auditable (prevents “magic routing”). | V7-PRB-0001 |
| `context_contract` | Prevent graphs from silently depending on whatever context happened to be injected by rules/mentions/commands; makes portability possible. | V7-DIS-0001; V7-PRB-0003; ADR `docs/explanation/agentos/decisions/2026-01-15-context-contract.md` |
| `context_contract.required[]` | Forces explicit declaration of minimum context needed; avoids “implicit context usage”. | V7-PRB-0003 |
| `context_contract.required[].path` | Names the exact `context.*` dependency so missing fields can be detected and explained. | V7-PRB-0003 |
| `context_contract.required[].description` | Keeps required fields understandable during review. | (general) |
| `context_contract.required[].type` | Gives a human hint to reduce mis-population of context. | (general) |
| `context_contract.required[].enum` | Constrains expected values when the graph depends on categories. | (general) |
| `context_contract.required[].example` | Makes authoring/debugging easier without reading other docs. | (general) |
| `context_contract.optional[]` | Lets graphs improve decisions when extra context exists, without making it mandatory. | V7-DIS-0001 |
| `context_contract.optional[].path` | Names optional `context.*` refiners explicitly for auditability. | (general) |
| `context_contract.optional[].description` | Prevents optional fields from becoming “mystery knobs”. | (general) |
| `context_contract.optional[].type` | Human hint for optional fields. | (general) |
| `context_contract.optional[].enum` | Optional category constraints. | (general) |
| `context_contract.optional[].example` | Optional example values. | (general) |
| `context_contract.notes` | Place for one-line caveats (e.g., “missing required → ask user”). | V7-PRB-0003 |
| `expression_language` | Allows future tightening (CEL/JSON-Logic) without redefining the whole graph concept. | (general) |
| `trace` | Lets a graph express trace expectations while keeping global policy centralized. | V7-PRB-0001 |
| `trace.enabled` | Allows disabling trace only when truly unnecessary (default on). | V7-PRB-0001 |
| `trace.display_policy` | Keeps v7 condensed while guaranteeing inspectability at decision points (auto-display when asking). | V7-DIS-0001; ADR `docs/explanation/agentos/decisions/2026-01-15-decision-traces.md` |
| `nodes[]` | Core control-flow structure: makes reasoning deterministic and diffable. | V7-PRB-0009 (v7-local analog) |
| `nodes[].id` | Makes the executed path referenceable in traces (“we took node X”). | V7-PRB-0001 |
| `nodes[].type` | Limits node kinds to a small set to keep evaluation/trace semantics predictable. | (general) |
| `nodes[].question` | Makes node intent reviewable without reading condition strings. | V7-PRB-0001 |
| `nodes[].when` | Encodes branching logic as data (no hidden heuristics). | (general) |
| `nodes[].then` | Explicit edge for true branch (deterministic flow). | (general) |
| `nodes[].else` | Explicit edge for false branch (deterministic flow). | (general) |
| `nodes[].hit_policy` | Determines how decision tables resolve multiple matches (avoid ambiguity). | V7-PRB-0001 |
| `nodes[].rules[]` | Structured alternative to nested if/else; easier to review and diff. | V7-PRB-0001 |
| `nodes[].rules[].id` | Makes the winning rule auditable (“rule r2 matched”). | V7-PRB-0001 |
| `nodes[].rules[].when` | The condition for each candidate decision rule. | (general) |
| `nodes[].rules[].output` | Encodes the result of matching a rule (route/load/confidence/mode). | (general) |
| `nodes[].rules[].output.route` | The primary output most downstream systems act on. | (general) |
| `nodes[].rules[].output.load[]` | Ensures decision-making can deterministically pull in the right docs/graphs next. | V7-DIS-0001 |
| `nodes[].rules[].output.confidence` | Captures uncertainty without narrative; helps trigger “ask user” when low. | V7-PRB-0003 |
| `nodes[].rules[].output.mode` | Encodes Trial vs Installed vs Ask-user governance as data, so it can be traced and audited. | V7-DIS-0002; `docs/reference/agentos/decision-graphs/trial-install-gate.md` |
| `nodes[].ask` | Encodes user gates as data instead of ad-hoc questions. | V7-PRB-0003 |
| `nodes[].ask.prompt` | Explains *why* the user is being asked (keeps trust). | V7-PRB-0003 |
| `nodes[].ask.questions[]` | Makes questions/options deterministic and reusable. | V7-PRB-0003 |
| `nodes[].ask.questions[].id` | Makes responses referenceable in traces and state. | (general) |
| `nodes[].ask.questions[].text` | The user-visible question (explicit ambiguity resolution). | V7-PRB-0003 |
| `nodes[].ask.questions[].options[]` | Ensures the choice set is explicit (no hidden branching). | V7-PRB-0003 |
| `nodes[].ask.questions[].default` | Supports Trial-by-default behavior without forcing re-asking. | V7-DIS-0002 |
| `nodes[].ask.questions[].branch_default` | When a user inserts an out-of-band graph or shifts objectives, defaulting to branching preserves history (no rewriting). | V7-DIS-0003; ADR `docs/explanation/agentos/decisions/2026-01-15-active-state.md` |
| `nodes[].output` | Allows terminal nodes to emit a final decision result deterministically. | (general) |
| `nodes[].output.route` | Terminal route output. | (general) |
| `nodes[].output.load[]` | Terminal “what to load next” output. | V7-DIS-0001 |
| `nodes[].output.confidence` | Terminal confidence output. | (general) |
| `nodes[].output.mode` | Terminal governance mode output. | V7-DIS-0002 |
| `nodes[].output.next_graph` | Supports chaining graphs as the reasoning grows (without hardcoding). | V7-DIS-0001 |
| `nodes[].anchors_used[]` | Replaces vague “SIG_*” explanations with concrete artifact pointers; enables review and future improvement. | V7-DIS-0001; V7-PRB-0001; ADR `docs/explanation/agentos/decisions/2026-01-15-decision-traces.md` |
| `nodes[].provenance` | Records how a node/graph entered the chain (rule/mention/command/search); essential under Cursor interplay. | V7-DIS-0001; mapping `docs/reference/agentos/cursor-feature-mapping.md` |
| `nodes[].provenance.source_kind` | Prevents “unknown origin” logic; makes source auditable. | V7-DIS-0001 |
| `nodes[].provenance.source_ref` | Concrete pointer (rule path, message id, command) so the origin can be inspected later. | V7-DIS-0001 |

