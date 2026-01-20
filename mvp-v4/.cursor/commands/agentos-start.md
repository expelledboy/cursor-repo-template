# /agentos-start - Task Lifecycle: Start

## Purpose
Begin task execution phase. Orchestrates features for task initialization and planning.

## Lifecycle Entrypoint
- Covers: intake → classify → route → complexity → plan
- Handoff: execute phase

## Instructions for Agent

### 1. Load Phase Rules
- Load: `.cursor/rules/core.mdc` (alwaysApply - already loaded)
- Load: `.cursor/rules/orchestration.mdc` (orchestration patterns)
- Check for phase-specific rules (if exist)

### 2. Review Task Plan Header
- Review task plan header from `/agentos` command
- Confirm orchestration metadata is complete
- Confirm semantic understanding is documented
- Confirm workflow is selected

### 3. Orchestrate Features Based on Complexity

#### Level 1: Streamlined
- Use basic rule layering (alwaysApply + description/globs)
- Skip subagents (already done in `/agentos`)
- Proceed directly to planning

#### Level 2: Standard
- Use full rule layering (alwaysApply + description + globs)
- Review pattern discovery results from `/agentos`
- Use semantic search if planning unclear
- Proceed to planning

#### Level 3: Enhanced
- Use cascading rules (rules trigger rules)
- Review pattern discovery results from `/agentos`
- Consult pattern library for planning patterns
- Use semantic search for planning guidance
- Launch `/validator` subagent if plan validation needed
- Proceed to comprehensive planning

#### Level 4: Maximum
- Use full cascading rules
- Review all pattern discovery results
- Consult pattern library extensively
- Use multi-dimensional semantic search
- Launch `/validator` subagent for plan validation
- Proceed to formal planning

### 4. Generate Detailed Plan
- Load workflow documentation: `docs/reference/agentos/workflows/<workflow-name>.md`
- Generate detailed execution steps
- Assign validation methods to each step
- Link success criteria to validation
- Document orchestration used in plan

### 5. Validate Plan (Level 2+)
- Call MCP tool: `validate_plan` (if available)
- For Level 3+: Launch `/validator` subagent for coherence validation
- Document validation results

### 6. Present Plan
- Show detailed plan with orchestration metadata
- Show validation results
- Request confirmation
- Suggest next command: `/agentos-execute`

## Canonical Entrypoints
- `docs/reference/agentos/core-contract.md`
- `docs/reference/agentos/meta-orchestration.md`
- `docs/reference/agentos/workflows/<workflow-name>.md`

## Next Command
After completion, proceed to: `/agentos-execute`
