---
status: stable
purpose: Explain the rationale for the documentation system structure.
governed_by:
  docs/domains/docs.md: Docs domain governance
  docs/reference/docs/system-governance.md: System governance
---

# System Rationale

## Purpose
Explain why the documentation system is structured around precedence and governance.

## Why Precedence Matters
- Reduces contradictions
- Enables deterministic context loading
- Makes authority explicit

## Why Relationship-Based Governance
- Frontmatter links encode authority
- The `governs` graph is the source of precedence
- The system scales without central lists

## Maintenance Philosophy
- Fix at the lowest level that resolves misalignment
- Keep docs lean and explicit
