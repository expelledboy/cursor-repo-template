---
doc_status: stable
purpose: Define why agent awareness degrades during sessions without recovery mechanisms.
intent: problem
governed_by:
  docs/system/model/problem-doc.md: Load if you need the contract for problem docs
related:
  docs/system/problem/context-loss-breaks-governance-executability.md: Load if you need the original compaction problem
  docs/system/problem/injection-doesnt-guarantee-internalization.md: Load if you need the related verification gap
  docs/system/decision/require-bootup-and-awareness-maintenance.md: Load if you need the decision that addresses this problem
---

# Problem: Awareness Degrades Without Recovery

## Problem Statement

Agent awareness of governance degrades during a session due to compaction, task transitions, and context noise. There is no mechanism to detect this degradation or recover awareness mid-session.

## Scope and Boundaries

- Applies to long sessions and complex tasks
- Covers compaction (context pruned by runtime) and drift (focus shifts away from governance)
- Distinct from initial injection — this is about awareness maintenance over time
- Applies to all agent runtimes with finite context windows

## Consequences

- Agent loses governance awareness without realizing it has been lost
- Decisions made late in session may violate constraints that were known earlier
- No recovery path when awareness is lost — agent continues in degraded state
- Compaction is silent — agent doesn't know context was pruned

## Related Decisions

- Require awareness maintenance through session
- Require compaction recovery (re-run status, reload kernel files)
- Require task transition reporting
