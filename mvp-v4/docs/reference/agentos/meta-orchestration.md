# Meta-Orchestration System

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Documents how AgentOS orchestrates its own feature usage based on task complexity and context.

---

## Overview

Meta-orchestration is the system's ability to orchestrate its own feature usage, selecting appropriate orchestration patterns based on task complexity and context. This enables the system to optimize feature usage for maximum efficiency and power.

---

## Complexity-Based Orchestration Selection

The system selects orchestration patterns based on assessed task complexity:

### Level 1: Streamlined Orchestration

**Characteristics**:
- Simple, isolated tasks
- Quick implementation
- Minimal dependencies

**Orchestration**:
- Basic rule layering (alwaysApply + description/globs)
- Skip subagents (orchestration already done in `/agentos` if needed)
- Minimal semantic search
- Basic MCP validation

**Use Cases**:
- Quick fixes
- Simple updates
- Isolated changes

### Level 2: Standard Orchestration

**Characteristics**:
- Typical implementation tasks
- Moderate scope
- Standard dependencies

**Orchestration**:
- Full rule layering (alwaysApply + description + globs)
- 2-3 subagents in parallel for pattern discovery (if needed)
- Standard semantic search
- Standard MCP validation

**Use Cases**:
- Standard features
- Typical implementations
- Moderate complexity

### Level 3: Enhanced Orchestration

**Characteristics**:
- Complex implementation tasks
- System-wide impact
- Multiple dependencies

**Orchestration**:
- Cascading rules (rules trigger rules)
- 3+ subagents in parallel for comprehensive discovery
- Multiple semantic searches in parallel
- Comprehensive MCP validation
- Pattern library consultation

**Use Cases**:
- Complex features
- Security-sensitive implementations
- System-wide changes

### Level 4: Maximum Orchestration

**Characteristics**:
- Enterprise implementation tasks
- Critical impact
- Extensive dependencies

**Orchestration**:
- Full cascading rules (rules trigger rules extensively)
- All relevant subagents in parallel
- Multi-dimensional semantic search
- Multi-layer validation (semantic + MCP + subagent)
- Pattern library learning and reuse

**Use Cases**:
- Enterprise features
- Critical implementations
- Strategic changes

---

## Orchestration Pattern Selection Process

1. **Assess Complexity**: Determine task complexity level (1-4)
2. **Select Pattern**: Choose orchestration pattern based on complexity
3. **Orchestrate Features**: Launch subagents, cascade rules, use semantic search
4. **Validate**: Use MCP and subagents for validation
5. **Learn**: Update pattern library with successful patterns (Level 3+)

---

## Feature Usage Optimization

### Rules
- **Level 1**: Basic layering only
- **Level 2**: Full layering with basic cascading
- **Level 3**: Full cascading with domain triggers
- **Level 4**: Maximum cascading with extensive triggers

### Commands
- **Level 1**: Streamlined command workflow
- **Level 2**: Standard command workflow
- **Level 3**: Enhanced command workflow with subagents
- **Level 4**: Maximum command workflow with all subagents

### Subagents
- **Level 1**: Skip subagents (orchestration done in `/agentos`)
- **Level 2**: Launch 2-3 subagents in parallel (if needed)
- **Level 3**: Launch 3+ subagents in parallel
- **Level 4**: Launch all relevant subagents in parallel

### Semantic Search
- **Level 1**: Basic search (if needed)
- **Level 2**: Standard search
- **Level 3**: Multiple searches in parallel
- **Level 4**: Multi-dimensional searches in parallel

### MCP
- **Level 1**: Basic validation (if available)
- **Level 2**: Standard validation
- **Level 3**: Comprehensive validation
- **Level 4**: Multi-layer validation

### Pattern Library
- **Level 1**: Skip pattern library
- **Level 2**: Skip pattern library
- **Level 3**: Consult pattern library, learn patterns
- **Level 4**: Consult extensively, learn extensively, update library

---

## Pattern Learning and Reuse

### When Patterns Are Learned (Level 3+)

Patterns are learned when:
- Task completed successfully
- Orchestration pattern was effective
- Semantic understanding was accurate
- Workflow selection was appropriate

### Pattern Learning Process

1. Extract successful orchestration metadata from task
2. Identify semantic indicators that led to success
3. Create pattern entry with:
   - Pattern characteristics
   - Orchestration used
   - Success indicators
4. Add to pattern library
5. Update pattern success rate

### Pattern Reuse Process

1. Match requirement to pattern library
2. Use pattern's orchestration metadata
3. Launch pattern's subagents
4. Cascade pattern's rules
5. Select pattern's workflow
6. Adapt pattern to current context

---

## Self-Improvement Mechanisms

### Pattern Success Tracking
- Track pattern success rates over time
- Prune patterns with low success rates
- Promote patterns with high success rates

### Orchestration Optimization
- Learn which orchestration patterns work best for which complexity levels
- Optimize feature usage based on past success
- Adapt orchestration patterns based on context

### Feature Synergy Learning
- Learn which feature combinations are most effective
- Optimize feature interplay based on task characteristics
- Discover new synergy patterns

---

## Integration with Other Systems

### Core Contract
- Meta-orchestration respects core invariants
- Maintains coherence across all surfaces
- Follows safety policy

### Decision Graphs
- Orchestration selection informs decision graph usage
- Decision graphs inform orchestration pattern selection
- Complexity assessment drives orchestration selection

### Workflows
- Orchestration patterns inform workflow selection
- Workflows use orchestration patterns for feature usage
- Workflow execution adapts to orchestration pattern

### Pattern Library
- Pattern library informs orchestration selection
- Orchestration patterns are learned and stored in pattern library
- Pattern reuse optimizes orchestration

---

## Best Practices

1. **Adapt to Complexity**: Always select orchestration pattern based on complexity
2. **Learn Patterns**: Learn patterns from successful tasks (Level 3+)
3. **Reuse Patterns**: Reuse patterns for similar tasks (Level 3+)
4. **Optimize Features**: Optimize feature usage based on task characteristics
5. **Track Success**: Track pattern success rates and optimize
6. **Maintain Coherence**: Ensure orchestration maintains system coherence

---

## Related Documentation

- `docs/reference/agentos/core-contract.md` - Core invariants
- `docs/reference/agentos/synergy-patterns.md` - Feature synergy patterns
- `docs/reference/agentos/pattern-library.md` - Pattern library documentation
- `.cursor/rules/core.mdc` - Meta-orchestration core rule
- `.cursor/rules/orchestration.mdc` - Orchestration patterns rule
