# Execution Workflow (Minimal Rigor)

**Complexity Level**: 1
**Rigor**: Minimal
**Use Case**: Simple, isolated implementation tasks

---

## Orchestration Pattern

**Streamlined Orchestration**:
- Basic rule layering (alwaysApply + description/globs)
- Skip subagents (orchestration already done in `/agentos`)
- Minimal semantic search
- Basic MCP validation

---

## Workflow Steps

### Step 1: Quick Planning
- **Action**: Brief plan review
- **Validation**: Basic checklist
- **Output**: Simple execution plan
- **Orchestration**: Use basic rule layering only

### Step 2: Direct Implementation
- **Action**: Implement solution directly
- **Validation**: Basic tests
- **Output**: Implementation code
- **Orchestration**: Use file context (globs) for domain understanding

### Step 3: Quick Verification
- **Action**: Verify success criteria
- **Validation**: Basic verification
- **Output**: Verification report
- **Orchestration**: Skip extensive validation

---

## Validation Gates

- **Structure**: Basic requirement validation (MCP if available)
- **Code**: Basic tests
- **Outcome**: Success criteria verification

---

## Documentation Requirements

- Minimal documentation updates
- Update changelog if needed

---

## Success Criteria

All success criteria from requirement must be met.

---

## Feature Orchestration

### Rules
- **alwaysApply**: Core rule always loaded
- **description/globs**: Domain rules load on keyword/file match
- **Cascading**: Skip cascading rules for Level 1

### Commands
- `/agentos` → `/agentos-start` → `/agentos-execute` → `/agentos-verify` → `/agentos-complete`
- Each command uses streamlined orchestration

### Subagents
- Skip subagents (already done in `/agentos` if needed)

### Semantic Search
- Use basic semantic search if unclear
- Skip parallel searches

### MCP
- Basic validation only (if available)

### Pattern Library
- Skip pattern library consultation

---

## Semantic Understanding Integration

When executing this workflow:
- Use semantic understanding to guide implementation
- Match semantic patterns from requirement
- Use basic semantic search if needed
- Leverage file context (globs) for domain understanding
