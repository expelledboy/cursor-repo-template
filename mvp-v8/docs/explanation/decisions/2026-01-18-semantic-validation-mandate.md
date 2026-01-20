---
title: "Decision: Semantic Validation Mandate"
status: accepted
created_date: 2026-01-18
purpose: "Establish mandatory semantic validation to prevent logical correctness failures in DOE framework execution"
domain: agentos
type: policy
related:
  - docs/work/problems/2026-01-18-doe-framework-execution-failure.md
  - docs/work/problems/2026-01-18-validation-script-inadequate.md
implementations:
  - scripts/docs/index.py
  - .cursor/rules/core.mdc
  - .cursor/commands/distill.md
---

# Decision: Semantic Validation Mandate

## Context
The DOE framework has been failing at the Execution layer due to validation scripts that check form/syntax but not semantic correctness (logical intent). This has led to repeated mistakes where work files containing valuable rationale are incorrectly archived as "superseded" despite clear policy stating they should remain as permanent records.

## Problem
- Validation validates **what** (syntax/form) but not **why** (semantic correctness)
- Work files incorrectly archived despite preservation policy
- Behavioral inconsistency between documented intent and actual execution
- Same logical errors repeated despite established rules

## Solution
Implement mandatory **semantic validation** that checks both form AND intent before allowing operations to proceed.

### Requirements
1. **Dual Validation**: Every operation must pass both syntactic (form) and semantic (intent) validation
2. **Work File Protection**: Work files (problems, discoveries) must NEVER be archived as "superseded" - they are permanent rationale
3. **Pre-Execution Gates**: Validate intent before executing operations, not just after
4. **Policy Enforcement**: Validation must enforce documented policies, not just schemas

### Implementation
- Enhanced validation script with semantic checks
- Updated core rules requiring semantic validation
- Modified commands with intent validation requirements
- Clear error messages distinguishing form vs intent violations

## Rationale
The root cause is a validation gap: form validation (syntax/schema) exists but semantic validation (logical correctness) does not. This allows operations that are mechanically correct but logically wrong to pass validation.

By requiring both form AND intent validation, we close the DOE execution gap and ensure the system actually follows its documented policies.

## Impact
- Eliminates incorrect archiving of rationale-rich work files
- Prevents semantic correctness failures
- Ensures DOE framework execution aligns with documented intent
- Provides clear feedback on both form and intent violations

## Validation
Semantic validation will be tested by:
1. Running validation on existing incorrectly archived files (should fail)
2. Attempting to archive work files (should be blocked)
3. Verifying proper superseded fields for canonical docs (should pass)