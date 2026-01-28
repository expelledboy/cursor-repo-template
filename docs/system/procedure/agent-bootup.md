---
doc_status: stable
purpose: Define the runtime bootup sequence and awareness maintenance for agent sessions.
intent: procedure
governed_by:
  docs/system/model/procedure-doc.md: Load if you need the contract for procedure docs
implements:
  docs/system/model/system-kernel-bootup.md: Load if you need the kernel contract this procedure implements
  docs/system/decision/require-bootup-and-awareness-maintenance.md: Load if you need the decision that mandates this procedure
related:
  docs/system/procedure/kernel-evaluation.md: Load if you need the procedure for updating the kernel contract
  docs/system/procedure/objective-graph-realignment.md: Load if you need realignment after finding active objective
---

# Procedure: Agent Bootup

## Purpose

Ground the agent in current state, verify healthy awareness, and establish maintenance practices for the session.

## Inputs

- Kernel files loaded via `opencode.json` instructions
- System state accessible via `just status`

## Procedure

### 1. Run Health Check

Run `just status` at session start.

This is a health check, not just display:
- If you can produce accurate status, you are grounded
- If you cannot produce status, investigate before proceeding

### 2. Process Objective State

If the status shows an active objective:
1. Load `docs/work/objective-graph.yaml`
2. State your understanding:
   - Objective ID
   - Current step
   - Next action
3. Follow `docs/system/procedure/objective-graph-realignment.md` if needed

If no objective exists:
- Await user task
- For complex multi-step tasks, consider creating an objective

### 3. Identify Task Type

From the user's request, identify the task type:
- `setup`: install, configure, bootstrap
- `operate`: run, use, execute
- `debug`: error, failure, diagnose
- `change`: modify, extend, add
- `explain`: why, rationale, architecture
- `decide`: choose, evaluate, compare

### 4. Proceed with Awareness Maintenance

Throughout the session, maintain awareness:

**Task transitions**: When switching task types, report minimally:
- "This is a `change` task — loading decision context."

**Governed edits**: Before editing any governed doc, report:
- "Editing `<path>`, governed by `<governing_path>`"

**Compaction recovery**: If context has been compacted:
1. Re-run `just status`
2. Reload kernel files if awareness seems degraded
3. State recovered position before proceeding

## Validation

Bootup is successful when:
- `just status` executes and produces accurate 2-line output
- If objective exists, agent can state its ID, current step, and next action
- Agent can identify task type from user request

Awareness is maintained when:
- Task transitions are reported
- Governed edits are reported with authority chain
- Compaction triggers re-anchoring

## Failure Modes

| Failure | Signal | Recovery |
|---------|--------|----------|
| Cannot produce status | `just status` fails or output is wrong | Investigate: Is git available? Is the repo valid? |
| Objective exists but not acknowledged | Agent starts work without stating objective | Stop, load objective graph, state understanding |
| Edits governed doc without checking | No "Editing X, governed by Y" report | Stop, check `governed_by` frontmatter, report before proceeding |
| Compacted but doesn't re-anchor | Agent seems confused, repeats mistakes | Re-run `just status`, reload kernel files, state position |
| Cannot identify task type | User request is ambiguous | Ask user to clarify intent |
