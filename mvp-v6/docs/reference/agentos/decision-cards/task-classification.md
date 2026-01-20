# Decision Card: Task Classification

Status: Draft
Date: 2026-01-15

## Inputs
- primary objective
- scope of change
- risk level

## Types
- EXECUTION: implement or modify behavior
- DESIGN: system structure or architecture
- DEBUG: diagnose or fix failures
- DOCS: documentation change
- META: AgentOS system maintenance

## Rules
- If objective changes code or behavior -> EXECUTION.
- If objective changes structure or contracts -> DESIGN.
- If objective is to diagnose or fix a fault -> DEBUG.
- If objective is to update docs only -> DOCS.
- If objective is to change AgentOS itself -> META.
- If multiple types match, pick primary and log secondary.
