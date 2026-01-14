# Structured Exploration (Reference)

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Defines the 5-phase structured exploration methodology for design-decision checkpoints. Enhances rationale preservation by providing systematic exploration phases while maintaining compatibility with complexity-based workflow variations and progressive documentation templates.

---

## 1. Overview

Structured exploration provides a systematic 5-phase methodology for design-decision checkpoints. It enhances rationale preservation (PRB-0005) by ensuring comprehensive exploration of alternatives, explicit decision criteria, and validation of decisions against requirements.

**Integration:**
- Enhances existing design-decision checkpoints (does not replace them)
- Integrates with progressive documentation templates (Batch 2)
- Aligns with complexity-based workflow variations (Batch 3)
- Phase 3 (Trade-off Analysis) maps to existing template "Tradeoffs (table)" requirement
- Phase 4 (Decision Documentation) maps to existing template "Selected approach" and "Rationale" requirements

---

## 2. Phase Definitions

### Phase 1: Component Breakdown

**Purpose**: Understand the component/decision in context before exploring options.

**Outputs:**
- Functional requirements (what the component must do)
- Technical constraints (limitations, dependencies, existing systems)
- Integration points (how it connects to other components)
- Dependencies (what it requires from other components/systems)

**Acceptance Criteria:**
- All relevant requirements identified
- Constraints documented (technical, time, resource)
- Integration points clearly identified
- Dependencies listed

**Complexity-Based Rigor:**
- **Level 1-2**: Brief list of key requirements and constraints
- **Level 3-4**: Comprehensive breakdown with detailed analysis

**Example (Level 2):**
```
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

### Phase 2: Option Exploration

**Purpose**: Systematically explore viable alternatives before making a decision.

**Outputs:**
- List of 2-4 viable options
- Brief description of each option
- Preliminary pros/cons for each option

**Acceptance Criteria:**
- At least 2 options explored (or rationale for single option)
- Each option has clear description
- Preliminary trade-offs identified

**Complexity-Based Rigor:**
- **Level 1-2**: 2-3 options with brief descriptions
- **Level 3-4**: 3-4 options with detailed descriptions

**Example (Level 2):**
```
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

### Phase 3: Trade-off Analysis

**Purpose**: Systematically compare options against decision criteria.

**Outputs:**
- Tabular comparison (options × criteria)
- Detailed analysis of trade-offs
- Risk assessment for each option

**Acceptance Criteria:**
- Tabular format (efficient, aligns with template requirement)
- Criteria clearly defined
- Trade-offs explicitly documented
- Risks identified

**Complexity-Based Rigor:**
- **Level 1-2**: 3-4 criteria, concise analysis
- **Level 3-4**: 4-6 criteria, comprehensive analysis with weights if useful

#### Criteria Selection

**Common criteria patterns**:
- **Performance**: Speed, throughput, latency, efficiency
- **Maintainability**: Code clarity, testability, documentation, ease of changes
- **Scalability**: Ability to handle growth, resource usage, bottlenecks
- **Complexity**: Implementation complexity, cognitive load, learning curve
- **Risk**: Technical risk, business risk, deployment risk, migration risk
- **Cost**: Development cost, operational cost, maintenance cost, time to market
- **Flexibility**: Extensibility, configurability, adaptability to change
- **Reliability**: Uptime, error handling, fault tolerance, data integrity
- **Security**: Vulnerability exposure, compliance, access control
- **Integration**: Ease of integration, compatibility, dependencies

**Criteria count guidance**:
- **Level 1-2**: 3-4 criteria (focus on most important)
- **Level 3-4**: 4-6 criteria (comprehensive coverage)

**Criteria specificity requirements**:
- Use specific, measurable criteria (e.g., "Development Speed" not "Pros")
- Avoid generic criteria like "Good" or "Bad"
- Make criteria relevant to the decision context
- Ensure criteria are comparable across options

**Examples of good criteria**:
- "Development Speed" (specific, measurable)
- "Maintainability" (clear, relevant)
- "Performance (latency)" (specific metric)
- "Integration Complexity" (specific aspect)

**Examples of poor criteria**:
- "Pros" (too generic)
- "Good" (not a criterion)
- "Features" (too vague)
- "Quality" (too broad, not measurable)

#### Examples by Complexity Level

**Level 1 (brief)**:
```
| Option | Speed | Complexity | Risk |
|--------|-------|------------|------|
| A: Direct | Fast | Low | Low |
| B: Wrapper | Moderate | Medium | Low |
```

**Level 2 (basic)**:
```
| Option | Development Speed | Maintainability | Flexibility | Risk |
|--------|-------------------|-----------------|-------------|------|
| A: Direct library | High | Medium | Low | Low |
| B: Custom wrapper | Low | High | High | Medium |
| C: Hybrid | Medium | Medium | Medium | Low |
```

**Level 3 (comprehensive)**:
```
| Option | Performance | Maintainability | Scalability | Complexity | Risk | Cost |
|--------|-------------|-----------------|-------------|------------|------|------|
| A: Redis KV | Medium | High | Medium | Low | Low | Low |
| B: Redis Hash | High | Medium | High | Medium | Low | Low |
| C: Hybrid Cache | High | Medium | High | High | Medium | Medium |
```

**Level 4 (enterprise with weights)**:
```
| Option | Performance (0.3) | Maintainability (0.2) | Scalability (0.3) | Risk (0.2) | Weighted |
|--------|------------------|----------------------|-------------------|------------|----------|
| A: Microservices | High (4) | Medium (3) | High (4) | Medium (3) | 3.5 |
| B: Monolith | Medium (3) | High (4) | Low (2) | Low (2) | 2.7 |
| C: Modular Monolith | Medium (3) | High (4) | Medium (3) | Low (2) | 2.9 |
```

**Note**: See `docs/reference/agentos/design-decision-templates.md` for complete table formatting standards and guidelines.

### Phase 4: Decision Documentation

**Purpose**: Document selected approach with comprehensive rationale.

**Outputs:**
- Selected approach description
- Rationale (why this option)
- Discarded alternatives with reasons
- Implementation guidance

**Acceptance Criteria:**
- Selected approach clearly described
- Rationale links to trade-off analysis
- Discarded alternatives documented with reasons
- Implementation guidance provided

**Complexity-Based Rigor:**
- **Level 1-2**: Brief description and rationale
- **Level 3-4**: Comprehensive documentation with detailed rationale

**Example (Level 2):**
```
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

### Phase 5: Decision Verification

**Purpose**: Validate decision against requirements, constraints, and integration points.

**Outputs:**
- Verification against functional requirements
- Verification against technical constraints
- Verification against integration points
- Risk assessment validation

**Acceptance Criteria:**
- Decision meets all functional requirements
- Decision respects all technical constraints
- Integration points are addressed
- Risks are acceptable

**Complexity-Based Rigor:**
- **Level 1-2**: Optional (brief verification if used)
- **Level 3-4**: Mandatory (comprehensive verification)

**Note**: This phase validates the design decision itself, separate from task verification gates that validate implementation.

**Example (Level 3):**
```
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

---

## 3. Phase Sequence and Dependencies

Phases must be completed in sequence:

1. **Phase 1 → Phase 2**: Component breakdown provides context for option exploration
2. **Phase 2 → Phase 3**: Options from Phase 2 are analyzed in Phase 3
3. **Phase 3 → Phase 4**: Trade-off analysis informs decision documentation
4. **Phase 4 → Phase 5**: Decision documentation is verified in Phase 5

**Iteration**: Phases may be iterated if exploration reveals new information, but all phases must be completed before checkpoint is considered complete.

---

## 4. Complexity-Based Rigor

### Level 1-2 (Optional/Brief)

**When to use**: Simple design decisions in Level 1-2 tasks

**Requirements:**
- Phases 1-4 recommended (brief)
- Phase 5 optional
- Phase outputs may be concise
- Structured exploration is optional (only if design decision exists)

**Example scope:**
- Brief component breakdown (key requirements only)
- 2-3 options explored
- Simple trade-off table (3-4 criteria)
- Brief decision documentation
- Optional verification

### Level 3-4 (Mandatory/Full)

**When to use**: Material design decisions in Level 3-4 tasks

**Requirements:**
- All 5 phases mandatory when material design decision exists
- Comprehensive phase outputs
- If no material decision exists, document rationale for skipping structured exploration

**Example scope:**
- Comprehensive component breakdown
- 3-4 options explored with detailed descriptions
- Comprehensive trade-off analysis (4-6 criteria, weights if useful)
- Detailed decision documentation
- Mandatory verification

---

## 5. Phase Output Preservation Format

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

**Cross-references**: Decision summary should link to all phases for traceability.

---

## 6. Integration with Design-Decision Templates

Structured exploration phases integrate with existing templates:

- **Phase 1** (Component Breakdown) → Provides context for rationale
- **Phase 2** (Option Exploration) → Maps to "Options considered" template requirement
- **Phase 3** (Trade-off Analysis) → Maps to "Tradeoffs (table)" template requirement
- **Phase 4** (Decision Documentation) → Maps to "Selected approach" and "Rationale" template requirements
- **Phase 5** (Decision Verification) → Enhancement (not in original templates)

Templates should include phase markers to guide structured exploration.

---

## 7. Usage Requirements

- **Level 1-2**: Use brief structured exploration if design decision exists
- **Level 3-4**: Use full structured exploration (all 5 phases) when material design decision exists
- All phases must produce documented outputs
- Phase outputs must be preserved in checkpoint document
- Decision must link to all phases for traceability

---

## 8. Related Docs

- `docs/reference/agentos/design-decision-templates.md` (templates with phase integration)
- `docs/how-to/agentos/design-decision-structured-exploration.md` (step-by-step guide)
- `docs/reference/agentos/behavior-spec.md` (checkpoint requirements)
- `docs/reference/agentos/workflow-variations.md` (complexity-based rigor)

---

## 9. Validation

Validation checks (see `scripts/agentos/validate_design_decisions.py`):
- Level 3-4: All 5 phases must be present and complete
- Level 1-2: Phase completion optional, but if phases present, validate structure
- Trade-off analysis must be tabular format
- Phase outputs must not be empty
- Decision must link to all phases
