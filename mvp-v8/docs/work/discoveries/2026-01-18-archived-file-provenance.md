---
title: "Archived File Provenance"
status: active
created_date: 2026-01-18
domain: agentos
Status: active---

# Archived File Provenance

## Observation
When files are moved to `docs/archive/`, the link to their original location is often lost. This breaks the "provenance chain" when other documents (like Decisions) reference the original path in their `related:` fields.

## Key Insights
- **Link Rot**: Moving a file to archive without recording its origin creates "ghost links" in the system.
- **Traceability**: Future readers need to know *where* an archived document used to live to understand its context.
- **Frontmatter Pattern**: Adding an `original_path` field to the frontmatter of archived files solves this deterministically.

## Implications
- Archived files become self-describing regarding their history.
- "Broken link" checkers can potentially use `original_path` to resolve redirects or validate historical references.
- Documentation refactoring becomes safer and more traceable.

## Recommendations
- Update the **Archiving Protocol**: When moving a file to `docs/archive/`, ALWAYS add `original_path: <path>` to its frontmatter.
- Update the **Superseded Banner**: Ensure the banner (if used) matches the metadata.
