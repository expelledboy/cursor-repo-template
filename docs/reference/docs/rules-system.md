---
governed_by:
  "docs/reference/docs/system-governance.md": "System governance"
---

# Rules System (Reference)

Status: Stable
Date: 2026-01-23
Purpose: Defines Cursor rule behavior and how this repo uses rules to load context deterministically.

## 1. Rule types and scope
- Project rules under `.cursor/rules/`.
- User rules in Cursor settings.
- Team rules from dashboard (if enabled).
- `AGENTS.md` is plain markdown, no metadata.

## 2. Rule matching and activation
- `alwaysApply` rules always load.
- `description` rules are agent-decided (intent-based).
- `globs` rules match file paths in context.
- Multiple rules can apply at once.
- Rules referenced in docs do not auto-load.

Example (`globs`)
If `docs/reference/dev/tool-stack.md` is in context:
- `.cursor/rules/domain/docs.mdc` activates (glob `docs/**`).
- `.cursor/rules/domain/dev.mdc` activates (glob `docs/**/dev/**`).
- `.cursor/rules/system.mdc` always applies.

## 3. Context installation scenarios
- File-context driven: `globs` match active files.
- Task-intent driven: `description` triggers.
- System invariants: `alwaysApply`.

## 4. Repository discovery baseline
- `ls`
- `find docs -type f -name "*.md"`
- `just docs-index`

## 5. Rule selection conditions
- Always Apply: core system invariants (precedence, `AGENTS.md` role).
- Apply to Specific Files: domain routing by `globs`.
- Apply Intelligently: process workflows.
- Apply Manually: optional or rare workflows.

## 6. Adapter constraints
- Rules load context but do not enforce behavior.
- Memory is not authoritative.
- Routing must be explicit in task planning.
- Commands are adapter entrypoints; core behavior lives in canonicals.
