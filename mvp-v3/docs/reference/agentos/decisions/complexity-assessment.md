# Complexity Assessment (Semantic)

**Purpose**: Determine task complexity level (1-4) using semantic understanding of multiple dimensions.

**Status**: Stable
**Date**: 2026-01-14

---

## How I Assess Complexity

I understand complexity semantically by analyzing the meaning of scope, decisions, risk, effort, and dependencies. I don't evaluate code expressions - I understand the semantic implications.

---

## Assessment Dimensions

### Dimension 1: Scope

**Level 1 (Minimal)**:
- Single component or file
- Isolated change
- No cross-module impact
- Semantic indicators: "single file", "one component", "isolated"

**Level 2 (Standard)**:
- Multiple related components
- Limited dependencies
- Contained impact
- Semantic indicators: "few files", "related components", "contained"

**Level 3 (Enhanced)**:
- System-wide changes
- Multiple dependencies
- Cross-module impact
- Semantic indicators: "system-wide", "multiple modules", "cross-cutting"

**Level 4 (Maximum)**:
- Cross-system impact
- Enterprise-wide changes
- Mission-critical
- Semantic indicators: "enterprise", "critical", "cross-system", "infrastructure"

**When Unclear**: Use semantic search for "tasks affecting [scope description]"

---

### Dimension 2: Decision Complexity

**Level 1 (Obvious)**:
- No tradeoffs needed
- Straightforward approach
- Semantic indicators: "obvious", "straightforward", "clear approach"

**Level 2 (Simple)**:
- Few options
- Clear best choice
- Semantic indicators: "few options", "clear choice"

**Level 3 (Complex)**:
- Multiple viable options
- Tradeoffs required
- Analysis needed
- Semantic indicators: "multiple options", "tradeoffs", "analysis", "design decision"

**Level 4 (Strategic)**:
- Strategic decisions
- Policy implications
- Long-term impact
- Semantic indicators: "strategic", "policy", "long-term", "architectural decision"

**When Unclear**: Use semantic search for "tasks requiring [decision type] decisions"

---

### Dimension 3: Risk

**Level 1 (Low)**:
- Easily reversible
- Isolated impact
- Semantic indicators: "low risk", "reversible", "isolated", "safe"

**Level 2 (Moderate)**:
- Some impact
- Manageable consequences
- Semantic indicators: "moderate risk", "some impact", "manageable"

**Level 3 (High)**:
- Significant impact
- Requires careful handling
- Semantic indicators: "high risk", "significant impact", "careful", "security"

**Level 4 (Critical)**:
- Mission-critical impact
- Failure unacceptable
- Semantic indicators: "critical", "mission-critical", "failure unacceptable", "production"

**When Unclear**: Use semantic search for "tasks with [risk level] risk in [domain]"

---

### Dimension 4: Effort

**Level 1 (Minutes to Hours)**:
- Quick implementation
- Semantic indicators: "quick", "minutes", "hours", "small"

**Level 2 (Hours to Days)**:
- Standard implementation
- Semantic indicators: "standard", "days", "moderate effort"

**Level 3 (Days to Weeks)**:
- Comprehensive implementation
- Semantic indicators: "comprehensive", "weeks", "substantial"

**Level 4 (Weeks to Months)**:
- Enterprise implementation
- Semantic indicators: "enterprise", "months", "large", "extensive"

**When Unclear**: Use semantic search for "tasks taking [time estimate]"

---

### Dimension 5: Dependencies

**Level 1 (Independent)**:
- Standalone
- No coordination needed
- Semantic indicators: "independent", "standalone", "no dependencies"

**Level 2 (Few Dependencies)**:
- Simple coordination
- Semantic indicators: "few dependencies", "simple coordination"

**Level 3 (Many Dependencies)**:
- Complex coordination
- Semantic indicators: "many dependencies", "complex coordination", "multiple teams"

**Level 4 (Critical Dependencies)**:
- Cross-team coordination
- Critical dependencies
- Semantic indicators: "critical dependencies", "cross-team", "enterprise coordination"

**When Unclear**: Use semantic search for "tasks with [dependency description]"

---

## Assessment Process

1. **Understand each dimension semantically**
   - Read requirement for meaning
   - Identify semantic indicators for each dimension
   - Understand implications, not just keywords

2. **Take maximum level across dimensions**
   - Assess each dimension independently
   - Take the highest level found
   - Document reasoning for each dimension

3. **Apply escalation rules semantically**
   - If max=1 but risk indicators suggest Level 3+ → Escalate to Level 2
   - If max=4 but scope/effort indicators suggest Level 2 → Reduce to Level 3
   - Use semantic understanding, not code evaluation

4. **Use semantic search when unclear**
   - Search for similar complexity assessments
   - Find patterns: "tasks with similar [dimension] complexity"
   - Learn from past assessments

---

## Workflow Variations by Level

### Level 1: Minimal Rigor
- Skip optional steps
- Brief documentation
- Basic validation
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
- Scope: 1 (single file)
- Decisions: 1 (obvious fix)
- Risk: 1 (low risk)
- Effort: 1 (minutes)
- Dependencies: 1 (none)
- **Result**: Level 1 (minimal rigor)

**Example 2**: "Add user authentication with OAuth"
- Scope: 3 (system-wide, affects multiple components)
- Decisions: 2 (OAuth provider choice)
- Risk: 3 (security-sensitive)
- Effort: 3 (days to weeks)
- Dependencies: 2 (OAuth provider, environment setup)
- **Result**: Level 3 (enhanced rigor, escalated by risk)

**Example 3**: "Refactor entire authentication system"
- Scope: 4 (system-wide, enterprise impact)
- Decisions: 4 (strategic architectural decisions)
- Risk: 4 (critical, production system)
- Effort: 4 (weeks to months)
- Dependencies: 4 (cross-team coordination)
- **Result**: Level 4 (maximum rigor)

---

## Integration with Task Classification

Complexity assessment happens **after** task classification:
1. Classify task type semantically (Execution, Coordination, Architecture, Direct)
2. Assess complexity level semantically (1-4)
3. Select appropriate workflow variation
4. Load complexity-appropriate directives
