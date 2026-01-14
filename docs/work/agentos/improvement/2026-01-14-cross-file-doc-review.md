# Improvement: Cross-File Doc Review

**Status**: Draft
**Date**: 2026-01-14
**Event**: retrospective
**Task**: Cross-file review of docs/**/*.md per self-improvement process
**Evidence**: Manual cross-file review recorded in this note
**Affected artifacts**: `docs/reference/agentos/*`, `docs/how-to/agentos/*`, `docs/explanation/agentos/*`, `docs/work/agentos/research/2026-01-13-codex-session-truncated.md`, `docs/reference/dev/*`, `docs/how-to/dev/*`, `docs/index.md`, `docs/tutorials/getting-started.md`

## Planned
Batch all docs by domain/type, read fully, and surface cross-file alignment gaps with concrete action items.

## Observed
- AgentOS core references are internally consistent and traceability covers PRB-0001 through PRB-0011.
- Several non-AgentOS docs lack the Status/Date/Purpose header pattern used in core references (dev/tooling and doc-system docs).
- A work note (`docs/work/agentos/research/2026-01-13-codex-session-truncated.md`) is missing Status/Date and contains many historical references to non-existent docs.
- Some lists in `docs/reference/agentos/components.md` have inconsistent indentation that reads as nested bullets.
- Tutorial and index examples use real-looking paths without marking them as placeholders, which makes automated reference checks noisy.

## Why it happened
The AgentOS core was standardized first; peripheral and tutorial docs were created earlier or outside the stricter template and never normalized.

## Action items
- Normalize metadata headers (Status/Date/Purpose) for dev/tooling and doc-system docs where appropriate.
- Add Status/Date to the codex session work note and label historical references as non-authoritative.
- Mark example-only paths in the tutorial and index as placeholders (e.g., fenced blocks or explicit “example” labels).
- Fix bullet indentation in `docs/reference/agentos/components.md` for consistent rendering.
- Consider adding a lightweight “audit mode” note that explicitly permits loading all doc types for cross-file reviews.
