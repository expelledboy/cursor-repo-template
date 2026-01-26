---
doc_status: stable
purpose: Map tasks to required intents for context loading.
intent: contract
governed_by:
  docs/system/governance.md: Load if you need global rules that govern this mapping
implemented_by:
  scripts/docs/docs_validate.py: Load if you need to see enforcement of the task mapping
  scripts/docs/contract_specs.py: Load if you need the mapping used by validation
related:
  docs/system/loading-policy.md: Load if you need the procedure that uses this mapping
---

# Task to Intent Mapping

## Required Intents by Task
- `setup`: `facts`, `procedure`, `constraints`
- `operate`: `facts`, `procedure`, `constraints`
- `debug`: `facts`, `procedure`, `constraints`, `examples`
- `change`: `facts`, `procedure`, `constraints`, `decision`
- `explain`: `facts`, `rationale`, `glossary`
- `decide`: `facts`, `problem`, `decision`, `rationale`, `constraints`

## Notes
- `examples` are optional unless the task is `debug`.
- `contract` docs are required when creating or changing docs.
