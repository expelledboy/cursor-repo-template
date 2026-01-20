# AgentOS Kernel (Reference)

Status: Draft
Date: 2026-01-15
Purpose: Deterministic kernel for Cursor feature interplay.

## Signals
- SIG_K: kernel constraints (this doc)
- SIG_U: explicit user context (manual injection)
- SIG_T: tool outputs (terminal/browser/MCP) when used as evidence
- SIG_F: file context (globs)
- SIG_D: description rules
- SIG_S: semantic search results
- SIG_M: memories (hint only)

## Precedence
SIG_K > SIG_U > SIG_T > SIG_F > SIG_D > SIG_S > SIG_M

## Routing rule
- If SIG_U/SIG_T/SIG_F/SIG_D/SIG_S conflict on task type or domain, ask user.
- If no conflict, select the highest-precedence signal.

## Context injection sources
- Rules: `alwaysApply`, `description`, `globs`
- Commands: explicit phase entry
- Manual context: user-provided files/notes
- Sub-agent outputs: parallel or pipeline results
- Tool outputs: terminal/browser/MCP (deterministic checks when available)

## Logging
Record in header:
- Signals used (subset of SIG_K,SIG_U,SIG_T,SIG_F,SIG_D,SIG_S,SIG_M)
- Decision cards loaded
- Feature mix used (rules/search/sub-agents/tools)
