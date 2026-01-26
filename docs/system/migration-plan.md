---
doc_status: stable
purpose: Capture the current state and outline migration into `docs/`.
intent: procedure
governed_by:
  docs/domains/system.md: Load if you need domain constraints for migration
---

# Migration Plan

## Goal
Capture the current system understanding in `docs/` and migrate legacy content gradually.

## Immediate Capture
- System governance and authority rules live in `docs/system/`.
- Intent and task vocabularies are controlled here.
- Loading policy is the canonical procedure.

## Migration Steps
1) Inventory docs/ by domain and purpose.
2) For each doc, assign intent and domain.
3) Create or update `docs/<domain>/` equivalents under the domain folder.
4) Link authority using `governs` and `governed_by`.
5) Mark legacy docs as replaced once equivalents exist.

## Open Decisions
- Whether to keep docs/ directory structure long term.
- How to represent cross-domain authority at scale.
