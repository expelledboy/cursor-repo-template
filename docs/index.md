# Documentation Map (start here)

Read this file first. It lists the canonical sources of truth and where to add new information. Authority order: **reference -> how-to -> explanation -> tutorials -> work -> archive**.

## Documentation System

This repository uses a **Software-Defined Documentation System** optimized for Cursor IDE and AI agents.

- **Global Rule**: `.cursor/rules/00-global.mdc`
- **Context Rule:** `.cursor/rules/10-docs-routing.mdc`
- **System rationale**: `docs/explanation/architecture/doc-system-rationale.md` (why this structure exists)
- **Tutorial**: `docs/tutorials/getting-started.md` (learn the system)
- **Restructuring guide**: `docs/how-to/docs/content-aware-restructuring.md` (how to restructure docs systematically)

## Development Tools

Development environment setup and tooling (direnv, just, Nix Flake).

- **Tool stack reference**: `docs/reference/dev/tool-stack.md` (what each tool does)
- **Justfile editing rule**: `.cursor/rules/20-justfile.mdc` (load just reference + quickstart when editing a `justfile`)
- **Just quickstart**: `docs/how-to/dev/just-quickstart.md` (minimal setup + basic usage)
- **Just modules**: `docs/how-to/dev/just-modules.md` (module organization by domain)
- **Justfile reference**: `docs/reference/dev/justfile.md` (authoring guide and reference)
- **Setup guide**: `docs/how-to/dev/setup.md` (how to set up the environment)
- **Cursor integration**: `docs/how-to/dev/cursor-integration.md` (Cursor IDE workarounds)
- **Rationale**: `docs/explanation/dev/tool-stack-rationale.md` (why this stack)

## Your Project Domains

Add your project-specific domains here. Each domain should have:
- A **Context Rule** reference (`<rule-path>`)
- Canonical docs organized by type (reference, how-to, explanation)

**Example structure (example only):**
```markdown
## Your Domain Name
- **Context Rule:** `<rule-path>`
- Reference: `docs/reference/your-domain/config.md`
- How-to: `docs/how-to/your-domain/setup.md`
- Explanation: `docs/explanation/your-domain/architecture.md`
```

## AgentOS Framework
- **Context Rule (optional adapter):** `.cursor/rules/20-agentos.topic.mdc`
- Reference: `docs/reference/agentos/behavior-spec.md`
- Reference: `docs/reference/agentos/architecture.md`
- Reference: `docs/reference/agentos/components.md`
- Reference: `docs/reference/agentos/problem-registry.md`
- Reference: `docs/reference/agentos/routing.md`
- Reference: `docs/reference/agentos/context-compass.md`
- Reference: `docs/reference/agentos/safety-policy.md`
- Reference: `docs/reference/agentos/registry.md`
- Reference: `docs/reference/agentos/truth-surface.md`
- Reference: `docs/reference/agentos/verification-contract.md`
- Reference: `docs/reference/agentos/verification-gates.md`
- Reference: `docs/reference/agentos/meta-questions.md`
- Reference: `docs/reference/agentos/bootstrap-gates.md`
- Reference: `docs/reference/agentos/cursor-mechanics.md`
- Reference: `docs/reference/agentos/validation-scripts.md`
- Reference: `docs/reference/agentos/self-improvement.md`
- Reference: `docs/reference/agentos/self-model.md`
- Reference: `docs/reference/agentos/self-awareness-framework.md`
- Reference: `docs/reference/agentos/meta-analysis.md`
- Reference: `docs/reference/agentos/directive-tiers.md`
- Reference: `docs/reference/agentos/design-decision-templates.md`
- Reference: `docs/reference/agentos/complexity-determination.md`
- Reference: `docs/reference/agentos/workflow-variations.md`
- Reference: `docs/reference/agentos/data-model.md`
- Reference: `docs/reference/agentos/decision-record-format.md`
- Reference: `docs/reference/agentos/traceability.md`
- Reference: `docs/reference/agentos/state-surface.md`
- How-to: `docs/how-to/agentos/problem-intake.md`
- How-to: `docs/how-to/agentos/cursor-adapter.md` (Cursor adapter only)
- How-to: `docs/how-to/agentos/capture-gaps.md` (gap capture workflow)
- How-to: `docs/how-to/agentos/maintain-alignment.md`
- How-to: `docs/how-to/agentos/bootstrap-repo.md`
- How-to: `docs/how-to/agentos/porting-to-new-repo.md`
- How-to: `docs/how-to/agentos/validate-routing.md`
- How-to: `docs/how-to/agentos/maintain-registry.md`
- How-to: `docs/how-to/agentos/run-self-improvement-cycle.md`
- How-to: `docs/how-to/agentos/local-state.md`
- Tutorial: `docs/tutorials/agentos/using-commands.md` (learn how to use commands)
- Explanation: `docs/explanation/agentos/decision-records.md` (why decision records exist)
- Explanation: `docs/explanation/agentos/architecture-rationale.md`
- Explanation: `docs/explanation/agentos/design-highlights.md` (design rationale overview)
- Explanation: `docs/explanation/agentos/cursor-adapter-notes.md`
- Note: Adapter rules are optional and must not override core behavior.

## Work notes (non-authoritative)

Located under `docs/work/**` with dates and Status. Examples: `rfcs/`, `research/`, `verification/`, `plans/`, `reviews/`. Promote stable findings into reference/how-to/explanation, then add a Superseded banner to the work note or move it to `docs/archive/`.

## Adding new docs

- Stable facts/config/contracts -> `docs/reference/...`
- Repeatable steps/runbooks -> `docs/how-to/...`
- Rationale/architecture -> `docs/explanation/...`
- Drafts/notes/tests -> `docs/work/<category>/YYYY-MM-DD-<slug>.md` with a **Status** field.
- Superseded -> `docs/archive/` with a banner:
  `Status: Superseded | Superseded by: <path> | Date: YYYY-MM-DD | Reason: ...`

## When tasks change behavior or contracts

Update the relevant **reference** doc first, then link from how-to/explanation. If contracts/config change, also update tests/gates noted above.
