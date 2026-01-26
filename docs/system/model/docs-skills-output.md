---
doc_status: stable
purpose: Define the contract for `just docs-skills` output.
intent: contract
governed_by:
  docs/system/governance.md: Load if you need global rules that govern this contract
implemented_by:
  scripts/docs/docs_skills.py: Load if you need the renderer that implements this contract
related:
  docs/system/procedure/creating-agent-skills.md: Load if you need steps to create indexed skills
---

# docs-skills Output Contract

## Purpose
Define the expected output of `just docs-skills`.

## Inputs
- Skill folders under `agent/skills/` with `SKILL.md`.

## Output
- Render a deterministic list of skills.
- Include `name`, `description`, and `path`.

## Constraints
- Output must be ASCII.
- Ordering must be deterministic.
