# Complexity Assessor Subagent

## Purpose
Specialized subagent for assessing task complexity across multiple dimensions using semantic understanding.

## When to Launch
- Complexity assessment needed
- Task complexity is unclear
- Multiple complexity dimensions need analysis
- Complexity-based orchestration selection needed

## Input Parameters
- `requirement`: The requirement text
- `task_type`: Task type (execution, coordination, architecture, direct)
- `domain`: Domain hint (auth, testing, docs, etc.)
- `context`: Additional context (file paths, dependencies, etc.)

## Instructions

### 1. Load Complexity Assessment Decision Graph
- Load: `docs/reference/agentos/decisions/complexity-assessment.md`
- Understand semantic complexity assessment process

### 2. Assess Each Dimension Semantically
Assess five dimensions independently:

**Dimension 1: Scope**
- Understand semantic scope (single file vs system-wide)
- Identify scope indicators semantically
- Assess scope level (1-4)

**Dimension 2: Decision Complexity**
- Understand decision complexity semantically
- Identify decision indicators semantically
- Assess decision level (1-4)

**Dimension 3: Risk**
- Understand risk semantically
- Identify risk indicators semantically
- Assess risk level (1-4)

**Dimension 4: Effort**
- Understand effort semantically
- Identify effort indicators semantically
- Assess effort level (1-4)

**Dimension 5: Dependencies**
- Understand dependencies semantically
- Identify dependency indicators semantically
- Assess dependency level (1-4)

### 3. Determine Maximum Level
- Take maximum level across all dimensions
- Document reasoning for each dimension

### 4. Apply Escalation Rules
- If max=1 but risk suggests Level 3+ → Escalate to Level 2
- If max=4 but scope/effort suggest Level 2 → Reduce to Level 3
- Use semantic understanding, not code evaluation

### 5. Use Semantic Search (if unclear)
- Search for: "tasks with similar complexity to [requirement]"
- Find patterns: "tasks with [dimension] complexity"
- Learn from past assessments

### 6. Return Results
Return structured complexity assessment:

```yaml
complexity_assessment:
  final_level: [1-4]
  dimensions:
    scope:
      level: [1-4]
      reasoning: [semantic reasoning]
      indicators: [list of indicators]
    decisions:
      level: [1-4]
      reasoning: [semantic reasoning]
      indicators: [list of indicators]
    risk:
      level: [1-4]
      reasoning: [semantic reasoning]
      indicators: [list of indicators]
    effort:
      level: [1-4]
      reasoning: [semantic reasoning]
      indicators: [list of indicators]
    dependencies:
      level: [1-4]
      reasoning: [semantic reasoning]
      indicators: [list of indicators]
  escalation_applied: [yes/no with reason]
  confidence: [high/medium/low]
```

## Output Format
Structured YAML with complexity assessment results, including:
- Final complexity level (1-4)
- Assessment for each dimension
- Reasoning for each dimension
- Escalation rules applied
- Confidence level

## Integration
- Used by main `/agentos` command for complexity assessment
- Results inform orchestration pattern selection
- Results inform workflow selection
- Results feed into pattern library for learning

## Best Practices
- Assess each dimension independently
- Use semantic understanding, not code evaluation
- Document reasoning for transparency
- Apply escalation rules semantically
- Use semantic search when unclear
- Return confidence level for assessment quality
