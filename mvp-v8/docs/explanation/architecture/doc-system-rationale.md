---
title: "Documentation system rationale (v8)"
status: draft
created_date: 2026-01-16
purpose: "Preserve the 'why' behind Hybrid Diátaxis + Domain for this fork"
domain: docs
---

# Documentation system rationale (v8)

## Goals
- Minimize context load while keeping sources of truth obvious.
- Separate content intents (facts vs procedures vs rationale vs drafts).
- Make Cursor agents reliable via rules that route to the smallest authoritative set.

## Design choices
- **Hybrid Diátaxis + Domain**: See `docs/reference/docs/doc-authority.md` for complete Diátaxis framework and domain organization rules.
- **Doc map first**: `docs/index.md` provides lightweight navigation to authoritative sources.
- **Routing layer**: `.cursor/rules/*.mdc` enables context-efficient loading based on task intent.
- **Content lifecycle**: Work content matures through validation into reference/how-to/explanation; local content remains ephemeral.
- **Problem/discovery integration**: Decisions link to problems and discoveries for complete solution traceability.
- **Registry system**: Bidirectional doc-code traceability through `implementations` fields and `@directive` annotations.
- **Advanced validation**: Categorized error reporting ensures content quality and structural consistency.
- **Dynamic indexing**: Sophisticated filtering enables efficient information discovery.

## See Also
- `docs/reference/docs/doc-authority.md` - Complete documentation structure and authority rules
- `docs/reference/docs/frontmatter-schema.md` - Metadata schema and validation
- `docs/how-to/docs/writing-effective-docs.md` - Content creation guidance

## Authority order
reference → how-to → explanation → tutorials → work → archive

## When to update
Update this rationale if we change doc buckets, authority order, or routing mechanisms.