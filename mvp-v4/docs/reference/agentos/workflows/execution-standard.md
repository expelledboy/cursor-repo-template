# Execution Workflow (Standard Rigor)

**Complexity Level**: 2
**Rigor**: Standard
**Use Case**: Typical implementation tasks with moderate scope

---

## Orchestration Pattern

**Standard Orchestration**:
- Full rule layering (alwaysApply + description + globs)
- 2-3 subagents in parallel for pattern discovery (if needed)
- Standard semantic search
- Standard MCP validation

---

## Workflow Steps

### Step 1: Planning
- **Action**: Review requirement and create detailed plan
- **Validation**: Plan review checklist, MCP validation
- **Output**: Structured execution plan
- **Orchestration**: Use full rule layering, standard semantic search

### Step 2: Design
- **Action**: Design solution approach
- **Validation**: Design review (if complexity warrants)
- **Output**: Design notes
- **Orchestration**: Use semantic search for design patterns

### Step 3: Implementation
- **Action**: Implement solution
- **Validation**: Unit tests, code review
- **Output**: Implementation code
- **Orchestration**: Use file context (globs) for domain understanding

### Step 4: Integration
- **Action**: Integrate with existing system
- **Validation**: Integration tests
- **Output**: Integrated solution
- **Orchestration**: Use semantic search for integration patterns

### Step 5: Verification
- **Action**: Verify success criteria met
- **Validation**: End-to-end tests, manual verification, MCP validation
- **Output**: Verification report
- **Orchestration**: Use MCP for coherence validation

---

## Validation Gates

- **Structure**: Requirement schema validation (MCP)
- **Code**: Unit tests, linting
- **Integration**: Integration tests
- **Outcome**: Success criteria verification
- **Coherence**: MCP coherence validation (if available)

---

## Documentation Requirements

- Update relevant documentation
- Document design decisions (if any)
- Update changelog

---

## Success Criteria

All success criteria from requirement must be met and verified.

---

## Feature Orchestration

### Rules
- **alwaysApply**: Core rule always loaded
- **description**: Domain rules load on keyword match
- **globs**: File rules load on file context
- **Cascading**: Basic cascading (domain rules trigger related rules)

### Commands
- `/agentos` → `/agentos-start` → `/agentos-plan` → `/agentos-execute` → `/agentos-verify` → `/agentos-complete`
- Each command uses standard orchestration

### Subagents
- Launch `/pattern-searcher` and `/code-pattern-searcher` in parallel (if pattern discovery needed)
- Launch `/complexity-assessor` (if complexity reassessment needed)
- Launch `/workflow-selector` (if workflow reselection needed)

### Semantic Search
- Use standard semantic search for pattern discovery
- Search for similar implementations

### MCP
- Standard validation (plan, requirement, coherence)

### Pattern Library
- Skip pattern library consultation (Level 2)

---

## Semantic Understanding Integration

When executing this workflow:
- Use semantic understanding to guide implementation
- Match semantic patterns from requirement
- Use semantic search for similar implementations
- Leverage file context (globs) for domain understanding
