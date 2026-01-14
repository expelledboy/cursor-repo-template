# Cursor Adapter Notes (Explanation)

**Status**: Stable
**Date**: 2026-01-13
**Purpose**: Explains Cursor-specific constraints without changing the core.

---

## 1. Adapter scope
- Cursor rules can load context but cannot enforce behavior.
- Cursor memories are opaque and not authoritative.
- The task plan header is the authoritative declaration of routing and directives.

## 2. Implications
- Always record what was loaded.
- Re-validate routing when rules or docs move.
- Treat missing rules as a bootstrap trigger.
- Rule isolation requires explicit loading; phase rules load only if their description matches the command or they are manually opened.
