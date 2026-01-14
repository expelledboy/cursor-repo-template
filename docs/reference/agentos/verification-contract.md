# Verification Contract (Reference)

**Status**: Stable
**Date**: 2026-01-13
**Purpose**: Defines verification expectations and gate discipline.

---

## 1. Gate requirement
Every task must define verification gates aligned with CI.
If a gate catalog exists, reference `docs/reference/agentos/verification-gates.md`.

```mermaid
graph TD
    start[Task ready for verification] --> checkGates{Gates defined?}
    checkGates -->|No| defineGates[Define verification gates aligned with CI]
    checkGates -->|Yes| checkCatalog{Gate catalog exists?}
    defineGates --> checkCatalog
    checkCatalog -->|Yes| selectGates[Select gates from verification-gates.md]
    checkCatalog -->|No| useDefined[Use task-defined gates]
    selectGates --> checkRunnable{Can gates be run?}
    useDefined --> checkRunnable
    checkRunnable -->|No| listCommands[List exact commands and expected outcomes]
    checkRunnable -->|Yes| runGates[Run verification gates]
    listCommands --> report[Report: gates passed/deferred and commands listed]
    runGates --> checkResults{All gates pass?}
    checkResults -->|No| documentFail[Document failures and next steps]
    checkResults -->|Yes| report
    documentFail --> report
    report --> end[Verification complete]
```

> **Note:** This diagram is supplementary. The authoritative contract is in Section 1: Gate requirement above. See `docs/reference/agentos/verification-contract.md#1-gate-requirement` for complete requirements.

## 2. Gate hierarchy
- CI workflows are the minimum standard.
- Task-specific gates may add stricter checks.

## 3. Gate reporting
- Verification output must not be truncated.
- If gates cannot be run, list exact commands and expected outcomes.

## 4. Updates
If gates are missing or stale, capture a gap and update canonical docs.
