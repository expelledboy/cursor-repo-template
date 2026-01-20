---
title: "Agent Restructuring Operations"
status: stable
created_date: 2026-01-18
purpose: "Operational instructions for agents performing documentation restructuring"
domain: docs
related:
  - docs/explanation/decisions/2026-01-16-restructuring-process-design.md
---

# Agent Restructuring Operations

## Your Role in Documentation Restructuring

You are the intelligent actor responsible for analyzing, deciding, and executing documentation restructuring. Tools provide deterministic infrastructure; you provide judgment and context.

## Enhanced Restructuring Process

Follow this 6-phase enhanced process to ensure quality, traceability, and semantic integrity.

### Phase 1: Analysis & Metrics

#### 1. Inventory & Baseline Metrics
- **Action**: Run `just docs-inventory`.
- **Metrics**: Capture baseline counts for validation errors, cross-reference completeness, and implementation traceability.
- **Goal**: Establish a quantifiable starting point.

#### 2. Validation Error Analysis
- **Action**: Analyze validation results (`just docs::validate`).
- **Categorization**:
  - **Critical**: Missing required sections (Decision, Impact, Evidence).
  - **Warning**: Missing optional sections, invalid values.
  - **Info**: Broken links to existing files (fixable).
- **Opportunity**: Treat error fixes as restructuring opportunities.

#### 3. Semantic Comprehension
- **Content Analysis**: Detect >70% similarity (duplication) and content gaps.
- **Integrity Check**: Verify all `related:` links are semantically relevant.
- **Traceability**: Identify decisions missing `implementations:` and code missing `@directive`.

### Phase 2: Strategy & Opportunity

#### 4. Opportunity Prioritization
- **Scoring**: Calculate Priority = (Impact × Value) / (Risk × Effort).
- **Impact**: Files affected, user visibility.
- **Value**: Alignment with restructuring goals.
- **Risk**: Likelihood of breaking changes.
- **Effort**: Implementation complexity.

#### 5. Bidirectional Verification
- **Requirement**: Before adding `implementations:` references.
- **Verification**: Check if target code file exists and has `@directive`.
- **Action**: If safe (config/scripts), add `@directive`. If complex (logic), flag for approval.

### Phase 3: Execution & Impact

#### 6. Impact Assessment
- **Downstream**: Check all docs referencing modified files.
- **Registry**: Run `just docs::validate-registry`.
- **Consistency**: Verify formatting and section orphans.

#### 7. User Approval Gate
- **Always Require Approval**:
  - >5 changes per batch.
  - Structural changes (add/delete sections).
  - Cross-reference mods >3 files.
- **Auto-Apply**: Single-file frontmatter fixes, broken link path corrections.

#### 8. Incremental Validation
- **Method**: Apply changes one at a time.
- **Check**: Validate after *each* change.
- **Recovery**: Rollback immediately on failure.

### Phase 4: Completion

#### 9. Metrics Update
- **Calculate**: Error reduction, completeness improvement, traceability gain.
- **Record**: Update batch metrics.

#### 10. Summary
- **Report**: Generate summary with clear "Before vs After" metrics.
- **Cleanup**: Run `just docs-cleanup-all` only on full success.

## Decision Frameworks

### Consolidation Criteria
- **Similarity**: >70% content overlap.
- **Authority**: One clear definitive source exists.
- **Maintenance**: Consolidation reduces update burden.

### Opportunity Scoring Reference
| Factor | Low (1-3) | High (7-10) |
|--------|-----------|-------------|
| **Impact** | Single file | Critical path, many files |
| **Risk** | Frontmatter only | Deletions, structural changes |
| **Effort** | Single field | Complex merge |

## Integration with Existing Validation

Always run existing validation:
- `just docs-health` - Overall documentation health
- `just lint` - Frontmatter validation
- `just docs::validate-registry` - Link integrity

## Success Indicators

- **Zero Critical Errors**: All required sections present.
- **Registry Integrity**: 100% valid bidirectional links.
- **Measurable Improvement**: Positive delta in error counts and completeness.
- **Traceability**: Decisions linked to implementation code.
