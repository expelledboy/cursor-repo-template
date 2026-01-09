# Agent Guide

You are working in this repository. Follow this behavior contract on every task.

## Context Efficiency & The Compass
The "Context Window" is your scarcest resource. Do not load all docs. Use the **Diátaxis Compass** to decide what to read based on your task:

| If your task is... | And you need to... | Load ONLY... | Ignore... |
|---|---|---|---|
| **Coding / Execution** | Apply skills (Work) | **How-to** (Steps) + **Reference** (Facts) | Tutorials, Explanation |
| **Learning / Onboarding** | Acquire skills (Study) | **Tutorials** (Lessons) | Reference (too dense) |
| **Architecture / Design** | Understand context (Study) | **Explanation** (Why) + **Reference** (Facts) | Tutorials, How-to |

## Context Loading Quickstart (copy/paste)

Use these when you’re about to start work. They are designed to prevent “context bloat”.

- **Implement / modify code (execution task)**
  - **Load**: `docs/reference/<domain>/**` + `docs/how-to/<domain>/**` (and the domain’s `.cursor/rules/*.mdc` if it exists).
  - **Ignore**: `docs/tutorials/**` and `docs/explanation/**` unless you are blocked on intent/rationale.

- **Debug / troubleshoot**
  - **Load**: `docs/how-to/<domain>/**` first, then `docs/reference/<domain>/**` for contracts/invariants.
  - **Ignore**: `docs/tutorials/**` (learning) and most `docs/explanation/**` (background) unless needed.

- **Architecture / design / “why is it like this?”**
  - **Load**: `docs/explanation/<domain>/**` + `docs/reference/<domain>/**`.
  - **Ignore**: `docs/how-to/**` and `docs/tutorials/**`.

- **Onboarding / learn the system**
  - **Load**: `docs/tutorials/**` only.
  - **Ignore**: `docs/reference/**` until you need exact facts/contracts.

## Authority order
reference → how-to → explanation → tutorials → work → archive. When docs conflict, defer to the highest authority.

## First steps for any task
1) Read `docs/index.md` (doc map + sources of truth).
2) Load only the minimal relevant docs (Cursor Rules route context).
3) For third‑party/vendor details, use MCP (e.g., Context7); do **not** embed external facts into project docs as truth.
4) Implement change + verification.
5) If contracts/config/flows change: update the canonical **reference** doc first, then link from how-to/explanation.

## Creating or updating docs
- Stable, evergreen facts → `docs/reference/**`.
- Repeatable procedures → `docs/how-to/**`.
- Rationale/architecture → `docs/explanation/**`.
- Drafts/notes/plans/tests → `docs/work/<category>/YYYY-MM-DD-<slug>.md` with a **Status** field.
- Use lowercase kebab-case filenames (no ALL_CAPS). When adding dates to filenames or headers, use the actual current date in `YYYY-MM-DD` (no placeholders).
- Superseded material goes to `docs/archive/` with a banner:
  `Status: Superseded | Superseded by: <path> | Date: YYYY-MM-DD | Reason: …`
- Do not create new top-level markdown files outside `docs/` unless agreed.

## Context routing (Cursor)
- Rules live in `.cursor/rules/*.mdc`. They describe when to load which docs.
- Always honor `alwaysApply` rules (global guardrails) and topic/file routing rules.
- Keep rules in sync with `docs/index.md`. If you add a new domain or change canonical paths, update the corresponding `.cursor/rules/*.mdc`.

## Verification expectations
- Prefer targeted tests (unit/component/e2e) relevant to your change; if you run suites, do **not** truncate output.
- When contracts/config/flows change, run the documented testing gates in `docs/index.md`.

## MCP
- Use MCP for volatile external knowledge (library/vendor docs).
- Keep project truths (flows, mappings, env vars, contracts) in repo docs.

## Where to start
- Read `docs/index.md` for the doc map, sources of truth, and where to put new information.
