---
name: system context mechanics
description: Use when you need to understand context limits, loading order, compaction behavior, or optimize what is in the context window.
---

# Purpose
Understand and work within the constraints of agent context windows to maintain governance executability.

# Scope
Covers context window limits, loading order, compaction behavior, and continuous injection mechanisms. Does not cover governance rules (see `system-governance`) or task state (see `system-objective-state`).

# Minimal Path
1) Understand that context windows are finite and compaction is inevitable.
2) Prioritize loading governance pointers (`loading-policy.md`, `core-values.md`) early.
3) Use skills and on-demand loading rather than stuffing all docs into context.
4) For long sessions, periodically re-anchor to governance docs.
5) Record operational findings before context loss occurs.

# Validation
- Critical governance docs remain accessible throughout the session.
- Compaction does not silently drop authority constraints.
- Agent behavior remains aligned after context pressure.

# Failure Modes
- Assuming all initial context survives indefinitely.
- Overloading context with non-essential docs.
- Losing governance awareness after compaction without re-injection.

# References
- `docs/dev/facts/agent-mechanics.md`: Universal constraints on context behavior (all runtimes)
- `docs/dev/facts/cursor-mechanics.md`: Cursor-specific context mechanics
- `docs/dev/facts/opencode-mechanics.md`: OpenCode-specific context mechanics
- `docs/system/loading-policy.md`: What to load and when
- `docs/system/decision/require-continuous-context-injection.md`: Why injection is required
