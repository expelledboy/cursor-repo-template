---
status: stable
purpose: Define the contract for `just docs-index` output.
governed_by:
  docs/reference/docs/system-governance.md: System governance
implemented_by:
  scripts/docs/docs_index.py: Docs index generator
---

# docs-index (Reference)

## What It Does
`just docs-index` prints a precedence tree of docs using `governed_by` links.
The output is used to load minimal context and verify governance links.

## Inputs
- Files under `docs/**` with YAML frontmatter.
- Relationship fields: `governed_by`, `governs`, `implements`, `implemented_by`, `related`.

## Output Contract
- Root is any doc with no in-repo `governed_by`. If multiple roots exist, a `ROOT` node is shown.
- Nodes are rendered with full paths and file size in KB.
- `implemented_by` is rendered as a child metadata node.
- Unlinked docs (not reachable from any root) are listed under `Unlinked`.

## Usage
- `just docs-index`
- `just docs-index --filter docs/reference/docs/system-governance.md`

## Constraints
- Output must be ASCII-only.
- Precedence is derived from `governed_by` only.
