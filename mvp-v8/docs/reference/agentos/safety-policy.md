---
title: "Safety Policy"
status: stable
created_date: 2026-01-18
purpose: "Defines safety constraints and validation requirements for AgentOS operations"
domain: agentos
---

# Safety Policy (Reference)

## Purpose
Establishes mandatory safety constraints and validation requirements to prevent harm, data loss, and security incidents during AgentOS operations. Safety is integrated into all DOE (Directive-Orchestration-Execution) processes.

## Core Safety Principles

### Least Privilege
- Operations assume minimal permissions by default
- Explicit permission elevation required for privileged actions
- Safety constraints apply regardless of user context or tool access

### Destructive Action Protection
- **Definition**: Operations that modify, delete, or irreversibly change data/artifacts
- **Requirement**: Explicit user confirmation before execution
- **Validation**: Confirmation recorded in task plan header
- **Rollback**: Contingency plan documented for all destructive operations

### Data Protection
- **Secrets**: Never logged, committed, or exposed in outputs
- **Detection**: Pattern-based identification of potential secrets
- **Prevention**: Operations blocked if secret material detected

## Safety Validation Levels

### Risk Assessment
- **Low Risk**: Read-only operations, documentation changes
- **Medium Risk**: Code modifications, non-destructive file operations
- **High Risk**: Database changes, destructive operations, system modifications

### Validation Enforcement
- **Low Risk**: Basic `/retrospect` audit
- **Medium Risk**: Full `/retrospect` audit required
- **High Risk**: `/retrospect` audit + explicit user confirmation

## Implementation in Commands

### `/retrospect` Safety Checks
```
🛡️  Safety Confirmed
   ❌ Destructive operations detected - user confirmation required
   ❌ Rollback plan must be documented in task header

4.5 🔐 Extended Safety Checks
   ⚠️  Safety concerns: Potential secrets exposure detected
   💡 Get explicit user confirmation and document rollback plan
```

### Validation Integration
- **Hard Errors**: Destructive operations without confirmation block execution
- **Pattern Detection**: Secrets, untrusted inputs, destructive keywords identified
- **Rollback Requirements**: Contingency plans mandatory for critical operations

## Safety Constraints by Operation Type

### File Operations
- **Create/Modify**: Low-medium risk, validation required
- **Delete/Overwrite**: High risk, confirmation + rollback required
- **Batch Operations**: Medium-high risk, individual confirmation may be required

### System Operations
- **Command Execution**: Risk assessed by command type and scope
- **Network Access**: Explicit permission required
- **Process Management**: High risk, confirmation required

### Data Operations
- **Read Access**: Low risk, standard validation
- **Write Access**: Medium risk, rollback planning required
- **Schema Changes**: High risk, full confirmation protocol

## Emergency Procedures

### Safety Violation Detection
- Operations blocked if safety constraints not met
- Clear error messages indicating specific violations
- Suggestion of remediation steps

### Override Protocol
- Safety overrides require explicit user justification
- Overrides logged for audit purposes
- Override reasoning validated for completeness

## Integration Points
- **DOE Flow**: Safety validation at all execution checkpoints
- **Command System**: All commands implement safety validation
- **Validation Scripts**: Safety checks integrated into `scripts/docs/index.py`
- **Rules System**: Safety constraints enforced by `.cursor/rules/core.mdc`

## Related
- `docs/reference/agentos/architecture.md#doe-integrated-flow`
- `docs/reference/agentos/task-plan-spec.md`
- `.cursor/commands/retrospect.md`
- `.cursor/rules/core.mdc`