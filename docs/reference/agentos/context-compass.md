# Context Compass (Reference)

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Defines which doc types are allowed by task intent to protect context.

---

## 1. Constraint
Doc types must be loaded by task intent, not by convenience.

## 2. Allowed doc types by intent
- **Execution (apply skills)**: reference + how-to only.
- **Learning (acquire skills)**: tutorials only.
- **Architecture (understand why)**: explanation + reference only.
- **AgentOS Meta-Maintenance**: reference + how-to + explanation.

## 3. Enforcement
- The task plan header must record the task type.
- Routing must select doc types that match the task type.
- If doc types do not match intent, the agent must stop and re-route.

## 4. Rationale
- Loading the wrong doc types wastes context and increases misrouting.
- The compass enforces the authority order by intent, not by habit.

## 5. Hierarchical loading tiers (context-aware)

### 5.1. Loading sequence

Directives must be loaded in tier order, respecting Context Compass intent constraints:

1. **Tier 1 (Core)**: Load first if intent allows reference docs
   - Required core directives: behavior-spec, architecture, routing, context-compass
   - Only load if task intent allows reference doc types (see Section 2)
   - These provide foundational behavior contracts

2. **Tier 2 (Task-type)**: Load after Tier 1 based on routing
   - Task-type/domain directives selected by routing
   - Load only directives relevant to the task type and allowed domains
   - Examples: verification-contract (for Testing tasks), safety-policy (for destructive actions)

3. **Tier 3 (Complexity)**: Load based on complexity level
   - Complexity-appropriate directives (e.g., level-appropriate gates/templates)
   - Load verification-gates catalog if needed for complexity level
   - Load complexity-specific templates if design-decision checkpoint required

4. **Tier 4 (Phase)**: Load only on lifecycle triggers
   - Design-decision checkpoint: design-decision-templates, structured-exploration
   - Meta-analysis mode: meta-analysis, self-model
   - Load only when the specific phase is reached

5. **Tier 5 (Specialized)**: Load only on rare explicit triggers
   - Registry work: registry.md
   - Bootstrap: bootstrap-gates.md
   - Load only when explicitly needed for the task

### 5.2. Tier loading triggers

**Tier 1 (Core)**:
- Trigger: Always (if intent allows reference docs)
- Load: behavior-spec.md, architecture.md, routing.md, context-compass.md, components.md, directive-tiers.md
- Defer: Never (core contracts required)

**Tier 2 (Task-type)**:
- Trigger: After routing determines task type and allowed domains
- Load: Task-type-specific directives from allowed domains
- Defer: If task type unclear or routing incomplete

**Tier 3 (Complexity)**:
- Trigger: After complexity level determined
- Load: Complexity-appropriate verification gates, templates
- Defer: If complexity level not yet determined

**Tier 4 (Phase)**:
- Trigger: When specific lifecycle phase reached
  - Design-decision checkpoint: when checkpoint required (Level 3-4 or material decision)
  - Meta-analysis: when MAM triggered
- Load: Phase-specific directives (design-decision-templates, structured-exploration, etc.)
- Defer: Until phase is reached

**Tier 5 (Specialized)**:
- Trigger: Explicit need identified
  - Registry: when registry mapping work required
  - Bootstrap: during bootstrap mode only
- Load: Specialized directive (registry.md, bootstrap-gates.md)
- Defer: Until explicit need identified

### 5.3. Deferral criteria

Defer loading a directive when:
- **Intent constraint**: Doc type not allowed by Context Compass for task intent
- **Phase not reached**: Directive is Tier 4/5 and trigger not yet occurred
- **Routing incomplete**: Task type or allowed domains not yet determined
- **Complexity unknown**: Tier 3 directive but complexity level not determined
- **Context constrained**: Minimal mode active (see Section 5.4)

**Deferral requirements**:
- Must list deferred directives in task plan header
- Must include explicit, auditable trigger for each deferred directive
- Must load deferred directives when trigger occurs
- Example: "Deferred: design-decision-templates.md (trigger: design-decision checkpoint required)"

### 5.4. Minimal mode

**Definition**: Minimal mode is used when context window is severely constrained (>80% full) or for very complex tasks requiring maximum implementation space.

**When to use**:
- Context window >80% full
- Complex tasks (Level 3-4) with many dependencies
- Large codebases requiring extensive context for implementation
- When guidance can be reduced to maximize implementation capacity

**What to load in minimal mode**:
- Tier 1 (Core): Only absolute minimum (behavior-spec.md, architecture.md, routing.md)
- Tier 2-5: Defer all except absolutely critical for current phase
- Load additional directives only when explicitly needed for current action

**Tradeoffs**:
- **Reduced guidance**: Less directive context available, more reliance on agent's knowledge
- **More implementation space**: More context available for code, files, and implementation details
- **Use with caution**: Only when context constraints are severe; prefer normal selective loading when possible

**Documentation**: If minimal mode is used, must be documented in task plan header with rationale.

### 5.5. Context window monitoring

**Guidance for tracking context usage**:
- Monitor context window usage during task execution
- If context >70% full, consider deferring non-critical directives
- If context >80% full, consider minimal mode
- Track which directives are actually used vs. loaded but unused

**Optional tracking in task plan header**:
- Context usage estimate: "Low/Medium/High" or percentage if known
- Minimal mode indicator: "yes/no" if minimal mode used
- Rationale: Brief explanation if minimal mode used or context tracking shows issues

**Note**: Context tracking is optional guidance, not a requirement. The primary mechanism for context efficiency is selective loading by tier.

---

**Directive loading plan requirements**:
- Must list tiers loaded/deferred with explicit triggers
- Must follow loading sequence (Tier 1 → Tier 2 → Tier 3 → Tier 4/5)
- Must respect Context Compass intent constraints
- Must document minimal mode usage if applicable
