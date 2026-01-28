---
doc_status: stable
purpose: Define required doc-code linking for implementation changes.
intent: contract
governed_by:
  docs/system/governance.md: Load if you need global rules that govern doc-code linking
related:
  docs/system/decision/require-doc-code-linking.md: Load if you need the decision that mandates doc-code linking
  docs/system/procedure/implementing-from-doc-deltas.md: Load if you need the implementation procedure
---

# Doc-Code Linking Model

## Purpose
Define how docs and code must link to ensure alignment.

## Required Doc Frontmatter
- `implemented_by` when the doc changes implementation.
- `implements` when the doc operationalizes another doc.

## Required Code Annotations
- Code files must declare which docs they implement using a header comment.
- Example: `# @implements docs/system/procedure/example.md`

## Scope Rules
- Required for procedures that direct code changes.
- Required for contracts that define runtime behavior.
- Not required for glossary, rationale, or external reference docs.
- If unsure, add the link.

## Validation Rules
- Doc links must exist in code.
- Code annotations must point to existing docs.
- Missing links are validation errors.
