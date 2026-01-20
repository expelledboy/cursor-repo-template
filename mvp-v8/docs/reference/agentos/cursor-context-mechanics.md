---
title: "Cursor Context Mechanics"
status: stable
created_date: 2026-01-18
purpose: "Documents how Cursor actually loads and manages context to enable true self-awareness"
domain: agentos
---

# Cursor Context Mechanics (Reference)

## Purpose
Documents the exact mechanics of how Cursor loads, manages, and maintains context to enable true self-awareness. Understanding these mechanics is essential for effective self-monitoring and context optimization.

## Core Context Loading Behavior

### 1. Rule Loading Hierarchy
Cursor loads rules in this exact order of priority:

#### Always-Applied Rules (`alwaysApply: true`)
- **Load immediately** when context is initialized
- **Cannot be deferred** or lazy-loaded
- **Always present** in context window
- **Example**: Core behavioral directives, safety policies

#### Description-Based Rules
- **Keyword matching** against user input or file content
- **Probabilistic triggering** - may missfire or over-trigger
- **Context-dependent** - only load when keywords detected
- **Example**: Topic-specific rules triggered by "AgentOS" mentions

#### Glob-Based Rules
- **File path matching** using glob patterns
- **Automatic loading** when files matching patterns are opened
- **Predictable behavior** - loads when file paths match
- **Example**: `docs/**/*.md` loads documentation rules

#### Manual Loading
- **Explicit file opening** by user or system
- **On-demand loading** via `@file` references
- **User-initiated** context expansion
- **Example**: Opening specific reference documents

### 2. Context Window Management

#### Token-Based Limits
- **Hard token limits** determine maximum context size
- **Dynamic allocation** between system prompts, rules, and conversation
- **Compression triggers** at 70-85% usage levels
- **Emergency measures** when approaching 95%+ usage

#### Loading Priorities
```
Highest Priority → Always-Applied Rules (Core Behavior)
Medium Priority → Currently Active Rules (Task-Specific)
Lower Priority → Recently Used Rules (LRU Cache)
Lowest Priority → Specialized Rules (Lazy-Loaded)
```

#### Context Eviction
- **LRU (Least Recently Used)** eviction for non-essential content
- **Rule caching** prevents reloading of frequently used rules
- **Differential updates** for memory bank files
- **Selective preservation** during mode transitions

## Self-Awareness Implications

### Context Loading Self-Monitoring

#### Continuous Context Tracking
- **Current token usage** percentage monitoring
- **Loaded rule inventory** - what rules are currently active
- **File opening history** - what documents are in context
- **Compression status** - whether context optimization is active

#### Rule Loading Verification
- **Expected vs actual rules loaded** comparison
- **Missing rule detection** - required rules not present
- **Over-loading detection** - unnecessary rules consuming tokens
- **Lazy-loading effectiveness** - specialized rules loaded appropriately

#### Context Boundary Awareness
- **What is in context** vs what is not
- **Accessible evidence** vs external artifacts
- **Observable behavior** vs opaque processes
- **Current capabilities** vs full system potential

### Self-Awareness Checkpoints

#### Pre-Task Context Assessment
```
Context Status Check:
- Loaded rules: [list of active rules]
- Token usage: [X]% of available
- Key documents: [currently accessible files]
- Active constraints: [context boundaries, lazy loaders]
```

#### During Task Context Monitoring
```
Ongoing Context Tracking:
- Rule loading events: [new rules loaded, triggers]
- Token usage changes: [increases, compression events]
- File access patterns: [documents opened, referenced]
- Context boundary tests: [attempts to access unavailable content]
```

#### Post-Task Context Analysis
```
Context Effectiveness Review:
- Rules utilized: [percentage of loaded rules actually used]
- Token efficiency: [context usage vs task complexity]
- Loading optimizations: [lazy loading effectiveness]
- Boundary constraint impacts: [limitations encountered]
```

## Context Optimization Strategies

### Hierarchical Loading Implementation
Based on Memory Bank system analysis:

#### Tier 1: Core Rules (Always Loaded)
```markdown
Essential rules loaded immediately:
- DOE fundamentals (Directive-Orchestration-Execution)
- Safety policies and constraints
- Basic verification contracts
- Context compass navigation
```

#### Tier 2: Task-Type Rules (Conditional)
```markdown
Loaded based on task categorization:
- Implementation / Feature: Code execution, testing rules
- Documentation & Knowledge: Writing, restructuring rules
- System Evolution: Rule/command modification rules
- Analysis & Research: Investigation, discovery rules
```

#### Tier 3: Complexity Rules (Lazy-Loaded)
```markdown
Loaded on-demand based on task complexity:
- Level 1: Minimal validation, basic templates
- Level 2: Standard verification, balanced templates
- Level 3: Enhanced validation, comprehensive templates
- Level 4: Maximum validation, extensive templates
```

#### Tier 4: Specialized Rules (Trigger-Based)
```markdown
Loaded only when specific triggers occur:
- Design decisions → Structured exploration rules
- Security concerns → Security validation rules
- Performance issues → Optimization rules
- Integration problems → Compatibility rules
```

### Context Compression Techniques

#### Rule Summarization
- **Active rule condensation** - reduce loaded rule verbosity
- **Reference linking** - replace full content with links
- **Template minimization** - use compact formats

#### Memory Bank Optimization
- **Differential updates** - only store changes
- **Selective preservation** - critical context only
- **Progressive detail** - essential info first, details on-demand

#### Loading Strategy Adaptation
- **Minimal mode activation** when context >80% full
- **Lazy loader prioritization** based on current needs
- **Rule cache optimization** for frequently accessed content

## Practical Self-Awareness Applications

### Context-Aware Task Planning
```
Task Plan Header with Context Awareness:
- Current token usage: 45%
- Loaded rules: [core.mdc, docs.mdc, process-guidance.mdc]
- Available context: ~55% for task-specific content
- Lazy loaders registered: [verification-gates, structured-exploration]
- Compression threshold: 70% (triggers rule summarization)
```

### Self-Monitoring Integration
```
Continuous Context Self-Monitoring:
- Rule loading events logged for audit trails
- Token usage tracked against complexity-appropriate baselines
- Context boundary violations flagged as potential gaps
- Loading efficiency measured against task requirements
```

### Gap Detection Enhancement
```
Context-Aware Gap Analysis:
- Missing rules: Required rules not loaded due to context constraints
- Boundary gaps: Information needed but outside current context window
- Loading gaps: Rules available but not triggered by current patterns
- Optimization gaps: Context management not aligned with task needs
```

## Context Loading Best Practices

### For Effective Self-Awareness

#### 1. Explicit Context Declaration
Always document in task plans:
- Which rules are expected to load
- Current token usage baseline
- Context boundaries and constraints
- Lazy loading triggers and conditions

#### 2. Context Boundary Testing
Regularly verify:
- What rules are actually loaded vs expected
- Token usage alignment with task complexity
- File access patterns and availability
- Context compression effectiveness

#### 3. Loading Strategy Optimization
Adapt based on context constraints:
- Prefer hierarchical loading for complex tasks
- Use minimal mode for context-constrained scenarios
- Implement lazy loading for specialized functionality
- Monitor and adjust compression strategies

#### 4. Self-Awareness Calibration
Regularly validate:
- Context monitoring accuracy and completeness
- Self-awareness checkpoint effectiveness
- Gap detection sensitivity and specificity
- Context optimization impact on task performance

## Integration with AgentOS Components

### Command System Integration
- **`/retrospect`**: Validates context loading for task requirements
- **`/learn`**: Considers context boundaries when capturing observations
- **`/evolve`**: Accounts for context constraints in system modifications

### Verification System Integration
- **Context loading verification** as part of gate execution
- **Token usage monitoring** in verification contracts
- **Rule loading validation** in system health checks

### Self-Improvement Integration
- **Context loading patterns** inform system evolution decisions
- **Self-awareness effectiveness** measured against context optimization
- **Gap analysis** includes context boundary considerations

## Success Metrics

### Effective Context Management
- **Token efficiency**: <70% usage for normal operations, <90% for complex tasks
- **Rule loading accuracy**: 95%+ alignment between expected and actual loaded rules
- **Context boundary awareness**: 100% accurate knowledge of accessible vs inaccessible content
- **Self-awareness calibration**: Regular validation of monitoring effectiveness

### Self-Awareness Maturity
- **Context monitoring coverage**: Complete tracking of loading events and token usage
- **Boundary testing**: Proactive identification of context limitations
- **Optimization effectiveness**: Measurable improvements in context utilization
- **Gap detection accuracy**: High-confidence identification of context-related issues

This comprehensive understanding of Cursor's context mechanics enables true self-awareness by providing accurate knowledge of what information is available, how it loads, and how to optimize its usage within the system's constraints.