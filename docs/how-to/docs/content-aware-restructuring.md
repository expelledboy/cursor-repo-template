---
status: stable
purpose: Procedure for restructuring docs via the precedence graph.
governed_by:
  docs/domains/docs.md: Docs domain governance
  docs/reference/docs/system-governance.md: System governance
---

# Content-Aware Documentation Restructuring

## Purpose
Refactor docs by following the `governs` and `governed_by` precedence graph.

## When To Use
- Mixed concerns across files
- Contradicting facts
- Overlapping procedures

## Process
1) Run: `just docs-index`
2) Identify governors for the affected files.
3) Fix conflicts at the nearest governing document.
4) Propagate changes down the chain.
5) Re-run `just docs-index` to validate links.

## Success Criteria
- Precedence chain is intact
- No conflicts between governed docs
- Canonicals are explicit
