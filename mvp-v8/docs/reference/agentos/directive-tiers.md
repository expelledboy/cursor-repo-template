---
title: "Directive Tiers"
status: stable
created_date: 2026-01-18
purpose: "Defines hierarchical loading tiers for AgentOS directives to support efficient, context-aware directive loading"
domain: agentos
---

# Directive Tiers (Reference)

## Purpose
Establishes a tiered hierarchy for loading AgentOS directives (documentation) to ensure efficient context usage and respect intent-based loading constraints from the Context Compass.

## Loading Principles

### Sequential Loading
Directives are loaded in tier order, never skipping tiers. This ensures foundational knowledge is loaded before specialized knowledge.

### Intent Constraints
All loading respects Context Compass intent categories. Tiers cannot load documentation types prohibited by the current task intent.

### Trigger Conditions
Higher tiers (4-5) require explicit trigger conditions to prevent unnecessary loading.

## Tier Definitions

### Tier 1: Core (Foundation)
**Purpose**: Foundational directives that establish basic system contracts and constraints
**Loading**: Always loaded first if intent allows reference docs
**Trigger**: Task routing completion

**Directives**:
- `behavior-spec.md` - Core behavioral constraints
- `architecture.md` - System architecture model
- `routing.md` - Routing model and constraints
- `context-compass.md` - Documentation loading constraints
- `components.md` - Core component registry
- `validation-scripts.md` - Validation system index

### Tier 2: Task-Type Specific
**Purpose**: Directives specific to the task type being executed
**Loading**: Loaded after Tier 1 based on routing decisions
**Trigger**: Task type classification

**Directives**:
- `verification-contract.md` - Verification requirements (Testing tasks)
- `safety-policy.md` - Safety constraints (destructive operations)
- `cursor-mechanics.md` - Cursor-specific operations
- `routing.md` extensions - Domain-specific routing rules
- `problem-registry.md` - Problem catalog (meta-maintenance)

### Tier 3: Complexity-Based
**Purpose**: Complexity-appropriate directives and templates
**Loading**: Selected based on task complexity level (1-4)
**Trigger**: Complexity assessment completion

**Directives**:
- `verification-gates.md` - Gate catalog selection
- `workflow-variations.md` - Workflow selection by complexity
- `design-decision-templates.md` - Decision templates (Level 3+)
- Complexity-specific validation rules

### Tier 4: Phase-Triggered
**Purpose**: Directives loaded only when specific task phases are reached
**Loading**: On-demand when phase conditions are met
**Trigger**: Explicit lifecycle phase transitions

**Directives**:
- `design-decision-checkpoint.md` - Design decision process
- `structured-exploration.md` - Design exploration phases
- `design-decision-structured-exploration.md` - Exploration guidance
- `meta-analysis.md` - Meta-analysis mode (MAM)

### Tier 5: Specialized
**Purpose**: Highly specialized directives for niche scenarios
**Loading**: Only when specific conditions are met
**Trigger**: Narrow, explicit trigger conditions

**Directives**:
- `bootstrap-gates.md` - System initialization
- `registry.md` - Advanced registry operations
- Domain-specific extensions with limited applicability

## Loading Process

### 1. Intent Declaration
Task declares intent category (Execution/Learning/Architecture/Meta-Maintenance)

### 2. Tier 1 Loading
Load core directives if intent allows reference documentation

### 3. Task Classification
Determine task type and complexity level

### 4. Tier 2-3 Loading
Load task-type and complexity-appropriate directives

### 5. Phase Monitoring
Monitor for phase triggers to load Tier 4-5 directives

### 6. Validation
Ensure all loaded directives respect Context Compass constraints

## Tier Assignment Rules

### Default Assignments
- Reference documentation: Tier 1 (core) or Tier 2 (task-specific)
- How-to documentation: Tier 2 (procedures)
- Explanation documentation: Tier 3 (complexity) or Tier 4 (phase)
- Tutorial documentation: Not loaded (intent constraint)

### Override Conditions
- Explicit triggers can promote directives to higher tiers
- Complexity assessment can demote Tier 3 directives
- Context constraints can prevent loading entirely

### Assignment Guidelines
- If directive applies to all tasks: Tier 1
- If directive applies to specific task types: Tier 2
- If directive depends on complexity: Tier 3
- If directive requires phase triggers: Tier 4
- If directive has very narrow applicability: Tier 5

## Integration with Context Compass

### Intent Filtering
Context Compass intent categories determine which documentation types can be loaded, regardless of tier.

### Authority Integration
Within allowed documentation types, higher authority sources are preferred.

### Loading Validation
Tier loading must validate against Context Compass constraints before proceeding.

## Performance Considerations

### Context Efficiency
Tiered loading prevents context waste by ensuring only relevant directives are loaded.

### Loading Order
Sequential tier loading ensures foundational knowledge is available before specialized knowledge.

### Trigger Optimization
Phase-triggered loading (Tiers 4-5) prevents loading unnecessary directives for simple tasks.

## Related
- `docs/reference/agentos/context-compass.md` - Intent-based loading constraints
- `docs/reference/agentos/architecture.md#doe-integrated-flow`
- `docs/reference/agentos/routing.md` - Routing model integration