# Decision Record Format (Lean ADR, v7)

Status: Draft
Date: 2026-01-15
Purpose: Lean decision records to preserve “why” with minimal overhead.

## Location and naming
- Location: `docs/explanation/agentos/decisions/`
- Filename: `YYYY-MM-DD-<slug>.md` (kebab-case)

## Required fields (lean)
- Status (Proposed | Accepted | Superseded)
- Date (YYYY-MM-DD)
- Scope (mvp-v7)
- Problem IDs (V7-PRB-*)
- Context (max 5 bullets)
- Decision (max 5 bullets)
- Consequences (max 5 bullets)
- Artifacts (paths only)

## Template
```markdown
# Decision: <short title>

Status: Proposed
Date: YYYY-MM-DD
Scope: mvp-v7
Problem IDs: V7-PRB-0001
Supersedes: (optional)

## Context
- …

## Decision
- …

## Consequences
- Pros: …
- Cons: …

## Artifacts
- <path>
```

