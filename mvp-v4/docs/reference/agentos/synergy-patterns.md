# Feature Synergy Patterns

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Documents all feature synergy patterns and their power multipliers.

---

## Overview

Feature synergy patterns describe how Cursor features work together to create exponentially powerful capabilities. Each pattern multiplies the power of individual features.

---

## Pattern 1: Parallel Pattern Discovery

**Formula**: Commands × Subagents × Semantic Search

**Flow**:
```
Command → Launch 3 subagents in parallel:
  - /pattern-searcher (semantic patterns)
  - /code-pattern-searcher (code patterns)
  - /doc-pattern-searcher (doc patterns)
→ Wait for all results
→ Synthesize best patterns
→ Route based on synthesis
```

**Power Multiplier**: 3x faster pattern discovery

**When to Use**: Level 2+ tasks needing pattern discovery

**Components**:
- **Commands**: Orchestrate subagent launches
- **Subagents**: Execute searches in parallel
- **Semantic Search**: Each subagent uses semantic search independently

---

## Pattern 2: Cascading Rule Enrichment

**Formula**: Rules × Rules × File Context

**Flow**:
```
alwaysApply rule loads → Foundation
User mentions "auth" → description rule loads → Auth context
User opens auth file → globs rule loads → File-specific context
Auth rule triggers → Security rule loads → Security context
All rules layer → Exponential context enrichment
```

**Power Multiplier**: Exponential context loading

**When to Use**: All levels (intensity varies by complexity)

**Components**:
- **alwaysApply Rules**: Foundation context
- **description Rules**: Domain context on keyword match
- **globs Rules**: File-specific context on file match
- **Cascading Rules**: Rules trigger other rules

---

## Pattern 3: Command Workflow Chaining

**Formula**: Commands × Commands × Rules

**Flow**:
```
/agentos → Orchestrates features → Routes to /agentos-start
/agentos-start → Orchestrates features → Routes to /agentos-plan
/agentos-plan → Orchestrates features → Routes to /agentos-execute
/agentos-execute → Orchestrates features → Routes to /agentos-verify
/agentos-verify → Orchestrates features → Routes to /agentos-complete
```

**Power Multiplier**: Structured, orchestrated workflows

**When to Use**: All levels (all tasks use command workflows)

**Components**:
- **Commands**: Each command orchestrates features for its phase
- **Command Chaining**: Commands reference next command
- **Rules**: Each command triggers appropriate rules

---

## Pattern 4: Two-Layer Validation

**Formula**: Commands × MCP × Subagents

**Flow**:
```
Semantic understanding → Routes task
MCP validates structure → Validates plan
Subagent /validator → Validates coherence
All validations → Comprehensive validation
```

**Power Multiplier**: Multi-layer validation

**When to Use**: Level 2+ tasks (intensity varies by complexity)

**Components**:
- **Commands**: Orchestrate validation
- **MCP**: Structure validation
- **Subagents**: Coherence validation

---

## Pattern 5: Context-Aware Orchestration

**Formula**: File Context × Rules × Commands × Subagents

**Flow**:
```
File context → Triggers globs rules → Domain awareness
Domain awareness → Triggers domain rules → Domain context
Domain context → Launches domain-specific subagents → Specialized execution
```

**Power Multiplier**: Context-aware specialization

**When to Use**: All levels (when file context available)

**Components**:
- **File Context**: Open files inform domain
- **globs Rules**: File patterns trigger domain rules
- **Domain Rules**: Domain rules trigger related rules
- **Commands**: Commands adapt to domain context
- **Subagents**: Subagents specialize by domain

---

## Pattern 6: Meta-Orchestration

**Formula**: Complexity × Orchestration Pattern × All Features

**Flow**:
```
Task complexity assessed → Selects orchestration pattern
Orchestration pattern → Determines feature usage
Feature usage → Optimized for complexity level
System orchestrates itself → Maximum efficiency
```

**Power Multiplier**: Self-optimizing system

**When to Use**: All levels (system automatically selects)

**Components**:
- **Complexity Assessment**: Determines orchestration pattern
- **Orchestration Pattern**: Determines feature usage
- **All Features**: Work together based on orchestration pattern

---

## Complete Synergy Matrix

| Feature | Rules | Commands | Subagents | Semantic Search | File Context | MCP |
|---------|-------|----------|-----------|-----------------|--------------|-----|
| **Rules** | Cascading | Trigger | Instruct | Guide | Trigger (globs) | Trigger |
| **Commands** | Trigger | Chain | Orchestrate | Guide | Adapt | Use |
| **Subagents** | Inherit | Orchestrated | Nested | Parallel | Inherit | Use |
| **Semantic Search** | Guided | Used | Parallel | Multi-Query | Informed | Validated |
| **File Context** | Trigger (globs) | Adapt | Inherit | Informed | Multi-File | Guided |
| **MCP** | Trigger | Used | Used | Validated | Guided | Multi-Tool |

---

## Power Synergy Patterns Summary

### Pattern 1: Cascading Context Enrichment
**Formula**: Rules × Rules × File Context
**Power**: Exponential context loading

### Pattern 2: Orchestrated Parallelism
**Formula**: Commands × Subagents × Semantic Search
**Power**: Parallel execution with coordination

### Pattern 3: Two-Layer Validation
**Formula**: Commands × MCP × Subagents
**Power**: Semantic + structural validation

### Pattern 4: Context-Aware Discovery
**Formula**: File Context × Semantic Search × Rules
**Power**: Domain-aware pattern discovery

### Pattern 5: Complete Workflow
**Formula**: Commands × Commands × All Features
**Power**: End-to-end structured workflows

### Pattern 6: Maximum Synergy
**Formula**: All Features Together
**Power**: Exponential capability amplification

---

## Feature Power Multipliers

### Individual Features
- **Rules**: Context loading (1x)
- **Commands**: Workflow orchestration (1x)
- **Subagents**: Parallel execution (Nx where N = number of subagents)
- **Semantic Search**: Pattern discovery (1x)
- **File Context**: Domain awareness (1x)
- **MCP**: Structure validation (1x)

### Synergy Multipliers
- **Rules × Rules**: Cascading context (Exponential)
- **Commands × Subagents**: Parallel orchestration (Nx)
- **Subagents × Semantic Search**: Parallel search (Nx)
- **File Context × Rules**: Automatic domain loading (2x)
- **All Features Together**: Maximum synergy (Exponential)

---

## Best Practices

1. **Always orchestrate**: Don't use features in isolation
2. **Parallel when possible**: Launch subagents in parallel
3. **Cascade rules**: Let rules trigger other rules
4. **Adapt to complexity**: Select patterns based on complexity level
5. **Learn patterns**: Capture successful orchestration patterns
6. **Context-aware**: Use file context to inform orchestration

---

## Related Documentation

- `docs/reference/agentos/meta-orchestration.md` - Meta-orchestration system
- `docs/reference/agentos/core-contract.md` - Core invariants
- `.cursor/rules/orchestration.mdc` - Orchestration patterns rule
- `.cursor/rules/core.mdc` - Meta-orchestration core rule
