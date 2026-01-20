# Cursor–Decision Graph Interplay (v7)

Status: Draft
Date: 2026-01-15
Purpose: Map Cursor features to decision-graphing in a deterministic, reviewable way.

## Principle
Every Cursor feature contributes as one (or more) of:
- **Graph introduction**: adds candidate graphs or graph bundles.
- **Evidence anchoring**: adds concrete anchors (path + optional lines + note).
- **Deterministic entry**: commands select known graph bundles and trace policy.

## Feature mapping
### Rules
- Introduce graph candidates and load docs/graphs.
- Record provenance: source_kind=rule + anchor to rule file/lines.

### Mentions
- Explicit injection of artifacts and/or graphs.
- If a manual insertion does not clearly fit the current chain, default to **new branch**.

### Commands
- Deterministic entrypoints for checkpointing, resuming, and showing traces.

### Semantic search
- Suggests candidates; never authoritative.
- Record the query + top hits as anchors; provenance may be search_suggested.

### MCP/tools
- Produce evidence anchors.
- Tool evidence may short-circuit a branch; record the tool anchor and which decision it affected.

## Trace policy
- Always compute traces.
- Auto-display trace when asking the user a question; otherwise on `/trace`.

