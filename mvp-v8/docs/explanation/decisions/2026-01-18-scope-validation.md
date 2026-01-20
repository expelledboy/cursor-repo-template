---
title: "Decision: Mandatory Scope Verification"
status: accepted
created_date: 2026-01-18
purpose: "Prevent premature optimization by enforcing scope validation before execution"
domain: agentos
related:
  - docs/work/problems/2026-01-18-premature-optimization-failure.md
---

# Decision: Mandatory Scope Verification

## Decision
We mandate that the agent must explicitly validate the **Scope** of every request before creating a plan or executing a fix. The agent must categorize the request as either:
1.  **Local Patch**: A fix for a specific file, command, or instance.
2.  **Systemic Pattern**: A general change to rules, behaviors, or architecture.

If the scope is ambiguous, the agent MUST ask the user for clarification.

## Rationale
The agent previously demonstrated a tendency to "prematurely optimize," applying narrow fixes to broad problems without verifying user intent. This leads to:
-   **Misaligned Solutions**: Solving symptom X when the user wanted to cure disease Y.
-   **Fragmentation**: Creating special cases instead of coherent patterns.
-   **Inefficiency**: Wasting cycles on fixes that need to be undone or generalized later.

By forcing a "Scope Check" at the start of the Orchestration phase, we ensure the agent's mental model matches the user's requirements.

## Implications
-   **Slower Start**: The agent may ask more clarifying questions at the beginning of a task.
-   **Better Alignment**: The probability of "missed requirements" drops significantly.
-   **Architectural Coherence**: Fixes will naturally gravitate towards systemic improvements (Rules/Commands) when appropriate, rather than ad-hoc patches.

## Implementation
-   **Core Rule**: Added `Scope Verification Mandate` to `.cursor/rules/core.mdc`.
-   **Process**: Agent must self-query "Is this local or systemic?" during planning.
