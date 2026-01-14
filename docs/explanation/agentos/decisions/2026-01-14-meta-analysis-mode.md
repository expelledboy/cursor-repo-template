# Decision: Meta Analysis Mode

**Status**: Accepted
**Date**: 2026-01-14
**Scope**: agentos
**Problem IDs**: PRB-0002; PRB-0005

## Context
AgentOS has no log access and cannot validate its own behavior without relying on visible context.

## Decision
Define Meta Analysis Mode (MAM) as a bounded self-audit that uses only the current chat context and loaded directives.
Require the agent to ask the user before entering MAM and to follow a fixed checklist.

## Alternatives
- Require persistent logs for behavioral validation.
- Allow unstructured self-audits without a checklist.

## Consequences
- Adds a repeatable self-audit step without logs.
- Requires users to approve MAM when triggers occur.

## Why this worked
MAM provides bounded, explainable validation using only visible evidence, reducing reliance on opaque memory.

## Artifacts
- `docs/reference/agentos/meta-analysis.md`
- `docs/reference/agentos/self-improvement.md`
