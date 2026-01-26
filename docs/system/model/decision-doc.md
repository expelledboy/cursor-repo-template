---
doc_status: stable
purpose: Define the structure and rules for decision docs.
intent: contract
governed_by:
  docs/system/governance.md: Load if you need global rules that govern decision contracts
implemented_by:
  scripts/docs/docs_validate.py: Load if you need to see enforcement of decision doc requirements
  docs/system/procedure/creating-decision-docs.md: Load if you need the procedure that implements this contract
related:
  docs/system/loading-policy.md: Load if you need the loading rules that require this contract
governs:
  docs/system/decision/separate-intent-from-authority.md: Load to verify this decision follows the contract
  docs/system/decision/domain-first-organization.md: Load to verify this decision follows the contract
  docs/system/decision/automate-governed-by-graph.md: Load to verify this decision follows the contract
  docs/system/decision/enforce-doc-contracts.md: Load to verify this decision follows the contract
  docs/system/decision/introduce-domain-index.md: Load to verify this decision follows the contract
  docs/dev/decision/prefer-authoritative-sources.md: Load to verify this decision follows the contract
---

# Decision Doc Model

## Purpose
Define what a decision doc is and how it must be structured.

## Definition
A decision doc records a choice, the drivers behind it, and its implications.

## Required Frontmatter
- `doc_status`
- `purpose`
- `intent` (must be `decision`)
- `decision_status` (accepted, rejected, superseded, reversed)
- `decision_date` (YYYY-MM-DD)
- `governed_by`
- `related` (required for linking to problems)

## Required Body Sections
- Decision statement
- Context and drivers
- Alternatives considered
- Outcome and implications
- Related problems

## Decision Types
- Reversible
- Irreversible
- Time bound

## Linkage Rules
- Link to at least one problem doc in `related`.
- Link to authority docs in `governed_by`.

## Naming and Path Guidance
- Use `docs/system/decision/<slug>.md`.
- Use a short verb phrase, for example `separate-intent-from-authority`.
