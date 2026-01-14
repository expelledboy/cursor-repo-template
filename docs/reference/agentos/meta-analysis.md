# Meta Analysis Mode (Reference)

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Defines how AgentOS validates its own behavior using the current chat context window.

---

## 1. Definition
Meta Analysis Mode (MAM) is a bounded, on-demand self-audit performed using only the visible chat context and loaded directives. It does not create or rely on logs.

**Relationship to continuous self-awareness**: MAM is a deep, one-time audit that complements continuous self-awareness (see `docs/reference/agentos/self-awareness-framework.md`). While continuous self-awareness provides ongoing monitoring during normal task execution, MAM provides a comprehensive, structured audit when triggered by specific events or user request.

## 2. Allowed evidence
- Current chat context window.
- Loaded AgentOS directives and referenced repo artifacts.
- No external logs or hidden memories.
- Local state in `docs/local/state/` is not evidence unless promoted to `docs/work/**`.

## 3. Required checklist
When MAM is approved, the agent must check and report:
1. Task plan header present and complete.
2. Task type declared and matches routing.
3. Required directives loaded before execution.
4. Evidence sources declared.
5. Verification gates defined or referenced.
6. Destructive actions confirmed when applicable.
7. Gaps captured when discovered.

## 4. Outputs
- A structured self-audit in the response.
- If gaps are found, create a gap work note per `docs/how-to/agentos/capture-gaps.md`.
- If no gaps are found, state "No gaps detected in current context."

## 5. Related docs
- `docs/reference/agentos/self-improvement.md`
- `docs/reference/agentos/self-model.md`
- `docs/reference/agentos/self-awareness-framework.md` (continuous self-awareness during normal execution)
