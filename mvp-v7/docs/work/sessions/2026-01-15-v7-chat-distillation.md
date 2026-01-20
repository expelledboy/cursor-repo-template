Status: Draft
Date: 2026-01-15
Purpose: Distill chat-only rationale for v7 into durable artifacts (discoveries/ADRs/specs).

## What changed (high-signal)
- We replaced vague SIG_* reasoning explanations with **anchors** (file + optional lines) and **structured decision traces**.
- We chose a **reactive governance model**: Trial-by-default (session-local), Install-by-approval (explicit user approval).
- We made active context resumable via an artifact: `.agentos/active-state.yaml` with **frames as a graph** (jumpable).
- Manual graph insertion that doesn’t fit the current chain defaults to **new branch** (preserve history).
- We avoided subagents for v7 (too slow right now).
- We made graphs safer by adding `context_contract` to declare required `context` fields.

## Cursor feature interplay rationale (why these choices exist)
- Rules can introduce graphs/context implicitly; therefore traces must record **provenance** and anchors to rule files.
- Mentions can inject out-of-band artifacts/graphs; therefore default handling is **branch**, not rewriting the chain.
- Commands are deterministic entrypoints; therefore `/trace`, `/checkpoint`, `/resume`, `/branch` exist as control surfaces.
- Semantic search is advisory; therefore it must be recorded as `search_suggested` provenance + search anchors.
- Tools/MCP produce evidence; therefore tool outputs must be anchors and can short-circuit ambiguity.

## Where the durable “why” lives now
- Stable constraints (reference):
  - `docs/reference/agentos/cursor-feature-mapping.md`
  - `docs/reference/agentos/discovery-registry.md`
  - `docs/reference/agentos/problem-registry.md`
  - `docs/reference/agentos/decision-record-format.md`
- Rationale (explanation):
  - `docs/explanation/agentos/discoveries/2026-01-15-cursor-interplay-constrains-schemas.md`
  - ADRs under `docs/explanation/agentos/decisions/`

## Follow-ups (if we continue evolving v7)
- Promote the “trial vs install” governance rationale into a dedicated discovery record if it grows.
- Add a docs decision-graph (where-to-put-docs) only if we use v7 to maintain docs frequently.

