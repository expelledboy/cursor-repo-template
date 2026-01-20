# Execution Workflow (Enhanced Rigor)

**Complexity Level**: 3
**Rigor**: Enhanced
**Use Case**: Complex implementation tasks with system-wide impact

---

## Orchestration Pattern

**Enhanced Orchestration**:
- Cascading rules (rules trigger rules)
- 3+ subagents in parallel for comprehensive discovery
- Multiple semantic searches in parallel
- Comprehensive MCP validation
- Pattern library consultation

---

## Workflow Steps

### Step 1: Comprehensive Planning
- **Action**: Detailed planning with stakeholder input (if needed)
- **Validation**: Plan review, MCP validation, subagent validation
- **Output**: Comprehensive execution plan
- **Orchestration**: Use cascading rules, pattern library, parallel subagents

### Step 2: Design Review
- **Action**: Design solution approach with alternatives
- **Validation**: Design review, architecture review
- **Output**: Design documentation
- **Orchestration**: Use semantic search extensively, consult pattern library

### Step 3: Phased Implementation
- **Action**: Implement solution in phases with checkpoints
- **Validation**: Unit tests, integration tests, code review
- **Output**: Implementation code with checkpoints
- **Orchestration**: Use file context, launch `/code-pattern-searcher` for code patterns

### Step 4: Integration Testing
- **Action**: Comprehensive integration with existing system
- **Validation**: Integration tests, system tests
- **Output**: Integrated solution
- **Orchestration**: Use semantic search for integration patterns

### Step 5: Comprehensive Verification
- **Action**: Verify success criteria with extensive testing
- **Validation**: End-to-end tests, manual verification, MCP validation, subagent validation
- **Output**: Comprehensive verification report
- **Orchestration**: Launch `/validator` subagent for coherence validation

---

## Validation Gates

- **Structure**: Requirement schema validation (MCP)
- **Code**: Unit tests, integration tests, linting, code review
- **Integration**: Integration tests, system tests
- **Outcome**: Success criteria verification
- **Coherence**: MCP coherence validation, subagent validation
- **Security**: Security audit (if security-sensitive)

---

## Documentation Requirements

- Update relevant documentation comprehensively
- Document design decisions with rationale
- Update changelog
- Create architecture documentation (if needed)

---

## Success Criteria

All success criteria from requirement must be met and verified comprehensively.

---

## Feature Orchestration

### Rules
- **alwaysApply**: Core rule always loaded
- **description**: Domain rules load on keyword match
- **globs**: File rules load on file context
- **Cascading**: Full cascading (rules trigger rules, domain rules trigger related rules)

### Commands
- `/agentos` → `/agentos-start` → `/agentos-plan` → `/agentos-execute` → `/agentos-verify` → `/agentos-complete`
- Each command uses enhanced orchestration

### Subagents
- Launch `/pattern-searcher`, `/code-pattern-searcher`, `/doc-pattern-searcher` in parallel
- Launch `/complexity-assessor` for complexity assessment
- Launch `/workflow-selector` for workflow selection
- Launch `/validator` for validation

### Semantic Search
- Use multiple semantic searches in parallel
- Search for similar implementations, patterns, documentation

### MCP
- Comprehensive validation (plan, requirement, coherence)

### Pattern Library
- Consult pattern library for similar patterns
- Learn new patterns from successful task

---

## Semantic Understanding Integration

When executing this workflow:
- Use semantic understanding extensively to guide implementation
- Match semantic patterns from requirement and pattern library
- Use semantic search extensively for similar implementations
- Leverage file context (globs) for domain understanding
- Learn patterns for future reuse
