---
doc_status: stable
purpose: Define the context loading procedure for docs.
intent: procedure
governed_by:
  docs/system/model/procedure-doc.md: Load if you need the contract for procedure docs
  docs/system/authority-model.md: Load if you need authority rules this procedure must obey
implements:
  docs/system/authority-model.md: Load if you need the authority rules this procedure enforces
related:
  docs/system/intent-task-matrix.md: Load if you need the required intents for the task
  docs/system/model/docs-index-output.md: Load if you need the output contract for docs-index
  docs/system/model/domain-doc.md: Load if you need the domain doc contract for scope definitions
  docs/system/model/docs-domains-output.md: Load if you need the domain index output contract
  docs/system/model/problem-doc.md: Load if you need the contract for problem docs you create or validate
  docs/system/model/decision-doc.md: Load if you need the contract for decision docs you create or validate
  docs/system/model/procedure-doc.md: Load if you need the contract for procedure docs you create or validate
  docs/system/procedure/creating-problem-docs.md: Load if you need steps to create problem docs
  docs/system/procedure/creating-decision-docs.md: Load if you need steps to create decision docs
  docs/system/procedure/creating-procedure-docs.md: Load if you need steps to create procedure docs
  docs/system/decision/automate-governed-by-graph.md: Load if you need the decision that defines this tool
  docs/system/decision/enforce-doc-contracts.md: Load if you need the decision that requires validation
  docs/system/procedure/validating-doc-contracts.md: Load if you need steps to validate doc contracts
implemented_by:
  scripts/docs/docs_index.py: Load if you need the tool that renders the governed_by DAG for loading
---

# Context Loading Policy

## Inputs
- `domain`
- `task`

## Procedure
1) Load the domain doc to understand scope and boundaries.
2) Load the `governed_by` chain up to the root for the target doc.
3) Determine the task from the user request.
4) Load docs whose `intent` is required by the task to intent mapping.
5) Validate that all required governing docs are present.
6) If the task creates or changes docs, load the relevant `contract` docs first.

## Task Discovery Rules
- `setup`: install, configure, bootstrap, first time use.
- `operate`: run, use, execute, deploy, standard workflow.
- `debug`: error, failure, broken, diagnose, fix.
- `change`: modify, extend, add, refactor, migrate.
- `explain`: why, rationale, architecture, tradeoff.
- `decide`: choose, evaluate, compare, pick.

## Compaction Safety
- Maintain a manifest of required docs for the current task, for example a checklist or `docs-index` output.
- After compaction, compare loaded docs to the manifest.
- If any required doc is missing, reload it before proceeding.

## Example Commands
- `just docs-index --from docs/system/governance.md`
- `just docs-index --from docs/system/problem/context-limits-break-correctness.md`
- `just docs-index`
- `just docs-domains`
- `just docs-skills`

## docs-index Output Interpretation
- The output is a governed_by DAG rendered as a branching tree.
- Repeated nodes appear multiple times to preserve all paths.
- `implemented_by` branches show enforcement or operationalization links.
- Output includes only active docs (`doc_status: stable`) by default.
