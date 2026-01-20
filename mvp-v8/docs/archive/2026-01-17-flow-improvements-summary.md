---
title: "Decision Flow Improvements Summary"
created_date: 2026-01-17
purpose: "Summary of proposed improvements to restructuring flow and execution instructions"
domain: docs
type: proposal
status: superseded
superseded_by: docs/how-to/docs/restructuring-agent.md
superseded_date: 2026-01-18
superseded_reason: Summary of improvements implemented in v2
original_path: docs/work/proposals/2026-01-17-flow-improvements-summary.md
related:
  - docs/work/analysis/2026-01-17-refine-process-review.md
  - docs/work/proposals/2026-01-17-improved-restructuring-flow-v2.yaml
  - docs/work/proposals/2026-01-17-enhanced-decision-flow-execution.md
  - docs/explanation/decisions/2026-01-16-restructuring-process-design.md
---

## Overview

Based on the process review analysis, this document summarizes proposed improvements to the restructuring decision flow specification and execution instructions.

## Key Changes to Flow Specification

### 1. **Baseline Metrics Capture** (New Invariant)

**Added to `runtime.invariants`**:
```yaml
metrics:
  rule: "Baseline metrics MUST be captured at inventory-assessment and final metrics at restructuring-completion."
```

**Impact**: Ensures quantitative measurement of restructuring effectiveness.

### 2. **New Steps Added**

#### `validation-error-analysis` (After `batch-context-loading`)
- Runs validation before semantic analysis
- Categorizes errors by severity (critical/warning/info)
- Includes validation errors as restructuring opportunities
- **Addresses**: Issue #2 (Validation Errors Ignored)

#### `prioritize-opportunities` (After `identify-opportunities`)
- Scores opportunities by impact, risk, effort, value
- Groups by category (structural/content/traceability/cross-refs/organization)
- Sorts by priority score
- **Addresses**: Issue #6 (No Opportunity Prioritization)

#### `bidirectional-link-verification` (After `generate-suggestions`)
- Verifies `@directive` exists before adding `implementations:` field
- Auto-adds `@directive` if safe, flags for approval if risky
- Runs registry validation
- **Addresses**: Issue #3 (Bidirectional Link Verification Missing)

#### `incremental-validation` (Replaces direct `validation-phase`)
- Applies changes one at a time
- Validates after each change
- Creates checkpoints on success, rollbacks on failure
- **Addresses**: Issue #8 (No Resumability Granularity)

#### `update-batch-metrics` (After `validation-result-routing`)
- Tracks error reduction per batch
- Updates completeness metrics
- Stores in `.docs-metrics.yaml`
- **Addresses**: Issue #10 (No Progress Metrics)

### 3. **Enhanced Existing Steps**

#### `inventory-assessment` → `analyze_documentation_inventory_capture_baseline_metrics`
- Captures baseline metrics (validation errors, cross-ref completeness, traceability, section completeness)
- Stores in `.docs-metrics.yaml`
- **Addresses**: Issue #10 (No Progress Metrics)

#### `semantic-comprehension` → `analyze_content_semantics_quality_and_relationships`
- Adds content duplication detection
- Adds content gap analysis
- Adds cross-reference integrity checking
- Adds implementation traceability analysis
- Adds content quality assessment
- **Addresses**: Issue #1 (Shallow Semantic Analysis), Issue #7 (Missing Content Quality Analysis)

#### `impact-assessment` → `evaluate_changes_link_content_and_downstream_impact`
- Adds downstream effects analysis
- Adds registry validation
- Adds content consistency checking
- Adds risk assessment
- **Addresses**: Issue #5 (Incomplete Impact Assessment)

#### `restructuring-completion` → `generate_comprehensive_restructuring_summary_with_metrics`
- Calculates baseline vs final metrics
- Reports deltas (improvement)
- Includes processing efficiency metrics
- **Addresses**: Issue #10 (No Progress Metrics)

### 4. **Enhanced User Approval**

**Added `runtime.user_approval_criteria`**:
```yaml
user_approval_criteria:
  always_require:
    - ">5 changes per batch"
    - "structural changes (section additions/deletions)"
    - "cross-reference modifications affecting >3 files"
    - "implementation field additions without @directive verification"
  auto_apply:
    - "single-file, low-risk frontmatter additions (<3 changes)"
    - "broken link path corrections (file exists, wrong path)"
```

**Enhanced `user-approval-gate` condition**:
- Uses explicit criteria from runtime config
- **Addresses**: Issue #4 (No User Approval Gate Triggered)

**New approval options**:
- `approve-high-priority-only` - Apply only high-priority changes
- **Addresses**: Issue #6 (No Opportunity Prioritization)

### 5. **Enhanced Error Handling**

**New `log-warning-continue` step**:
- Non-blocking warning handling
- Logs warnings but continues processing
- **Addresses**: Issue #11 (Missing Error Recovery)

**Enhanced `error-handling` condition**:
- New `warning` branch for non-critical issues
- **Addresses**: Issue #11 (Missing Error Recovery)

## Key Changes to Execution Instructions

### 1. **New Step Implementation Guides**

Added detailed implementation guidance for:
- `inventory-assessment` (baseline metrics capture)
- `validation-error-analysis` (error categorization)
- `semantic-comprehension` (enhanced analysis)
- `prioritize-opportunities` (scoring algorithm)
- `bidirectional-link-verification` (link verification)
- `incremental-validation` (checkpoint system)
- `update-batch-metrics` (metrics tracking)
- `restructuring-completion` (metrics reporting)

### 2. **Metrics File Schema**

Defined `docs/local/docs-metrics.yaml` structure:
- Baseline metrics (captured at start)
- Per-batch metrics (tracked during processing)
- Final metrics (captured at completion)
- Enables delta calculation and trend analysis

### 3. **Priority Scoring Algorithm**

Defined scoring formula:
```
Priority Score = (Impact × Value) / (Risk × Effort)
```

Where:
- **Impact** (1-10): Files affected, users benefited
- **Value** (1-10): Alignment with restructuring goals
- **Risk** (1-10): Likelihood of breaking something
- **Effort** (1-10): Complexity of implementation

### 4. **Bidirectional Link Verification Logic**

Defined decision tree:
- **Safe to add**: Simple files (justfile, config) → Auto-add `@directive`
- **Needs approval**: Complex files (Python scripts) → Flag for approval
- **Skip**: File doesn't exist → Remove opportunity

## Issues Addressed

| Issue | Solution | Status |
|-------|----------|--------|
| #1: Shallow Semantic Analysis | Enhanced `semantic-comprehension` with content quality analysis | ✅ Addressed |
| #2: Validation Errors Ignored | New `validation-error-analysis` step | ✅ Addressed |
| #3: Bidirectional Link Verification | New `bidirectional-link-verification` step | ✅ Addressed |
| #4: No User Approval Gate | Enhanced `user-approval-gate` with explicit criteria | ✅ Addressed |
| #5: Incomplete Impact Assessment | Enhanced `impact-assessment` with downstream analysis | ✅ Addressed |
| #6: No Opportunity Prioritization | New `prioritize-opportunities` step | ✅ Addressed |
| #7: Missing Content Quality Analysis | Enhanced `semantic-comprehension` | ✅ Addressed |
| #8: No Resumability Granularity | New `incremental-validation` with checkpoints | ✅ Addressed |
| #10: No Progress Metrics | New metrics capture and tracking | ✅ Addressed |
| #11: Missing Error Recovery | Enhanced error handling with warning branch | ✅ Addressed |

## Migration Path

### Phase 1: Add New Steps (Non-Breaking)
1. Add `validation-error-analysis` step
2. Add `prioritize-opportunities` step
3. Add `bidirectional-link-verification` step
4. Add `update-batch-metrics` step
5. Add `incremental-validation` step

### Phase 2: Enhance Existing Steps
1. Update `inventory-assessment` to capture baseline metrics
2. Enhance `semantic-comprehension` with quality analysis
3. Enhance `impact-assessment` with downstream analysis
4. Enhance `restructuring-completion` with metrics reporting

### Phase 3: Update Conditions
1. Add explicit `user_approval_required` criteria
2. Add `warning` branch to `error_severity` condition
3. Update `user_response` condition with new options

### Phase 4: Add Metrics Infrastructure
1. Create `docs/local/docs-metrics.yaml` schema
2. Implement metrics capture functions
3. Add metrics reporting to summary

## Testing Strategy

1. **Unit Tests**: Test each new step implementation independently
2. **Integration Tests**: Test flow execution with new steps
3. **Metrics Validation**: Verify metrics capture and calculation accuracy
4. **Error Recovery**: Test error handling and rollback mechanisms
5. **User Approval**: Test approval gate with various change counts and types

## Expected Improvements

- **Error Detection**: 100% of validation errors identified and categorized
- **Opportunity Detection**: 3x more opportunities found (from 3 to ~9 per batch)
- **User Control**: Approval required for >5 changes or structural modifications
- **Traceability**: 100% bidirectional link verification before adding implementations
- **Metrics**: Quantitative measurement of restructuring effectiveness
- **Resumability**: Granular checkpoints enable resume from any change
- **Quality**: Content quality analysis detects duplication and gaps

## Next Steps

1. Review and approve proposed changes
2. Implement new steps in flow specification
3. Update execution instructions with implementation details
4. Create metrics infrastructure (`docs/local/docs-metrics.yaml` handling)
5. Test enhanced flow with sample documentation set
6. Iterate based on test results
