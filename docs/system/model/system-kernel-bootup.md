---
doc_status: stable
purpose: Define the kernel files, awareness they provide, and bootup sequence contract.
intent: contract
governed_by:
  docs/system/governance.md: Load if you need global rules that govern this contract
  docs/system/decision/require-bootup-and-awareness-maintenance.md: Load if you need the decision that mandates this contract
implemented_by:
  scripts/status.py: Load if you need the implementation of just status
  docs/system/procedure/agent-bootup.md: Load if you need the runtime bootup procedure
related:
  opencode.json: Configuration that loads kernel files via instructions array
  AGENTS.md: Bootup instruction that triggers just status
  docs/system/procedure/kernel-evaluation.md: Load if you need the procedure for updating this contract
---

# System Kernel Bootup Contract

## Purpose

Define the minimal set of files that bootstrap agent awareness and the bootup sequence that grounds the agent in current state.

## Kernel Files

| File | Size | Awareness Provided |
|------|------|-------------------|
| `docs/system/core-values.md` | ~0.6 KB | Non-negotiable values: minimal context, explicit authority, governance = precedence, protect against compaction |
| `docs/system/loading-policy.md` | ~3.5 KB | How to load context: domain → governed_by chain → task → intents |
| `docs/system/intent-task-matrix.md` | ~1.0 KB | What intents to load for each task type (setup, operate, debug, change, explain, decide) |
| `docs/dev/facts/agent-mechanics.md` | ~4.6 KB | Self-model: finite context, compaction inevitability, on-demand discovery, external state via objective graph |

**Total**: ~9.7 KB (~2,500 tokens)

## Kernel Inclusion Criteria

A file belongs in the kernel if it is:

1. **Essential** — Without it, the agent cannot orient itself
2. **Stable** — Changes rarely, high authority
3. **Compact** — Under 5 KB individually, total kernel under 15 KB
4. **Self-describing** — Points to how to load more context

## Bootup Report Format

The bootup report is 2 lines only:

```
Agent OS | <YYYY-MM-DD HH:MM> | <branch> +<ahead> | <n> staged
Objective: <id> → <next_action> | none
```

Example (no objective):
```
Agent OS | 2026-01-28 14:32 | master +8 | 12 staged
Objective: none
```

Example (with objective):
```
Agent OS | 2026-01-28 14:32 | master +8 | 12 staged
Objective: restructure-agent-mechanics → commit staged changes
```

## Bootup as Health Check

Running `just status` is a health check, not just display:

- If you can produce accurate status, you are grounded
- If you cannot produce status, investigate before proceeding
- If objective exists, load it and state understanding before proceeding

## Awareness Maintenance

After bootup, maintain awareness throughout the session:

### Task Transition Reporting

When switching task types, report minimally:
- "This is a `change` task — loading decision context."

### Governed Edit Reporting

Before editing any governed doc, report:
- "Editing `docs/system/model/X.md`, governed by `docs/system/governance.md`"

This creates an accountability trail and forces the agent to check authority.

### Compaction Recovery

If context has been compacted (detected by loss of earlier conversation details):

1. Re-run `just status` to re-ground in current state
2. Reload kernel files if awareness seems degraded
3. State recovered position before proceeding

## Responsibility Acceptance

By completing bootup without error, the agent accepts responsibility to:

1. Follow `governed_by` chains for authority resolution
2. Use `intent-task-matrix` for context loading decisions
3. Check `docs/work/objective-graph.yaml` before multi-step work
4. Maintain awareness through task reporting and governed edit reporting
5. Recover from compaction via re-anchoring

## Implementation Points

- **Kernel loading**: `opencode.json` instructions array
- **Bootup trigger**: `AGENTS.md` instructs agent to run `just status`
- **Status command**: `scripts/status.py` implements the report format
