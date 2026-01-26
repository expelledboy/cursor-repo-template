---
doc_status: stable
purpose: Explain why docs separates `intent` from authority.
intent: rationale
governed_by:
  docs/system/governance.md: Load if you need global rules that this rationale must align with
---

# System Rationale

## Why Separate Intent from Authority
- `intent` helps route and load information.
- Authority resolves conflicts deterministically.
- Mixing these creates ambiguity when rationale or examples exist.

## Why Move Away from Fixed Buckets
- Buckets can force content into rigid bins.
- Governance links provide explicit authority without rigid directories.
- Intent tags preserve retrieval benefits without the overhead.

## Why Emphasize Context Loading
- Context limits are a hard constraint for agents.
- Missing constraints cause incorrect actions.
- A deterministic load policy reduces variance.
