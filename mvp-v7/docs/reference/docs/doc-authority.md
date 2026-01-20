# Doc authority + structure (v7, Reference)

Status: Draft
Date: 2026-01-15
Purpose: Deterministically route documentation changes using Hybrid Diátaxis + Domain.

## Authority order (conflict resolver)
reference → how-to → explanation → tutorials → work → archive

## Where content goes
- **Reference (`docs/reference/**`)**: stable facts, contracts, schemas, invariants.
- **How-to (`docs/how-to/**`)**: repeatable procedures, runbooks.
- **Explanation (`docs/explanation/**`)**: rationale and “why”.
- **Tutorials (`docs/tutorials/**`)**: learning-oriented walkthroughs.
- **Work (`docs/work/<category>/YYYY-MM-DD-<slug>.md`)**: drafts/notes/research; must include **Status**.
- **Archive (`docs/archive/**`)**: superseded material; include a Superseded banner.

## Domain rule
Within each bucket, group by **domain** (e.g., `agentos/`, `docs/`, `dev/`) to keep routing deterministic.

