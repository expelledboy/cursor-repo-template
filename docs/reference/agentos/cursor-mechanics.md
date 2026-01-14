# Cursor Mechanics (Reference)

**Status**: Stable
**Date**: 2026-01-13
**Purpose**: Describes Cursor rule and memory behavior as adapter constraints.

---

## 1. Rule types
- Project rules under `.cursor/rules/`.
- User rules in global settings.
- Memories are automatic and opaque.

## 2. Rule matching
- `alwaysApply` rules always load.
- `description` rules use keyword matching.
- `globs` rules match file paths.
- Multiple rules can apply at once.
- Cursor does not auto-load rules referenced inside docs; rules must match or be explicitly opened.

## 3. Mode constraints
- Ask mode is read-only.
- Agent mode can write and run commands, subject to sandbox limits.

## 4. Adapter implications
- Rules can load context but cannot enforce behavior.
- Memories are not authoritative.
- Routing must be explicit in the task plan header.
- Commands are adapter-only entrypoints; core behavior lives in canonical docs.
