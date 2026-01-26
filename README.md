# Cursor Repository Template

A **Software-Defined Documentation System** optimized for Cursor IDE and AI agents.

## What This Is

A documentation structure that routes context intelligently, maintains single sources of truth, and self-corrects by linking content to routing rules.

## Quick Start

1. Copy this template to your project
2. Run `just docs-index --from docs/system/governance.md` (governed_by DAG)
3. Customize `AGENTS.md` for your project
4. Add your first domain docs and create a corresponding `.cursor/rules/*.mdc` (verify with `just docs-index`)

## Key Insight

The documentation system is **software**, not just text files. When you add a domain, you must update both:
- `just docs-index` output (governed_by DAG)
- `.cursor/rules/*.mdc` (the Router)

This bidirectional linking ensures agents can find and maintain context correctly.

## Learn More

- **System rationale**: `docs/system/system-rationale.md`
- **Loading policy**: `docs/system/loading-policy.md`

---

**Status**: Template | **Last Updated**: 2026-01-09
