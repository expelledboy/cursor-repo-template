# How-to: Design-Decision Structured Exploration

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Step-by-step guide for using structured exploration phases in design-decision checkpoints.

---

## When to use

- Material design/architecture decisions in any complexity level task
- Level 1-2: Optional structured exploration (if design decision exists, use brief exploration)
- Level 3-4: Mandatory structured exploration (all 5 phases required when material decision exists)

---

## Overview

Structured exploration provides a systematic 5-phase methodology:
1. **Component Breakdown**: Understand context
2. **Option Exploration**: Explore alternatives
3. **Trade-off Analysis**: Compare options
4. **Decision Documentation**: Document selection
5. **Decision Verification**: Validate decision (Level 3-4 mandatory)

See `docs/reference/agentos/structured-exploration.md` for phase definitions and `docs/reference/agentos/design-decision-templates.md` for template integration.

---

## Step-by-step process

### Step 1: Determine complexity and exploration rigor

**Level 1-2:**
- Brief structured exploration (optional if design decision exists)
- Phases 1-4 recommended (brief)
- Phase 5 optional
- Use Level 1-2 templates

**Level 3-4:**
- Full structured exploration (mandatory if material decision exists)
- All 5 phases required
- Comprehensive outputs
- Use Level 3-4 templates

**If no material decision (Level 3-4):**
- Document "No material design decisions required" with rationale
- Skip structured exploration

---

### Step 2: Phase 1 - Component Breakdown

**Purpose**: Understand the component/decision in context.

**Actions:**
1. Identify functional requirements (what must it do?)
2. Document technical constraints (limitations, dependencies)
3. List integration points (how it connects)
4. Identify dependencies (what it requires)

**Outputs:**
- **Level 1-2**: Brief list of key requirements and constraints
- **Level 3-4**: Comprehensive breakdown with detailed analysis

**Example (Level 2):**
```markdown
## Phase 1: Component Breakdown

Functional requirements:
- Support user authentication
- Integrate with existing auth service
- Handle session management

Technical constraints:
- Must use existing auth library (v2.1+)
- No database schema changes allowed
- Must support OAuth2 flow

Integration points:
- Auth service API
- Session storage
- User profile service

Dependencies:
- Auth library v2.1+
- Session middleware
```

**Checklist:**
- [ ] All relevant requirements identified
- [ ] Constraints documented
- [ ] Integration points listed
- [ ] Dependencies identified

---

### Step 3: Phase 2 - Option Exploration

**Purpose**: Systematically explore viable alternatives.

**Actions:**
1. Identify 2-4 viable options
2. Write brief description of each option
3. Note preliminary pros/cons for each

**Outputs:**
- **Level 1-2**: 2-3 options with brief descriptions
- **Level 3-4**: 3-4 options with detailed descriptions

**Example (Level 2):**
```markdown
## Phase 2: Option Exploration

Option A: Use existing auth library directly
- Pros: Fast implementation, proven reliability
- Cons: Limited customization, vendor lock-in

Option B: Build custom auth wrapper
- Pros: Full control, easier to test
- Cons: More development time, maintenance burden

Option C: Hybrid approach (library + wrapper)
- Pros: Balance of speed and control
- Cons: Additional abstraction layer
```

**Checklist:**
- [ ] At least 2 options explored (or rationale for single option)
- [ ] Each option has clear description
- [ ] Preliminary trade-offs identified

---

### Step 4: Phase 3 - Trade-off Analysis

**Purpose**: Systematically compare options against criteria.

**Actions:**
1. Define decision criteria (3-6 criteria based on complexity)
2. Create tabular comparison (options × criteria)
3. Analyze trade-offs for each option
4. Assess risks for each option (Level 3-4)

**Outputs:**
- **Level 1-2**: 3-4 criteria, concise analysis
- **Level 3-4**: 4-6 criteria, comprehensive analysis with weights if useful

**Example (Level 2):**
```markdown
## Phase 3: Trade-off Analysis

Decision criteria:
- Development speed
- Maintainability
- Flexibility
- Risk

| Option | Development Speed | Maintainability | Flexibility | Risk |
|--------|-------------------|-----------------|-------------|------|
| A: Direct library | High | Medium | Low | Low |
| B: Custom wrapper | Low | High | High | Medium |
| C: Hybrid | Medium | Medium | Medium | Low |
```

**Checklist:**
- [ ] Tabular format used (efficient, aligns with template requirement)
- [ ] Criteria clearly defined
- [ ] Trade-offs explicitly documented
- [ ] Risks identified (Level 3-4)

---

### Step 5: Phase 4 - Decision Documentation

**Purpose**: Document selected approach with comprehensive rationale.

**Actions:**
1. Select approach based on trade-off analysis
2. Write rationale (why this option)
3. Document discarded alternatives with reasons
4. Provide implementation guidance

**Outputs:**
- **Level 1-2**: Brief description and rationale
- **Level 3-4**: Comprehensive documentation with detailed rationale

**Example (Level 2):**
```markdown
## Phase 4: Decision Documentation

Selected Approach: Option C (Hybrid approach)

Rationale:
- Balances development speed (faster than custom) with flexibility (more than direct)
- Lower risk than custom wrapper
- Allows future customization without full rewrite

Discarded Alternatives:
- Option A: Rejected due to lack of flexibility for future needs
- Option B: Rejected due to high development time and maintenance burden

Implementation Guidance:
- Create wrapper layer around auth library
- Implement adapter pattern for easy swapping
- Add comprehensive tests for wrapper
```

**Checklist:**
- [ ] Selected approach clearly described
- [ ] Rationale links to trade-off analysis
- [ ] Discarded alternatives documented with reasons
- [ ] Implementation guidance provided

---

### Step 6: Phase 5 - Decision Verification (Level 3-4 mandatory, Level 1-2 optional)

**Purpose**: Validate decision against requirements, constraints, and integration points.

**Actions:**
1. Verify decision meets all functional requirements
2. Verify decision respects all technical constraints
3. Verify integration points are addressed
4. Validate risk assessment

**Outputs:**
- **Level 1-2**: Optional (brief verification if used)
- **Level 3-4**: Mandatory (comprehensive verification)

**Example (Level 3):**
```markdown
## Phase 5: Decision Verification

Verification against Requirements:
✅ Supports user authentication (wrapper provides auth interface)
✅ Integrates with existing auth service (library handles integration)
✅ Handles session management (wrapper adds session layer)

Verification against Constraints:
✅ Uses existing auth library (wrapper wraps library)
✅ No database schema changes (library handles DB)
✅ Supports OAuth2 flow (library supports OAuth2)

Verification against Integration Points:
✅ Auth service API: Library handles API calls
✅ Session storage: Wrapper manages session layer
✅ User profile service: Wrapper provides interface

Risk Assessment:
- Low risk: Uses proven library with wrapper for flexibility
- Mitigation: Comprehensive testing of wrapper layer
```

**Checklist:**
- [ ] Decision meets all functional requirements
- [ ] Decision respects all technical constraints
- [ ] Integration points are addressed
- [ ] Risks are acceptable

**Note**: This phase validates the design decision itself, separate from task verification gates that validate implementation.

---

## Integration with templates

Templates from `docs/reference/agentos/design-decision-templates.md` include phase markers. Use the template that matches your complexity level:

- **Level 1**: Brief template with phase markers
- **Level 2**: Basic template with phase markers
- **Level 3**: Comprehensive template with all 5 phases
- **Level 4**: Enterprise template with all 5 phases

Fill each phase section in the template with the outputs from the corresponding structured exploration phase.

---

## Phase completion checklist

**Before proceeding to execution:**
- [ ] All required phases completed (Level 3-4: all 5 phases; Level 1-2: Phases 1-4 if used)
- [ ] Phase outputs are documented and preserved
- [ ] Decision links to all phases for traceability
- [ ] Trade-off analysis is in tabular format
- [ ] Selected approach and rationale are clear
- [ ] Template level matches complexity level

---

## Common pitfalls and solutions

### Pitfall 1: Skipping phases to save time
**Solution**: Level 3-4 requires all 5 phases. If time is limited, use Level 1-2 brief exploration and document time constraint.

### Pitfall 2: Superficial exploration
**Solution**: Ensure phase outputs meet acceptance criteria. Validation script checks for empty outputs.

### Pitfall 3: Decision bias (confirming pre-existing preference)
**Solution**: Structured phases force systematic exploration. Ensure multiple options are genuinely explored in Phase 2.

### Pitfall 4: Only one viable option
**Solution**: Document why only one option exists in Phase 2. Still complete all phases to preserve rationale.

### Pitfall 5: Confusing Phase 5 with task verification
**Solution**: Phase 5 validates the design decision. Task verification gates validate the implementation. Both are required.

---

## Output preservation

Phase outputs must be preserved in the checkpoint document with clear markers:

```markdown
## Design Decision: [Component Name]

### Phase 1: Component Breakdown
[Phase 1 outputs]

### Phase 2: Option Exploration
[Phase 2 outputs]

### Phase 3: Trade-off Analysis
[Phase 3 outputs - tabular format]

### Phase 4: Decision Documentation
[Phase 4 outputs]

### Phase 5: Decision Verification (Level 3-4 only)
[Phase 5 outputs]

## Summary
- Selected Approach: [Summary]
- Rationale: [Summary, full in Phase 4]
```

---

## Related docs

- `docs/reference/agentos/structured-exploration.md` (phase definitions)
- `docs/reference/agentos/design-decision-templates.md` (templates with phase integration)
- `docs/reference/agentos/behavior-spec.md` (checkpoint requirements)
- `docs/reference/agentos/workflow-variations.md` (complexity-based rigor)
