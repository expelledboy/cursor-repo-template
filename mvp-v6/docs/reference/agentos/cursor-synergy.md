# Cursor Synergy (Reference)

Status: Draft
Date: 2026-01-15
Purpose: Minimal feature interplay patterns.

## Feature set
- Rules (alwaysApply, description, globs)
- Commands (explicit phase entry)
- Mentions (explicit injection)
- Semantic search (context for routing)
- Sub-agents (parallel or pipeline)
- MCP tools (deterministic checks)
- Manual context (explicit user injection)
- Memories (non-authoritative)

## Synergy patterns
S1: Rules(alwaysApply) + Rules(description) -> base + domain constraints
S2: Rules(globs) + Manual context -> file-anchored routing cues
S3: Commands + Decision cards -> deterministic phase gating
S4: Mentions + Routing -> explicit injection reduces ambiguity
S5: Semantic search + Routing -> context enrichment (not authority)
S6: Sub-agents(parallel) + Search -> candidate set (proposals)
S7: Sub-agents(pipeline) + Commands -> chained context
S8: MCP/Tools + Validation -> deterministic confirmation (SIG_T)

## Selection rule
- Use 1-2 synergies per phase.
- Prefer synergies that reduce ambiguity.
