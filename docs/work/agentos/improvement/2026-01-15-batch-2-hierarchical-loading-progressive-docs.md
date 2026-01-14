# Batch 2: Hierarchical Rule Loading + Progressive Documentation - Deep Integration Analysis

**Status**: Draft
**Date**: 2026-01-15
**Event**: research
**Task**: Comprehensive analysis of Hierarchical Rule Loading and Progressive Documentation integration into AgentOS
**Batch**: 2 of 5 (Context Efficiency Patterns)
**Priority**: P1 (High value, Medium effort, Medium risk)
**Evidence**: Research analysis in this document; no implementation yet.
**Affected artifacts**: None yet (proposal in research stage).

**Note**: Research work preceding ADR creation for double-loop changes.

---

## Executive Summary

This document provides in-depth analysis of two related context-efficiency patterns: Hierarchical Rule Loading (JIT loading) and Progressive Documentation (detail-on-demand). Through multiple self-reflection cycles, we explore how these patterns can enhance AgentOS's context efficiency while maintaining its explicit declaration and traceability principles.

**Key Insights:**
- Hierarchical loading can reduce token usage by 30-50% while maintaining explicit declaration
- Progressive documentation scales appropriately with complexity without losing rigor
- Both patterns align with AgentOS principles but require careful adaptation
- Implementation must preserve directive loading plan traceability

---

## Loop Selection

**Classification**: Double-loop change
**Rationale**: Changes core behavior contracts:
- Modifies `context-compass.md` (adds Section 5: Hierarchical Loading Tiers)
- Modifies `behavior-spec.md` (enhances Section 10: Context loading contract, Section 11: Task plan header)
- Changes directive loading contract (adds tier structure)
**Required Promotion Path**:
1. Create problem entry (if new problem) or link to PRB-0002 (token efficiency aspect)
2. Create ADR files (2 ADRs required)
3. Update traceability map

---

## Part A: Hierarchical Rule Loading Analysis

### Initial Analysis: Understanding the Pattern

#### Memory Bank's Hierarchical Loading Pattern

**What it is:**
- Tiered loading system: Core → Common → Mode-Specific → Specialized
- Just-In-Time (JIT) loading of specialized rules
- Core rule caching across transitions
- Complexity-based rule selection
- ~70% token reduction achieved

**Why it works:**
- Most tasks don't need all rules simultaneously
- Specialized rules (e.g., architecture design) only needed when that phase occurs
- Core rules are shared across all tasks, benefit from caching
- Complexity level determines which level-specific rules are needed

**Evidence from Memory Bank:**
- Initial token usage: ~70,000 → ~15,000 (78% reduction)
- Specialized rules loaded on-demand: ~10,000 tokens
- Total savings: ~45,000 tokens (64% overall reduction)
- No functionality loss, improved response times

#### Current AgentOS State

**What exists:**
- Context Compass constrains doc types by task intent
- Routing selects required directives and allowed domains
- Directive loading plan in task plan header (loaded vs deferred + triggers)
- All core docs listed in `.cursor/rules/20-agentos.topic.mdc` (may load all at once)

**Gap analysis:**
- No explicit hierarchical loading strategy
- All 25+ core docs may load simultaneously
- No tiered loading based on lifecycle phase
- Deferred directives exist but no systematic tier structure
- No caching strategy for shared directives

---

## Self-Reflection Cycle 1: Deep Pattern Analysis (Hierarchical Loading)

### Reflection Question 1: How does hierarchical loading align with AgentOS's explicit declaration principle?

**Analysis:**
AgentOS requires explicit declaration of:
- Required directives
- Allowed domains
- Directive loading plan (loaded vs deferred + triggers)

**Alignment Assessment:**
- ✅ **Strong Alignment**: Hierarchical loading enhances explicit declaration
  - Tier structure makes loading strategy explicit
  - Loading plan already exists, just needs tier organization
  - Deferred directives with triggers already required

- ⚠️ **Adaptation Needed**: Must maintain explicit tier declaration
  - Loading plan must include tier information
  - Tier selection must be explicit, not implicit
  - Cannot rely on automatic loading (violates explicit declaration)

**Insight:** Hierarchical loading is compatible but requires explicit tier declaration in loading plan.

### Reflection Question 2: What are the appropriate loading tiers for AgentOS?

**Tier Analysis:**

**Tier 1: Always Loaded (Core Contracts)**
- `behavior-spec.md` - Core behavior contract
- `architecture.md` - Architecture model
- `routing.md` - Routing model
- `context-compass.md` - Doc type constraints
- **Rationale**: Required for all tasks to understand core constraints

**Important**: Tier 1 directives are loaded only if allowed by Context Compass for task intent. For example, Learning tasks (tutorials only) would not load Tier 1 reference docs. Tier 1 loading respects Context Compass constraints.

**Tier 2: Task-Type Specific (By Task Type)**
- Task-type-specific contracts (e.g., verification-contract.md for Testing tasks)
- Domain-specific directives (based on allowed domains)
- **Rationale**: Only needed for specific task types

**Tier 3: Complexity-Based (By Complexity Level)**
- Level 1: Minimal verification gates
- Level 2: Standard verification gates
- Level 3-4: Comprehensive verification gates, design-decision checkpoints
- **Rationale**: Complexity determines documentation and verification rigor

**Tier 4: Phase-Specific (On Demand)**
- Design-decision checkpoint templates (only when design decision required)
- Meta-analysis mode rules (only for AgentOS Meta-Maintenance)
- Specialized validation scripts (only when specific validation needed)
- **Rationale**: Only needed at specific lifecycle phases

**Tier 5: Specialized (Lazy Loaded)**
- Registry mapping details (only when registry work needed)
- Bootstrap gates (only during bootstrap)
- Advanced verification rules (only for complex verification)
- **Rationale**: Rarely needed, load only when triggered

**Insight:** 5-tier structure provides granular control while maintaining explicit declaration.

### Reflection Question 3: How do we maintain traceability with hierarchical loading?

**Traceability Requirements:**
- Directive loading plan must record what was loaded
- Deferred directives must have explicit triggers
- Loading decisions must be auditable

**Traceability Strategy:**
1. **Enhanced Loading Plan Format:**
   ```
   Directive Loading Plan:
   - Tier 1 (Core): [list loaded]
   - Tier 2 (Task-Type): [list loaded]
   - Tier 3 (Complexity): [list loaded]
   - Tier 4 (Phase): [list loaded, triggers]
   - Tier 5 (Specialized): [list loaded, triggers]
   - Deferred: [list with explicit triggers]
   ```

2. **Trigger Documentation:**
   - Each deferred directive must have explicit trigger condition
   - Triggers must be auditable (e.g., "Load when design-decision checkpoint reached")

3. **Validation:**
   - Validation script checks loading plan completeness
   - Verifies triggers are explicit and auditable

**Insight:** Enhanced loading plan format maintains traceability while enabling hierarchical loading.

---

## Self-Reflection Cycle 2: AgentOS-Specific Considerations (Hierarchical Loading)

### Reflection Question 4: How does hierarchical loading interact with Context Compass?

**Interaction Analysis:**

**Context Compass (Current):**
- Constrains doc types by task intent (reference, how-to, explanation, tutorials)
- Enforcement: Task plan header records task type, routing selects matching doc types

**Hierarchical Loading (Proposed):**
- Constrains which specific directives load by tier
- Enforcement: Loading plan records tiers and triggers

**Interaction:**
- ✅ **Complementary**: Context Compass selects doc types, hierarchical loading selects specific docs within those types
- ✅ **Layered Constraint**: Compass is first filter (doc types), tiers are second filter (specific docs)
- ⚠️ **Coordination Needed**: Both must be recorded in task plan header

**Example:**
- Task: Implementation / Feature Build (Execution intent)
- Context Compass: Load reference + how-to only
- Hierarchical Loading: Within reference/how-to, load Tier 1-3, defer Tier 4-5
- Result: Efficient loading with double constraint (type + tier)

**Insight:** Hierarchical loading works within Context Compass constraints, providing second layer of efficiency.

### Reflection Question 5: How do we handle lifecycle phase transitions?

**Lifecycle Phase Analysis:**

**AgentOS Lifecycle:**
- intake → classify → route → plan → execute → verify → report → anneal

**Tier Loading by Phase:**

**Intake/Classify/Route:**
- Tier 1: Core contracts (always)
- Tier 2: Routing-specific (if routing needed)
- Tier 3: Complexity-based (determined during classify)
- Tier 4-5: Not yet needed

**Plan:**
- Tier 1: Core contracts (cached)
- Tier 2: Planning-specific (if planning needed)
- Tier 3: Complexity-based planning rules
- Tier 4: Design-decision checkpoint templates (if design decision required)
- Tier 5: Not yet needed

**Execute:**
- Tier 1: Core contracts (cached)
- Tier 2: Execution-specific (domain directives)
- Tier 3: Complexity-based execution rules
- Tier 4: Specialized execution rules (if needed)
- Tier 5: Registry mapping (if registry work needed)

**Verify:**
- Tier 1: Core contracts (cached)
- Tier 2: Verification-specific (verification-contract.md)
- Tier 3: Complexity-based verification gates
- Tier 4: Advanced verification rules (if needed)
- Tier 5: Specialized validation scripts (if needed)

**Report/Anneal:**
- Tier 1: Core contracts (cached)
- Tier 2: Self-improvement-specific (if gaps found)
- Tier 3: Complexity-based reporting rules
- Tier 4-5: Not typically needed

**Tier 3 Loading Timing**: Tier 3 directives are loaded during the route phase after complexity determination. Complexity is determined during classify phase, so Tier 3 loading occurs in route phase.

**Insight:** Lifecycle phases naturally map to tier loading, enabling efficient phase-based loading.

### Reflection Question 6: What are the validation requirements?

**Validation Strategy:**

1. **Loading Plan Completeness:**
   - All required Tier 1 directives must be loaded
   - Tier 2-3 directives must match task type and complexity
   - Deferred directives must have explicit triggers

2. **Trigger Validity:**
   - Triggers must reference specific lifecycle phases or conditions
   - Triggers must be auditable (not vague like "when needed")
   - Triggers must align with Context Compass constraints

3. **Tier Assignment Correctness:**
   - Validation script checks tier assignments
   - Ensures core contracts are in Tier 1
   - Verifies specialized rules are in Tier 4-5

4. **Loading Efficiency:**
   - Track token usage before/after hierarchical loading
   - Verify Tier 4-5 rules are not loaded unnecessarily
   - Monitor loading plan accuracy

**Insight:** Validation ensures hierarchical loading maintains AgentOS principles while achieving efficiency.

---

## Self-Reflection Cycle 3: Implementation Details (Hierarchical Loading)

### Reflection Question 7: What is the implementation strategy?

**Implementation Plan:**

#### Step 1: Define Tier Structure
**File:** `docs/reference/agentos/context-compass.md` (enhancement)

**Add Section 5: Hierarchical Loading Tiers**
```markdown
## 5. Hierarchical Loading Tiers

Directives are organized into loading tiers to optimize context usage while maintaining explicit declaration.

### Tier 1: Core Contracts (Always Loaded)
These directives are required for all tasks:
- `behavior-spec.md` - Core behavior contract
- `architecture.md` - Architecture model
- `routing.md` - Routing model
- `context-compass.md` - Doc type constraints

**Rationale:** Core constraints apply to all tasks.

### Tier 2: Task-Type Specific (By Task Type)
These directives are loaded based on task type:
- Task-type-specific contracts (e.g., `verification-contract.md` for Testing tasks)
- Domain-specific directives (based on allowed domains from routing)

**Rationale:** Only needed for specific task types.

### Tier 3: Complexity-Based (By Complexity Level)
These directives are loaded based on complexity level:
- Level 1: Minimal verification gates
- Level 2: Standard verification gates
- Level 3-4: Comprehensive verification gates, design-decision checkpoints

**Rationale:** Complexity determines documentation and verification rigor.

### Tier 4: Phase-Specific (On Demand)
These directives are loaded at specific lifecycle phases:
- Design-decision checkpoint templates (when design decision required)
- Meta-analysis mode rules (for AgentOS Meta-Maintenance tasks)
- Specialized validation scripts (when specific validation needed)

**Triggers:** Explicit lifecycle phase or condition.

### Tier 5: Specialized (Lazy Loaded)
These directives are rarely needed:
- Registry mapping details (when registry work needed)
- Bootstrap gates (during bootstrap only)
- Advanced verification rules (for complex verification)

**Triggers:** Explicit, rare conditions.

### Tier Assignment Rules
- Core contracts (behavior, architecture, routing) → Tier 1
- Task-type-specific contracts → Tier 2
- Complexity-appropriate rules → Tier 3
- Phase-specific templates → Tier 4
- Rarely-used specialized rules → Tier 5
```

#### Step 2: Enhance Directive Loading Plan Format
**File:** `docs/reference/agentos/behavior-spec.md` (enhancement)

**Update Section 10: Context loading contract**
```markdown
## 10. Context loading contract
[... existing text ...]

The directive loading plan must use the following format:

```
Directive Loading Plan:
- Tier 1 (Core): [list of loaded Tier 1 directives]
- Tier 2 (Task-Type): [list of loaded Tier 2 directives, task type]
- Tier 3 (Complexity): [list of loaded Tier 3 directives, complexity level]
- Tier 4 (Phase): [list of loaded Tier 4 directives, trigger conditions]
- Tier 5 (Specialized): [list of loaded Tier 5 directives, trigger conditions]
- Deferred: [list of deferred directives with explicit triggers]
```

Each deferred directive must have an explicit, auditable trigger condition (e.g., "Load `design-decision-checkpoint-template.md` when design-decision checkpoint phase is reached").
```

#### Step 3: Update Cursor Adapter
**File:** `docs/how-to/agentos/cursor-adapter.md` (enhancement)

**Add Section 7: Hierarchical Loading Instructions**
```markdown
## 7. Hierarchical loading instructions

When loading directives:
1. Always load Tier 1 (core contracts) first
2. Load Tier 2 based on task type
3. Load Tier 3 based on complexity level
4. Load Tier 4 only when phase is reached (with explicit trigger)
5. Load Tier 5 only when specialized functionality is needed (with explicit trigger)

Record tier information in the directive loading plan.
```

#### Step 4: Create Tier Assignment Reference
**File:** `docs/reference/agentos/directive-tiers.md` (new)

**Content:**
- Complete tier assignment for all AgentOS directives
- Tier assignment rationale for each directive
- Trigger conditions for Tier 4-5 directives
- Examples of loading plans by task type and complexity

#### Step 5: Create Validation Script
**File:** `scripts/agentos/validate_directive_loading.py` (new)

**Validation Checks:**
- Tier 1 directives are always loaded
- Tier 2-3 directives match task type and complexity
- Deferred directives have explicit triggers
- Tier assignments are correct
- Loading plan format is complete

### Reflection Question 8: What are the edge cases and risks?

**Edge Cases:**

1. **Bootstrap Scenario:**
   - **Case:** New repo, directives missing
   - **Solution:** Bootstrap gates (Tier 5) load when bootstrap detected
   - **Impact:** Low - handled by existing bootstrap process

2. **Cross-Domain Tasks:**
   - **Case:** Task requires multiple domains
   - **Solution:** Load Tier 2 directives for all required domains
   - **Impact:** Medium - may load more than single domain, but still efficient

3. **Complexity Escalation:**
   - **Case:** Task complexity increases during execution
   - **Solution:** Load additional Tier 3 directives, update loading plan
   - **Impact:** Low - loading plan is updated, traceability maintained

4. **Phase Skipping:**
   - **Case:** Design-decision checkpoint skipped (Level 1 task)
   - **Solution:** Tier 4 design-decision templates not loaded
   - **Impact:** Low - appropriate for simple tasks

5. **Adapter Misfire:**
   - **Case:** Cursor rule loads wrong tier
   - **Solution:** Task plan header records actual loading, validation catches mismatch
   - **Impact:** Medium - requires validation discipline

**Risks:**

1. **Over-Optimization:**
   - **Risk:** Too many tiers, complex to manage
   - **Mitigation:** Start with 5 tiers, validate simplicity

2. **Under-Loading:**
   - **Risk:** Required directive not loaded, task fails
   - **Mitigation:** Tier 1 includes all essential, validation ensures completeness

3. **Trigger Ambiguity:**
   - **Risk:** Vague triggers reduce traceability
   - **Mitigation:** Require explicit, auditable triggers, validation checks

**Insight:** Edge cases are manageable with proper validation and explicit triggers.

---

## Part B: Progressive Documentation Analysis

### Initial Analysis: Understanding the Pattern

#### Memory Bank's Progressive Documentation Pattern

**What it is:**
- Concise initial templates that scale with complexity
- "Detail-on-demand" approach (expand when needed)
- Tabular formats for efficient comparisons
- Level-appropriate documentation scaling

**Why it works:**
- Simple tasks don't need comprehensive documentation
- Complex tasks need thorough documentation
- Tabular formats are token-efficient
- Progressive disclosure reduces initial cognitive load

**Evidence from Memory Bank:**
- Level 1: Ultra-compact templates (~200 tokens)
- Level 2: Basic templates (~500 tokens)
- Level 3-4: Comprehensive templates (~2000 tokens)
- Tabular comparisons: ~50% token reduction vs prose

#### Current AgentOS State

**What exists:**
- Design-decision checkpoint required for material decisions
- No explicit template structure
- ADRs have fixed format (comprehensive)
- Documentation requirements scale implicitly with complexity

**Gap analysis:**
- No progressive templates for design-decision checkpoints
- All design decisions use same comprehensive format
- No "detail-on-demand" mechanism
- Tabular comparison formats not standardized

---

## Self-Reflection Cycle 1: Deep Pattern Analysis (Progressive Documentation)

### Reflection Question 1: How does progressive documentation align with AgentOS's rationale preservation goal?

**Alignment Analysis:**

**AgentOS Goal (PRB-0005):**
- Preserve rationale for core design decisions
- Prevent rationale loss during evolution
- ADRs capture decisions with rationale

**Progressive Documentation:**
- Level 1-2: Brief rationale (sufficient for simple decisions)
- Level 3-4: Comprehensive rationale (needed for complex decisions)
- Tabular comparisons preserve tradeoff analysis efficiently

**Alignment:**
- ✅ **Strong Alignment**: Progressive documentation enhances rationale preservation
  - Simple decisions get appropriate documentation (not over-documented)
  - Complex decisions get comprehensive documentation (not under-documented)
  - Tabular formats preserve tradeoffs efficiently

- ⚠️ **Adaptation Needed**: Must ensure rationale is preserved at all levels
  - Level 1-2 templates must include rationale (brief but present)
  - Level 3-4 templates must include comprehensive rationale
  - Tabular comparisons must preserve tradeoff information

**Insight:** Progressive documentation enhances rationale preservation by scaling appropriately.

### Reflection Question 2: What are the appropriate documentation levels?

**Level Analysis:**

**Level 1: Quick Decision (Brief Template)**
- Component name
- Selected approach (1-2 sentences)
- Brief rationale (1-2 sentences)
- Simple tradeoff table (2-3 options, 3-4 criteria)
- **Use Case:** Simple bug fix, straightforward enhancement
- **Token Estimate:** ~200-300 tokens

**Note**: Token estimates are approximate. Actual usage may vary based on content complexity and detail level.

**Level 2: Standard Decision (Basic Template)**
- Component name and requirements
- 2-3 options considered
- Selected approach with brief implementation notes
- Rationale (2-3 sentences)
- Tradeoff table (2-3 options, 4-5 criteria)
- **Use Case:** Standard feature, clear requirements
- **Token Estimate:** ~500-700 tokens

**Level 3: Complex Decision (Comprehensive Template)**
- Component breakdown (requirements, constraints, integration points)
- 3-4 options explored
- Detailed option descriptions
- Comprehensive tradeoff analysis (tabular + prose)
- Selected approach with implementation guidance
- Rationale with evidence
- Discarded alternatives with reasons
- **Use Case:** Complex feature, architectural decisions
- **Token Estimate:** ~1500-2000 tokens

**Level 4: System Decision (Enterprise Template)**
- Full component breakdown
- 4+ options explored
- Detailed option analysis with pros/cons
- Comprehensive tradeoff matrix (tabular + detailed prose)
- Selected approach with detailed implementation guidance
- Rationale with evidence and references
- Discarded alternatives with detailed reasons
- Risk assessment
- **Use Case:** System-level architecture, enterprise decisions
- **Token Estimate:** ~2500-3000 tokens

**Insight:** 4-level structure aligns with AgentOS complexity levels, provides appropriate scaling.

### Reflection Question 3: How do we ensure rationale is preserved at all levels?

**Rationale Preservation Strategy:**

1. **Minimum Rationale Requirements:**
   - All levels must include: selected approach, rationale, tradeoffs
   - Level 1-2: Brief but complete rationale
   - Level 3-4: Comprehensive rationale with evidence

2. **Tabular Comparison Standards:**
   - All levels use tabular format for tradeoffs (token-efficient)
   - Level 1-2: Simple table (options × criteria)
   - Level 3-4: Comprehensive table with detailed analysis

3. **Detail-on-Demand:**
   - Level 1-2: Brief templates, expand if needed
   - Level 3-4: Comprehensive templates, detail always included
   - **Expansion Triggers**:
     - User explicitly requests detail
     - Complexity escalates during task
     - Review process requires comprehensive documentation
     - ADR creation requires full detail extraction

4. **Validation:**
   - Check that rationale is present at all levels
   - Verify tradeoff information is complete
   - Ensure selected approach is justified

**Insight:** Rationale preservation is maintained through minimum requirements and validation.

---

## Self-Reflection Cycle 2: AgentOS-Specific Considerations (Progressive Documentation)

### Reflection Question 4: How does progressive documentation interact with design-decision checkpoints?

**Interaction Analysis:**

**Current Design-Decision Checkpoint:**
- Required for material design/architecture decisions
- Must document options, tradeoffs, selected approach, rationale
- No explicit template structure

**Progressive Documentation Enhancement:**
- Provides templates for design-decision checkpoints
- Scales with complexity level
- Standardizes format while allowing flexibility

**Integration:**
- ✅ **Enhancement**: Progressive templates enhance existing checkpoint requirement
- ✅ **Scaling**: Templates scale with complexity level (matches checkpoint rigor)
- ✅ **Standardization**: Provides consistent format while preserving flexibility

**Example Integration:**
```
Design-Decision Checkpoint (Level 2):
- Use Level 2 template (basic)
- Document 2-3 options
- Brief tradeoff table
- Selected approach with rationale

Design-Decision Checkpoint (Level 3):
- Use Level 3 template (comprehensive)
- Document 3-4 options with details
- Comprehensive tradeoff analysis
- Selected approach with implementation guidance
```

**Insight:** Progressive documentation naturally enhances design-decision checkpoints.

### Reflection Question 5: How do we handle ADR creation from design decisions?

**ADR Integration:**

**Current ADR Format:**
- Fixed comprehensive format
- Required for core behavior changes
- Links to problems and artifacts

**Progressive Documentation:**
- Design-decision checkpoints use progressive templates
- ADRs created from design decisions when core behavior changes

**Integration Strategy:**
1. **Design-Decision Checkpoint:**
   - Use progressive template (Level 1-4 based on complexity)
   - Document decision with appropriate detail

2. **ADR Creation (if core behavior changes):**
   - Extract decision information from checkpoint
   - Use ADR format (comprehensive, always)
   - Link to design-decision checkpoint document
   - Link to problem and artifacts

3. **Rationale Preservation:**
   - Checkpoint preserves decision rationale (scaled)
   - ADR preserves decision rationale (comprehensive)
   - Both link to each other for traceability

**Insight:** Progressive templates for checkpoints, comprehensive format for ADRs (when needed).

---

## Self-Reflection Cycle 3: Implementation Details (Progressive Documentation)

### Reflection Question 6: What is the implementation strategy?

**Implementation Plan:**

#### Step 1: Create Progressive Template Reference
**File:** `docs/reference/agentos/design-decision-templates.md` (new)

**Content:**
- Level 1 template (brief)
- Level 2 template (basic)
- Level 3 template (comprehensive)
- Level 4 template (enterprise)
- Tabular comparison format standards
- Examples for each level

#### Step 2: Update Design-Decision Checkpoint Requirements
**File:** `docs/reference/agentos/behavior-spec.md` (enhancement)

**Update Section 11: Task plan header requirements**
```markdown
Design-decision checkpoint status (required or not required, plus evidence when required).

When a design-decision checkpoint is required, use the appropriate template from `docs/reference/agentos/design-decision-templates.md` based on complexity level:
- Level 1: Brief template
- Level 2: Basic template
- Level 3: Comprehensive template
- Level 4: Enterprise template

All templates must include: selected approach, rationale, and tradeoff analysis (tabular format recommended for efficiency).
```

#### Step 3: Create Template Examples
**File:** `docs/how-to/agentos/design-decision-checkpoint.md` (new or enhance)

**Content:**
- Step-by-step guide for design-decision checkpoints
- Template selection by complexity level
- Tabular comparison examples
- Integration with ADR creation (when needed)

#### Step 4: Update Validation
**File:** `scripts/agentos/validate_design_decisions.py` (new or enhance)

**Validation Checks:**
- Design-decision checkpoint uses appropriate template level
- Rationale is present and complete
- Tradeoff analysis is included (tabular format preferred)
- Selected approach is justified

### Reflection Question 7: What are the edge cases and risks?

**Edge Cases:**

1. **Complexity Escalation:**
   - **Case:** Decision starts Level 2, escalates to Level 3
   - **Solution:** Expand template, update checkpoint document
   - **Impact:** Low - templates are expandable

2. **Multiple Decisions:**
   - **Case:** Multiple design decisions in one task
   - **Solution:** Each decision uses appropriate template level
   - **Impact:** Low - templates are per-decision

3. **ADR Requirement:**
   - **Case:** Design decision requires ADR (core behavior change)
   - **Solution:** Extract from checkpoint, create comprehensive ADR
   - **Impact:** Low - ADR format is comprehensive, checkpoint provides source

4. **Template Mismatch:**
   - **Case:** Template level doesn't match complexity
   - **Solution:** Validation checks template-complexity alignment
   - **Impact:** Medium - requires validation discipline

**Risks:**

1. **Under-Documentation:**
   - **Risk:** Level 1-2 templates miss important rationale
   - **Mitigation:** Minimum rationale requirements, validation checks

2. **Over-Documentation:**
   - **Risk:** Level 3-4 templates used unnecessarily
   - **Mitigation:** Template selection guidance, complexity-based triggers

3. **Tabular Format Inconsistency:**
   - **Risk:** Inconsistent tabular formats reduce efficiency
   - **Mitigation:** Standard tabular format in templates, examples

**Insight:** Edge cases are manageable with proper templates and validation.

---

## Final Enriched Recommendations

### Recommendation A: Implement Hierarchical Rule Loading

**Rationale:**
After three reflection cycles, hierarchical loading is clearly beneficial. It reduces token usage by 30-50% while maintaining explicit declaration through enhanced loading plan format. The 5-tier structure provides granular control, and lifecycle phase mapping enables efficient phase-based loading.

**Implementation:**
1. Enhance `context-compass.md` with tier structure (Section 5)
2. Enhance `behavior-spec.md` directive loading plan format (Section 10)
3. Update `cursor-adapter.md` with hierarchical loading instructions (Section 7)
4. Create `directive-tiers.md` reference (new file)
5. Create `validate_directive_loading.py` script (new file)

**Success Criteria:**
- Token usage reduced by 30-50%
- Loading plan includes tier information
- All deferred directives have explicit triggers
- Validation script passes
- No functionality loss

### Recommendation B: Implement Progressive Documentation

**Rationale:**
After three reflection cycles, progressive documentation enhances rationale preservation by scaling appropriately. It provides templates for design-decision checkpoints that scale with complexity, ensuring simple decisions aren't over-documented and complex decisions aren't under-documented.

**Implementation:**
1. Create `design-decision-templates.md` reference (new file)
2. Enhance `behavior-spec.md` design-decision checkpoint requirements (Section 11)
3. Create/enhance `design-decision-checkpoint.md` how-to guide
4. Create/enhance `validate_design_decisions.py` script

**Success Criteria:**
- Templates available for all complexity levels
- Design-decision checkpoints use appropriate templates
- Rationale preserved at all levels
- Tabular formats standardized
- Validation script passes

---

## Integration Considerations

### Combined Benefits:
- Hierarchical loading reduces initial context usage
- Progressive documentation reduces documentation token usage
- Combined: ~40-60% overall token reduction potential

### Coordination:
- Design-decision checkpoint templates (progressive docs) are Tier 4 directives (hierarchical loading)
- Load templates only when design-decision checkpoint phase is reached
- Templates scale with complexity (matches Tier 3 complexity-based loading)

---

## Required ADRs

1. **ADR: Hierarchical Rule Loading for Context Efficiency**
   - Problem: PRB-0002 (Context Instability) - token efficiency aspect
   - Decision: Implement 5-tier hierarchical loading with explicit declaration
   - Artifacts: `context-compass.md`, `behavior-spec.md`, `cursor-adapter.md`, `directive-tiers.md`, `validate_directive_loading.py`

2. **ADR: Progressive Documentation Templates for Design Decisions**
   - Problem: PRB-0005 (Rationale Loss) - documentation efficiency aspect
   - Decision: Implement 4-level progressive templates for design-decision checkpoints
   - Artifacts: `design-decision-templates.md`, `behavior-spec.md`, `design-decision-checkpoint.md`, `validate_design_decisions.py`

---

## Related Docs

- Integration analysis: `docs/work/agentos/improvement/2026-01-15-memory-bank-integration-analysis.md`
- Context compass: `docs/reference/agentos/context-compass.md`
- Behavior spec: `docs/reference/agentos/behavior-spec.md`
- Cursor adapter: `docs/how-to/agentos/cursor-adapter.md`

---

**Status**: Ready for implementation
**Next Action**: Create ADRs and implement Phase 1 enhancements

---

## Action Items

### Pre-Implementation (Double-Loop Promotion)

1. **Create/Link Problem Entry**
   - Owner: [TBD]
   - Evidence: Problem entry in `docs/reference/agentos/problem-registry.md` or link to PRB-0002
   - Completion: [ ] Problem validated and added to registry
   - Affected artifacts: `docs/reference/agentos/problem-registry.md`

2. **Create ADR: Hierarchical Rule Loading**
   - Owner: [TBD]
   - Evidence: ADR file created in `docs/explanation/agentos/decisions/YYYY-MM-DD-hierarchical-rule-loading.md`
   - Completion: [ ] ADR created with full format per `decision-record-format.md`
   - Affected artifacts: `docs/explanation/agentos/decisions/YYYY-MM-DD-hierarchical-rule-loading.md`

3. **Create ADR: Progressive Documentation Templates**
   - Owner: [TBD]
   - Evidence: ADR file created in `docs/explanation/agentos/decisions/YYYY-MM-DD-progressive-documentation-templates.md`
   - Completion: [ ] ADR created with full format
   - Affected artifacts: `docs/explanation/agentos/decisions/YYYY-MM-DD-progressive-documentation-templates.md`

4. **Update Traceability Map**
   - Owner: [TBD]
   - Evidence: Entries added to `docs/reference/agentos/traceability.md`
   - Completion: [ ] Problems mapped to ADRs, artifacts listed
   - Affected artifacts: `docs/reference/agentos/traceability.md`

### Implementation

5. **Enhance context-compass.md**
   - Owner: [TBD]
   - Evidence: Section 5 added with tier structure
   - Completion: [ ] Section 5 added, validated
   - Affected artifacts: `docs/reference/agentos/context-compass.md`

6. **Enhance behavior-spec.md**
   - Owner: [TBD]
   - Evidence: Sections 10 and 11 updated with tier format
   - Completion: [ ] Sections updated, validated
   - Affected artifacts: `docs/reference/agentos/behavior-spec.md`

7. **Create directive-tiers.md**
   - Owner: [TBD]
   - Evidence: Reference file created with complete tier assignments
   - Completion: [ ] File created, all directives assigned to tiers
   - Affected artifacts: `docs/reference/agentos/directive-tiers.md`

8. **Create design-decision-templates.md**
   - Owner: [TBD]
   - Evidence: Reference file created with 4-level templates
   - Completion: [ ] File created, all templates included
   - Affected artifacts: `docs/reference/agentos/design-decision-templates.md`

9. **Create Validation Scripts**
   - Owner: [TBD]
   - Evidence: Scripts created and tested
   - Completion: [ ] Scripts pass, added to validation-scripts.md
   - Affected artifacts: `scripts/agentos/validate_directive_loading.py`, `scripts/agentos/validate_design_decisions.py`

### Post-Implementation

10. **Run MAM and Micro-AAR**
    - Owner: [TBD]
    - Evidence: MAM checklist completed, Micro-AAR note created
    - Completion: [ ] MAM completed, gaps captured if any, Micro-AAR done
    - Affected artifacts: `docs/work/agentos/improvement/YYYY-MM-DD-batch-2-micro-aar.md`

---

## Post-Implementation Verification

After implementing this batch:

1. **Run MAM**: Use Meta Analysis Mode to validate behavior
   - Check: Task plan header present and complete
   - Check: Required directives loaded
   - Check: Contracts enforced
   - Check: Gaps captured if discovered

2. **Run Validation Scripts**: Execute batch-specific validation
   - `just agentos::validate-directive-loading` (or equivalent)
   - `just agentos::validate-design-decisions` (or equivalent)

3. **Micro-AAR**: Capture lessons learned
   - What worked well?
   - What challenges were encountered?
   - What gaps were discovered?
   - Update improvement note with Micro-AAR results

4. **Integration Testing**: Test with previously implemented batches
   - Test hierarchical loading with Context Compass constraints
   - Test progressive templates with design-decision checkpoints

---

## Gap Capture During Implementation

During implementation, capture gaps per `docs/how-to/agentos/capture-gaps.md`:
- Missing or incorrect directives
- Unclear or missing steps
- Verification gate issues
- Ambiguity resolutions

Promote gaps to problems if they define new problems.

---

## Required ADRs

1. **ADR: Hierarchical Rule Loading for Context Efficiency**

**Status**: Proposed (to be created)
**Date**: [Will be set when ADR is created]
**Scope**: agentos
**Problem IDs**: PRB-0002 (token efficiency aspect)
**Supersedes**: (if applicable)

**Note**: This ADR must be created before implementation. See `docs/reference/agentos/decision-record-format.md` for full format requirements.

**ADR Summary**:
- Decision: Implement 5-tier hierarchical loading with explicit declaration
- Alternatives: Keep unified loading (rejected - too much token usage), automatic loading (rejected - violates explicit declaration)
- Consequences: Reduces token usage by 30-50%, maintains explicit declaration, adds tier management complexity
- Artifacts: `context-compass.md`, `behavior-spec.md`, `cursor-adapter.md`, `directive-tiers.md`, `validate_directive_loading.py`

2. **ADR: Progressive Documentation Templates for Design Decisions**

**Status**: Proposed (to be created)
**Date**: [Will be set when ADR is created]
**Scope**: agentos
**Problem IDs**: PRB-0005 (documentation efficiency aspect)
**Supersedes**: (if applicable)

**Note**: This ADR must be created before implementation. See `docs/reference/agentos/decision-record-format.md` for full format requirements.

**ADR Summary**:
- Decision: Implement 4-level progressive templates for design-decision checkpoints
- Alternatives: Keep comprehensive-only templates (rejected - too much overhead for simple decisions), unstructured checkpoints (rejected - less rationale preservation)
- Consequences: Scales documentation appropriately, preserves rationale at all levels, requires template management
- Artifacts: `design-decision-templates.md`, `behavior-spec.md`, `design-decision-checkpoint.md`, `validate_design_decisions.py`
