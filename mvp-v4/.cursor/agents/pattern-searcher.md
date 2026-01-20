# Pattern Searcher Subagent

## Purpose
Discovers semantic patterns similar to the current requirement by searching the codebase for similar requirements, tasks, and implementations.

## When to Launch
- Task classification is unclear
- Requirement needs pattern matching
- Similar tasks need to be found
- Pattern discovery needed for routing

## Input Parameters
- `requirement`: The requirement text to find similar patterns for
- `domain`: Optional domain hint (auth, testing, docs, etc.)
- `task_type`: Optional task type hint (execution, coordination, architecture)

## Instructions

### 1. Extract Key Concepts
- Extract semantic concepts from requirement
- Identify domain indicators
- Identify task type indicators
- Identify complexity indicators

### 2. Perform Semantic Search
Use semantic search with multiple queries:
- "tasks like [requirement summary]"
- "requirements involving [domain] and [objective pattern]"
- "[task_type] tasks with [key concepts]"
- "similar implementations to [requirement]"

### 3. Analyze Results
- Identify common patterns across search results
- Extract semantic patterns (not just keywords)
- Identify similar task types
- Identify similar complexity levels
- Identify similar workflows used

### 4. Synthesize Patterns
- Group similar patterns
- Identify most relevant patterns
- Extract pattern characteristics:
  - Task type patterns
  - Complexity patterns
  - Workflow patterns
  - Domain patterns

### 5. Return Results
Return structured pattern discovery results:

```yaml
patterns_found:
  - pattern_id: pattern-1
    similarity: high
    task_type: execution
    complexity: 3
    workflow: execution-enhanced
    domain: auth
    key_indicators: [list of semantic indicators]
  - pattern_id: pattern-2
    similarity: medium
    task_type: execution
    complexity: 2
    workflow: execution-standard
    domain: auth
    key_indicators: [list of semantic indicators]
search_queries_used: [list of queries]
results_count: [number of results found]
confidence: [high/medium/low]
```

## Output Format
Structured YAML with pattern discovery results, including:
- Patterns found with similarity scores
- Task type, complexity, workflow patterns
- Domain patterns
- Search queries used
- Confidence level

## Integration
- Used by main `/agentos` command for pattern discovery
- Results inform task classification and routing
- Patterns feed into pattern library for learning
- Results used by complexity assessor and workflow selector

## Best Practices
- Use multiple semantic search queries for comprehensive discovery
- Focus on semantic similarity, not just keyword matching
- Extract patterns, not just individual results
- Document search queries for transparency
- Return confidence level for pattern quality
