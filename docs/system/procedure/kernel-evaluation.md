---
doc_status: stable
purpose: Define the procedure for evaluating candidates and generating the kernel contract.
intent: procedure
governed_by:
  docs/system/model/procedure-doc.md: Load if you need the contract for procedure docs
implements:
  docs/system/decision/require-bootup-and-awareness-maintenance.md: Load if you need the decision that mandates kernel evaluation
related:
  docs/system/model/system-kernel-bootup.md: Load if you need the kernel contract this procedure generates
  docs/system/procedure/agent-bootup.md: Load if you need the runtime bootup procedure
---

# Procedure: Kernel Evaluation

## Purpose

Evaluate all candidate files and generate a minimal kernel contract that provides complete agent orientation.

## Inputs

- Current kernel contract (`docs/system/model/system-kernel-bootup.md`) as reference material only
- All candidate files from `docs/system/*.md` (root level only)
- All candidate files from `docs/dev/facts/*.md`

## Procedure

### 1. Load Context

Load the current kernel contract as context for consideration. This is reference material, not a constraint — the evaluation may produce a different kernel.

### 2. List All Candidates

Enumerate all candidate files:

```
docs/system/*.md (root level only, not subdirectories)
docs/dev/facts/*.md
```

### 3. Read and Evaluate Each Candidate

For each candidate file, read the entire file and extract:

| Question | Answer |
|----------|--------|
| What awareness does this file provide? | List specific knowledge gained |
| Is this essential for agent orientation? | Yes/No with reasoning |
| Is this stable? | Does it change frequently? |
| Is this compact? | Size in KB |
| Does it point to how to load more? | Self-describing? |

### 4. Score Against Inclusion Criteria

A file belongs in the kernel if:

1. **Essential** — Without it, the agent cannot orient itself
2. **Stable** — Changes rarely, high authority
3. **Compact** — Under 5 KB individually
4. **Self-describing** — Points to how to load more context

### 5. Select Minimal Set

Select the minimal set of files that together provide:

| Awareness Type | Required |
|----------------|----------|
| **Values** | What matters, non-negotiable constraints |
| **Loading** | How to get more context when needed |
| **Task mapping** | What to load for each task type |
| **Self-model** | Context limits, compaction, recovery |

### 6. Verify Size Constraint

Calculate total kernel size. Must be under 15 KB.

If over 15 KB:
- Re-evaluate which files are truly essential
- Consider if any file can be deferred to on-demand loading
- Document why size exceeds target if unavoidable

### 7. Generate New Contract

Generate a new kernel contract from scratch with:

- **Kernel Files table**: File path, size, awareness provided
- **Inclusion criteria**: Why each file was selected
- **Bootup checks**: What state to verify at session start
- **Report format**: The minimal status output format
- **Awareness maintenance**: Task transitions, governed edits, compaction recovery
- **Responsibility acceptance**: What the agent commits to

### 8. Document Changes

Compare to previous kernel and document:

- Files added (with reasoning)
- Files removed (with reasoning)
- Size change
- Any criteria changes

## Validation

- Total kernel size under 15 KB
- Each kernel file has documented awareness
- No essential awareness is missing (values, loading, task mapping, self-model)
- No non-essential files included
- Contract is complete per the model in `docs/system/model/system-kernel-bootup.md`

## Failure Modes

| Failure | Signal | Recovery |
|---------|--------|----------|
| Essential awareness missing | Agent cannot orient after bootup | Re-evaluate, likely missed a candidate |
| Kernel too large | Total exceeds 15 KB | Trim non-essential files, defer to on-demand |
| Non-essential file included | File doesn't meet all 4 criteria | Remove and document why |
| Contract incomplete | Missing sections vs model | Compare to model, add missing sections |

## Output

- Updated `docs/system/model/system-kernel-bootup.md`
- Updated `opencode.json` instructions array (if kernel files changed)
- Change log documenting what changed and why
