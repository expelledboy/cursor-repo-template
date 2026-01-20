# AgentOS MVP Configuration

## Project Description

This is the AgentOS MVP - a self-sustaining coherence engine that maintains alignment between documentation, implementation, and behavior surfaces.

## Registry Scope

The following paths are in scope for registry validation (bidirectional docs↔code mapping):

### Core Contracts
- `docs/reference/agentos/coherence-contract.md`
- `docs/reference/agentos/evolution-framework.md`
- `docs/reference/agentos/validation-contract.md`
- `docs/reference/agentos/architectural-patterns.md`
- `docs/reference/agentos/alignment-mechanisms.md`

### Validation Scripts
- `scripts/agentos/validate_registry.py`
- `scripts/agentos/validate_traceability.py`
- `scripts/agentos/validate_behavior.py`
- `scripts/agentos/validate_docs.py`
- `scripts/agentos/validate_adr_format.py`
- `scripts/agentos/validate_verification_gates.py`
- `scripts/agentos/validate_core_list_sync.py`
- `scripts/agentos/validate_routing.py`
- `scripts/agentos/validate_improvement_notes.py`
- `scripts/agentos/validate_design_decisions.py`
- `scripts/agentos/validate_complexity_workflow.py`
- `scripts/agentos/validate_commands.py`
- `scripts/agentos/validate_directive_loading.py`
- `scripts/agentos/validate_agentos.py`

### Test Scripts
- `tests/agentos/validation.bats`

### Configuration
- `AGENTS.md` (this file)
- `.cursor/rules/20-agentos.topic.mdc` (routing rules)

## Verification Expectations

### CI Gates
- Registry validation passes
- Traceability validation passes
- Documentation validation passes
- ADR format validation passes

### Task Runner Integration
- `just agentos::validate-agentos` runs all validations
- Individual validation commands available for targeted checks

## Domain Configuration

### Primary Domain: agentos
**Routing Rule**: `.cursor/rules/20-agentos.topic.mdc`
**Reference Docs**: `docs/reference/agentos/`
**How-To Docs**: `docs/how-to/agentos/`
**Explanation Docs**: `docs/explanation/agentos/`

### Context Compass Intent
- **Execution tasks**: Load reference + how-to docs
- **Architecture tasks**: Load explanation + reference docs
- **Meta-maintenance tasks**: Load all doc types

## Bootstrap Requirements

To exit bootstrap mode, the following must be true:

1. Registry scope defined (this file)
2. Core validation scripts implemented
3. Routing rules created
4. Problem registry populated
5. Initial coherence validation passes

## Evolution Tracking

Changes to this configuration follow the evolution protocol:
- Gap detection through validation failures
- Work notes in `docs/work/agentos/`
- ADRs in `docs/explanation/agentos/decisions/`
- Traceability updates in `docs/reference/agentos/traceability.md`