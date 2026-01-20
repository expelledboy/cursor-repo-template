---
title: "Decision: Archived File Provenance"
status: accepted
created_date: 2026-01-18
purpose: "Mandate original_path metadata in archived files to preserve provenance"
domain: docs
related:
  - docs/work/discoveries/2026-01-18-archived-file-provenance.md
  - docs/reference/docs/doc-authority.md
---

# Decision: Archived File Provenance

## Decision
We mandate the inclusion of `original_path: <path>` in the frontmatter of all files moved to `docs/archive/`.

## Rationale
Moving files to the archive breaks the "provenance chain" when other documents (like Decisions) reference the original location in their `related:` fields. This creates "ghost links" and loss of context. By explicitly recording the original path, we ensure traceability and allow future tools to resolve historical references.

## Implications
-   **Archive Protocol**: Any process that archives a file (e.g., `/evolve`, `/distill`) must inject this field.
-   **Validation**: The documentation doctor or validator can verify that archived files have this field.
-   **Link Integrity**: `related:` fields pointing to old paths can potentially be resolved to the archive location.

## Implementation
-   Updated `docs/reference/docs/doc-authority.md` to include this requirement.
