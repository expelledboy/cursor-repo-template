---
doc_status: stable
purpose: Define why context injection alone is insufficient for governance execution.
intent: problem
governed_by:
  docs/system/model/problem-doc.md: Load if you need the contract for problem docs
related:
  docs/system/problem/context-loss-breaks-governance-executability.md: Load if you need the original compaction problem this extends
  docs/system/problem/awareness-degrades-without-recovery.md: Related problem on awareness maintenance
  docs/system/decision/require-bootup-and-awareness-maintenance.md: Load if you need the decision that addresses this problem
---

# Problem: Injection Doesn't Guarantee Internalization

## Problem Statement

Context injection delivers governance rules to the agent, but delivery doesn't guarantee the agent internalized them. An agent can have rules in its context window without understanding or applying them.

## Scope and Boundaries

- Applies to all injection mechanisms (instructions, rules, AGENTS.md, skills)
- Distinct from injection failure (rules not delivered) — this is about verification of absorption
- Covers the gap between "rules are present" and "rules are followed"

## Consequences

- Agent proceeds without governance awareness despite rules being in context
- Rules are present but not followed — governance becomes advisory
- No signal that internalization failed — failures are silent
- Violations discovered late (at validation) or never

## Related Decisions

- Require bootup health check that verifies internalization
- Require awareness maintenance throughout session
