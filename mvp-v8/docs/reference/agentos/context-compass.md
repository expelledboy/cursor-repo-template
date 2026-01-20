---
title: "Context Compass"
status: stable
created_date: 2026-01-18
purpose: "Defines which documentation types are allowed by task intent to protect context and ensure efficient routing"
domain: agentos
---

# Context Compass (Reference)

## Purpose
Establishes constraints on which documentation types can be loaded based on task intent. Prevents context waste and misrouting by ensuring directives match the user's purpose for the interaction.

## Core Constraint

**Documentation types must be loaded by task intent, not by convenience.**

Loading the wrong documentation types wastes limited context windows and increases the chance of misrouting decisions.

## Task Intent Categories

### Execution (Apply Skills)
**Purpose**: Apply known skills and procedures to complete specific tasks
**Allowed Doc Types**: `reference/`, `how-to/` only
**Intent Focus**: "How do I implement X?" or "How do I use Y?"

**Examples**:
- Implementing a feature: `how-to/implement-feature.md`, `reference/api-spec.md`
- Configuring a tool: `how-to/configure-tool.md`, `reference/tool-options.md`
- Following a process: `how-to/process-steps.md`, `reference/process-contract.md`

### Learning (Acquire Skills)
**Purpose**: Learn new concepts, patterns, or capabilities
**Allowed Doc Types**: `tutorials/` only
**Intent Focus**: "How do I learn X?" or "What is Y?"

**Examples**:
- Learning a framework: `tutorials/getting-started.md`
- Understanding concepts: `tutorials/concepts-overview.md`
- Exploring examples: `tutorials/examples.md`

### Architecture (Understand Why)
**Purpose**: Understand system design, rationale, and architectural decisions
**Allowed Doc Types**: `explanation/`, `reference/` only
**Intent Focus**: "Why is it designed this way?" or "What are the tradeoffs?"

**Examples**:
- System rationale: `explanation/architecture/design-rationale.md`
- Decision analysis: `explanation/decisions/decision-analysis.md`
- Design patterns: `reference/architecture-patterns.md`

### AgentOS Meta-Maintenance
**Purpose**: Maintain and evolve the AgentOS system itself
**Allowed Doc Types**: `reference/`, `how-to/`, `explanation/`
**Intent Focus**: System administration, improvement, and evolution

**Examples**:
- System maintenance: `how-to/maintain-agentos.md`
- Evolution planning: `explanation/agentos/evolution-rationale.md`
- Core contracts: `reference/agentos/core-contracts.md`

## Compass Enforcement

### Task Declaration
Every task must declare its intent category upfront. This determines which documentation types can be loaded.

### Routing Validation
The routing process must validate that selected directives match the declared intent category.

### Loading Prevention
If documentation types don't match the intent, the agent must either:
1. Re-route to a different intent category, or
2. Stop and ask the user to clarify intent

### Authority Integration
Context compass constraints work with the evidence authority hierarchy. Even within allowed types, higher authority sources are preferred.

## Hierarchical Loading Tiers

Directives are loaded in tiered sequence to respect context compass constraints:

### Tier 1: Core (Always First)
**Purpose**: Load foundational contracts that apply to all tasks
**Constraints**: Must match intent category
**Examples**: `behavior-spec.md`, `architecture.md`, `routing.md`, `context-compass.md`

### Tier 2: Task-Type Specific
**Purpose**: Load directives relevant to the specific task type within allowed intent
**Constraints**: Must match both intent and task type
**Examples**: `verification-gates.md` (Testing tasks), `safety-policy.md` (destructive operations)

### Tier 3: Complexity-Based
**Purpose**: Load complexity-appropriate directives and templates
**Constraints**: Must be at appropriate complexity level for task
**Examples**: `design-decision-templates.md` (Level 3+), `workflow-variations.md` (complexity routing)

### Tier 4: Phase-Triggered
**Purpose**: Load directives only when specific lifecycle phases are reached
**Constraints**: Must have explicit trigger conditions
**Examples**: `structured-exploration.md` (design checkpoint), `meta-analysis.md` (MAM triggered)

### Tier 5: Specialized
**Purpose**: Load highly specialized directives for niche scenarios
**Constraints**: Must have explicit trigger conditions and narrow applicability
**Examples**: `bootstrap-gates.md` (initial setup only)

## Rationale

### Context Protection
Limited context windows require strict curation. Loading inappropriate documentation types:
- Wastes valuable context space
- Increases likelihood of misrouting
- Slows down decision-making
- Creates cognitive load without benefit

### Intent Alignment
Different task intents require different information architectures:
- **Execution**: Reference + procedural (what/how)
- **Learning**: Tutorial + examples (step-by-step)
- **Architecture**: Explanation + rationale (why)
- **Meta-Maintenance**: All types (system evolution)

### Authority Preservation
Context compass ensures the documentation authority order is respected by intent, preventing inappropriate use of lower-authority sources for high-stakes decisions.

## Integration Points
- **Routing System**: Validates directive selection against compass constraints
- **Directive Loading**: Tiered loading respects intent categories
- **Evidence Authority**: Works with authority hierarchy within allowed types
- **Task Planning**: Intent declaration drives compass application

## Related
- `docs/reference/agentos/architecture.md#doe-integrated-flow`
- `docs/reference/agentos/directive-tiers.md`
- `docs/reference/agentos/evidence-authority.md`
- `docs/reference/agentos/routing.md`