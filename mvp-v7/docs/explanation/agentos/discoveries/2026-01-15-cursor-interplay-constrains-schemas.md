# Discovery: Cursor interplay constrains schemas (provenance + anchors + context)

Status: Draft
Date: 2026-01-15
Scope: mvp-v7
Cursor features: Rules, Mentions, Commands, Search, Tools/MCP
Discovery ID: V7-DIS-0001

## Observation
- Cursor Rules inject persistent instructions; they can introduce graphs and context.
- Mentions inject artifacts explicitly; users may insert graphs out-of-band.
- Commands create deterministic entrypoints and can change what context is loaded.
- Semantic search suggests candidates but is not authoritative.
- Tools/MCP produce evidence that should be anchored and can short-circuit ambiguity.

## Implication
- Decision traces must record **provenance** (how graphs entered the chain) and **anchors** (what artifacts were used).
- Graphs should declare a `context_contract` to avoid implicit dependencies on whatever context happened to be injected.
- When a question is asked, the evaluated decision trace should be auto-displayed for review.

## Artifacts
- `docs/reference/agentos/cursor-feature-mapping.md`
- `docs/reference/agentos/spec-decision-graph.md`
- `docs/reference/agentos/spec-decision-trace.md`
- `schemas/decision-graph.yaml`
- `schemas/decision-trace.yaml`

