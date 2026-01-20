# /agentos-verify - Task Lifecycle: Verify

## Purpose
Verify implementation phase. Orchestrates features for comprehensive verification.

## Lifecycle Entrypoint
- Covers: verification → validation → testing
- Handoff: complete phase

## Instructions for Agent

### 1. Load Phase Rules
- Load: `.cursor/rules/core.mdc` (alwaysApply - already loaded)
- Load: `.cursor/rules/orchestration.mdc` (orchestration patterns)
- Load verification-specific rules (if exist)

### 2. Review Implementation
- Review implementation from `/agentos-execute`
- Review success criteria
- Review validation results
- Review orchestration metadata

### 3. Orchestrate Features for Verification

#### Level 1: Streamlined
- Basic verification
- Quick testing
- Proceed to completion

#### Level 2: Standard
- Standard verification
- Standard testing
- Call MCP tool: `validate_coherence` (if available)
- Proceed to completion

#### Level 3: Enhanced
- Comprehensive verification
- Comprehensive testing
- Call MCP tool: `validate_coherence` (if available)
- Launch `/validator` subagent for coherence validation
- Proceed to completion

#### Level 4: Maximum
- Extensive verification
- Extensive testing
- Call MCP tool: `validate_coherence` (if available)
- Launch `/validator` subagent for comprehensive validation
- Request stakeholder review (if needed)
- Proceed to completion

### 4. Verify Success Criteria
- Check each success criterion
- Run tests
- Validate outcomes
- Document verification results

### 5. Validate Coherence
- Check documentation ↔ implementation alignment
- Call MCP tool: `validate_coherence` (Level 2+)
- Launch `/validator` subagent (Level 3+)
- Document validation results

### 6. Present Verification Results
- Show verification results
- Show validation results
- Show orchestration metadata
- Request confirmation
- Suggest next command: `/agentos-complete`

## Canonical Entrypoints
- `docs/reference/agentos/core-contract.md`
- `docs/reference/agentos/workflows/<workflow-name>.md`

## Next Command
After completion, proceed to: `/agentos-complete`
