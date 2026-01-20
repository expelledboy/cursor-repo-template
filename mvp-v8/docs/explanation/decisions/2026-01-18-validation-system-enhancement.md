---
title: "Decision: Comprehensive Validation System Enhancement"
status: accepted
created_date: 2026-01-18
purpose: "Enhance validation script to enforce all documentation patterns and provide actionable guidance"
domain: agentos
related:
  - docs/work/problems/2026-01-18-validation-script-inadequate.md
  - docs/reference/docs/doc-authority.md
  - docs/reference/docs/frontmatter-schema.md
implementations:
  - scripts/docs/index.py
---

# Decision: Comprehensive Validation System Enhancement

## Decision
We will enhance `scripts/docs/index.py` to provide comprehensive validation of all documentation system patterns, including Diátaxis compliance, domain consistency, authority order validation, and semantic correctness.

## Rationale
The current validation script only checks basic syntax and structure, missing critical pattern violations that lead to documentation drift. Comprehensive validation will provide actionable feedback to maintain system integrity and guide agents toward correct documentation practices.

## Issues Addressed
1. **Diátaxis Compliance**: Files in correct buckets, appropriate content types
2. **Domain Consistency**: Proper domain assignment and validation
3. **Authority Order**: No inappropriate cross-authority references
4. **Work Requirements**: Status fields, naming patterns for work docs
5. **Archive Completeness**: Required metadata for archived files
6. **Decision Quality**: Semantic validation of decision criteria
7. **Registry Coverage**: Complete bidirectional traceability

## Implementation
- **Enhanced Validation**: Add semantic checks beyond syntax validation
- **Actionable Feedback**: Provide specific commands to fix violations
- **Progressive Levels**: Syntax → Structure → Semantics validation
- **Pattern Research**: Comprehensive audit of all documentation constraints

## Systemic Benefits
- **Self-Correction**: Agents receive clear guidance on documentation compliance
- **Pattern Preservation**: Automated enforcement of established conventions
- **Quality Assurance**: Proactive identification of structural issues
- **Learning Acceleration**: Faster agent adaptation to documentation standards