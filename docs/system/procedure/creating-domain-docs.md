---
doc_status: stable
purpose: Define how to create a domain doc.
intent: procedure
governed_by:
  docs/system/model/procedure-doc.md: Load if you need the contract for procedure docs
implements:
  docs/system/model/procedure-doc.md: Load if you need the contract this procedure must satisfy
implemented_by:
  scripts/docs/docs_domains.py: Load if you need the tool that indexes domain docs
related:
  docs/system/model/domain-doc.md: Load if you need the domain doc contract
  docs/system/decision/introduce-domain-index.md: Load if you need the decision that mandates this process
---

# Creating Domain Docs

## Purpose
Create a domain doc that defines scope and is indexable by `docs-domains`.

## When to Create
- A new domain is introduced.
- A domain scope changes materially.

## Steps
1) Create `docs/domains/<domain>.md`.
2) Set `doc_status`, `intent`, `domain_id`, `domain_scope`, and `domain_status` in frontmatter.
3) Write Purpose, Scope, and Boundaries sections.
4) Run `just docs-domains` to verify indexing.
5) Run `just docs-validate` to ensure compliance.

## Quality Checklist
- Scope is clear and bounded.
- The domain does not imply authority.
- Index fields are complete and accurate.

## Failure Modes
- Missing domain metadata in frontmatter.
- Scope overlaps another domain without clarification.
