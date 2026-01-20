# Decision Card: Command Role Selection

Status: Draft
Date: 2026-01-15

## Inputs
- user request
- explicit verb (if any)
- file context (SIG_F)
- description rules (SIG_D)
- semantic search (SIG_S)

## Roles
- DISCOVER: ambiguity or exploration
- SHAPE: scope, constraints, routing
- ACT: implementation or change
- CHECK: verification or validation
- CLOSE: report, record, anneal

## Rules
- If user provides a verb, map it to the closest role.
- If request is ambiguous or exploratory -> DISCOVER.
- If request is about scope, constraints, or routing -> SHAPE.
- If request is about changes or implementation -> ACT.
- If request is about tests, proof, or checks -> CHECK.
- If request is about summaries, outcomes, or gaps -> CLOSE.
- If multiple roles match, pick primary + secondary and ask user.
