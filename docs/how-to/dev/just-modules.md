# Just Modules for Domain Tasks (How-to)

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Procedure for using just modules to colocate domain tasks with related code.

---

## 1. When to use modules
- Tasks are owned by a domain or subsystem.
- Recipes mostly touch files under a single domain folder.
- The task set is large enough to justify a boundary.

## 2. When NOT to use modules
- Cross-cutting workflows (format, lint, CI, release).
- Project-wide tasks that touch many domains.
- One-off recipes (keep in root until they grow).

## 3. Module placement
- Place the module in a subdirectory that owns the tasks.
- Use `mod.just` as the module file name in that directory.
- Example: `scripts/agentos/mod.just` for AgentOS validation tasks.

## 4. Working directory
- Module recipes run in the module directory by default.
- If module recipes must run from repo root, set `set working-directory := "../.."` in the module (adjust for depth).

## 5. Naming and ownership
- Module name matches domain folder (`auth`, `payments`, `ui`).
- Avoid ambiguous synonyms (`auth` vs `authn`).
- Ownership: domain owner maintains the module.

## 6. Root justfile responsibilities
- Declare modules with an explicit path: `mod <name> "<path>"`.
- Example: `mod agentos "scripts/agentos"`.
- Keep only global tasks in root.
- Document modules in comments or groups.

## 7. Recipe discovery standard
- Each module must have a short doc comment or `[doc]` entry.
- Root default must use `just --list --list-submodules`.

## 8. Invocation pattern
- Always use module namespace: `just <module>::<task>`.
- Example: `just agentos::validate-agentos`.
- Avoid root proxy recipes.

## 9. Migration checklist
- Move recipe to module.
- Update doc comments.
- Update any references in docs.
- Run `just --list --list-submodules` to confirm visibility.

## 10. Validation tasks
- If module adds validation tasks, name them consistently (e.g., `validate-*`).
- Prefer module namespace in docs (no root proxies).

## Related docs
- Reference: `docs/reference/dev/justfile.md`
- Tool stack: `docs/reference/dev/tool-stack.md`
