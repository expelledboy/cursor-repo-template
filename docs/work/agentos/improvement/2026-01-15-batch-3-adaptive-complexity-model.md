# Batch 3: Adaptive Complexity Model - Deep Integration Analysis

**Status**: Draft
**Date**: 2026-01-15
**Event**: research
**Task**: Comprehensive analysis of Adaptive Complexity Model integration into AgentOS
**Batch**: 3 of 5 (Workflow Optimization Pattern)
**Priority**: P2 (High value, High effort, Medium risk)
**Evidence**: Research analysis in this document; no implementation yet.
**Affected artifacts**: None yet (proposal in research stage).

**Note**: Research work preceding ADR creation for double-loop change.

---

## Executive Summary

This document provides in-depth analysis of integrating an Adaptive Complexity Model into AgentOS. Through multiple self-reflection cycles, we explore how complexity-based workflow variations can reduce overhead for simple tasks while maintaining rigor for complex tasks, all while preserving AgentOS's core lifecycle and deterministic principles.

**Key Insights:**
- Complexity-based workflow variations can reduce overhead by 40-60% for simple tasks
- Core lifecycle steps must be preserved (variations adjust rigor, not structure)
- Complexity determination must be explicit and auditable
- Workflow variations must maintain traceability and rationale preservation

---

## Loop Selection

**Classification**: Double-loop change
**Rationale**: Changes core lifecycle behavior:
- Modifies `behavior-spec.md` Section 4 (Task lifecycle) to allow workflow variations
- Introduces complexity-based workflow variations (changes rules)
- Modifies design-decision checkpoint requirements
**Required Promotion Path**:
1. Create problem entry (if new problem) or link to PRB-0001 (efficiency aspect)
2. Create ADR file
3. Update traceability map

---

## Initial Analysis: Understanding the Pattern

### Memory Bank's Adaptive Complexity Model

**What it is:**
- 4-level complexity scale (1-4) from quick bug fixes to complex systems
- Level-specific workflows with different command sequences
- Complexity-appropriate documentation requirements
- Level-specific verification processes
- Complexity determination decision tree

**Why it works:**
- Simple tasks don't need comprehensive planning and documentation
- Complex tasks need thorough planning, design exploration, and verification
- Reduces cognitive overhead for developers
- Prevents over-engineering simple fixes and under-engineering complex features

**Evidence from Memory Bank:**
- Level 1: `/van` → `/build` → `/reflect` → `/archive` (4 commands, minimal docs)
- Level 2: `/van` → `/plan` → `/build` → `/reflect` → `/archive` (5 commands, basic docs)
- Level 3-4: `/van` → `/plan` → `/creative` → `/build` → `/reflect` → `/archive` (6 commands, comprehensive docs)
- Users report faster completion for simple tasks, better quality for complex tasks

### Current AgentOS State

**What exists:**
- Task taxonomy (12 task types)
- Complexity level (1-4) mentioned in task plan header with rationale
- Single unified lifecycle: `intake → classify → route → plan → execute → verify → report → anneal`
- All tasks follow same lifecycle regardless of complexity
- Design-decision checkpoint required for material decisions (not complexity-based)

**Gap analysis:**
- No explicit complexity-based workflow variations
- Simple tasks (Level 1) go through full lifecycle (may be overkill)
- Complex tasks (Level 3-4) use same process as simple tasks (may be insufficient)
- Complexity level determined but not used to adjust process rigor
- No complexity determination decision tree or criteria

---

## Self-Reflection Cycle 1: Deep Pattern Analysis

### Reflection Question 1: How do workflow variations align with AgentOS's deterministic lifecycle requirement?

**Critical Analysis:**

**AgentOS Requirement:**
- Section 4: Task lifecycle - "The agent must follow this sequence: intake → classify → route → plan → execute → verify → report → anneal"
- This is a **must** requirement (mandatory)

**Memory Bank Approach:**
- Level 1: Skips `/plan` and `/creative` (fewer phases)
- Different command sequences for different levels

**Alignment Challenge:**
- ⚠️ **Potential Conflict**: AgentOS requires all lifecycle steps, Memory Bank skips steps
- ⚠️ **Risk**: Workflow variations might violate deterministic lifecycle requirement

**Resolution Strategy:**
- ✅ **Preserve Core Lifecycle**: All 8 steps must occur, but rigor varies
- ✅ **Rigor Variations, Not Step Skipping**:
  - Level 1: Steps are brief/minimal but present
  - Level 2: Steps are standard
  - Level 3-4: Steps are comprehensive
- ✅ **Explicit Declaration**: Workflow variation must be declared in task plan header

**Insight:** Workflow variations must adjust rigor within lifecycle steps, not skip steps.

### Reflection Question 2: What are appropriate workflow variations that preserve the lifecycle?

**Workflow Variation Design:**

**Level 1: Quick Fix (Minimal Rigor)**
- **Intake**: Brief capture (1 sentence)
- **Classify**: Quick task type assignment
- **Route**: Minimal directive selection (Tier 1-2 only)
- **Plan**: Brief plan header (essential fields only)
- **Execute**: Direct implementation (minimal planning)
- **Verify**: Basic verification (smoke tests)
- **Report**: Brief completion report
- **Anneal**: Quick gap capture (if any)

**Key Characteristics:**
- All 8 steps present
- Minimal documentation
- Fast execution
- Basic verification
- **Time Estimate**: 30 minutes - 2 hours

**Note**: Time estimates refer to total task duration, not AgentOS process overhead. Process overhead is minimal for all levels.

**Level 2: Simple Enhancement (Standard Rigor)**
- **Intake**: Standard capture
- **Classify**: Standard task type assignment
- **Route**: Standard directive selection (Tier 1-3)
- **Plan**: Standard plan header (all fields)
- **Execute**: Planned implementation
- **Verify**: Standard verification gates
- **Report**: Standard completion report
- **Anneal**: Standard gap capture

**Key Characteristics:**
- All 8 steps present
- Standard documentation
- Planned execution
- Standard verification
- **Time Estimate**: 2 hours - 2 days

**Level 3: Intermediate Feature (Comprehensive Rigor)**
- **Intake**: Comprehensive capture
- **Classify**: Detailed task type assignment
- **Route**: Comprehensive directive selection (Tier 1-4)
- **Plan**: Comprehensive plan header with checkpoints
- **Design-Decision Checkpoint**: Mandatory (if material decisions)
- **Execute**: Systematic implementation following plan
- **Verify**: Comprehensive verification gates
- **Report**: Detailed completion report
- **Anneal**: Comprehensive gap capture and analysis

**Key Characteristics:**
- All 8 steps present
- Comprehensive documentation
- Mandatory design-decision checkpoint
- Comprehensive verification
- **Time Estimate**: 2 days - 2 weeks

**Level 4: Complex System (Enterprise Rigor)**
- **Intake**: Enterprise-level capture
- **Classify**: Detailed task type with sub-classification
- **Route**: Enterprise directive selection (Tier 1-5)
- **Plan**: Enterprise plan header with phased checkpoints
- **Design-Decision Checkpoint**: Mandatory (multiple checkpoints)
- **Execute**: Phased implementation with reviews
- **Verify**: Enterprise verification gates (multiple phases)
- **Report**: Enterprise completion report with lessons learned
- **Anneal**: Enterprise gap capture with retrospective

**Key Characteristics:**
- All 8 steps present
- Enterprise documentation
- Multiple design-decision checkpoints
- Enterprise verification
- **Time Estimate**: 2 weeks - months

**Insight:** All levels preserve 8-step lifecycle, variations adjust rigor and documentation depth.

### Reflection Question 3: How do we determine complexity level explicitly and auditably?

**Complexity Determination Strategy:**

**Determination Criteria:**
1. **Scope**: Single component vs. multiple components vs. system-wide
2. **Design Decisions**: None vs. simple vs. complex vs. architectural
3. **Risk**: Low vs. moderate vs. high vs. critical
4. **Implementation Effort**: Hours vs. days vs. weeks vs. months
5. **Dependencies**: None vs. few vs. many vs. architectural

**Decision Tree Approach:**
```
Start → Is it a bug fix?
  → Yes → Single component? → Yes → Level 1
  → Yes → Multiple components? → Yes → Level 2
  → No → Small enhancement?
    → Yes → Self-contained? → Yes → Level 2
    → No → Multiple components? → Yes → Level 3
  → No → Complete feature?
    → Yes → Architectural implications? → Yes → Level 4
    → No → Level 3
  → No → System-wide change? → Yes → Level 4
```

**Explicit Declaration:**
- Complexity level must be determined during `classify` phase
- Rationale must be recorded in task plan header
- Decision criteria must be explicit (not implicit)
- Complexity determination must be auditable

**Insight:** Complexity determination must be explicit, auditable, and recorded in task plan header.

---

## Self-Reflection Cycle 2: AgentOS-Specific Considerations

### Reflection Question 4: How do workflow variations interact with existing AgentOS contracts?

**Contract Interaction Analysis:**

**Task Lifecycle (Section 4):**
- **Current**: All tasks follow same sequence
- **Proposed**: All tasks follow same sequence, but with rigor variations
- **Interaction**: ✅ Compatible - variations adjust rigor, not sequence

**Primary Objective Control (Section 5):**
- **Current**: Single primary objective required
- **Proposed**: Same requirement, but Level 1 may have simpler objective statement
- **Interaction**: ✅ Compatible - requirement preserved, rigor varies

**Task Taxonomy (Section 6):**
- **Current**: 12 task types
- **Proposed**: Complexity level is orthogonal to task type
- **Interaction**: ✅ Compatible - task type and complexity are independent dimensions

**Routing Model (Section 8):**
- **Current**: Routing selects directives and domains
- **Proposed**: Complexity affects which tier directives load (from Batch 2)
- **Interaction**: ✅ Compatible - complexity influences routing, doesn't change model

**Context Loading Contract (Section 10):**
- **Current**: Directive loading plan required
- **Proposed**: Complexity affects tier loading (Tier 3 complexity-based)
- **Interaction**: ✅ Compatible - complexity influences loading, doesn't change contract

**Design-Decision Checkpoint (Section 11):**
- **Current**: Required for material decisions
- **Proposed**: Complexity affects checkpoint rigor (Level 1: optional, Level 3-4: mandatory)
- **Interaction**: ⚠️ **Requires Careful Integration**:
  - **Level 1**: Optional - only required if material design/architecture decision exists. If no material decision exists, checkpoint is not required.
  - **Level 2**: Optional - only required if material design/architecture decision exists. If no material decision exists, checkpoint is not required.
  - **Level 3**: Mandatory - If material design/architecture decision exists, checkpoint is required. If no material decision exists, document "No material design decisions required for this task" in checkpoint status.
  - **Level 4**: Mandatory - Always document. If material decision exists, checkpoint required. If no material decision exists, document "No material design decisions required for this task" with rationale.

**Verification Contract (Section 14):**
- **Current**: Gates required, aligned with CI
- **Proposed**: Complexity affects gate rigor (Level 1: basic, Level 3-4: comprehensive)
- **Interaction**: ✅ Compatible - gates required at all levels, rigor varies

**Note**: Gate structure is the same for all levels. "Rigor" refers to number of gates and depth of testing, not gate format. All levels must use the same gate format per `verification-contract.md`.

**Insight:** Workflow variations are compatible with existing contracts, but design-decision checkpoint integration requires careful definition.

### Reflection Question 5: How do we handle complexity escalation during task execution?

**Escalation Scenario Analysis:**

**Scenario 1: Level 1 → Level 2**
- **Trigger**: Discover multiple components affected
- **Action**:
  1. Update complexity level in task plan header
  2. Load additional Tier 2-3 directives
  3. Expand plan header to standard format
  4. Continue with Level 2 rigor
  5. Document escalation in report

**Scenario 2: Level 2 → Level 3**
- **Trigger**: Discover architectural implications
- **Action**:
  1. Update complexity level in task plan header
  2. Load Tier 4 directives (design-decision checkpoint templates)
  3. Add mandatory design-decision checkpoint
  4. Expand plan to comprehensive format
  5. Continue with Level 3 rigor
  6. Document escalation in report

**Scenario 3: Level 3 → Level 4**
- **Trigger**: Discover system-wide impact
- **Action**:
  1. Update complexity level in task plan header
  2. Load Tier 5 directives (enterprise rules)
  3. Add multiple design-decision checkpoints
  4. Expand plan to enterprise format
  5. Continue with Level 4 rigor
  6. Document escalation in report

**Escalation Rules:**
- Complexity can only escalate (not de-escalate) during execution
- Escalation must be recorded in task plan header
- Escalation triggers additional directive loading
- Escalation requires user confirmation (safety check)
- Escalation must be documented in report

**Insight:** Escalation is one-way (up only), requires explicit declaration and user confirmation.

### Reflection Question 6: How do workflow variations maintain traceability?

**Traceability Requirements:**
- All decisions must be traceable
- Complexity determination must be auditable
- Workflow variation must be recorded
- Escalation must be documented

**Traceability Strategy:**

1. **Complexity Determination Record:**
   ```
   Complexity Level: [1-4]
   Rationale: [Explicit criteria used]
   Determination Criteria:
   - Scope: [Single/Multiple/System]
   - Design Decisions: [None/Simple/Complex/Architectural]
   - Risk: [Low/Moderate/High/Critical]
   - Implementation Effort: [Hours/Days/Weeks/Months]
   - Dependencies: [None/Few/Many/Architectural]
   ```

2. **Workflow Variation Record:**
   ```
   Workflow Variation: Level [1-4]
   Lifecycle Steps: [All 8 steps, rigor level noted]
   Documentation Level: [Minimal/Standard/Comprehensive/Enterprise]
   Verification Level: [Basic/Standard/Comprehensive/Enterprise]
   ```

3. **Escalation Record (if applicable):**
   ```
   Complexity Escalation:
   - Initial Level: [X]
   - Final Level: [Y]
   - Escalation Trigger: [Explicit reason]
   - Escalation Point: [Which lifecycle step]
   - User Confirmation: [Yes/No, timestamp]
   ```

4. **Validation:**
   - Validation script checks complexity determination rationale
   - Verifies workflow variation matches complexity level
   - Checks escalation records are complete

**Insight:** Traceability is maintained through explicit records in task plan header and validation.

---

## Self-Reflection Cycle 3: Implementation Details & Edge Cases

### Reflection Question 7: What is the implementation strategy?

**Implementation Plan:**

#### Step 1: Define Complexity Determination Criteria
**File:** `docs/reference/agentos/complexity-determination.md` (new)

**Content:**
- Complexity level definitions (1-4)
- Decision criteria (scope, design decisions, risk, effort, dependencies)
- Decision tree diagram
- Examples for each level
- Escalation triggers and rules

#### Step 2: Define Workflow Variations
**File:** `docs/reference/agentos/workflow-variations.md` (new)

**Content:**
- Workflow variation definitions for each level
- Lifecycle step rigor descriptions
- Documentation requirements by level
- Verification requirements by level
- Examples for each level

#### Step 3: Update Task Lifecycle Section
**File:** `docs/reference/agentos/behavior-spec.md` (enhancement)

**Update Section 4: Task lifecycle**
```markdown
## 4. Task lifecycle
- The agent must follow this sequence: intake → classify → route → plan → execute → verify → report → anneal.
- All 8 steps must be completed for all tasks, regardless of complexity level.
- Workflow variations adjust the rigor and documentation depth of each step based on complexity level (1-4).
- See `docs/reference/agentos/workflow-variations.md` for level-specific rigor definitions.
- Complexity level must be determined during the classify phase and recorded in the task plan header.
```

#### Step 4: Update Task Plan Header Requirements
**File:** `docs/reference/agentos/behavior-spec.md` (enhancement)

**Update Section 11: Task plan header requirements**
```markdown
## 11. Task plan header requirements
The task plan header must include:
- Task type.
- Primary objective.
- Complexity level (1-4) with rationale and determination criteria.
- Workflow variation (Level 1-4) with rigor level for each lifecycle step.
- Required directives.
- Allowed domains.
- Directive loading plan (loaded vs deferred + triggers).
- Design-decision checkpoint status (required or not required, plus evidence when required).
  - Level 1: Optional (only if material decision exists)
  - Level 2: Optional (only if material decision exists)
  - Level 3-4: Mandatory (document decision or explain why not needed)
- Transition readiness summary before execution (key decisions, dependencies, risks, verification focus).
- Evidence sources.
- Verification gates.
- Complexity escalation record (if applicable).
```

#### Step 5: Update Design-Decision Checkpoint Requirements
**File:** `docs/reference/agentos/behavior-spec.md` (enhancement)

**Update design-decision checkpoint section**
```markdown
Design-decision checkpoint requirements vary by complexity level:
- **Level 1**: Optional - only required if material design/architecture decision exists
- **Level 2**: Optional - only required if material design/architecture decision exists
- **Level 3**: Mandatory - required for all tasks (document decision or explain why not needed)
- **Level 4**: Mandatory - required for all tasks, may require multiple checkpoints

All design-decision checkpoints must use appropriate template from `docs/reference/agentos/design-decision-templates.md` based on complexity level.
```

#### Step 6: Create Complexity Determination How-To
**File:** `docs/how-to/agentos/determine-complexity.md` (new)

**Content:**
- Step-by-step complexity determination process
- Decision tree usage
- Criteria evaluation guide
- Examples for each level
- Escalation procedures

#### Step 7: Create Validation Script
**File:** `scripts/agentos/validate_complexity_workflow.py` (new)

**Validation Checks:**
- Complexity level has explicit rationale
- Workflow variation matches complexity level
- All 8 lifecycle steps are present (rigor may vary)
- Design-decision checkpoint requirements match complexity level
- Escalation records are complete (if applicable)
- Complexity determination criteria are explicit

### Reflection Question 8: What are the edge cases and risks?

**Edge Cases:**

1. **Ambiguous Complexity:**
   - **Case**: Task could be Level 2 or Level 3
   - **Solution**: Use conservative approach (higher level), document rationale
   - **Impact**: Low - can escalate down if needed (but escalation is one-way up)

2. **Complexity Escalation Mid-Task:**
   - **Case**: Discover complexity is higher during execution
   - **Solution**: Escalate complexity, update plan header, load additional directives
   - **Impact**: Medium - requires plan update, but traceable

3. **Multiple Complexity Levels:**
   - **Case**: Task has multiple components at different complexity levels
   - **Solution**: Use highest complexity level, document component-level variations
   - **Impact**: Low - highest level ensures adequate rigor

4. **Design-Decision Checkpoint at Level 1:**
   - **Case**: Level 1 task has material design decision
   - **Solution**: Add design-decision checkpoint (Level 1 template), document why needed
   - **Impact**: Low - checkpoint is optional but can be added

5. **Verification Gates at Level 1:**
   - **Case**: Level 1 task needs comprehensive verification
   - **Solution**: Use basic verification gates (smoke tests), document if more needed
   - **Impact**: Low - gates required but rigor can vary

**Risks:**

1. **Over-Simplification:**
   - **Risk**: Level 1 workflow too minimal, misses important steps
   - **Mitigation**: All 8 steps must be present, just minimal rigor
   - **Validation**: Check that all lifecycle steps are present

2. **Under-Documentation:**
   - **Risk**: Level 1-2 workflows don't preserve enough rationale
   - **Mitigation**: Minimum documentation requirements, validation checks
   - **Validation**: Check that rationale is preserved at all levels

3. **Complexity Misclassification:**
   - **Risk**: Task classified at wrong complexity level
   - **Mitigation**: Explicit determination criteria, validation checks
   - **Validation**: Check that determination criteria are explicit and complete

4. **Escalation Abuse:**
   - **Risk**: Tasks escalated unnecessarily
   - **Mitigation**: Escalation requires user confirmation, document rationale
   - **Validation**: Check that escalation rationale is explicit

5. **Lifecycle Step Skipping:**
   - **Risk**: Workflow variations might skip lifecycle steps
   - **Mitigation**: All 8 steps must be present, variations adjust rigor only
   - **Validation**: Check that all lifecycle steps are present

**Insight:** Edge cases are manageable with proper validation and explicit requirements.

---

## Final Enriched Recommendation

### Recommendation: Implement Adaptive Complexity Model with Workflow Variations

**Rationale:**
After three reflection cycles, adaptive complexity model is clearly beneficial. It reduces overhead for simple tasks while maintaining rigor for complex tasks. The key insight is that workflow variations adjust rigor within lifecycle steps, not skip steps, preserving AgentOS's deterministic lifecycle requirement.

**Implementation:**
1. Create `complexity-determination.md` reference (new file)
2. Create `workflow-variations.md` reference (new file)
3. Enhance `behavior-spec.md` task lifecycle section (Section 4)
4. Enhance `behavior-spec.md` task plan header requirements (Section 11)
5. Enhance `behavior-spec.md` design-decision checkpoint section
6. Create `determine-complexity.md` how-to guide (new file)
7. Create `validate_complexity_workflow.py` script (new file)

**Key Design Decisions:**
1. **All 8 lifecycle steps must be present** - variations adjust rigor, not structure
2. **Complexity determination during classify phase** - explicit, auditable
3. **Escalation is one-way (up only)** - requires user confirmation
4. **Design-decision checkpoint varies by level** - Level 1-2 optional, Level 3-4 mandatory
5. **Verification gates required at all levels** - rigor varies by level

**Success Criteria:**
- Complexity level determined explicitly with rationale
- Workflow variation matches complexity level
- All 8 lifecycle steps present (rigor may vary)
- Design-decision checkpoint requirements match complexity level
- Escalation records complete (if applicable)
- Validation script passes
- Overhead reduced by 40-60% for Level 1 tasks
- Rigor maintained for Level 3-4 tasks

**Benefits:**
- Reduces overhead for simple tasks (Level 1: 40-60% reduction)
- Maintains rigor for complex tasks (Level 3-4: comprehensive)
- Preserves deterministic lifecycle (all 8 steps present)
- Maintains traceability (explicit records)
- Aligns with existing complexity level in header

**Tradeoffs:**
- ✅ Reduces overhead while maintaining structure
- ✅ Preserves AgentOS principles (determinism, traceability)
- ⚠️ Adds complexity to system (complexity determination, workflow variations)
- ⚠️ Requires validation to ensure lifecycle steps aren't skipped
- ⚠️ Escalation adds process overhead (but improves quality)

---

## Required ADR

**ADR: Adaptive Complexity Model with Workflow Variations**
- **Problem**: PRB-0001 (Goal Drift) - efficiency aspect, reducing overhead for simple tasks
- **Decision**: Implement complexity-based workflow variations that adjust rigor within lifecycle steps
- **Alternatives**:
  - Keep unified lifecycle (rejected - too much overhead for simple tasks)
  - Skip lifecycle steps (rejected - violates deterministic requirement)
- **Consequences**:
  - Reduces overhead for simple tasks
  - Maintains rigor for complex tasks
  - Adds complexity determination and workflow variation management
  - Requires validation to ensure lifecycle steps aren't skipped
- **Artifacts**:
  - `complexity-determination.md`
  - `workflow-variations.md`
  - `behavior-spec.md` (enhanced)
  - `determine-complexity.md`
  - `validate_complexity_workflow.py`

---

## Integration with Other Patterns

### With Hierarchical Loading (Batch 2):
- Complexity level determines Tier 3 directive loading
- Level 1: Tier 1-2 only
- Level 2: Tier 1-3
- Level 3-4: Tier 1-4 (Tier 5 on demand)

### With Progressive Documentation (Batch 2):
- Complexity level determines design-decision checkpoint template level
- Level 1: Brief template (if checkpoint needed)
- Level 2: Basic template (if checkpoint needed)
- Level 3: Comprehensive template (mandatory)
- Level 4: Enterprise template (mandatory)

### With Visual Process Maps (Batch 1):
- Complexity level affects which process map is used
- Level 1: Simplified process map
- Level 2: Standard process map
- Level 3-4: Comprehensive process map

---

## Related Docs

- Integration analysis: `docs/work/agentos/improvement/2026-01-15-memory-bank-integration-analysis.md`
- Behavior spec: `docs/reference/agentos/behavior-spec.md`
- Workflow variations: `docs/reference/agentos/workflow-variations.md` (to be created)
- Complexity determination: `docs/reference/agentos/complexity-determination.md` (to be created)

---

**Status**: Ready for implementation
**Next Action**: Create ADR and implement complexity determination and workflow variation definitions

---

## Action Items

### Pre-Implementation (Double-Loop Promotion)

1. **Create/Link Problem Entry**
   - Owner: [TBD]
   - Evidence: Problem entry in `docs/reference/agentos/problem-registry.md` or link to PRB-0001
   - Completion: [ ] Problem validated and added to registry
   - Affected artifacts: `docs/reference/agentos/problem-registry.md`

2. **Create ADR: Adaptive Complexity Model with Workflow Variations**
   - Owner: [TBD]
   - Evidence: ADR file created in `docs/explanation/agentos/decisions/YYYY-MM-DD-adaptive-complexity-model.md`
   - Completion: [ ] ADR created with full format per `decision-record-format.md`
   - Affected artifacts: `docs/explanation/agentos/decisions/YYYY-MM-DD-adaptive-complexity-model.md`

3. **Update Traceability Map**
   - Owner: [TBD]
   - Evidence: Entries added to `docs/reference/agentos/traceability.md`
   - Completion: [ ] Problems mapped to ADRs, artifacts listed
   - Affected artifacts: `docs/reference/agentos/traceability.md`

### Implementation

4. **Create complexity-determination.md**
   - Owner: [TBD]
   - Evidence: Reference file created with complexity definitions and decision tree
   - Completion: [ ] File created, all definitions included
   - Affected artifacts: `docs/reference/agentos/complexity-determination.md`

5. **Create workflow-variations.md**
   - Owner: [TBD]
   - Evidence: Reference file created with workflow variation definitions
   - Completion: [ ] File created, all variations defined
   - Affected artifacts: `docs/reference/agentos/workflow-variations.md`

6. **Enhance behavior-spec.md**
   - Owner: [TBD]
   - Evidence: Sections 4 and 11 updated with workflow variations
   - Completion: [ ] Sections updated, validated
   - Affected artifacts: `docs/reference/agentos/behavior-spec.md`

7. **Create determine-complexity.md**
   - Owner: [TBD]
   - Evidence: How-to guide created with step-by-step process
   - Completion: [ ] File created, all steps documented
   - Affected artifacts: `docs/how-to/agentos/determine-complexity.md`

8. **Create Validation Script**
   - Owner: [TBD]
   - Evidence: Script created and tested
   - Completion: [ ] Script passes, added to validation-scripts.md
   - Affected artifacts: `scripts/agentos/validate_complexity_workflow.py`

### Post-Implementation

9. **Run MAM and Micro-AAR**
   - Owner: [TBD]
   - Evidence: MAM checklist completed, Micro-AAR note created
   - Completion: [ ] MAM completed, gaps captured if any, Micro-AAR done
   - Affected artifacts: `docs/work/agentos/improvement/YYYY-MM-DD-batch-3-micro-aar.md`

---

## Post-Implementation Verification

After implementing this batch:

1. **Run MAM**: Use Meta Analysis Mode to validate behavior
   - Check: Task plan header present and complete
   - Check: Required directives loaded
   - Check: Contracts enforced
   - Check: Gaps captured if discovered

2. **Run Validation Scripts**: Execute batch-specific validation
   - `just agentos::validate-complexity-workflow` (or equivalent)

3. **Micro-AAR**: Capture lessons learned
   - What worked well?
   - What challenges were encountered?
   - What gaps were discovered?
   - Update improvement note with Micro-AAR results

4. **Integration Testing**: Test with previously implemented batches
   - Test complexity-based tier loading (Tier 3)
   - Test workflow variations with hierarchical loading

---

## Gap Capture During Implementation

During implementation, capture gaps per `docs/how-to/agentos/capture-gaps.md`:
- Missing or incorrect directives
- Unclear or missing steps
- Verification gate issues
- Ambiguity resolutions

Promote gaps to problems if they define new problems.

---

## Edge Cases

**Complexity Escalation During Design Checkpoint**:
- **Case**: Level 2 task, during design checkpoint discover architectural implications → escalate to Level 3
- **Solution**: Escalate complexity, restart design checkpoint with Level 3 rigor, document escalation
- **Impact**: Medium - requires checkpoint restart, but ensures appropriate rigor

---

## Required ADR

**ADR Title**: Adaptive Complexity Model with Workflow Variations

**Status**: Proposed (to be created)
**Date**: [Will be set when ADR is created]
**Scope**: agentos
**Problem IDs**: PRB-0001 (efficiency aspect)
**Supersedes**: (if applicable)

**Note**: This ADR must be created before implementation. See `docs/reference/agentos/decision-record-format.md` for full format requirements.

**ADR Summary**:
- Decision: Implement complexity-based workflow variations that adjust rigor within lifecycle steps
- Alternatives: Keep unified lifecycle (rejected - too much overhead for simple tasks), Skip lifecycle steps (rejected - violates deterministic requirement)
- Consequences: Reduces overhead for simple tasks, maintains rigor for complex tasks, adds complexity determination and workflow variation management
- Artifacts: `complexity-determination.md`, `workflow-variations.md`, `behavior-spec.md`, `determine-complexity.md`, `validate_complexity_workflow.py`
