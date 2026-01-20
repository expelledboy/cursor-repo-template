# Reactive Coherence Loop (RCL)

Status: Draft
Date: 2026-01-15
Purpose: Improve reasoning without requiring an auditable backlog; changes are negotiated and diffable.

## RCL steps
RCL-0 Guardrails:
- Use decision graphs and produce traces with anchors.
- Trial-by-default (session-local) is allowed when reversible and low-risk.
- Install requires explicit user approval.

RCL-1 Detect a gap event:
- user correction ("not what I meant")
- repeated ambiguity / multiple clarification loops
- tool evidence contradicts the plan

RCL-2 Explain the current reasoning:
- show evaluated graphs + path + anchors

RCL-3 Propose a reasoning patch:
- small, reversible change to a decision graph (condition/threshold/route/load)

RCL-4 Apply as Trial:
- apply the patch session-locally if low-risk

RCL-5 Negotiate Install:
- present the diff and ask for explicit approval to persist it

