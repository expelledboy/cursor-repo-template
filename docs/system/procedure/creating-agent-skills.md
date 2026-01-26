---
doc_status: stable
purpose: Define how to create agent skills in agent/skills.
intent: procedure
governed_by:
  docs/system/model/procedure-doc.md: Load if you need the contract for procedure docs
related:
  docs/system/model/docs-skills-output.md: Load if you need the docs-skills output contract
  docs/system/model/reference-doc.md: Load if you need the contract for reference docs
  docs/dev/procedure/caching-external-references.md: Load if you need the cache procedure for skills
---

# Creating Agent Skills

## Purpose
Create skills that are discoverable, scoped, and reliable for agents.

## Inputs
- A clear outcome the skill enables.
- The trigger phrasing used to select the skill.
- Any required tools, permissions, or environment details.

## Procedure
1) Create a folder under `agent/skills/<skill-name>/`.
2) Add `SKILL.md` with YAML frontmatter including `name` and `description`.
3) Make the description begin with a trigger phrase, for example: "Use when ...".
4) Keep the body short and action oriented.
5) Prefer authoritative sources for external knowledge and use MCP to access them.
6) Add `references/` only when rapid recall is required.
7) If caching, store reference docs under `agent/skills/<skill>/references/` with `intent: reference` and `source_url`.
8) Add `scripts/` only when a repeatable command is required.
9) Run `just docs-skills` to confirm the skill is indexed.
10) If Cursor is not resolving skills, run `just sync-skills`.

## Validation
- The skill appears in `just docs-skills` output.
- The trigger phrase matches a real request.
- The skill can be executed without hidden context.
- External sources are linked instead of duplicated.

## Failure Modes
- Missing `name` or `description` in `SKILL.md`.
- The description is too vague to trigger correctly.
- The skill depends on tools or context not stated in the body.
