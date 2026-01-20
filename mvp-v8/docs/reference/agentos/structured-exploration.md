---
title: "Structured Exploration"
status: stable
created_date: 2026-01-18
purpose: "Defines the 5-phase structured exploration process for design decisions and architectural choices"
domain: agentos
---

# Structured Exploration (Reference)

## Purpose
Provides a systematic, phase-based approach for exploring design decisions and architectural choices. Ensures comprehensive analysis of options, tradeoffs, and implementation considerations before making critical decisions.

## When to Use

### Required Usage
Structured exploration is **mandatory** when:
- Design or architectural decisions are material to the task
- Task complexity level is 3-4
- Multiple viable options exist with significant tradeoffs
- Decision impacts future development or maintenance

### Optional Usage
Structured exploration is **recommended** when:
- Task complexity level is 1-2 with material design decisions
- Tradeoffs need systematic evaluation
- Decision documentation is required for stakeholders

## 5-Phase Process

### Phase 1: Component Breakdown (Foundation)
**Purpose**: Establish clear understanding of the problem space and requirements
**Duration**: 10-20% of exploration time

**Activities**:
- Decompose the decision into core components
- Identify explicit requirements and constraints
- Define success criteria and evaluation metrics
- Document assumptions and dependencies

**Deliverables**:
- Component list with clear boundaries
- Requirements matrix (must-have vs nice-to-have)
- Success criteria with measurable outcomes
- Assumption log with validation approaches

**Templates**:
```
## Phase 1: Component Breakdown

### Core Components
- [Component 1]: [Purpose and scope]
- [Component 2]: [Purpose and scope]
- [Component 3]: [Purpose and scope]

### Requirements & Constraints
- **Functional**: [List key requirements]
- **Non-Functional**: [Performance, security, usability]
- **Technical**: [Platform, integration, compatibility]
- **Business**: [Cost, timeline, resources]

### Success Criteria
- [Measurable outcome 1]: [Acceptance criteria]
- [Measurable outcome 2]: [Acceptance criteria]
- [Measurable outcome 3]: [Acceptance criteria]

### Assumptions & Risks
- [Assumption 1]: [Validation approach]
- [Assumption 2]: [Validation approach]
```

### Phase 2: Option Exploration (Discovery)
**Purpose**: Generate and evaluate multiple viable solution approaches
**Duration**: 20-30% of exploration time

**Activities**:
- Brainstorm 2-4 distinct solution approaches
- Research existing patterns and proven solutions
- Evaluate technical feasibility for each option
- Identify potential implementation approaches

**Deliverables**:
- 2-4 solution options with high-level designs
- Feasibility assessment for each option
- Implementation approach outline per option
- Research findings and pattern references

**Templates**:
```
## Phase 2: Option Exploration

### Option 1: [Descriptive Name]
**Description**: [High-level solution approach]
**Key Technologies**: [Tech stack and components]
**Implementation Strategy**: [How it would be built]
**Feasibility Assessment**: [Technical viability rating]

### Option 2: [Descriptive Name]
**Description**: [High-level solution approach]
**Key Technologies**: [Tech stack and components]
**Implementation Strategy**: [How it would be built]
**Feasibility Assessment**: [Technical viability rating]

### Option 3: [Descriptive Name] (if applicable)
**Description**: [High-level solution approach]
**Key Technologies**: [Tech stack and components]
**Implementation Strategy**: [How it would be built]
**Feasibility Assessment**: [Technical viability rating]
```

### Phase 3: Trade-off Analysis (Evaluation)
**Purpose**: Systematically compare options against requirements and constraints
**Duration**: 30-40% of exploration time

**Activities**:
- Create evaluation matrix with weighted criteria
- Score each option against all criteria
- Document qualitative tradeoffs and risks
- Identify deal-breakers and show-stoppers

**Deliverables**:
- Tradeoff matrix with quantitative scoring
- Qualitative analysis of key tradeoffs
- Risk assessment per option
- Recommendation with rationale

**Templates**:
```
## Phase 3: Trade-off Analysis

### Evaluation Criteria
| Criteria | Weight | Option 1 | Option 2 | Option 3 |
|----------|--------|----------|----------|----------|
| **Technical Feasibility** | 25% | [Score] | [Score] | [Score] |
| **Development Cost** | 20% | [Score] | [Score] | [Score] |
| **Maintenance Complexity** | 15% | [Score] | [Score] | [Score] |
| **Performance Impact** | 15% | [Score] | [Score] | [Score] |
| **Security Considerations** | 10% | [Score] | [Score] | [Score] |
| **Scalability Potential** | 10% | [Score] | [Score] | [Score] |
| **User Experience** | 5% | [Score] | [Score] | [Score] |

### Qualitative Tradeoffs

#### Option 1 Advantages
- [Advantage 1]: [Detailed explanation]
- [Advantage 2]: [Detailed explanation]

#### Option 1 Disadvantages
- [Disadvantage 1]: [Detailed explanation]
- [Disadvantage 2]: [Detailed explanation]

#### Option 2 Advantages
- [Advantage 1]: [Detailed explanation]
- [Advantage 2]: [Detailed explanation]

#### Option 2 Disadvantages
- [Disadvantage 1]: [Detailed explanation]
- [Disadvantage 2]: [Detailed explanation]

### Risk Assessment
- **Option 1 Risks**: [High/Med/Low impact risks]
- **Option 2 Risks**: [High/Med/Low impact risks]
- **Option 3 Risks**: [High/Med/Low impact risks]

### Recommendation
**Recommended Option**: [Option X]
**Rationale**: [Why this option best meets requirements]
**Confidence Level**: [High/Med/Low]
```

### Phase 4: Decision Documentation (Recording)
**Purpose**: Formally document the chosen approach and implementation plan
**Duration**: 15-20% of exploration time

**Activities**:
- Document final decision with comprehensive rationale
- Create implementation roadmap and milestones
- Define success metrics and validation approach
- Document decision constraints and assumptions

**Deliverables**:
- Final decision document with complete rationale
- Implementation plan with phases and dependencies
- Validation approach and success criteria
- Decision constraints and change triggers

**Templates**:
```
## Phase 4: Decision Documentation

### Final Decision
**Chosen Option**: [Option X - Descriptive Name]
**Decision Date**: [YYYY-MM-DD]
**Decision Maker**: [Individual or group]

### Comprehensive Rationale
**Why This Option**:
- [Reason 1]: [Detailed explanation with evidence]
- [Reason 2]: [Detailed explanation with evidence]
- [Reason 3]: [Detailed explanation with evidence]

**Why Not Other Options**:
- **Option Y Rejected Because**: [Detailed explanation]
- **Option Z Rejected Because**: [Detailed explanation]

### Implementation Approach
**Phase 1**: [Description, duration, deliverables]
**Phase 2**: [Description, duration, deliverables]
**Phase 3**: [Description, duration, deliverables]

### Success Metrics
- **Quantitative**: [Measurable outcomes]
- **Qualitative**: [Quality and experience measures]
- **Validation Approach**: [How success will be verified]

### Decision Constraints
**Must be true for decision to remain valid**:
- [Constraint 1]: [Explanation]
- [Constraint 2]: [Explanation]
- [Constraint 3]: [Explanation]

**Change Triggers**:
- [Trigger 1]: [When to reconsider decision]
- [Trigger 2]: [When to reconsider decision]
```

### Phase 5: Decision Verification (Validation)
**Purpose**: Validate the decision against requirements and identify monitoring needs
**Duration**: 5-10% of exploration time

**Activities**:
- Verify decision meets all requirements from Phase 1
- Identify decision validation checkpoints
- Create monitoring plan for implementation
- Document decision reversal triggers

**Deliverables**:
- Requirements compliance matrix
- Implementation monitoring plan
- Decision validation checklist
- Reversal criteria and process

**Templates**:
```
## Phase 5: Decision Verification

### Requirements Compliance Matrix
| Requirement | Met? | Evidence | Notes |
|-------------|------|----------|-------|
| [Req 1] | ✅ | [Evidence] | [Notes] |
| [Req 2] | ✅ | [Evidence] | [Notes] |
| [Req 3] | ⚠️ | [Partial] | [Notes] |

### Implementation Monitoring
**Checkpoint 1**: [When, what to check, success criteria]
**Checkpoint 2**: [When, what to check, success criteria]
**Checkpoint 3**: [When, what to check, success criteria]

### Decision Validation Checklist
- [ ] Requirements fully met
- [ ] Tradeoffs acceptable to stakeholders
- [ ] Implementation plan feasible
- [ ] Risks identified and mitigated
- [ ] Success metrics defined and measurable

### Reversal Criteria
**Decision should be reconsidered if**:
- [Criterion 1]: [When and why]
- [Criterion 2]: [When and why]
- [Criterion 3]: [When and why]

**Reversal Process**:
1. [Step 1]: [What to do]
2. [Step 2]: [What to do]
3. [Step 3]: [What to do]
```

## Complexity-Based Application

### Level 1-2 Tasks (Brief Exploration)
- **Recommended Phases**: 1-4 (Phase 5 optional)
- **Depth**: High-level analysis, concise documentation
- **Duration**: Hours to 1-2 days
- **Deliverables**: Brief versions of all templates

### Level 3-4 Tasks (Full Exploration)
- **Required Phases**: All 5 phases mandatory
- **Depth**: Comprehensive analysis with detailed documentation
- **Duration**: Days to weeks depending on scope
- **Deliverables**: Complete versions of all templates

## Integration Points

### Task Lifecycle Integration
- Triggered during design-decision checkpoints
- Results documented in task plan
- Feeds into implementation planning

### Command Integration
- `/retrospect` can reference structured exploration outcomes
- Design decision templates used in exploration phases
- Results feed into `/learn` and `/evolve` processes

### Documentation Integration
- Results stored in `docs/explanation/decisions/`
- Links to problem statements and requirements
- Referenced in architectural documentation

## Quality Assurance

### Completeness Checks
- All 5 phases completed (for applicable complexity levels)
- All required deliverables produced
- Decision rationale comprehensive and evidence-based
- Tradeoffs systematically evaluated

### Stakeholder Validation
- Key stakeholders reviewed exploration process
- Decision communicated and acknowledged
- Implementation plan approved
- Monitoring plan agreed

## Common Pitfalls

### Premature Commitment
- Avoid deciding before completing all phases
- Don't skip trade-off analysis
- Ensure all options fairly evaluated

### Insufficient Research
- Research existing solutions and patterns
- Validate assumptions through prototyping
- Consult domain experts when needed

### Poor Documentation
- Document rationale comprehensively
- Include evidence for all claims
- Make tradeoffs explicit and quantitative

## Related
- `docs/reference/agentos/design-decision-templates.md` - Complexity-scaled templates
- `docs/reference/agentos/task-plan-spec.md` - Integration with task planning
- `docs/how-to/agentos/design-decision-structured-exploration.md` - Step-by-step guidance
- `docs/explanation/decisions/` - Where exploration results are stored