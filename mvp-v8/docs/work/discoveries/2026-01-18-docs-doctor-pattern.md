---
title: "Documentation Doctor Pattern"
status: active
created_date: 2026-01-18
domain: agentos
status: active
---

# Documentation Doctor Pattern

## Observation
The "Doctor" command pattern (inspired by `brew doctor`) provides a powerful deterministic feedback loop for system health that differs from strict validation (CI/CD). It enables user-guided maintenance through diagnostic warnings rather than blocking errors.

## Key Insights
- **Diagnostic vs Blocking**: A "Doctor" checks for *health* (best practices, hygiene, warnings), whereas a "Validator" checks for *correctness* (syntax, broken links, errors).
- **Prescriptive Guidance**: Deterministic tools can provide actionable "Resolution" steps for each warning, reducing cognitive load on the user.
- **DOE Alignment**: This pattern perfectly fits the **Execution** layer of DOE. It is a deterministic tool that verifies the system state against Directives (standards).

## Implications
- Reduces "rot" in the documentation system (stale drafts, orphaned assets) that strict validation misses.
- Provides a "safe" way to guide users toward better practices without breaking their workflow.
- Can be applied to other domains (e.g., `agentos doctor` for checking rule conflicts).

## Recommendations
- Implement `just docs doctor` as a standard maintenance tool.
- Differentiate between "Errors" (Validator) and "Warnings" (Doctor) in the system architecture.
