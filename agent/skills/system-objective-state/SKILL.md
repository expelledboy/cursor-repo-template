---
name: system objective state
description: Use when you need to manage task state across sessions, after compaction, or for multi-step tasks that exceed context limits.
---

# Purpose
Persist and recover task state using the Objective Graph to survive context loss and ensure continuity across sessions.

# Scope
Covers the Objective Graph schema, state management lifecycle, and operational findings promotion. Does not cover governance rules (see `system-governance`) or context mechanics (see `system-context-mechanics`).

# Minimal Path
1) At session start, check if `docs/work/objective-graph.yaml` exists and load active objectives.
2) For complex tasks, create an objective with `id`, `goal`, `status`, and `next_actions`.
3) Update the objective as work progresses, recording blockers and findings.
4) Before closing an objective, promote any `operational_findings` to canonical docs.
5) Mark objective `done` only when all acceptance criteria are met.

# Validation
- Objective Graph parses as valid YAML matching the schema.
- Active objectives have clear `next_actions` defined.
- Closed objectives have empty or promoted `operational_findings`.

# Failure Modes
- Starting work without checking existing objective state (context loss).
- Leaving objectives open with stale `next_actions`.
- Closing objectives without promoting findings (knowledge loss).

# References
- `docs/system/model/objective-graph.md`: Schema and semantics
- `docs/system/procedure/maintaining-objective-graph.md`: Lifecycle procedure
- `docs/system/procedure/promoting-operational-findings.md`: Findings promotion
- `docs/system/procedure/objective-graph-realignment.md`: Recovery from drift
