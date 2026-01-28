---
doc_status: stable
purpose: Define authority and precedence for docs.
intent: contract
governed_by:
  docs/system/governance.md: Load if you need global rules that govern authority
governs:
  docs/system/loading-policy.md: Load to apply authority rules within loading steps
implemented_by:
  docs/system/loading-policy.md: Load if you need the procedure that operationalizes authority rules
related:
  docs/system/procedure/resolving-conflicts.md: Load if you need the conflict resolution procedure
---

# Authority Model

## Definitions
- Authority: the right to resolve conflicts between documents.
- Precedence: the deterministic ordering derived from governance links.

## Rules
- Authority is derived from `governs` and `governed_by` only.
- A document that `governs` another has higher authority.
- If two documents conflict, follow the `governed_by` chain upward.

## Conflict Resolution Protocol
1) Identify the conflict.
2) Trace `governed_by` upward until a governing document can resolve it.
3) Fix at the lowest governing document that can resolve it.
4) Propagate changes downward.
