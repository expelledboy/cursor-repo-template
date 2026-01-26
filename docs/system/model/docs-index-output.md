---
doc_status: stable
purpose: Define the contract for `just docs-index` output.
intent: contract
governed_by:
  docs/system/governance.md: Load if you need global rules that govern this contract
implemented_by:
  scripts/docs/docs_index.py: Load if you need the renderer that implements this contract
related:
  docs/system/loading-policy.md: Load if you need the procedure that consumes this output
  docs/system/decision/automate-governed-by-graph.md: Load if you need the decision that mandates this tool
---

# docs-index Output Contract

## Purpose
Define the expected output of `just docs-index`.

## Inputs
- Docs under `docs/` with frontmatter.
- Relationships: `governed_by`, `governs`, `implements`, `implemented_by`, `related`.

## Output
- Render the `governed_by` DAG for active docs as a branching tree.
- Render `implemented_by` as a child branch under the source doc.
- Include file sizes in KB.

## Output Format
- Unicode tree glyphs are allowed.
- Output is deterministic for a given docs state.

## Flags
- `--from <path>`: render the graph starting from a specific entrypoint.
  Use only active docs unless the loader is configured otherwise.

## Interpretation
- Repeated nodes appear multiple times to preserve all paths.
- `implemented_by` branches indicate enforcement or operationalization.
- `[cycle]` indicates a detected cycle during traversal.

## Constraints
- Ordering must be deterministic.
