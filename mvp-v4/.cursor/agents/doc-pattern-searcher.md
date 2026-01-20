# Documentation Pattern Searcher Subagent

## Purpose
Discovers documentation patterns, guides, and reference materials relevant to the current requirement by searching documentation.

## When to Launch
- Documentation patterns needed
- Reference materials needed
- Similar documentation needs to be found
- Documentation structure needs to be understood

## Input Parameters
- `requirement`: The requirement text
- `domain`: Domain hint (auth, testing, docs, etc.)
- `doc_type`: Optional hint (reference, how-to, explanation, tutorial)

## Instructions

### 1. Extract Documentation Concepts
- Extract documentation concepts from requirement
- Identify documentation types needed (reference, how-to, explanation)
- Identify domain-specific documentation patterns
- Identify documentation structure patterns

### 2. Perform Semantic Documentation Search
Use semantic search with documentation-focused queries:
- "documentation for [requirement concept]"
- "[domain] documentation patterns"
- "[doc_type] guides for [requirement]"
- "similar documentation to [requirement]"
- "documentation structure for [requirement]"

### 3. Analyze Documentation Patterns
- Identify common documentation patterns
- Extract documentation structures
- Identify documentation best practices
- Identify documentation anti-patterns

### 4. Synthesize Documentation Patterns
- Group similar documentation
- Identify most relevant documentation patterns
- Extract pattern characteristics:
  - Documentation structure
  - Documentation type
  - Domain-specific patterns
  - Reference patterns

### 5. Return Results
Return structured documentation pattern discovery results:

```yaml
doc_patterns_found:
  - pattern_id: doc-pattern-1
    similarity: high
    doc_type: reference
    doc_structure: [structure description]
    domain: auth
    doc_paths: [list of relevant docs]
    key_concepts: [list of concepts]
  - pattern_id: doc-pattern-2
    similarity: medium
    doc_type: how-to
    doc_structure: [structure description]
    domain: auth
    doc_paths: [list of relevant docs]
    key_concepts: [list of concepts]
search_queries_used: [list of queries]
results_count: [number of results found]
confidence: [high/medium/low]
```

## Output Format
Structured YAML with documentation pattern discovery results, including:
- Documentation patterns found with similarity scores
- Documentation types
- Documentation structures
- Relevant documentation paths
- Confidence level

## Integration
- Used by main `/agentos` command for documentation pattern discovery
- Results inform documentation approach
- Patterns feed into pattern library for learning
- Results used by documentation workflows

## Best Practices
- Focus on semantic documentation patterns, not just file matches
- Extract documentation structures, not just individual docs
- Identify documentation best practices
- Document doc paths for reference
- Return confidence level for pattern quality
