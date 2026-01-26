---
doc_status: stable
purpose: Define the structure and rules for domain docs.
intent: contract
governed_by:
  docs/system/governance.md: Load if you need global rules that govern domain docs
implemented_by:
  scripts/docs/docs_validate.py: Load if you need to see enforcement of domain doc requirements
  scripts/docs/docs_domains.py: Load if you need the domain index generator
related:
  docs/system/model/docs-domains-output.md: Load if you need the output contract for domain indexing
  docs/system/loading-policy.md: Load if you need the loading rules that use domain scope
  docs/system/procedure/creating-domain-docs.md: Load if you need the procedure for creating domain docs
  docs/system/decision/introduce-domain-index.md: Load if you need the decision that mandates domain indexing
governs:
  docs/domains/system.md: Load to verify this domain doc follows the contract
  docs/domains/dev.md: Load to verify this domain doc follows the contract
---

# Domain Doc Model

## Purpose
Define what a domain doc is and how it must be structured.

## Definition
A domain doc defines the scope and boundaries of a domain and acts as an index entry.

## Required Frontmatter
- `doc_status`
- `purpose`
- `intent` (must be `facts`)
- `domain_id`
- `domain_scope`
- `domain_status` (active, deprecated)
- `governed_by`

## Required Body Sections
- Purpose
- Scope
- Boundaries

## Scope Rules
- Domain docs define what belongs in the domain.
- Domain docs do not govern other docs.

## Naming and Path Guidance
- Use `docs/domains/<domain>.md`.
- Use the domain id as the filename.
