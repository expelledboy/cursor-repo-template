# Decision Card: Validation

Status: Draft
Date: 2026-01-15

## Inputs
- task type
- complexity level
- change surface (code/docs/config)

## Rules
- L1: run minimal check or list expected command.
- L2: run targeted tests; add doc validation if DOCS.
- L3: run integration + regression gates.
- L4: run full suite; deferrals require explicit user approval.
- If MCP tools exist, use them for deterministic checks.
