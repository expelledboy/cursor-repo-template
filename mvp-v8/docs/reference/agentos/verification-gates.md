---
title: "Verification Gates Catalog"
status: stable
created_date: 2026-01-18
purpose: "Canonical catalog mapping task types to verification commands for deterministic quality assurance"
domain: agentos
---

# Verification Gates Catalog (Reference)

## Purpose
Provides a canonical mapping between task types and their appropriate verification commands (gates). Ensures consistent, deterministic quality assurance across all AgentOS operations. Gates are designed to catch issues early while allowing efficient execution of validated work.

## Gate Design Principles

### Deterministic Commands
- Gates must be runnable, non-interactive commands
- Commands return clear pass/fail exit codes
- No external dependencies beyond standard development environment
- Commands complete within reasonable time limits (< 5 minutes)

### Task-Type Specificity
- Gates match the risk profile and validation needs of each task type
- Higher-risk tasks have more comprehensive gates
- Gates scale with task complexity (Level 1-4)
- Unmapped task types generate warnings with suggestions

### CI Alignment
- Gates represent the minimum standard for continuous integration
- Additional project-specific gates can extend but not replace these
- Gates validate both form (syntax) and intent (correctness)

## Verification Gate Catalog

### Core Development Tasks

| Task Type | Primary Gate | Risk Level | Purpose |
|-----------|--------------|------------|---------|
| **Implementation / Feature** | `just test` | High | Validates code correctness, integration, and regressions |
| **Documentation & Knowledge** | `just docs::validate` | Low | Ensures documentation integrity and link validity |
| **Design/Architecture** | `just docs::validate` | Medium | Validates design documentation and structural integrity |
| **Testing & Verification** | `just test` | High | Ensures testing frameworks and coverage validation |
| **Refactoring & Tech-Debt** | `just test` | Medium | Prevents regression during code restructuring |

### Project Management Tasks

| Task Type | Primary Gate | Risk Level | Purpose |
|-----------|--------------|------------|---------|
| **Discovery & Requirements** | `just docs::validate` | Low | Validates requirement documentation completeness |
| **Planning & Estimation** | `just docs::validate` | Low | Ensures planning artifacts are well-formed |
| **Release/Deploy** | build/smoke | High | Validates deployment readiness and basic functionality |
| **Operations & Maintenance** | smoke-test | Medium | Ensures system stability after maintenance |

### Security & Compliance Tasks

| Task Type | Primary Gate | Risk Level | Purpose |
|-----------|--------------|------------|---------|
| **Security & Compliance** | lint/baseline | High | Validates security posture and compliance requirements |
| **Incident Response & Debugging** | diagnostic-check | Medium | Ensures diagnostic capabilities and issue isolation |

### Meta-Maintenance Tasks

| Task Type | Primary Gate | Risk Level | Purpose |
|-----------|--------------|------------|---------|
| **AgentOS Meta-Maintenance** | `just docs::validate` | High | Validates AgentOS system integrity and documentation |

## Gate Implementation Details

### `just test`
**Scope**: Unit tests, integration tests, basic functionality
**Exit Codes**: 0 = pass, non-zero = fail
**Timeout**: 10 minutes
**Dependencies**: Test framework configured in project

### `just docs::validate`
**Scope**: Markdown syntax, link validity, frontmatter completeness, authority compliance
**Exit Codes**: 0 = pass, 1 = validation errors
**Timeout**: 2 minutes
**Dependencies**: Python environment with validation scripts

### `build/smoke`
**Scope**: Basic build process and smoke tests for deployment readiness
**Exit Codes**: 0 = deployable, non-zero = not ready
**Timeout**: 5 minutes
**Dependencies**: Build system and minimal test environment

### `smoke-test`
**Scope**: Basic system functionality after maintenance operations
**Exit Codes**: 0 = stable, non-zero = issues detected
**Timeout**: 3 minutes
**Dependencies**: System access and monitoring tools

### `lint/baseline`
**Scope**: Code quality, security scanning, compliance checks
**Exit Codes**: 0 = compliant, non-zero = issues found
**Timeout**: 5 minutes
**Dependencies**: Linting and security scanning tools

### `diagnostic-check`
**Scope**: System diagnostic capabilities and issue isolation tools
**Exit Codes**: 0 = diagnostics functional, non-zero = diagnostic failures
**Timeout**: 2 minutes
**Dependencies**: Diagnostic and logging tools

## Gate Execution Integration

### `/retrospect` Command Integration
- Validates gate existence for task type
- Checks gate command availability
- Reports gate mapping status
- Suggests gate additions for unmapped types

### Task Lifecycle Integration
- **Pre-execution**: Gates validated and runnable
- **Post-execution**: Gates executed and results captured
- **Failure handling**: Gate failures block progression with clear error messages

### Risk-Based Gate Application
- **Low Risk**: Basic validation (docs, linting)
- **Medium Risk**: Functional testing + validation
- **High Risk**: Comprehensive testing + security + deployment validation

## Gate Maintenance

### Adding New Gates
1. Identify task type not covered by existing gates
2. Define appropriate validation command meeting deterministic criteria
3. Add to catalog with risk level and purpose
4. Update `/retrospect` task type mappings
5. Test gate integration

### Gate Updates
- Gates can be enhanced but must maintain backwards compatibility
- New gate versions should be additive (stricter but not breaking)
- Gate failures should provide actionable remediation steps

### Gate Validation
- Gates themselves are validated for correctness
- Gate execution is monitored for performance and reliability
- Gate failures trigger investigation and potential gate updates

## Related
- `docs/reference/agentos/architecture.md#doe-integrated-flow`
- `docs/reference/agentos/task-plan-spec.md`
- `docs/reference/agentos/safety-policy.md`
- `.cursor/commands/retrospect.md`