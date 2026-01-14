# Decision Record Format (ADR)

**Status**: Stable
**Date**: 2026-01-13
**Purpose**: Defines the required format for AgentOS decision records (Reference/Contract).

---

## 1. Location and naming
- Location: `docs/explanation/agentos/decisions/`
- Filename: `YYYY-MM-DD-<slug>.md` (kebab-case)

## 2. Required fields
- Status (Proposed | Accepted | Superseded)
- Date (YYYY-MM-DD)
- Scope
- Problem IDs (from `docs/reference/agentos/problem-registry.md`)
- Decision
- Alternatives
- Consequences
- Why this worked
- Artifacts (docs/files affected)

## 3. Status rules
- Proposed: awaiting ratification.
- Accepted: ratified and implemented or scheduled.
- Superseded: replaced by another ADR (must link).

## 4. Template
```markdown
# Decision: <short title>

**Status**: Proposed
**Date**: YYYY-MM-DD
**Scope**: agentos
**Problem IDs**: PRB-0001
**Supersedes**: (optional) <adr-file>

## Context
## Decision
## Alternatives
## Consequences
## Why this worked
## Artifacts
- <path>
```
