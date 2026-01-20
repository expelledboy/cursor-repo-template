---
title: "Decision: Mandatory Migration Validation Gates"
status: accepted
created_date: 2026-01-18
purpose: "Prevent cumulative migration errors through mandatory validation checkpoints"
domain: agentos
related:
  - docs/work/problems/2026-01-18-cumulative-migration-errors.md
---

# Decision: Mandatory Migration Validation Gates

## Decision
We mandate that all multi-step file operations (migrations, bulk edits, restructuring) must include validation gates between each step. Operations must validate successfully before proceeding to the next step.

## Rationale
Recent documentation migrations demonstrated how errors compound without intermediate validation, leading to corrupted files and manual cleanup burden. By requiring validation at each step, we prevent the accumulation of issues that become difficult to diagnose and fix.

## Implications
- **Slower Operations**: Each step includes validation overhead
- **Higher Reliability**: Issues caught immediately when they occur
- **Easier Debugging**: Problems isolated to specific operation steps
- **User Confidence**: Operations become predictable and trustworthy

## Implementation
- **Core Rule**: Added `Migration Validation Gates` to `.cursor/rules/core.mdc`
- **Validation Command**: Use `just docs::validate` or equivalent after each file operation step
- **Atomic Operations**: Design operations to be individually testable and revertible