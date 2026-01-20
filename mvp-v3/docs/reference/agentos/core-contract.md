# AgentOS Core Contract

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Core invariants and principles for AgentOS MVP-v3 semantic system.

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

## Invariants

1. **Semantic Understanding**: All requirements understood by meaning, not forced structure
2. **Feature Interplay**: Rules (alwaysApply + description + globs) work together
3. **Self-Description**: System describes itself so Cursor can understand it
4. **Pattern Discovery**: Semantic search finds similar requirements/patterns
5. **Context Awareness**: File context (globs) informs domain understanding
6. **Two-Layer Validation**: Semantic routing + MCP structure validation
7. **Documentation-Driven**: Behavior is defined in documentation, not code

---

## Authority Order

When sources conflict, defer to:
1. **Core Contract** (this document)
2. **Decision Graphs** (semantic patterns)
3. **Workflow Documentation** (execution guidance)
4. **Domain Rules** (domain-specific patterns)

---

## Task Plan Header

Every task must include semantic understanding:

```yaml
plan:
  task_id: TASK-YYYYMMDD-XXXXXX
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
4. **Coherence Checks**: Run validation before committing changes
5. **Rollback Plan**: Document how to undo changes

---

## Validation Contract

1. **Semantic Validation**: Validate semantic understanding quality
2. **Structure Validation**: Validate requirement/plan structure (MCP)
3. **Coherence Validation**: Check documentation ↔ implementation alignment
4. **Outcome Validation**: Verify success criteria met

---

## Feature Interplay

**Rules work together**:
- alwaysApply: Core semantic patterns always available
- description: Domain patterns load on keyword match
- globs: File patterns load on file context
- Combined: Rich semantic context from multiple sources

**Semantic Search**:
- Find similar requirements/patterns when unclear
- Discover patterns from past tasks
- Inform routing decisions

**File Context**:
- Understand domain from open files
- Load domain-specific patterns via globs
- Inform semantic understanding

**MCP**:
- Validate structure (semantic understanding routes)
- Two-layer validation (semantic + structure)

---

## Evolution

Changes to this contract require:
1. Problem identification (semantic understanding)
2. Decision record (ADR)
3. Semantic pattern update (if structural change)
4. Validation update (if validation change)

---

## Self-Awareness

The system monitors:
- Semantic understanding quality
- Feature usage effectiveness
- Gap detection (when semantic understanding insufficient)
- Self-reflection on semantic understanding

See `docs/reference/agentos/self-awareness.md` for details.
