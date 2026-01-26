---
doc_status: stable
purpose: Define the task vocabulary for docs.
intent: contract
governed_by:
  docs/system/governance.md: Load if you need global rules that govern task vocabulary
implemented_by:
  scripts/docs/docs_validate.py: Load if you need to see enforcement of allowed tasks
  scripts/docs/contract_specs.py: Load if you need the allowed task list used by validation
---

# Task Model

## Purpose
Tasks represent user goals that drive context loading.

## Initial Task List
- `setup`: install or configure for first use.
- `operate`: perform standard use.
- `debug`: diagnose or fix a problem.
- `change`: modify or extend behavior.
- `explain`: understand rationale or architecture.
- `decide`: choose among options.

## Management Rules
- The task list is a controlled vocabulary.
- Additions or removals must update this document and the mapping doc.
- Task discovery rules live in `docs/system/loading-policy.md`.
