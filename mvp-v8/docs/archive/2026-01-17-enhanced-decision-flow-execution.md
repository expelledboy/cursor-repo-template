---
title: "Enhanced Decision Flow Execution Guide"
created_date: 2026-01-17
purpose: "Implementation guidance for enhanced restructuring flow with validation, prioritization, and metrics"
domain: agentos
type: proposal
status: superseded
superseded_by: docs/how-to/docs/restructuring-agent.md
superseded_date: 2026-01-18
superseded_reason: Proposal adopted and implemented
original_path: docs/work/proposals/2026-01-17-enhanced-decision-flow-execution.md
related:
  - docs/how-to/docs/restructuring-agent.md
  - docs/how-to/agentos/decision-flow-execution.md
  - docs/work/proposals/2026-01-17-improved-restructuring-flow-v2.yaml
---

This document extends `docs/how-to/agentos/decision-flow-execution.md` with implementation guidance for the enhanced restructuring flow (v2).

## New Step Implementations

### `inventory-assessment` (Enhanced)

**Action**: `analyze_documentation_inventory_capture_baseline_metrics`

**Implementation**:
1. Run `just docs::docs-inventory` to create inventory
2. Run `just docs::validate` and capture error counts by category:
   - YAML syntax errors
   - Missing required fields
   - Invalid field values
   - Content validation failures (broken links, missing sections)
3. Calculate cross-reference completeness:
   - Total `related:` links in all docs
   - Valid links (file exists)
   - Invalid links (file missing)
   - Completeness % = (valid / total) × 100
4. Calculate implementation traceability:
   - Decisions with `implementations:` field
   - Implementation files with `@directive` annotations
   - Coverage % = (decisions with implementations / total decisions) × 100
5. Calculate required section completeness:
   - Decisions: check for "Decision" section (required)
   - Problems: check for "Impact", "Evidence" sections
   - Discoveries: check for "Key Insights", "Technical Grounding" sections
   - Completeness % per document type
6. Store metrics in `docs/local/docs-metrics.yaml`:
   ```yaml
   baseline:
     timestamp: "2026-01-17T..."
     validation_errors:
       yaml_syntax: 0
       missing_fields: 5
       invalid_values: 2
       content_failures: 45
       total: 52
     cross_references:
       total: 120
       valid: 95
       invalid: 25
       completeness_pct: 79.2
     implementation_traceability:
       decisions_with_implementations: 3
       total_decisions: 14
       coverage_pct: 21.4
     required_sections:
       decisions_complete: 12/14
       problems_complete: 4/4
       discoveries_complete: 10/10
   ```

**Progress Output**:
```
✅ [action] inventory-assessment
- **what**: inventory docs and capture baseline metrics
- **result**: 49 files found, 52 validation errors, 79.2% cross-reference completeness
- **next**: determine-scope
```

### `validation-error-analysis` (New)

**Action**: `run_validation_categorize_errors_by_severity`

**Implementation**:
1. Run `just docs::validate` for current batch files only
2. Categorize errors by severity:
   - **Critical**: Missing required sections (Decision, Impact, Evidence, Key Insights, Technical Grounding)
   - **Warning**: Missing optional sections, invalid field values
   - **Info**: Broken cross-references (file exists but wrong path - auto-fixable)
   - **Error**: Broken cross-references (file doesn't exist - needs investigation)
3. For each error, determine if it's a restructuring opportunity:
   - Missing sections → opportunity to add section
   - Broken links → opportunity to fix link or remove if target doesn't exist
   - Invalid values → opportunity to correct value
4. Include validation errors in opportunity list with category and auto-fix flag
5. Store error analysis in batch state

**Progress Output**:
```
✅ [action] validation-error-analysis
- **what**: run validation and categorize errors
- **result**: 8 critical, 3 warning, 12 info errors found; 15 auto-fixable
- **next**: semantic-comprehension
```

### `semantic-comprehension` (Enhanced)

**Action**: `analyze_content_semantics_quality_and_relationships`

**Implementation**:
1. **Content Duplication Detection**:
   - Compare content similarity between documents (>70% threshold)
   - Identify duplicate sections across documents
   - Flag consolidation opportunities

2. **Content Gap Analysis**:
   - Find references to topics/documents that don't exist
   - Identify missing cross-references (documents that should link but don't)
   - Detect incomplete content (sections mentioned but empty)

3. **Cross-Reference Integrity**:
   - Verify all `related:` links are semantically appropriate (content similarity check)
   - Identify missing bidirectional links (if A references B, should B reference A?)
   - Detect orphaned references (documents referenced but don't exist)

4. **Implementation Traceability**:
   - Find decisions that mention implementation files but lack `implementations:` field
   - Find `implementations:` fields where `@directive` is missing in code
   - Identify code files that should have `@directive` but don't

5. **Content Quality Assessment**:
   - Check section completeness (required sections present and substantive)
   - Assess terminology consistency
   - Identify outdated or superseded content

**Progress Output**:
```
✅ [action] semantic-comprehension
- **what**: analyze content semantics, quality, and relationships
- **result**: 2 duplicates found, 5 gaps identified, 3 missing cross-refs, 4 traceability issues
- **next**: identify-opportunities
```

### `prioritize-opportunities` (New)

**Action**: `score_opportunities_by_impact_risk_effort_value`

**Implementation**:
1. For each opportunity, calculate scores:
   - **Impact** (1-10): Files affected, users benefited
     - 1-3: Single file, low visibility
     - 4-6: Multiple files, moderate visibility
     - 7-10: Many files, high visibility, critical paths
   - **Value** (1-10): Alignment with restructuring goals
     - 1-3: Nice to have
     - 4-6: Quality improvement
     - 7-10: Critical for documentation integrity
   - **Risk** (1-10): Likelihood of breaking something
     - 1-3: Very safe (frontmatter additions, path corrections)
     - 4-6: Moderate (section additions, cross-reference changes)
     - 7-10: High risk (content deletion, structural changes)
   - **Effort** (1-10): Complexity of implementation
     - 1-3: Simple (single field addition)
     - 4-6: Moderate (multiple changes, validation needed)
     - 7-10: Complex (content restructuring, many files)

2. Calculate priority score: `(Impact × Value) / (Risk × Effort)`

3. Group opportunities by category:
   - **Structural**: Missing sections, broken links, frontmatter issues
   - **Content**: Duplication, gaps, quality issues
   - **Traceability**: Missing implementations, broken @directive links
   - **Cross-references**: Missing, broken, or incorrect links
   - **Organization**: Misplaced documents, better categorization

4. Sort by priority score (highest first)

5. Present grouped, prioritized list to user

**Progress Output**:
```
✅ [action] prioritize-opportunities
- **what**: score opportunities by impact/risk/effort/value
- **result**: 23 opportunities scored, top 5: fix broken links (8.5), add missing sections (7.2), ...
- **next**: generate-suggestions
```

### `bidirectional-link-verification` (New)

**Action**: `verify_bidirectional_links_for_implementation_references`

**Implementation**:
1. For each opportunity that adds `implementations:` field:
   - Check if implementation file exists
   - Check if file contains `@directive <doc-path>` annotation
   - If missing:
     - **Safe to add**: File is simple (justfile, config), no complex logic
       - Add `@directive` annotation to code file
       - Proceed with `implementations:` field addition
     - **Needs approval**: File is complex (Python script, multiple functions)
       - Flag for user approval
       - Don't add `implementations:` field until approved
     - **Skip**: File doesn't exist or can't be modified
       - Remove opportunity or flag as blocked

2. Run `just docs::validate-registry` to verify bidirectional integrity

3. Store verification results in opportunity metadata

**Progress Output**:
```
✅ [action] bidirectional-link-verification
- **what**: verify @directive annotations for implementation references
- **result**: 3/3 verified, 2 auto-added @directive, 1 flagged for approval
- **next**: impact-assessment
```

### `impact-assessment` (Enhanced)

**Action**: `evaluate_changes_link_content_and_downstream_impact`

**Implementation**:
1. **Downstream Effects Analysis**:
   - Find all documents that reference files being modified
   - Check if changes break any references
   - Verify content consistency after changes

2. **Registry Validation**:
   - Run `just docs::validate-registry` to check bidirectional links
   - Verify no broken `@directive` annotations
   - Check implementation file existence

3. **Content Consistency**:
   - Verify no orphaned sections after deletions
   - Check formatting consistency
   - Validate YAML syntax after frontmatter changes

4. **Risk Assessment**:
   - Categorize each change by risk level
   - Identify changes that require rollback capability
   - Flag changes that affect multiple files

**Progress Output**:
```
✅ [action] impact-assessment
- **what**: evaluate downstream impact and registry integrity
- **result**: 3 files affected downstream, registry valid, low risk changes
- **next**: user-approval-gate
```

### `user-approval-gate` (Enhanced)

**Condition**: `user_approval_required`

**Implementation**:
Use explicit criteria from `runtime.user_approval_criteria`:

**Always require approval if**:
- >5 changes per batch
- Structural changes (section additions/deletions)
- Cross-reference modifications affecting >3 files
- Implementation field additions without @directive verification

**Auto-apply if**:
- Single-file, low-risk frontmatter additions (<3 changes)
- Broken link path corrections (file exists, wrong path)

**Evaluation Logic**:
```python
def user_approval_required(opportunities):
    if len(opportunities) > 5:
        return True
    if any(op.is_structural_change() for op in opportunities):
        return True
    if sum(op.affected_files_count() for op in opportunities) > 3:
        return True
    if any(op.needs_directive_verification() for op in opportunities):
        return True
    return False
```

**Progress Output**:
```
🔎 [condition] user-approval-gate
- **eval**: user_approval_required
- **result**: true (6 changes, 2 structural)
- **next**: present-suggestions-for-approval
```

### `incremental-validation` (New)

**Action**: `validate_after_each_change_with_checkpoint`

**Implementation**:
1. Apply changes one at a time (not all at once)
2. After each change:
   - Run `just docs::validate` for modified file
   - Check for broken references
   - Verify YAML syntax
3. If validation passes:
   - Create checkpoint (save state)
   - Continue to next change
4. If validation fails:
   - Rollback current change
   - Log error
   - Continue with next change (don't stop entire batch)
5. After all changes applied:
   - Run full validation suite
   - Check downstream effects
   - Verify registry integrity

**Progress Output**:
```
✅ [action] incremental-validation
- **what**: validate after each change with checkpoint
- **result**: 5/5 changes applied successfully, 0 rollbacks
- **next**: validation-result-routing
```

### `update-batch-metrics` (New)

**Action**: `update_batch_metrics_error_reduction_completeness`

**Implementation**:
1. Re-run validation for batch files
2. Calculate error reduction:
   - Errors before batch processing (from baseline)
   - Errors after batch processing
   - Reduction = before - after
3. Update cross-reference completeness
4. Update implementation traceability coverage
5. Calculate content quality scores
6. Store in `docs/local/docs-metrics.yaml`:
   ```yaml
   batches:
     batch-2-decisions:
       errors_fixed: 8
       links_added: 3
       traceability_improved: 2
       content_quality_score: 0.85
   ```

**Progress Output**:
```
✅ [action] update-batch-metrics
- **what**: update batch metrics for error reduction and completeness
- **result**: 8 errors fixed, 3 links added, traceability +14%
- **next**: batch-cleanup
```

### `restructuring-completion` (Enhanced)

**Action**: `generate_comprehensive_restructuring_summary_with_metrics`

**Implementation**:
1. Load baseline metrics from `docs/local/docs-metrics.yaml`
2. Calculate final metrics (same as baseline)
3. Compute deltas:
   - Error reduction: baseline.total - final.total
   - Cross-reference improvement: final.completeness_pct - baseline.completeness_pct
   - Traceability improvement: final.coverage_pct - baseline.coverage_pct
   - Section completeness improvement
4. Calculate processing efficiency:
   - Time per file
   - Opportunities per batch
   - Changes per opportunity
5. Generate summary report:
   ```
   ## Restructuring Summary

   **Files Processed**: 49 across 3 batches
   **Changes Applied**: 23
   **Opportunities Identified**: 28

   ### Metrics Improvement
   - Validation errors: 52 → 18 (65% reduction)
   - Cross-reference completeness: 79.2% → 94.5% (+15.3%)
   - Implementation traceability: 21.4% → 42.9% (+21.5%)
   - Required sections: 85% → 98% (+13%)

   ### Processing Efficiency
   - Time per file: 2.3s
   - Opportunities per batch: 9.3
   - Success rate: 100% (0 rollbacks)
   ```

**Progress Output**:
```
✅ [action] restructuring-completion
- **what**: generate comprehensive summary with metrics
- **result**: 65% error reduction, +15% cross-ref completeness, +22% traceability
- **next**: final-cleanup
```

## Condition Implementations

### `user_approval_required`

**Evaluation**:
- Count total opportunities
- Check for structural changes
- Count affected files
- Check for @directive verification needs
- Apply criteria from `runtime.user_approval_criteria`

### `error_severity`

**Evaluation**:
- **recoverable**: Broken link path corrections, missing optional sections
- **warning**: Invalid field values, suspicious cross-references
- **critical**: Missing required sections, broken @directive links, YAML syntax errors

## Metrics File Schema

`docs/local/docs-metrics.yaml`:
```yaml
baseline:
  timestamp: "2026-01-17T..."
  validation_errors: {...}
  cross_references: {...}
  implementation_traceability: {...}
  required_sections: {...}

batches:
  batch-1-core:
    errors_fixed: 0
    links_added: 0
    traceability_improved: 0
  batch-2-decisions:
    errors_fixed: 8
    links_added: 3
    traceability_improved: 2

final:
  timestamp: "2026-01-17T..."
  validation_errors: {...}
  cross_references: {...}
  implementation_traceability: {...}
  required_sections: {...}
```

## Best Practices

1. **Always capture baseline metrics** before processing any batches
2. **Categorize validation errors** to prioritize fixes
3. **Verify bidirectional links** before adding implementation references
4. **Apply changes incrementally** with validation checkpoints
5. **Track metrics per batch** to measure progress
6. **Report deltas** in final summary (not just final values)
