---
doc_status: stable
purpose: Define the structure and rules for procedure docs.
intent: contract
governed_by:
  docs/system/governance.md: Load if you need global rules that govern procedure contracts
implemented_by:
  scripts/docs/docs_validate.py: Load if you need to see enforcement of procedure doc requirements
  docs/system/procedure/creating-procedure-docs.md: Load if you need the procedure that implements this contract
  docs/system/procedure/validating-doc-contracts.md: Load if you need the procedure that validates contracts
  docs/system/procedure/creating-domain-docs.md: Load if you need the procedure that creates domain docs
related:
  docs/system/loading-policy.md: Load if you need the loading rules that require this contract
governs:
  docs/system/procedure/creating-problem-docs.md: Load to verify this procedure follows the contract
  docs/system/procedure/creating-decision-docs.md: Load to verify this procedure follows the contract
  docs/system/procedure/creating-procedure-docs.md: Load to verify this procedure follows the contract
  docs/system/procedure/validating-doc-contracts.md: Load to verify this procedure follows the contract
  docs/system/procedure/creating-domain-docs.md: Load to verify this procedure follows the contract
  docs/system/procedure/creating-agent-skills.md: Load to verify this procedure follows the contract
  docs/system/loading-policy.md: Load to verify this procedure follows the contract
  docs/dev/procedure/creating-discovery-procedures.md: Load to verify this procedure follows the contract
  docs/dev/procedure/caching-external-references.md: Load to verify this procedure follows the contract
  docs/system/procedure/maintaining-objective-graph.md: Load to verify this procedure follows the contract
  docs/system/procedure/objective-graph-realignment.md: Load to verify this procedure follows the contract
  docs/system/procedure/promoting-operational-findings.md: Load to verify this procedure follows the contract
  docs/system/procedure/objective-graph-behavior-guide.md: Load to verify this procedure follows the contract
  docs/system/procedure/defining-evaluation-frameworks.md: Load to verify this procedure follows the contract
  docs/system/procedure/implementing-from-doc-deltas.md: Load to verify this procedure follows the contract
  docs/system/procedure/resolving-conflicts.md: Load to verify this procedure follows the contract
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
