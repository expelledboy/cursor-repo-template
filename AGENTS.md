# Agent Guide

You are working in this repository. Follow this behavior contract on every task.

## Authority order
reference → how-to → explanation → work → archive. When docs conflict, defer to the highest authority.

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
