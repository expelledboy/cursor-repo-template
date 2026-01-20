# AgentOS v6 Operating Model (Whitepaper, Concise)

Status: Draft
Date: 2026-01-15
Purpose: A minimal, testable operating model for deterministic behavior + Cursor feature interplay.

## 1) Core claim
AgentOS v6 is an **experimental kernel**: it behaves deterministically by default, and it evolves by running explicit probes against explicit theories.

## 2) Determinism model (signals + precedence)
We model context as signals \(SIG_*\) with a strict precedence order (a total order):

- **Signals**: SIG_K (kernel) > SIG_U (user) > SIG_T (tool outputs) > SIG_F (files) > SIG_D (rules) > SIG_S (search) > SIG_M (memories)
- **Decision function**: for any decision \(d\) (routing, scope, validation), choose the maximum-precedence applicable signal.

If two signals disagree on a *semantic category* (task type, domain, intent) and the disagreement involves SIG_U, ask the user.

## 3) Cursor feature model (treated as mechanisms, not authority)
- **Rules**: deterministic context injection. Prefer small, composable rules.
- **Commands**: deterministic entrypoints into phase/probe workflows.
- **Mentions**: explicit injection of artifacts; treat as SIG_U (user provided) or SIG_F (file selected), depending on user intent.
- **Semantic search**: context enrichment only (SIG_S), never a contract.
- **Subagents**: controlled parallelism/pipelines; outputs are *proposals* unless promoted by SIG_U or verified by SIG_T.
- **MCP/tools**: when used as checks, their outputs are evidence (SIG_T).

## 4) Experimental loop (the “draft” engine)
Each behavior change is attached to:
- **Theory**: a falsifiable statement in `theory-cards/**`
- **Probe**: a repeatable test in `interplay-probes.md`
- **Log**: a short header note capturing which signals/tools were used

Promotion rule:
- Draft behavior becomes “stable guidance” only when a theory is validated by repeated probe runs + SIG_T evidence (when applicable).

## 5) Guardrails
The kernel is intentionally small. Change proposals must pass `evolution-guardrails.md`.
