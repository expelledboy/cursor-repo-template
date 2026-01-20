# Execution Workflow (Maximum Rigor)

**Complexity Level**: 4
**Rigor**: Maximum
**Use Case**: Enterprise implementation tasks with critical impact

---

## Orchestration Pattern

**Maximum Orchestration**:
- Full cascading rules (rules trigger rules extensively)
- All relevant subagents in parallel
- Multi-dimensional semantic search
- Multi-layer validation (semantic + MCP + subagent)
- Pattern library learning and reuse

---

## Workflow Steps

### Step 1: Formal Planning
- **Action**: Formal planning with stakeholder alignment
- **Validation**: Plan review, MCP validation, subagent validation, stakeholder review
- **Output**: Formal execution plan
- **Orchestration**: Use full cascading rules, pattern library extensively, all subagents

### Step 2: Architecture Design
- **Action**: Architecture design with multiple alternatives
- **Validation**: Architecture review, design review, stakeholder review
- **Output**: Architecture documentation
- **Orchestration**: Use semantic search extensively, consult pattern library, launch subagents

### Step 3: Phased Implementation with Checkpoints
- **Action**: Implement solution in formal phases with checkpoints
- **Validation**: Unit tests, integration tests, system tests, code review, checkpoint reviews
- **Output**: Implementation code with formal checkpoints
- **Orchestration**: Use file context, launch `/code-pattern-searcher`, consult pattern library

### Step 4: Comprehensive Integration
- **Action**: Enterprise integration with existing system
- **Validation**: Integration tests, system tests, performance tests
- **Output**: Integrated solution
- **Orchestration**: Use semantic search extensively, launch subagents for validation

### Step 5: Extensive Verification
- **Action**: Verify success criteria with extensive testing and validation
- **Validation**: End-to-end tests, manual verification, MCP validation, subagent validation, stakeholder review
- **Output**: Comprehensive verification report
- **Orchestration**: Launch `/validator` subagent, use multi-layer validation

---

## Validation Gates

- **Structure**: Requirement schema validation (MCP)
- **Code**: Unit tests, integration tests, system tests, linting, code review
- **Integration**: Integration tests, system tests, performance tests
- **Outcome**: Success criteria verification
- **Coherence**: MCP coherence validation, subagent validation
- **Security**: Security audit (if security-sensitive)
- **Performance**: Performance testing (if performance-critical)
- **Stakeholder**: Stakeholder review and approval

---

## Documentation Requirements

- Update relevant documentation comprehensively
- Document design decisions with extensive rationale
- Update changelog
- Create architecture documentation
- Create deployment documentation (if needed)

---

## Success Criteria

All success criteria from requirement must be met and verified extensively with stakeholder approval.

---

## Feature Orchestration

### Rules
- **alwaysApply**: Core rule always loaded
- **description**: Domain rules load on keyword match
- **globs**: File rules load on file context
- **Cascading**: Maximum cascading (rules trigger rules extensively, domain rules trigger related rules extensively)

### Commands
- `/agentos` → `/agentos-start` → `/agentos-plan` → `/agentos-execute` → `/agentos-verify` → `/agentos-complete`
- Each command uses maximum orchestration

### Subagents
- Launch all relevant subagents in parallel:
  - `/pattern-searcher`
  - `/code-pattern-searcher`
  - `/doc-pattern-searcher`
  - `/complexity-assessor`
  - `/workflow-selector`
  - `/validator`

### Semantic Search
- Use multi-dimensional semantic searches in parallel
- Search for similar implementations, patterns, documentation, architecture

### MCP
- Multi-layer validation (plan, requirement, coherence, security if applicable)

### Pattern Library
- Consult pattern library extensively for similar patterns
- Learn new patterns from successful task
- Update pattern library with learned patterns

---

## Semantic Understanding Integration

When executing this workflow:
- Use semantic understanding extensively to guide implementation
- Match semantic patterns from requirement and pattern library extensively
- Use semantic search extensively for similar implementations
- Leverage file context (globs) for domain understanding
- Learn patterns extensively for future reuse
- Update pattern library with successful patterns
