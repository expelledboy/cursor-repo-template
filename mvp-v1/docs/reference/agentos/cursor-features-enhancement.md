# Cursor Features Enhancement Plan

**Status**: Design
**Date**: 2026-01-14
**Purpose**: Leverage additional Cursor features to enhance AgentOS deterministic behavior.

---

## Current Usage

### ✅ What We're Using
- **alwaysApply rules**: Core rule that always loads
- **description rules**: Keyword matching (minimal usage)
- **Commands**: Entry points for task workflow
- **Decision graphs**: Documentation-based decision trees

### ❌ What We're Not Using
- **globs rules**: File pattern matching for contextual loading
- **Semantic search**: Intelligent directive discovery
- **MCP**: External tool integration for validation
- **Multiple description rules**: Domain-specific keyword matching

---

## Enhancement Opportunities

### 1. Globs Rules for Contextual Loading

**Opportunity**: Load domain-specific reasoning based on files being edited.

**Implementation**:
- Create globs rules for different file types/patterns
- Load appropriate directives when matching files are opened
- Provide file-type specific guidance

**Example Rules**:
```mdc
---
description: Python implementation
globs: ["**/*.py", "**/requirements.txt"]
---
# Python-specific AgentOS guidance
- Load: docs/reference/agentos/architectural-patterns.md (registry mapping)
- Check for @directive annotations in code
- Validate registry mappings for Python files
```

```mdc
---
description: Documentation work
globs: ["docs/**/*.md"]
---
# Documentation-specific AgentOS guidance
- Load: docs/reference/agentos/alignment-mechanisms.md (registry mapping)
- Verify authority order compliance
- Check for @implementation annotations
- Validate documentation structure
```

**Benefits**:
- Automatic context loading based on what files are open
- File-type specific guidance without manual intervention
- Better context awareness

---

### 2. Semantic Search for Intelligent Discovery

**Opportunity**: Use Cursor's built-in semantic search for directive discovery when task type is ambiguous.

**Implementation**:
- Add instructions to use semantic search when classification is unclear
- Search for similar tasks to determine classification
- Find relevant directives through content similarity

**Enhancement to Commands**:
```markdown
## When Task Classification is Unclear
1. Use Cursor's semantic search to find similar tasks
2. Search codebase for similar patterns or implementations
3. Use search results to inform classification decision
4. Document search terms and results in task plan header
```

**Benefits**:
- Better classification accuracy for ambiguous tasks
- Intelligent directive discovery
- Leverages Cursor's built-in intelligence

---

### 3. Domain-Specific Description Rules

**Opportunity**: Create multiple description rules for different domains/task types.

**Implementation**:
- Security tasks → Load security-specific directives
- Refactoring tasks → Load refactoring-specific guidance
- Testing tasks → Load testing-specific validation
- Documentation tasks → Load documentation-specific processes

**Example Rules**:
```mdc
---
description: security, auth, encrypt, authentication, authorization
---
# Security Task Instructions
- Load: docs/reference/agentos/coherence-contract.md (safety policy)
- Load: docs/reference/agentos/decision-graphs/validation-strategy.md
- Follow security validation protocol
- Require explicit confirmation for security boundary changes
- Block secrets logging
```

```mdc
---
description: test, testing, spec, validate, verify
---
# Testing Task Instructions
- Load: docs/reference/agentos/validation-contract.md
- Load: docs/reference/agentos/decision-graphs/validation-strategy.md
- Determine appropriate test strategy
- Verify test coverage requirements
- Check CI integration
```

**Benefits**:
- Automatic loading of relevant directives based on keywords
- Domain-specific guidance without manual selection
- Better context for specialized tasks

---

### 4. MCP Integration for Validation

**Opportunity**: Create MCP server to expose validation scripts as tools.

**Implementation**:
- Create MCP server that wraps validation scripts
- Expose validation tools to Cursor
- Enable agent to call validation tools directly

**MCP Server Structure**:
```python
# mvp/scripts/agentos/mcp_server.py
# Exposes validation tools via MCP
tools = [
    "validate_registry",      # Check docs↔code mappings
    "validate_traceability",  # Verify problem→decision links
    "validate_behavior",      # Check contract compliance
]
```

**Benefits**:
- Automated validation execution
- Integration with validation strategy decision graph
- Deterministic validation results

---

### 5. Enhanced Semantic Matching

**Opportunity**: Leverage Cursor's codebase indexing for better context awareness.

**Implementation**:
- Instruct agent to use codebase understanding for:
  - Finding similar implementations
  - Understanding project structure
  - Discovering related directives
  - Identifying patterns

**Enhancement to Core Rule**:
```mdc
## Leverage Cursor's Codebase Indexing
- Use semantic understanding to find similar tasks/patterns
- Leverage codebase context for better routing decisions
- Use project structure awareness for directive selection
- Document codebase insights in task plan header
```

**Benefits**:
- Better understanding of project context
- More accurate routing decisions
- Intelligent pattern recognition

---

## Implementation Priority

### Phase 1: Quick Wins (Week 1)
1. ✅ **Domain-specific description rules** - Easy to add, immediate value
2. ✅ **Globs rules for file patterns** - Automatic context loading

### Phase 2: Enhanced Intelligence (Week 2)
3. ✅ **Semantic search instructions** - Better classification accuracy
4. ✅ **Enhanced semantic matching** - Better context awareness

### Phase 3: Automation (Week 3-4)
5. ✅ **MCP validation server** - Automated validation execution

---

## Example Enhanced Configuration

### Multiple Description Rules
```
.cursor/rules/
├── agentos-core.mdc (alwaysApply)
├── agentos-security.mdc (description: security, auth...)
├── agentos-testing.mdc (description: test, testing...)
├── agentos-refactoring.mdc (description: refactor...)
└── agentos-docs.mdc (globs: docs/**/*.md)
```

### Enhanced Command with Semantic Search
```markdown
## When Classification is Unclear
- Use Cursor's semantic search: "similar tasks to [description]"
- Search codebase for patterns matching task description
- Use search results to inform decision graph traversal
```

### MCP Integration
```json
{
  "mcpServers": {
    "agentos-validation": {
      "command": "python",
      "args": ["scripts/agentos/mcp_server.py"]
    }
  }
}
```

---

## Expected Benefits

1. **Automatic Context Loading**: Globs rules load relevant directives automatically
2. **Better Classification**: Semantic search improves ambiguous task routing
3. **Domain Expertise**: Description rules provide specialized guidance
4. **Automated Validation**: MCP enables direct validation tool execution
5. **Intelligent Discovery**: Codebase indexing finds relevant patterns

---

## Next Steps

1. Create domain-specific description rules
2. Add globs rules for file patterns
3. Enhance commands with semantic search instructions
4. Design MCP validation server
5. Test enhanced configuration
