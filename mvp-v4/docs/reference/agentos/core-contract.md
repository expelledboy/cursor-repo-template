# AgentOS Core Contract

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Core invariants and principles for AgentOS MVP-v4 accelerated synergy system.

---

## Core Principle

**AgentOS maintains coherence across three surfaces:**
1. **Documentation** - What the system says it does
2. **Implementation** - What the system actually does
3. **Behavior** - What the system does in practice

---

## Semantic Understanding Principle

**AgentOS understands requirements semantically, not syntactically:**
- Read meaning, not just structure
- Recognize patterns in natural language
- Use semantic search to discover similar patterns
- Route based on semantic understanding, not code evaluation

---

## Meta-Orchestration Principle

**AgentOS orchestrates its own feature usage:**
- Selects orchestration patterns based on task complexity
- Adapts feature usage to optimize for efficiency
- Learns patterns from successful tasks (Level 3+)
- Reuses patterns for similar tasks (Level 3+)

---

## Invariants

1. **Semantic Understanding**: All requirements understood by meaning, not forced structure
2. **Feature Synergy**: All Cursor features work together for maximum power
3. **Meta-Orchestration**: System orchestrates its own feature usage based on complexity
4. **Cascading Rules**: Rules trigger other rules for exponential context enrichment
5. **Parallel Execution**: Subagents enable parallel pattern discovery and validation
6. **Pattern Learning**: Learned patterns become reusable components (Level 3+)
7. **Self-Description**: System describes itself so Cursor can understand it
8. **Context Awareness**: File context (globs) informs domain understanding
9. **Multi-Layer Validation**: Semantic routing + MCP structure validation + subagent validation
10. **Documentation-Driven**: Behavior is defined in documentation, not code

---

## Authority Order

When sources conflict, defer to:
1. **Core Contract** (this document)
2. **Meta-Orchestration** (orchestration pattern selection)
3. **Decision Graphs** (semantic patterns)
4. **Workflow Documentation** (execution guidance)
5. **Domain Rules** (domain-specific patterns)
6. **Pattern Library** (learned patterns, Level 3+)

---

## Task Plan Header

Every task must include orchestration and semantic understanding:

```yaml
plan:
  task_id: TASK-YYYYMMDD-XXXXXX
  orchestration:
    complexity_level: [1-4]
    orchestration_pattern: [selected pattern]
    subagents_launched: [list of subagents]
    rules_cascaded: [list of cascading rules]
    semantic_searches: [list of search queries]
    pattern_library_used: [patterns consulted, Level 3+]
  semantic_understanding:
    requirement_meaning: [what I understood]
    patterns_matched: [semantic patterns recognized]
    similar_patterns_found: [semantic search results]
    context_used: [file patterns, domain rules]
  type: [from semantic routing]
  objective: [from requirement]
  workflow: [from semantic pattern matching]
  steps: [structured execution steps]
  success_criteria: [from requirement]
  loaded_docs: [list of loaded documentation]
  rules_loaded: [rules that matched]
```

---

## Safety Policy

1. **Destructive Actions**: Require explicit confirmation
2. **Semantic Validation**: Validate semantic understanding quality
3. **Structure Validation**: Validate structure via MCP (if available)
4. **Subagent Validation**: Validate coherence via subagents (Level 3+)
5. **Coherence Checks**: Run validation before committing changes
6. **Rollback Plan**: Document how to undo changes

---

## Validation Contract

1. **Semantic Validation**: Validate semantic understanding quality
2. **Structure Validation**: Validate requirement/plan structure (MCP)
3. **Coherence Validation**: Check documentation ↔ implementation alignment (MCP + subagents)
4. **Outcome Validation**: Verify success criteria met
5. **Multi-Layer Validation**: Use semantic + structure + coherence validation (Level 2+)

---

## Feature Synergy Invariants

**All features work together**:
- **Rules**: Cascading context enrichment (alwaysApply → description → globs → related rules)
- **Commands**: Orchestrate all features together
- **Subagents**: Parallel execution for pattern discovery and validation
- **Semantic Search**: Multi-dimensional pattern discovery
- **File Context**: Automatic domain awareness via globs
- **MCP**: Structure validation and coherence checking
- **Pattern Library**: Learned patterns inform orchestration (Level 3+)

**Feature Synergy Patterns**:
- Parallel Pattern Discovery: Commands × Subagents × Semantic Search
- Cascading Rule Enrichment: Rules × Rules × File Context
- Command Workflow Chaining: Commands × Commands × Rules
- Two-Layer Validation: Commands × MCP × Subagents
- Context-Aware Orchestration: File Context × Rules × Commands × Subagents
- Meta-Orchestration: Complexity × Orchestration Pattern × All Features

---

## Meta-Orchestration Invariants

1. **Complexity-Based Selection**: Orchestration pattern selected based on complexity level
2. **Feature Optimization**: Feature usage optimized for complexity level
3. **Pattern Learning**: Patterns learned from successful tasks (Level 3+)
4. **Pattern Reuse**: Patterns reused for similar tasks (Level 3+)
5. **Self-Improvement**: System improves orchestration based on success patterns

---

## Evolution

Changes to this contract require:
1. Problem identification (semantic understanding)
2. Decision record (ADR)
3. Semantic pattern update (if structural change)
4. Validation update (if validation change)
5. Orchestration pattern update (if orchestration change)

---

## Self-Awareness

The system monitors:
- Semantic understanding quality
- Feature usage effectiveness
- Orchestration pattern effectiveness
- Pattern learning and reuse effectiveness
- Gap detection (when semantic understanding insufficient)
- Self-reflection on semantic understanding and orchestration

See `docs/reference/agentos/meta-orchestration.md` for orchestration details.

---

## Related Documentation

- `docs/reference/agentos/meta-orchestration.md` - Meta-orchestration system
- `docs/reference/agentos/synergy-patterns.md` - Feature synergy patterns
- `docs/reference/agentos/pattern-library.md` - Pattern library (Level 3+)
- `.cursor/rules/core.mdc` - Meta-orchestration core rule
- `.cursor/rules/orchestration.mdc` - Orchestration patterns rule
