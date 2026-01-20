# AgentOS Kernel (v7)

Status: Draft
Date: 2026-01-15
Purpose: Deterministic routing/planning via decision graphs, with reviewable traces and resumable active-state.

## 1) Determinism surfaces
- **Decision graphs**: the reasoning substrate (routing, scope, validation, next actions).
- **Decision traces**: review substrate (graph path + anchors).
- **Active state**: resumability substrate (frames/objectives graph + references to traces).

## 2) Trial vs install (reactive governance)
- **Trial**: session-local behavior adjustments are allowed when low-risk and reversible.
- **Install**: any persistent change to graphs/rules/specs requires explicit user approval.

## 3) Evidence anchoring (replace vague labels)
When explaining reasoning to a user, prefer **anchors** (file + line range + note) over abstract signal labels.

Anchor types: kernel, user, rule, file, doc, search, tool, memory_hint.

## 4) Trace display policy
- Always compute decision traces.
- Auto-display the trace when the agent asks the user a question.
- Otherwise show on request (e.g. `/trace` or "show trace").

## 5) Cursor integration rule
Cursor features (rules/mentions/commands/search/tools) may introduce graphs or evidence.
The provenance of introduced graphs must be recorded in the decision trace.

