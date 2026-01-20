# AgentOS MVP-v7

Status: Draft
Date: 2026-01-15

Purpose: Deterministic decision-graphing + reviewable traces + resumable active-state (Cursor-integrated), without subagents.

Use:
- To use v7 as a self-contained fork, run Cursor with this directory as the repo root.
- To vendor v7 into another repo, copy these folders into the target repo root:
  - `.cursor/`
  - `docs/`
  - `schemas/`
  - `.agentos/` (optional, for the active-state example)
- (Optional) Copy `.agentos/active-state.example.yaml` to `.agentos/active-state.yaml` in the target repo.
- Start with your own prompt. Ask for `show trace` or use `/trace` to inspect decisions.
- Use `/checkpoint` to save a new frame (summary + anchors) and `/resume` to jump to a prior frame.

