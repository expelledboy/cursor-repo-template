# /agentos-execute - Task Lifecycle: Execute

## Purpose
Execute implementation phase. Orchestrates features for systematic execution.

## Lifecycle Entrypoint
- Covers: implementation → testing → validation
- Handoff: verify phase

## Instructions for Agent

### 1. Load Phase Rules
- Load: `.cursor/rules/core.mdc` (alwaysApply - already loaded)
- Load: `.cursor/rules/orchestration.mdc` (orchestration patterns)
- Load domain-specific rules (from file context or requirement)

### 2. Review Execution Plan
- Review detailed plan from `/agentos-plan`
- Review execution steps
- Review validation methods
- Review success criteria

### 3. Orchestrate Features for Execution

#### Level 1: Streamlined
- Execute steps directly
- Basic validation
- Quick testing
- Proceed to verification

#### Level 2: Standard
- Execute steps systematically
- Use semantic search for implementation patterns
- Standard validation
- Standard testing
- Proceed to verification

#### Level 3: Enhanced
- Execute steps with checkpoints
- Use semantic search extensively
- Consult pattern library for implementation patterns
- Launch `/code-pattern-searcher` subagent if needed
- Comprehensive validation
- Comprehensive testing
- Proceed to verification

#### Level 4: Maximum
- Execute steps with formal checkpoints
- Use multi-dimensional semantic search
- Consult pattern library extensively
- Launch `/code-pattern-searcher` subagent for code patterns
- Launch `/validator` subagent for coherence validation
- Extensive validation
- Extensive testing
- Request stakeholder review (if needed)
- Proceed to verification

### 4. Execute Implementation Steps
- Follow workflow steps systematically
- Use semantic search for guidance (if needed)
- Consult pattern library (Level 3+)
- Launch subagents for pattern discovery (Level 3+)
- Document progress

### 5. Validate Implementation
- Run tests
- Call MCP tool: `validate_coherence` (if available, Level 2+)
- Launch `/validator` subagent (Level 3+)
- Document validation results

### 6. Present Results
- Show implementation progress
- Show validation results
- Show orchestration metadata
- Request confirmation
- Suggest next command: `/agentos-verify`

## Canonical Entrypoints
- `docs/reference/agentos/core-contract.md`
- `docs/reference/agentos/workflows/<workflow-name>.md`
- `docs/reference/agentos/safety-policy.md`

## Next Command
After completion, proceed to: `/agentos-verify`
