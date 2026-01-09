# Cursor Repository Template

A **Software-Defined Documentation System** optimized for Cursor IDE and AI agents.

## What This Is

A documentation structure that routes context intelligently, maintains single sources of truth, and self-corrects by linking content to routing rules.

## Quick Start

1. Copy this template to your project
2. Read `docs/index.md` (the doc map)
3. Customize `AGENTS.md` for your project
4. Add your first domain to `docs/index.md` and create a corresponding `.cursor/rules/*.mdc`

## Key Insight

The documentation system is **software**, not just text files. When you add a domain, you must update both:
- `docs/index.md` (the Map)
- `.cursor/rules/*.mdc` (the Router)

This bidirectional linking ensures agents can find and maintain context correctly.

## Learn More

- **System rationale**: `docs/explanation/architecture/doc-system-rationale.md`
- **Getting started**: `docs/how-to/docs/getting-started.md`

---

**Status**: Template | **Last Updated**: 2026-01-09
