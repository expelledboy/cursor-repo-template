---
doc_status: stable
purpose: Define governance constraints for the docs system domain.
intent: contract
governed_by:
  docs/system/governance.md: Load if you need the global rules this domain must obey
governs:
  docs/system/authority-model.md: Load to apply system domain constraints to authority rules
  docs/system/intent-model.md: Load to use the system domain intent vocabulary
  docs/system/task-model.md: Load to use the system domain task vocabulary
  docs/system/intent-task-matrix.md: Load to apply the system domain task mapping
  docs/system/loading-policy.md: Load to apply domain rules to context loading
  docs/system/system-rationale.md: Load to understand rationale within this domain
  docs/system/migration-plan.md: Load to migrate legacy docs into this domain
  docs/system/model/docs-index-output.md: Load to use the system domain docs-index contract
  docs/system/model/problem-doc.md: Load to use the system domain problem contract
  docs/system/model/decision-doc.md: Load to use the system domain decision contract
  docs/system/model/procedure-doc.md: Load to use the system domain procedure contract
  docs/system/procedure/creating-problem-docs.md: Load to follow the system domain problem procedure
  docs/system/procedure/creating-decision-docs.md: Load to follow the system domain decision procedure
  docs/system/procedure/creating-procedure-docs.md: Load to follow the system domain procedure procedure
  docs/system/procedure/validating-doc-contracts.md: Load to follow the system domain validation procedure
  docs/system/problem/context-limits-break-correctness.md: Load to see a canonical system problem
  docs/system/decision/separate-intent-from-authority.md: Load to see a canonical system decision
  docs/system/decision/domain-first-organization.md: Load to see a canonical system decision
  docs/system/decision/automate-governed-by-graph.md: Load to see a canonical system decision
  docs/system/decision/enforce-doc-contracts.md: Load to see a canonical system decision
---

# System Domain

## Purpose
Define governance constraints for the docs system domain.

## Constraints
- System docs must comply with `docs/system/governance.md`.
- Authority is resolved by the governance graph, not by intent.
- Changes that affect loading or authority must update the mapping doc.
