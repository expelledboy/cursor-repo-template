# Porting AgentOS to a New Repo (How-to)

**Status**: Stable
**Date**: 2026-01-13
**Purpose**: Procedure for porting AgentOS to a new repository.

---

## 1. Prerequisites
- `AGENTS.md` in repo root.
- `docs/index.md` exists or will be created by bootstrap.
- Global rules exist under `.cursor/rules/`.

## 2. Copy the core
- Copy `AGENTS.md` and the AgentOS docs folder structure.
- Copy `.cursor/rules/00-global.mdc` and `.cursor/rules/10-docs-routing.mdc`.

## 3. Align the repo
- Update `docs/index.md` with the repo domains.
- Define registry scope in `AGENTS.md` under **Registry Scope**.
- Identify the execution API (task runner or scripts).

## 4. Bootstrap if needed
If routing or directives are missing, run `docs/how-to/agentos/bootstrap-repo.md`.

## 5. Verify
- Confirm routing exists and matches `docs/index.md`.
- Confirm verification gates are aligned with CI.
- Record any gaps as work notes.
