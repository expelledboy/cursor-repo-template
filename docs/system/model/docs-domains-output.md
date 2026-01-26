---
doc_status: stable
purpose: Define the contract for `just docs-domains` output.
intent: contract
governed_by:
  docs/system/governance.md: Load if you need global rules that govern this contract
implemented_by:
  scripts/docs/docs_domains.py: Load if you need the renderer that implements this contract
related:
  docs/system/model/domain-doc.md: Load if you need the domain doc contract
  docs/system/decision/introduce-domain-index.md: Load if you need the decision that mandates this tool
  docs/system/loading-policy.md: Load if you need the procedure that consumes this output
---

# docs-domains Output Contract

## Purpose
Define the expected output of `just docs-domains`.

## Inputs
- Domain docs under `docs/domains/` with frontmatter.

## Output
- Render a deterministic list of domains.
- Include `domain_id`, `domain_scope`, and `domain_status`.

## Constraints
- Output must be ASCII.
- Ordering must be deterministic.
