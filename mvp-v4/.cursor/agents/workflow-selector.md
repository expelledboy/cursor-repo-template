# Workflow Selector Subagent

## Purpose
Specialized subagent for selecting the appropriate workflow based on task type and complexity level using semantic understanding.

## When to Launch
- Workflow selection needed
- Task type and complexity are known
- Workflow selection is unclear
- Multiple workflow options need evaluation

## Input Parameters
- `task_type`: Task type (execution, coordination, architecture, direct)
- `complexity_level`: Complexity level (1-4)
- `domain`: Domain hint (auth, testing, docs, etc.)
- `patterns_found`: Optional patterns from pattern discovery

## Instructions

### 1. Load Workflow Selection Decision Graph
- Load: `docs/reference/agentos/decisions/workflow-selection.md`
- Understand semantic workflow selection process

### 2. Understand Task Type Semantically
- What does the task type mean? (execution = implementation, coordination = alignment, etc.)
- What are the semantic implications?
- What workflow types are available for this task type?

### 3. Understand Complexity Semantically
- What does the complexity level mean? (1 = minimal, 4 = maximum)
- What are the semantic implications?
- What workflow variations are available for this complexity?

### 4. Match Combination Semantically
Match task type + complexity → workflow:
- Execution + Level 1 → `execution-minimal`
- Execution + Level 2 → `execution-standard`
- Execution + Level 3 → `execution-enhanced`
- Execution + Level 4 → `execution-maximum`
- Coordination + Level 1-2 → `coordination-standard`
- Coordination + Level 3-4 → `coordination-enhanced`
- Architecture + Level 1-2 → `architecture-standard`
- Architecture + Level 3-4 → `architecture-enhanced`
- Direct + All Levels → `direct-minimal`

### 5. Use Semantic Search (if unclear)
- Search for: "workflows for [task_type] tasks at [complexity] level"
- Find similar workflow selections
- Learn from past matches

### 6. Consider Patterns (if available)
- Review patterns found from pattern discovery
- Check if patterns suggest specific workflows
- Use pattern workflows if highly similar

### 7. Return Results
Return structured workflow selection:

```yaml
workflow_selection:
  selected_workflow: [workflow name]
  task_type: [execution/coordination/architecture/direct]
  complexity_level: [1-4]
  workflow_path: [path to workflow documentation]
  reasoning: [semantic reasoning for selection]
  alternatives_considered: [list of alternatives]
  pattern_influence: [how patterns influenced selection]
  confidence: [high/medium/low]
```

## Output Format
Structured YAML with workflow selection results, including:
- Selected workflow name
- Task type and complexity level
- Path to workflow documentation
- Reasoning for selection
- Alternatives considered
- Pattern influence
- Confidence level

## Integration
- Used by main `/agentos` command for workflow selection
- Results inform workflow loading
- Results feed into pattern library for learning
- Results used by execution workflows

## Best Practices
- Match semantically, not just by values
- Consider patterns when available
- Document reasoning for transparency
- Use semantic search when unclear
- Return confidence level for selection quality
