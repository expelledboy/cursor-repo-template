# Cursor Mechanics (v7, stable constraints)

Status: Draft
Date: 2026-01-15
Purpose: Minimal, stable constraints about how Cursor features affect v7 decision graphing.

## External references (non-authoritative)
- `https://cursor.com/docs/context/rules`
- `https://cursor.com/docs/context/commands`
- `https://cursor.com/docs/context/mentions`
- `https://cursor.com/docs/context/semantic-search`
- `https://cursor.com/docs/context/mcp`

## Constraints used by v7
1) Rules are persistent instruction injectors. They can introduce graphs/docs; therefore traces MUST record provenance + anchors to rule files.
2) Mentions are explicit injections. Manual graph insertions that don’t fit the current chain default to a new branch.
3) Commands are deterministic entrypoints. Use them for trace display and state navigation (`/trace`, `/checkpoint`, `/resume`, `/branch`).
4) Semantic search suggests candidates but is not authoritative; record search anchors and tag provenance as `search_suggested`.
5) Tools/MCP produce evidence; record tool anchors (command + hash/excerpt) and tie them to decisions via `anchors_used`.

## Where v7 encodes this
- Mapping contract: `docs/reference/agentos/cursor-feature-mapping.md`
- Rationale: `docs/explanation/agentos/discoveries/2026-01-15-cursor-interplay-constrains-schemas.md`
