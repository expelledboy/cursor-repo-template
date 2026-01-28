---
doc_status: stable
purpose: Define why agents can edit governed docs without verifying authority.
intent: problem
governed_by:
  docs/system/model/problem-doc.md: Load if you need the contract for problem docs
related:
  docs/system/problem/doc-code-links-missing.md: Load if you need the related traceability problem
  docs/system/decision/require-bootup-and-awareness-maintenance.md: Load if you need the decision that addresses this problem
---

# Problem: Governed Edits Not Verified

## Problem Statement

Agents can edit governed documents without checking authority or reporting the edit. The governance DAG exists but isn't consulted at edit time, making governance advisory rather than enforced.

## Scope and Boundaries

- Applies to all docs with `governed_by` relationships
- Covers both checking authority before edit and reporting after
- Distinct from post-hoc validation (which catches violations too late)
- Applies to any agent making doc changes

## Consequences

- Governance is advisory, not enforced — agents may violate authority without knowing
- Authority violations discovered late (at `just docs-validate`) or never
- No accountability trail for edits — unclear if agent checked governance
- The governance DAG becomes documentation rather than active constraint

## Related Decisions

- Require agents to report before editing governed docs
- Report format: "Editing X, governed by Y"
