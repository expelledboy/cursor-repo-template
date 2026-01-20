---
title: "Restructuring Runtime Implementation Issues"
status: active
created_date: 2026-01-18
domain: agentos
type: problem
related:
  - docs/explanation/process/restructuring-v2-rationale.md
  - docs/archive/2026-01-17-runtime-execution-review.md
---

# Restructuring Runtime Implementation Issues

## Context
A review of the v2 restructuring runtime execution (Run ID: DOCS-RUN-20260117-180258) identified several implementation gaps in the tooling.

## Issues

### 1. Validator Path Resolution (Critical)
**Observation**: Validator reports files don't exist when they actually do.
**Root Cause**: Validator uses `Path('docs') / related_path` which may not resolve correctly from script location.
**Impact**: False positive validation errors; inability to auto-fix links.
**Fix**: Update validator to use absolute paths or proper project-root resolution.

### 2. Opportunity Prioritization (High)
**Observation**: Prioritization step exists but scoring was manual/estimated.
**Impact**: Prioritization isn't systematic or reproducible.
**Fix**: Implement the scoring algorithm: `(Impact × Value) / (Risk × Effort)`.

### 3. User Input Handling (High)
**Observation**: Approval gate triggered, but user approval was simulated/skipped.
**Impact**: Interaction model is broken.
**Fix**: Tooling must actually block on `ask` steps and wait for user response.

### 4. Bidirectional Link Verification (Medium)
**Observation**: Checked for `@directive` but didn't fix or add it.
**Impact**: Traceability remains incomplete.
**Fix**: Implement logic to auto-add `@directive` to simple files and flag complex ones.

### 5. Metrics Tracking (Medium)
**Observation**: Partial metrics capture (baseline yes, efficiency no).
**Impact**: Cannot measure time-per-file or opportunities-per-batch.
**Fix**: Add timing and efficiency metrics to execution log.
