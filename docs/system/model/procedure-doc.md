---
doc_status: stable
purpose: Define the structure and rules for procedure docs.
intent: contract
governed_by:
  docs/domains/system.md: Load if you need domain rules that constrain procedure contracts
implemented_by:
  scripts/docs/docs_validate.py: Load if you need to see enforcement of procedure doc requirements
  docs/system/procedure/creating-procedure-docs.md: Load if you need the procedure that implements this contract
  docs/system/procedure/validating-doc-contracts.md: Load if you need the procedure that validates contracts
related:
  docs/system/loading-policy.md: Load if you need the loading rules that require this contract
governs:
  docs/system/procedure/creating-problem-docs.md: Load to verify this procedure follows the contract
  docs/system/procedure/creating-decision-docs.md: Load to verify this procedure follows the contract
  docs/system/procedure/creating-procedure-docs.md: Load to verify this procedure follows the contract
  docs/system/procedure/validating-doc-contracts.md: Load to verify this procedure follows the contract
---

# Procedure Doc Model

## Purpose
Define what a procedure doc is and how it must be structured.

## Definition
A procedure doc is a step by step guide to achieve a task outcome.

## Required Frontmatter
- `doc_status`
- `purpose`
- `intent` (must be `procedure`)
- `governed_by`

## Required Body Sections
- Purpose
- Inputs
- Procedure
- Validation
- Failure modes

## Scope Rules
- Procedures implement facts and constraints.
- Do not include rationale unless it affects steps.

## Linkage Rules
- Link to authority docs in `governed_by`.
- Use `related` to point at supporting facts or decisions.

## Naming and Path Guidance
- Use `docs/system/procedure/<slug>.md`.
- Use an action phrase, for example `creating-decision-docs`.
