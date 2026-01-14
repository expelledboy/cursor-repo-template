# Cursor Adapter (How-to)

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Instructions for applying AgentOS core behavior in Cursor.

---

## 1. When to use this
- Use this when running AgentOS workflows in Cursor.
- This adapter does not change the core; it only helps load core docs.

## 2. Adapter limits
- Cursor rules can load context but cannot enforce behavior.
- Cursor memories are opaque and not authoritative.
- Cursor rule matching is probabilistic and may misfire.

## 3. Required manual steps
1. If the AgentOS rule does not load, open `.cursor/rules/20-agentos.topic.mdc` and manually open the listed docs.
2. In the task plan header, list the core docs that were loaded.
3. If the task plan header is missing, draft it and only ask the user to confirm missing or ambiguous fields.
4. If the task type is **AgentOS Meta-Maintenance**, load `docs/reference/agentos/self-model.md`.

## 4. Task plan header template
```
Task type:
Primary objective:
Required directives:
Allowed domains:
Routing check:
Evidence sources:
Verification gates:
Loaded core docs:
AgentOS rule loaded (yes/no):
Destructive actions confirmed (yes/no):
```

## 5. Rule setup
- Create `.cursor/rules/20-agentos.topic.mdc` with a narrow description.
- The rule must only point to core docs and must not duplicate content.

## 6. Rule usage
- If the rule does not trigger, explicitly mention "AgentOS" in the request.
- Always include the task plan header using the template above.
- Validate routing with `docs/how-to/agentos/validate-routing.md` after doc or rule moves.
- Adapter constraints: `docs/reference/agentos/cursor-mechanics.md`

## 7. Optional Cursor commands (UI enhancement)
- Commands are adapter-layer only and do not replace core contracts.
- Setup commands:
  - `/agentos-bootstrap` → bootstrap a new repository with AgentOS (one-time setup)
  - `/agentos-init` → load core AgentOS system and self-validate
- Task lifecycle commands map to the AgentOS lifecycle and help enforce phase sequence:
  - `/agentos-start` → intake + classify + route + complexity
  - `/agentos-plan` → plan + header completion
  - `/agentos-design` → design-decision checkpoint (if required)
  - `/agentos-execute` → execute
  - `/agentos-verify` → verify
  - `/agentos-complete` → report + anneal
- Commands are thin entrypoints that inject behavior from canonical docs (they do not restate rules).
- Commands should reference the task plan header and directive loading plan.
- Commands live under `.cursor/commands/`.
- Commands load isolated rules under `.cursor/rules/agentos/` (core + phase + complexity).
- Local state lives under `docs/local/state/` and is ephemeral; promote only decision summaries that affect future work and gaps requiring contract/process changes (see `docs/how-to/agentos/local-state.md`).

## 8. Hierarchical loading (apply tiers)

**Reference**: See `docs/reference/agentos/context-compass.md` Section 5 for the complete selective loading protocol, loading sequence, tier triggers, deferral criteria, minimal mode definition, and context monitoring guidance.

### 8.1. Applying the protocol in Cursor

**Key steps**:
1. Check Context Compass intent (Section 2) before loading any directives
2. Follow the tier loading sequence (Section 5.1): Tier 1 → Tier 2 → Tier 3 → Tier 4/5
3. Use tier loading triggers (Section 5.2) to determine when to load each tier
4. Apply deferral criteria (Section 5.3) when context is constrained
5. Use minimal mode (Section 5.4) if context >80% full
6. Monitor context usage (Section 5.5) and track in task plan header

**Cursor-specific considerations**:
- Cursor rules may auto-load directives; verify only needed directives are loaded
- If rules load too many directives, manually defer non-critical ones
- Use Cursor's file opening to load directives on-demand when triggers occur
- Document actual loading in task plan header (may differ from rule behavior)

### 8.2. Examples

**Example 1: Level 2 task (standard feature)**
```
Directive Loading Plan:
  - Tier 1 (Core): behavior-spec, architecture, routing, context-compass
  - Tier 2 (Task-type): verification-contract
  - Tier 3 (Complexity): verification-gates (Level 2)
  - Deferred: design-decision-templates (trigger: if design decision needed)
  - Context usage: Medium
  - Minimal mode: no
```

**Example 2: Level 3 task with design decision**
```
Directive Loading Plan:
  - Tier 1 (Core): behavior-spec, architecture, routing, context-compass
  - Tier 2 (Task-type): verification-contract, safety-policy
  - Tier 3 (Complexity): verification-gates (Level 3)
  - Tier 4 (Phase): design-decision-templates, structured-exploration (trigger: design-decision checkpoint)
  - Deferred: registry.md (trigger: if registry mapping needed)
  - Context usage: High
  - Minimal mode: no
```

**Example 3: Minimal mode (context constrained)**
```
Directive Loading Plan:
  - Tier 1 (Core): behavior-spec, architecture, routing (minimal)
  - Tier 2-5: Deferred (load only when needed for current action)
  - Context usage: >80% full
  - Minimal mode: yes (rationale: context constrained, complex implementation requires maximum space)
```

### 8.3. Recording in task plan header

Always record the directive loading plan in the task plan header using the tiered format. See `docs/reference/agentos/behavior-spec.md` Section 10 and 11 for the complete directive loading plan format requirements.
