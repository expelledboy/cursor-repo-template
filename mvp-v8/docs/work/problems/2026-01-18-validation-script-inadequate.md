---
title: "Validation Script Provides Inadequate Guidance"
created_date: 2026-01-18
domain: agentos
Status: active
related:
  - docs/explanation/decisions/2026-01-18-validation-system-enhancement.md
---

# Validation Script Provides Inadequate Guidance

## Observation
The `scripts/docs/index.py` validation script only performs basic checks and misses critical documentation pattern violations, providing insufficient guidance for maintaining system integrity.

## Impact
- **Pattern Drift**: Documentation patterns degrade without comprehensive validation
- **Manual Oversight**: Agents must manually verify compliance instead of automated checks
- **Inconsistent Quality**: Some validations pass while major structural issues exist
- **Learning Barriers**: Agents don't receive clear feedback on what constitutes valid documentation

## Evidence
Current validation covers only:
- YAML syntax and basic frontmatter fields
- File existence for links and implementations
- Basic content sections for work docs

Missing critical validations:
- Diátaxis bucket compliance
- Domain consistency and assignment rules
- Authority order violations
- Work document requirements (Status field)
- Archive requirements
- Decision criteria compliance
- File naming pattern validation
- Cross-domain linking rules

## Root Cause
The validation script was built incrementally without comprehensive research into all documentation system patterns and constraints. It validates syntax but not semantics.

## Potential Solutions
1. **Comprehensive Pattern Audit**: Research all documentation patterns across Diátaxis, domains, and authority levels
2. **Semantic Validation**: Add checks for structural compliance beyond basic syntax
3. **Actionable Feedback**: Provide specific guidance on how to fix violations
4. **Progressive Validation**: Different validation levels (syntax → structure → semantics)
5. **Self-Correction Prompts**: Generate specific commands to fix identified issues