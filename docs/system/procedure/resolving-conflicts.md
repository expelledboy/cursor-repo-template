---
doc_status: stable
purpose: Define how to classify and resolve doc or implementation conflicts.
intent: procedure
governed_by:
  docs/system/model/procedure-doc.md: Load if you need the contract for procedure docs
related:
  docs/system/authority-model.md: Load if you need authority rules for conflict resolution
---

# Resolving Conflicts

## Purpose
Resolve conflicts by escalating to the appropriate governing document.

## Inputs
- The conflicting docs or code behavior.
- The governing chain for each doc.

## Conflict Classification
- Semantic mismatch: docs say X, code does Y.
- Scope mismatch: doc scope excludes the code behavior.
- Authority mismatch: lower doc contradicts a governing doc.
- Outdated source: external authority changed.

## Procedure
1) Classify the conflict type (semantic, scope, authority, outdated source).
2) Write a one-sentence conflict note explaining the classification.
3) Identify the lowest governing doc that can resolve the issue.
4) Update that governing doc first.
5) Propagate changes downward to governed docs.
6) Re-validate relationships.

## Validation
- Conflicts are resolved at the lowest governing authority.
- Governing chains are consistent after updates.

## Failure Modes
- Fixes applied only at the leaf document.
- Conflicts resolved without checking governing chains.
