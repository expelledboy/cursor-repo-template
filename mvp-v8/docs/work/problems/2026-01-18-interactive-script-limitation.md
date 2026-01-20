---
title: "Interactive Script Limitations in Chat Environments"
status: active
date: 2026-01-18
domain: agentos
type: problem
evidence_sources: [script execution failures, MAM audit context, interactive input discovery]
---

# Interactive Script Limitations in Chat Environments

## Context
Identified during MAM audit and script architecture analysis. Scripts attempting interactive functionality fail in chat environments due to fundamental interface constraints, yet the codebase contains remnants of such attempts.

## Observation
Scripts cannot use interactive input methods (`input()`, `sys.stdin.readline()`) in chat environments. These calls either fail immediately or behave unpredictably. Despite documented knowledge of this limitation, the codebase still contains interactive script patterns that cannot work.

## Impact Assessment
- **Severity**: High - Creates false expectations of functionality
- **Scope**: Systemic - Affects all script-based interactive features
- **Cost**: Development time wasted on non-functional features, user confusion, architectural inconsistency

## Evidence
- **Script failures**: `run_interactive_retrospect()` cannot execute in chat environment
- **Documented limitation**: `docs/work/discoveries/2026-01-18-interactive-input-limitation.md` explicitly states this constraint
- **Code remnants**: Leftover interactive code that serves no functional purpose
- **MAM audit findings**: Architectural analysis revealed these non-functional patterns

## Root Cause Analysis
Scripts were designed assuming terminal-like interactive capabilities that don't exist in chat interfaces. The architecture mixed interactive intent with script execution constraints without proper separation of concerns.

## Potential Solutions
1. **Complete interactive removal**: Eliminate all interactive script code
2. **Command-layer interactivity**: Move interactive features to Cursor command layer
3. **Clear separation**: Scripts handle execution, commands handle interaction
4. **Documentation alignment**: Ensure docs reflect actual capabilities, not aspirations

## Related Issues
- Context pollution from non-functional script code
- Architectural mismatch between design intent and execution reality
- Interactive input limitation discovery (already documented)
- Script bloat and maintenance overhead