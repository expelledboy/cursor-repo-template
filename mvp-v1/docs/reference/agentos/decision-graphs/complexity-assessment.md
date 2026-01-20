# Complexity Assessment Decision Graph

**Purpose**: Determine task complexity level (1-4) using multi-dimensional analysis.

**Status**: Initial Version
**Date**: 2026-01-14

---

## Assessment Dimensions

Evaluate each dimension independently, then take the maximum level.

### Dimension 1: Scope
- **Level 1**: Single component, isolated change, no dependencies
- **Level 2**: Multiple components, limited dependencies, contained impact
- **Level 3**: System-wide, multiple dependencies, cross-module impact
- **Level 4**: Cross-system, enterprise impact, mission-critical

### Dimension 2: Decision Complexity
- **Level 1**: Obvious solution, no tradeoffs, straightforward approach
- **Level 2**: Simple decisions, few options, clear best choice
- **Level 3**: Complex tradeoffs, multiple viable options, requires analysis
- **Level 4**: Strategic decisions, policy implications, long-term impact

### Dimension 3: Risk
- **Level 1**: Low risk, easily reversible, isolated impact
- **Level 2**: Moderate risk, some impact, manageable consequences
- **Level 3**: High risk, significant impact, requires careful handling
- **Level 4**: Critical risk, mission-critical impact, failure unacceptable

### Dimension 4: Effort
- **Level 1**: Minutes to hours, quick implementation
- **Level 2**: Hours to days, standard implementation
- **Level 3**: Days to weeks, comprehensive implementation
- **Level 4**: Weeks to months, enterprise implementation

### Dimension 5: Dependencies
- **Level 1**: Independent, standalone, no coordination needed
- **Level 2**: Few dependencies, simple coordination
- **Level 3**: Many dependencies, complex coordination
- **Level 4**: Critical dependencies, cross-team coordination

---

## Decision Process

1. **Assess each dimension** independently based on task description
2. **Take maximum level** across all dimensions
3. **Apply escalation rules**:
   - If max=1 but risk≥3 → Escalate to Level 2
   - If max=4 but scope≤2 and effort≤2 → Reduce to Level 3
4. **Return final complexity level** with brief rationale

---

## Workflow Variations by Level

### Level 1: Minimal Rigor
- Skip optional steps
- Brief documentation
- Basic verification
- Quick execution

### Level 2: Standard Rigor
- All steps required (can be brief)
- Standard documentation
- Standard verification gates
- Planned execution

### Level 3: Enhanced Rigor
- Comprehensive planning
- Detailed documentation
- Comprehensive verification
- Systematic execution with checkpoints

### Level 4: Maximum Rigor
- Formal planning and reviews
- Enterprise documentation
- Extensive verification
- Phased execution with stakeholder alignment

---

## Examples

**Example 1**: "Fix typo in README"
- Scope: 1, Decisions: 1, Risk: 1, Effort: 1, Dependencies: 1
- **Result**: Level 1 (minimal rigor)

**Example 2**: "Add user authentication"
- Scope: 3, Decisions: 2, Risk: 3, Effort: 3, Dependencies: 2
- **Result**: Level 3 (enhanced rigor)

**Example 3**: "Refactor authentication module"
- Scope: 2, Decisions: 3, Risk: 3, Effort: 2, Dependencies: 2
- **Result**: Level 3 (enhanced rigor, escalated by risk)

---

## Integration with Task Classification

Complexity assessment happens **after** task classification:
1. Classify task type (Execution, Coordination, Architecture, Direct)
2. Assess complexity level (1-4)
3. Select appropriate workflow variation
4. Load complexity-appropriate directives
