---
title: "Decision Record Format (ADR)"
status: stable
created_date: 2026-01-18
purpose: "Defines the required format for AgentOS decision records (ADRs) that document architectural and design decisions"
domain: agentos
---

# Decision Record Format (ADR) (Reference)

## Purpose
Provides a standardized format for documenting architectural and design decisions. ADRs ensure that decision rationale is preserved, alternatives are considered, and future changes can be made with full context.

## Scope
Applies to decisions that:
- Affect system architecture or design
- Have significant technical or business impact
- Involve multiple stakeholders or teams
- May need to be revisited or reversed in the future

## File Structure and Naming

### Location
```
docs/explanation/decisions/YYYY-MM-DD-<kebab-case-slug>.md
```

### Naming Convention
- **Date**: `YYYY-MM-DD` format
- **Slug**: Descriptive, kebab-case identifier
- **Examples**:
  - `2026-01-18-semantic-validation-mandate.md`
  - `2026-01-15-context-compass-implementation.md`
  - `2026-01-14-doe-integrated-flow.md`

## Required Frontmatter

```yaml
---
title: "Decision: [Short Title]"
status: proposed | accepted | superseded
created_date: YYYY-MM-DD
purpose: "[Brief description of decision impact]"
domain: agentos | [other domain]
type: policy | architecture | implementation | process
related:
  - docs/work/problems/[problem-id].md
  - docs/reference/[relevant-spec].md
implementations:
  - [path/to/implementation/file]
  - [path/to/another/implementation]
superseded_by: docs/explanation/decisions/[newer-adr].md  # if status: superseded
superseded_date: YYYY-MM-DD  # if status: superseded
superseded_reason: "[why this was superseded]"  # if status: superseded
---
```

## Required Sections

### 1. Context
**Purpose**: Explain the situation requiring the decision
**Content**:
- Business or technical problem being solved
- Current state and constraints
- Why a decision is needed now
- Impact of not making a decision

### 2. Problem
**Purpose**: Clearly state the problem being addressed
**Content**:
- Specific problem statement
- Current pain points or limitations
- Business or technical impact
- Evidence of the problem (metrics, incidents, feedback)

### 3. Decision
**Purpose**: State what was decided
**Content**:
- Clear statement of the chosen approach
- Specific implementation details
- Scope and boundaries of the decision
- Any constraints or limitations

### 4. Alternatives
**Purpose**: Document options that were considered
**Content**:
- List of alternatives evaluated (minimum 2-3)
- Brief description of each option
- Why each alternative was not chosen
- Any hybrids or compromises considered

### 5. Rationale
**Purpose**: Explain why this decision was made
**Content**:
- Detailed reasoning for the chosen approach
- Evidence supporting the decision
- Trade-offs that were made
- Assumptions and their validation

### 6. Consequences
**Purpose**: Describe expected outcomes and follow-up actions
**Content**:
- Positive consequences (benefits)
- Negative consequences (costs, risks)
- Required follow-up actions
- Metrics for measuring success

### 7. Why This Worked
**Purpose**: Reflect on decision quality and learning
**Content**:
- Evidence that the decision achieved its goals
- Unexpected outcomes (positive or negative)
- Lessons learned for future decisions
- Indicators that this was the right decision

### 8. Artifacts
**Purpose**: Link to all related implementation and documentation
**Content**:
- Code changes and implementations
- Documentation updates
- Tests and validation
- Related decisions or specifications

## Status Definitions

### Proposed
- Decision has been drafted but not yet ratified
- May still be under discussion or review
- Not yet implemented

### Accepted
- Decision has been approved and ratified
- Implementation is planned or in progress
- Decision is binding until superseded

### Superseded
- Decision has been replaced by a newer decision
- Original decision should no longer be followed
- Must link to superseding decision
- Implementation should migrate to new approach

## Decision Lifecycle

### Creation
1. Identify need for architectural decision
2. Draft ADR in proposed status
3. Gather input from stakeholders
4. Update status to accepted when approved

### Implementation
1. Update implementations field with actual code/docs
2. Track progress against consequences
3. Validate outcomes against rationale

### Evolution
1. Monitor for changing conditions
2. Create new ADR when decision needs revision
3. Update superseded fields when replacing old decisions
4. Ensure smooth transition for implementations

## Quality Criteria

### Completeness
- All required sections present and complete
- Evidence provided for claims
- Alternatives fairly evaluated
- Consequences realistically assessed

### Clarity
- Decision statement unambiguous
- Rationale clearly explained
- Trade-offs explicitly stated
- Implementation guidance specific

### Traceability
- Links to related problems and specifications
- Implementation artifacts identified
- Decision dependencies documented
- Evolution history maintained

## Integration Points

### Problem Registry
- ADRs link to problems they address
- Problem registry tracks ADR status
- Problems may spawn multiple ADRs

### Implementation Tracking
- `implementations:` field tracks code/docs changes
- Registry validation ensures links remain valid
- Implementation status can be audited

### Evolution System
- ADRs document system evolution
- Supersession chains track decision history
- Rationale preservation enables future changes

## Templates by Complexity

### Simple ADR Template
For straightforward decisions with clear trade-offs:

```markdown
---
title: "Decision: [Title]"
status: accepted
created_date: YYYY-MM-DD
purpose: "[Brief impact]"
domain: agentos
related:
  - docs/work/problems/[problem].md
implementations:
  - [implementation/path]
---

## Context
[Brief situation description]

## Decision
[Clear decision statement]

## Alternatives
- [Option 1]: [Why not chosen]
- [Option 2]: [Why not chosen]

## Rationale
[Why this decision, with evidence]

## Consequences
[Expected outcomes and follow-up actions]

## Artifacts
- [Code/docs changes]
```

### Complex ADR Template
For major architectural decisions:

```markdown
---
title: "Decision: [Title]"
status: accepted
created_date: YYYY-MM-DD
purpose: "[Detailed impact description]"
domain: agentos
type: architecture
related:
  - docs/work/problems/[problem].md
  - docs/reference/[spec].md
implementations:
  - [primary/implementation]
  - [secondary/implementation]
---

## Context
[Detailed situation and constraints]

## Problem
[Comprehensive problem statement with evidence]

## Decision
[Detailed decision with implementation specifics]

## Alternatives
- **[Option 1 Name]**: [Detailed description]
  - Pros: [Advantages]
  - Cons: [Disadvantages]
  - Why rejected: [Rationale]

- **[Option 2 Name]**: [Detailed description]
  - Pros: [Advantages]
  - Cons: [Disadvantages]
  - Why rejected: [Rationale]

## Rationale
[Comprehensive analysis with evidence, trade-offs, assumptions]

## Consequences
- **Positive**: [Benefits and opportunities]
- **Negative**: [Costs and risks]
- **Neutral**: [Implementation details]
- **Required Actions**: [Follow-up tasks with owners]

## Why This Worked
[Post-implementation reflection with evidence]

## Artifacts
- **Code Changes**: [Specific files and changes]
- **Documentation**: [Updated docs and guides]
- **Tests**: [New tests and validation]
- **Related Decisions**: [Other ADRs affected]
```

## Review and Approval Process

### Draft Review
- Author completes all sections
- Technical review by relevant experts
- Stakeholder input on business impact
- Update based on feedback

### Approval Criteria
- Problem clearly stated and evidenced
- Alternatives fairly evaluated
- Rationale supported by evidence
- Consequences realistically assessed
- Implementation feasible

### Approval Process
1. Technical review completed
2. Stakeholder review completed
3. Final updates incorporated
4. Status changed to `accepted`
5. Implementation begins

## Maintenance

### Regular Review
- Review ADRs annually or when major changes occur
- Update status if decision becomes obsolete
- Add evolution notes for significant changes

### Supersession Process
1. Create new ADR with improved approach
2. Update old ADR status to `superseded`
3. Add supersession metadata to old ADR
4. Ensure smooth transition for implementations

## Related
- `docs/reference/agentos/problem-registry.md` - Problem tracking system
- `docs/reference/agentos/traceability.md` - Decision change tracking
- `docs/explanation/decisions/` - Where ADRs are stored
- `docs/work/problems/` - Problems ADRs address