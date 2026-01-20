# Discovery: Default branching preserves auditability under manual insertion and objective shifts

Status: Draft
Date: 2026-01-15
Scope: mvp-v7
Cursor features: Mentions, Commands
Discovery ID: V7-DIS-0003

## Observation
- Users may insert graphs/artifacts out-of-band (mentions) or shift objectives mid-stream.
- Forcing such inserts into the current chain rewrites history and makes traces confusing.

## Implication
- Default to creating a new branch frame for manual insertions or objective shifts that don’t clearly refine the current chain.
- Provide explicit navigation commands to jump back (`/resume`) and to create branches (`/branch`).

## Artifacts
- `docs/reference/agentos/spec-active-state.md`
- `.cursor/commands/branch.md`
- `.cursor/commands/resume.md`
