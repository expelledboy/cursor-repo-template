---
doc_status: stable
purpose: Define the intent vocabulary for docs.
intent: contract
governed_by:
  docs/system/governance.md: Load if you need global rules that govern intent vocabulary
implemented_by:
  scripts/docs/docs_validate.py: Load if you need to see enforcement of allowed intents
  scripts/docs/contract_specs.py: Load if you need the allowed intent list used by validation
---

# Intent Model

## Purpose
Intent describes how a document is used. `intent` does not grant authority.

## Initial Intent List
- `facts`: stable statements and constraints.
- `contract`: schemas, required fields, and validation rules.
- `constraints`: explicit limits and non-negotiables.
- `procedure`: steps to accomplish a task.
- `problem`: the situation that requires a decision.
- `rationale`: why a decision exists.
- `decision`: the choice and its outcome.
- `examples`: illustrative usage.
- `glossary`: definitions of terms.
- `skill`: reusable capability packages with explicit triggers.
- `reference`: external sources or cached upstream material.

## Management Rules
- The intent list is a controlled vocabulary.
- Additions or removals must update this document and the mapping doc.
- If an intent is retired, provide a migration note in the relevant decision doc.
