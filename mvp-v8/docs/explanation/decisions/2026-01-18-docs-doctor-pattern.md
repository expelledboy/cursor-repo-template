---
title: "Decision: Documentation Doctor Pattern"
status: accepted
created_date: 2026-01-18
purpose: "Establish a distinct Diagnostic pattern for documentation health checks"
domain: agentos
related:
  - docs/reference/agentos/architecture.md
  - docs/work/discoveries/2026-01-18-docs-doctor-pattern.md
---

# Decision: Documentation Doctor Pattern

## Decision
We formally adopt the **Doctor Pattern** (Diagnostic Checks) as a distinct Execution primitive alongside **Validation** (Correctness Checks). We implement `just docs-doctor` as the standard tool for this pattern.

## Rationale
Strict validation (CI/CD) is binary: pass/fail. It cannot handle "hygiene" issues like stale drafts, orphaned assets, or organizational drift without blocking valid work.
The Doctor Pattern provides a non-blocking, deterministic feedback loop that offers:
1.  **Warnings vs Errors**: Distinguishing critical failures from maintenance needs.
2.  **Prescriptive Guidance**: Offering specific resolution steps for warnings.
3.  **Maintenance Automation**: Reducing the cognitive load of keeping the documentation system clean.

## Implications
-   **Architecture**: `architecture.md` now explicitly lists **Diagnostics** as an artifact of the Execution layer.
-   **Tooling**: `just docs-doctor` is available for maintenance tasks.
-   **Workflow**: Users/Agents should run the doctor periodically or as part of a restructuring session, but it does not block the build.

## Implementation
-   **Recipe**: `scripts/docs/mod.just` -> `doctor`
-   **Command**: `just docs-doctor`
