# /agentos - Semantic Entry Point

## Purpose
Single entry point for all AgentOS workflows. Uses semantic understanding to route requirements to appropriate workflows.

## Usage

### Natural Language Requirement
```
/agentos
I want to add user authentication with OAuth
```

### Structured YAML (Optional)
```
/agentos
```yaml
task:
  objective: Add user authentication with OAuth
  scope:
    domains: [auth, security]
  success_criteria:
    - OAuth flow works end-to-end
    - Tests pass
```

## Instructions for Agent

### 1. Understand Requirement Semantically
- Read requirement for meaning, not just structure
- Identify semantic patterns in the requirement
- Extract key concepts:
  - **Domain**: What area is this about? (auth, testing, docs, etc.)
  - **Objective**: What needs to be accomplished?
  - **Scope**: What's affected? (files, components, systems)
  - **Type**: Implementation? Coordination? Architecture? Direct?
- If structured YAML provided, understand the semantic meaning behind the structure

### 2. Use Semantic Search (if unclear)
When classification or understanding is unclear:
- Extract key concepts from requirement
- Use semantic search: "tasks like [requirement summary]"
- Search for: "requirements involving [domain] and [objective pattern]"
- Review similar patterns found
- Learn from past similar tasks
- Document search terms and results in task plan header

### 3. Leverage File Context (globs)
- Check what files are currently open
- Understand domain from file patterns:
  - `src/auth/**` → Authentication domain
  - `tests/**` → Testing domain
  - `docs/**` → Documentation domain
- Load domain-specific semantic patterns (via globs rules)
- Use file context to inform classification and routing

### 4. Layer Rules (alwaysApply + description + globs)
Rules work together to provide rich semantic context:
- **Core patterns** (alwaysApply): Always loaded, foundational
- **Domain patterns** (description): Load on keyword match (auth, security, testing, etc.)
- **File patterns** (globs): Load on file context (file paths match patterns)
- Combine all matching rules for comprehensive semantic understanding
- Document which rules loaded in task plan header

### 5. Classify Task Semantically
- Load: `docs/reference/agentos/decisions/task-classification.md`
- Understand requirement semantically
- Match semantic patterns to task types:
  - Execution: Implementation-focused, clear objective
  - Coordination: Stakeholder alignment needed
  - Architecture: System-wide, structural changes
  - Direct: Simple, isolated changes
- Use semantic search if classification unclear
- Document semantic reasoning in task plan header

### 6. Assess Complexity Semantically
- Load: `docs/reference/agentos/decisions/complexity-assessment.md`
- Understand complexity dimensions semantically:
  - Scope: What's the semantic scope? (single file vs system-wide)
  - Decisions: What decisions are needed? (obvious vs strategic)
  - Risk: What's the semantic risk? (low vs critical)
  - Effort: What's the semantic effort? (quick vs extensive)
  - Dependencies: What dependencies exist? (none vs critical)
- Take maximum level across dimensions
- Apply escalation rules semantically
- Use semantic search if complexity unclear
- Document complexity reasoning

### 7. Select Workflow Semantically
- Load: `docs/reference/agentos/decisions/workflow-selection.md`
- Match task type + complexity → workflow semantically
- Understand the meaning of the combination
- Load workflow documentation: `docs/reference/agentos/workflows/<workflow-name>.md`
- Use semantic search if workflow selection unclear

### 8. Generate Plan with Semantic Understanding
Create structured plan header including semantic understanding:

```yaml
plan:
  task_id: TASK-YYYYMMDD-XXXXXX
  semantic_understanding:
    requirement_meaning: [what I understood from the requirement]
    patterns_matched: [semantic patterns I recognized]
    similar_patterns_found: [results from semantic search, if used]
    context_used: [file patterns, domain rules that informed understanding]
  type: [from semantic classification]
  objective: [from requirement]
  complexity: [from semantic assessment]
  workflow: [from semantic workflow selection]
  steps: [structured execution steps from workflow]
  success_criteria: [from requirement]
  loaded_docs: [list of all documentation loaded]
  rules_loaded: [list of rules that matched: alwaysApply, description keywords, globs patterns]
```

### 9. Validate Structure (MCP)
- Semantic understanding routes the task
- MCP validates structure (if available):
  - `validate_requirement` - Validate requirement structure
  - `validate_plan` - Validate plan structure
- Two-layer validation: semantic routing + structure validation
- If MCP unavailable, use manual validation checklist

### 10. Present to User
- Show semantic understanding (what I understood)
- Show task plan header with semantic reasoning
- Show which rules loaded and why
- Show semantic search results (if used)
- Show file context used (if applicable)
- Request confirmation or adjustments

## Expected Outcome

```yaml
plan:
  task_id: TASK-20260114-ABC123
  semantic_understanding:
    requirement_meaning: "User wants to add OAuth authentication, which is a security-sensitive implementation task"
    patterns_matched: ["implementation-focused", "security domain", "clear objective"]
    similar_patterns_found: "Found 3 similar authentication tasks in codebase"
    context_used: ["auth domain rule loaded", "security patterns from globs"]
  type: execution
  objective: Add user authentication with OAuth
  complexity: 3
  workflow: execution-enhanced
  steps:
    - id: step-1
      action: Design OAuth flow
      validation: design-review
    - id: step-2
      action: Implement OAuth provider integration
      validation: unit-tests
    - id: step-3
      action: Add authentication middleware
      validation: integration-tests
  success_criteria:
    - OAuth flow works end-to-end
    - Tests pass
  loaded_docs:
    - docs/reference/agentos/workflows/execution-enhanced.md
    - docs/reference/agentos/decisions/task-classification.md
  rules_loaded:
    - alwaysApply: core.mdc
    - description: auth (matched "authentication")
    - globs: ["src/auth/**"] (file context)
```

## MCP Tools Used
- `validate_requirement` - Validate requirement structure (if available)
- `validate_plan` - Validate plan structure (if available)
- `validate_coherence` - Check system coherence (if available)

## Fallback (MCP Unavailable)
- Use manual validation checklist
- Continue with semantic understanding workflow
- Document that MCP validation was skipped

## Key Principles
- Semantic understanding over syntax parsing
- Feature interplay (rules work together)
- Pattern discovery via semantic search
- Context awareness from file patterns
- Two-layer validation (semantic + structure)
