# /agentos-plan - Task Lifecycle: Plan

## Purpose
Create detailed execution plan. Orchestrates features for comprehensive planning.

## Lifecycle Entrypoint
- Covers: detailed planning → validation → confirmation
- Handoff: execute phase

## Instructions for Agent

### 1. Load Phase Rules
- Load: `.cursor/rules/core.mdc` (alwaysApply - already loaded)
- Load: `.cursor/rules/orchestration.mdc` (orchestration patterns)
- Check for planning-specific rules (if exist)

### 2. Review Task Context
- Review task plan header from `/agentos-start`
- Review orchestration metadata
- Review semantic understanding
- Review workflow selected

### 3. Orchestrate Features for Planning

#### Level 1: Streamlined
- Generate brief plan
- Skip extensive validation
- Proceed to execution

#### Level 2: Standard
- Generate standard plan
- Use semantic search for planning patterns
- Call MCP tool: `validate_plan`
- Proceed to execution

#### Level 3: Enhanced
- Generate comprehensive plan
- Use semantic search extensively
- Consult pattern library for planning patterns
- Call MCP tool: `validate_plan`
- Launch `/validator` subagent for coherence validation
- Proceed to execution

#### Level 4: Maximum
- Generate formal plan
- Use multi-dimensional semantic search
- Consult pattern library extensively
- Call MCP tool: `validate_plan`
- Launch `/validator` subagent for comprehensive validation
- Request stakeholder review (if needed)
- Proceed to execution

### 4. Generate Execution Steps
- Load workflow documentation
- Generate detailed steps from workflow
- Assign validation to each step
- Link success criteria to steps
- Document orchestration used

### 5. Validate Plan
- Call MCP tool: `validate_plan` (Level 2+)
- Launch `/validator` subagent (Level 3+)
- Document validation results

### 6. Present Plan
- Show detailed execution plan
- Show validation results
- Show orchestration metadata
- Request confirmation
- Suggest next command: `/agentos-execute`

## Canonical Entrypoints
- `docs/reference/agentos/core-contract.md`
- `docs/reference/agentos/workflows/<workflow-name>.md`

## Next Command
After completion, proceed to: `/agentos-execute`
