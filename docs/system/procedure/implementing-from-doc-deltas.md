---
doc_status: stable
purpose: Define how to implement code changes from doc deltas.
intent: procedure
governed_by:
  docs/system/model/procedure-doc.md: Load if you need the contract for procedure docs
related:
  docs/system/model/doc-code-linking.md: Load if you need the doc-code linking contract
  docs/system/decision/require-doc-code-linking.md: Load if you need the decision that mandates doc-code linking
---

# Implementing from Doc Deltas

## Purpose
Ensure implementation changes match doc deltas.

## Inputs
- Doc changes that define the requirement delta.
- Objective graph entries that reference those docs.

## Doc Delta Definition
- List of changed docs.
- Changed sections or fields per doc.
- Intent summary for the change.

## Procedure
1) Identify the doc delta that defines the required change.
2) Map each doc change to implementation tasks.
3) Update code and add doc-code links for each task.
4) Verify implementation matches the doc delta scope.
5) If scope expands, return to negotiation and update docs.

## Validation
- Each implementation task references a doc change.
- Doc-code links exist in both docs and code.

## Failure Modes
- Code changes exceed the doc delta.
- Missing doc-code links for new implementation.
