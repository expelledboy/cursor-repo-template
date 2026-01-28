---
doc_status: stable
purpose: Require agents to verify governance awareness at bootup and maintain it through session.
intent: decision
decision_status: accepted
decision_date: 2026-01-28
governed_by:
  docs/system/model/decision-doc.md: Load if you need the contract for decision docs
governs:
  docs/system/model/system-kernel-bootup.md: Load if you need the kernel contract this decision mandates
implemented_by:
  docs/system/procedure/agent-bootup.md: Load if you need the bootup procedure
  docs/system/procedure/kernel-evaluation.md: Load if you need the kernel evaluation procedure
  scripts/status.py: Load if you need the status command implementation
  AGENTS.md: Load if you need the agent instructions
related:
  docs/system/problem/injection-doesnt-guarantee-internalization.md: Load if you need the injection verification problem
  docs/system/problem/awareness-degrades-without-recovery.md: Load if you need the awareness degradation problem
  docs/system/problem/governed-edits-not-verified.md: Load if you need the governed edits problem
  docs/system/problem/context-loss-breaks-governance-executability.md: Load if you need the original compaction problem
  docs/system/decision/require-continuous-context-injection.md: Load if you need the injection decision this extends
---

# Decision: Require Bootup and Awareness Maintenance

## Decision Statement

Require agents to:

1. Run a health check at session start that verifies governance internalization
2. Maintain awareness through session via reporting and recovery mechanisms
3. Check and report authority before editing governed docs

## Context and Drivers

- **Injection is necessary but insufficient**: The decision to require continuous context injection (`.cursor/rules/`, `AGENTS.md`, etc.) ensures rules are delivered, but delivery doesn't guarantee internalization.
- **Awareness degrades silently**: Compaction, task transitions, and context noise erode governance awareness without any signal to the agent or user.
- **Governance is theoretical without verification**: The governance DAG exists, but if agents don't consult it at edit time, it becomes documentation rather than enforcement.

## Alternatives Considered

| Alternative | Outcome |
|-------------|---------|
| **Trust injection alone** | Rejected — No verification that agent absorbed rules |
| **Continuous re-injection** | Rejected — Token-expensive, still doesn't verify understanding |
| **Post-hoc validation only** | Rejected — Catches violations too late, after damage done |
| **Health check + maintenance** | Accepted — Verifies at start, maintains during, catches at edit time |

## Outcome and Implications

### Bootup Health Check

- Agent runs `just status` at session start
- This is a health check, not just display — if agent cannot produce accurate status, it must investigate
- If objective exists, agent loads and states understanding before proceeding

### Awareness Maintenance

- **Task transitions**: Report new task type minimally
- **Governed edits**: Before editing any governed doc, report "Editing X, governed by Y"
- **Compaction recovery**: Re-run `just status` AND reload kernel files if awareness is degraded

### Kernel Contract

- Defines minimal files that provide complete agent orientation
- Evaluated via procedure that reads all candidates and selects minimal set
- Total size constrained to < 15 KB

## Related Problems

- Injection doesn't guarantee internalization
- Awareness degrades without recovery
- Governed edits not verified
- Context loss breaks governance executability
