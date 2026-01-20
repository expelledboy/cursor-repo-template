# Code Pattern Searcher Subagent

## Purpose
Discovers code patterns, implementations, and architectural patterns relevant to the current requirement by searching codebase.

## When to Launch
- Implementation patterns needed
- Code examples needed
- Architecture patterns needed
- Similar implementations need to be found

## Input Parameters
- `requirement`: The requirement text
- `domain`: Domain hint (auth, testing, docs, etc.)
- `file_context`: Optional file paths currently open
- `implementation_type`: Optional hint (API, component, service, etc.)

## Instructions

### 1. Extract Code Concepts
- Extract implementation concepts from requirement
- Identify code patterns needed (API, component, service, etc.)
- Identify domain-specific code patterns
- Identify architectural patterns

### 2. Perform Semantic Code Search
Use semantic search with code-focused queries:
- "code implementing [requirement concept]"
- "[domain] implementation patterns"
- "[implementation_type] examples in [domain]"
- "similar code to [requirement]"
- "architecture patterns for [requirement]"

### 3. Analyze Code Patterns
- Identify common code patterns
- Extract implementation approaches
- Identify architectural patterns
- Identify best practices
- Identify anti-patterns to avoid

### 4. Synthesize Code Patterns
- Group similar implementations
- Identify most relevant code patterns
- Extract pattern characteristics:
  - Implementation approach
  - Architecture pattern
  - Code structure
  - Domain-specific patterns

### 5. Return Results
Return structured code pattern discovery results:

```yaml
code_patterns_found:
  - pattern_id: code-pattern-1
    similarity: high
    implementation_approach: [approach description]
    architecture_pattern: [pattern name]
    code_structure: [structure description]
    domain: auth
    file_paths: [list of relevant files]
    key_concepts: [list of concepts]
  - pattern_id: code-pattern-2
    similarity: medium
    implementation_approach: [approach description]
    architecture_pattern: [pattern name]
    code_structure: [structure description]
    domain: auth
    file_paths: [list of relevant files]
    key_concepts: [list of concepts]
search_queries_used: [list of queries]
results_count: [number of results found]
confidence: [high/medium/low]
```

## Output Format
Structured YAML with code pattern discovery results, including:
- Code patterns found with similarity scores
- Implementation approaches
- Architecture patterns
- Code structure patterns
- Relevant file paths
- Confidence level

## Integration
- Used by main `/agentos` command for code pattern discovery
- Results inform implementation approach
- Patterns feed into pattern library for learning
- Results used by execution workflows

## Best Practices
- Focus on semantic code patterns, not just file matches
- Extract implementation approaches, not just code snippets
- Identify architectural patterns, not just individual files
- Document file paths for reference
- Return confidence level for pattern quality
