# Documentation Map (start here)

Read this file first. It lists the canonical sources of truth and where to add new information. Authority order: **reference → how-to → explanation → tutorials → work → archive**.

## Documentation System

This repository uses a **Software-Defined Documentation System** optimized for Cursor IDE and AI agents.

- **Context Rule:** `.cursor/rules/10-docs-routing.mdc`
- **System rationale**: `docs/explanation/architecture/doc-system-rationale.md` (why this structure exists)
- **Tutorial**: `docs/tutorials/getting-started.md` (learn the system)
- **Restructuring guide**: `docs/how-to/docs/content-aware-restructuring.md` (how to restructure docs systematically)

## Development Tools

Development environment setup and tooling (direnv, just, Nix Flake).

- **Tool stack reference**: `docs/reference/dev/tool-stack.md` (what each tool does)
- **Justfile editing rule**: `.cursor/rules/20-justfile.mdc` (load just reference + quickstart when editing a `justfile`)
- **Just quickstart**: `docs/how-to/dev/just-quickstart.md` (minimal setup + basic usage)
- **Justfile reference**: `docs/reference/dev/justfile.md` (authoring guide and reference)
- **Setup guide**: `docs/how-to/dev/setup.md` (how to set up the environment)
- **Cursor integration**: `docs/how-to/dev/cursor-integration.md` (Cursor IDE workarounds)
- **Rationale**: `docs/explanation/dev/tool-stack-rationale.md` (why this stack)

## Your Project Domains

Add your project-specific domains here. Each domain should have:
- A **Context Rule** reference (`.cursor/rules/XX-domain-name.mdc`)
- Canonical docs organized by type (reference, how-to, explanation)

**Example structure:**
```markdown
## Your Domain Name
- **Context Rule:** `.cursor/rules/20-your-domain.topic.mdc`
- Reference: `docs/reference/your-domain/config.md`
- How-to: `docs/how-to/your-domain/setup.md`
- Explanation: `docs/explanation/your-domain/architecture.md`
```

## Work notes (non-authoritative)

Located under `docs/work/**` with dates and Status. Examples: `rfcs/`, `research/`, `verification/`, `plans/`, `reviews/`. Promote stable findings into reference/how-to/explanation, then add a Superseded banner to the work note or move it to `docs/archive/`.

## Adding new docs

- Stable facts/config/contracts → `docs/reference/...`
- Repeatable steps/runbooks → `docs/how-to/...`
- Rationale/architecture → `docs/explanation/...`
- Drafts/notes/tests → `docs/work/<category>/YYYY-MM-DD-<slug>.md` with a **Status** field.
- Superseded → `docs/archive/` with a banner:
  `Status: Superseded | Superseded by: <path> | Date: YYYY-MM-DD | Reason: …`

## When tasks change behavior or contracts

Update the relevant **reference** doc first, then link from how-to/explanation. If contracts/config change, also update tests/gates noted above.
