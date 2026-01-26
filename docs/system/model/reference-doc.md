---
doc_status: stable
purpose: Define the structure and rules for reference docs sourced externally.
intent: contract
governed_by:
  docs/system/governance.md: Load if you need global rules that govern reference docs
related:
  docs/system/procedure/creating-agent-skills.md: Load if you need the skill procedure that uses reference docs
  docs/dev/procedure/caching-external-references.md: Load if you need the procedure that caches references
---

# Reference Doc Model

## Purpose
Define how to capture external sources without claiming authority over them.

## Definition
A reference doc points to an external source and records where to find information.

## Required Frontmatter
- `doc_status`
- `purpose`
- `intent` (must be `reference`)
- `source_url`
- `governed_by`

## Required Body Sections
- Purpose
- Source Summary
- Refresh Policy
- Validation

## Scope Rules
- Do not restate upstream content beyond a brief summary.
- Do not include steps, decisions, or constraints.
- Prefer live access to the source unless caching is required for recall.

## Naming and Path Guidance
- Skill-scoped references live under `agent/skills/<skill>/references/`.
- Doc-scoped references live under `docs/reference/`.
