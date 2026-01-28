---
doc_status: stable
purpose: Record the decision to require doc-code linking for implementation changes.
intent: decision
decision_status: accepted
decision_date: 2026-01-28
governed_by:
  docs/system/model/decision-doc.md: Load if you need the required fields for decision docs
related:
  docs/system/problem/doc-code-links-missing.md: Load if you need the problem that motivates this decision
  docs/system/model/doc-code-linking.md: Load if you need the doc-code linking contract
  docs/system/procedure/implementing-from-doc-deltas.md: Load if you need the implementation procedure
---

# Decision: Require Doc-Code Linking

## Decision Statement
Require explicit bidirectional links between docs and implementation files.

## Context and Drivers
- Doc changes must map to implementation changes deterministically.
- Linkage enables continuous alignment checks.

## Alternatives Considered
- Commit-based traceability only.
- Manual references in task notes.

## Outcome and Implications
- Docs must list `implemented_by` paths when they affect code.
- Code must declare which docs it implements.
- Validation must enforce missing links.

## Related Problems
- Context loss breaks alignment.
