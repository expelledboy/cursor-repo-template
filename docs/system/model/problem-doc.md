---
doc_status: stable
purpose: Define the structure and rules for problem docs.
intent: contract
governed_by:
  docs/system/governance.md: Load if you need global rules that govern problem contracts
implemented_by:
  scripts/docs/docs_validate.py: Load if you need to see enforcement of problem doc requirements
  docs/system/procedure/creating-problem-docs.md: Load if you need the procedure that implements this contract
related:
  docs/system/loading-policy.md: Load if you need the loading rules that require this contract
governs:
  docs/system/problem/context-limits-break-correctness.md: Load to verify this problem follows the contract
---

# Problem Doc Model

## Purpose
Define what a problem doc is and how it must be structured.

## Definition
A problem doc describes a specific situation that requires a decision or action.

## Required Frontmatter
- `doc_status`
- `purpose`
- `intent` (must be `problem`)
- `governed_by`
- `related` (required for linking to decisions)

## Required Body Sections
- Problem statement
- Scope and boundaries
- Consequences if unresolved
- Related decisions

## Scope Rules
- Define the problem in the smallest scope that still captures the risk.
- Exclude decisions, solutions, or procedures.

## Linkage Rules
- Link to at least one decision doc in `related`.
- Link to authority docs in `governed_by`.

## Naming and Path Guidance
- Use `docs/system/problem/<slug>.md`.
- Use a short verb phrase, for example `context-limits-break-correctness`.
