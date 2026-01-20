# /agentos - AgentOS Entry Point

## Purpose
Single entry point for all AgentOS workflows. Takes structured requirement and routes to appropriate workflow.

## Usage

### Option 1: Structured YAML
```
/agentos
```yaml
task:
  type: execution
  objective: Add user authentication with OAuth
  scope:
    domains: [auth, security]
  success_criteria:
    - OAuth flow works end-to-end
    - Tests pass
```

### Option 2: Guided Form
```
/agentos
I want to add user authentication
```
→ Agent will prompt for structured fields

## Instructions for Agent

1. **Requirement Intake**
   - If YAML provided: Parse and validate structure
   - If unstructured text: Guide user through structured form
   - Validate against `schemas/requirement.yaml`
   - Generate task ID: `TASK-YYYYMMDD-XXXXXX`

2. **Load Decision Graphs**
   - Read: `docs/reference/agentos/decisions/task-classification.yaml`
   - Read: `docs/reference/agentos/decisions/complexity-assessment.yaml`
   - Read: `docs/reference/agentos/decisions/workflow-selection.yaml`

3. **Classify Task**
   - Apply task classification decision graph
   - Evaluate each step condition against requirement
   - Route to appropriate workflow type
   - Load workflow documentation

4. **Assess Complexity**
   - Apply complexity assessment decision graph
   - Evaluate 5 dimensions: scope, decisions, risk, effort, dependencies
   - Determine complexity level (1-4)
   - Select workflow variation

5. **Select Workflow**
   - Apply workflow selection decision graph
   - Match task type + complexity → workflow
   - Load workflow documentation: `docs/reference/agentos/workflows/<workflow-name>.md`

6. **Generate Plan**
   - Create structured plan header
   - Generate execution steps from workflow
   - Assign validation methods to each step
   - Link success criteria to validation

7. **Validate Plan**
   - Validate plan structure against schema
   - Check all referenced docs exist
   - Verify workflow steps are complete
   - Call MCP tool: `validate_plan` (if available)

8. **Present to User**
   - Show structured requirement (confirmed)
   - Show task plan header
   - Show execution steps
   - Request confirmation or adjustments

## Expected Outcome

```yaml
plan:
  task_id: TASK-20260114-ABC123
  type: execution
  objective: Add user authentication with OAuth
  workflow: execution-standard
  complexity: 3
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
    - docs/reference/agentos/workflows/execution-standard.md
```

## MCP Tools Used
- `validate_requirement` - Validate requirement structure
- `validate_plan` - Validate plan structure
- `validate_coherence` - Check system coherence

## Fallback (MCP Unavailable)
- Use JSON Schema validation via Python script
- Manual validation checklist
- Continue with plan generation
