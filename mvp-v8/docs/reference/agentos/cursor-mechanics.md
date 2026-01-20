---
title: "Cursor Mechanics Specification"
status: stable
created_date: 2026-01-17
purpose: "Reference specification for Cursor mechanics constraints and their operationalization"
domain: docs
related:
  - docs/explanation/agentos/design-rationale.md
---

# Cursor Mechanics Specification

## Overview

This guide shows how to operationalize [Cursor mechanics constraints](docs/reference/docs/glossary.md#cursor-mechanics-constraints) using Cursor's native features. The mechanics define how Cursor features affect reasoning and documentation provenance - this guide provides practical implementation using Rules, Commands, Mentions, Semantic Search, and MCP.

## 1. Rules: Persistent Instruction Injectors

### Core Constraint
"Rules are persistent instruction injectors. They can introduce documentation context; therefore traces MUST record provenance + anchors to rule files."

### Implementation Strategy

#### Project Rules (.cursor/rules/*.mdc)
```
# File patterns: docs/**/*.md
## Documentation Mechanics Enforcement
- When introducing documentation, record rule provenance
- Use @file references to anchor rule sources
- Tag rule injections as `rule_injected` in traces

# File patterns: src/**/*.py,src/**/*.js,src/**/*.ts
## Code Mechanics Enforcement
- Record rule anchors when rules influence code decisions
- Maintain provenance chain from rule → decision → implementation
- Use decision traces for complex rule applications

@file docs/explanation/agentos/design-rationale.md
@file docs/reference/agentos/cursor-mechanics.md
```

#### Global Rules (Cursor Settings)
```
# Cursor Mechanics - Global Constraints
- Always record rule provenance when rules introduce documentation
- Use trace anchors for rule-injected content
- Tag rule applications as `rule_sourced` in decision logs
- Maintain bidirectional traceability between rules and decisions
```

### Provenance Tracking
- **Rule Injection Recording**: When rules introduce content, record: `rule_file.mdc:line_number`
- **Anchor Format**: `rule_anchor: {file: "rules/mechanics.mdc", line: 15, type: "injection"}`
- **Trace Integration**: Include rule anchors in decision traces

## 2. Commands: Deterministic Entrypoints

### Core Constraint
"Commands are deterministic entrypoints. Use them for trace display and state navigation (`/trace`, `/checkpoint`, `/resume`, `/branch`)."

### Command Integration

#### Trace Commands
```
/trace view
/trace export
/trace compare HEAD~1
/trace anchor-rule rules/mechanics.mdc:15
```

#### State Navigation Commands
```
/checkpoint "Mechanics integration analysis"
/resume checkpoint-2026-01-17-001
/branch "mechanics-implementation" "Implementing Cursor mechanics constraints"
```

#### Command Usage Patterns
- **State Management**: Use `/checkpoint` before major mechanics changes
- **Trace Recording**: Use `/trace` to document mechanics applications
- **Branching**: Use `/branch` for experimental mechanics implementations

### Command Evidence Anchoring
Commands produce deterministic evidence:
- **Command Anchor**: `{command: "/trace view", timestamp: "2026-01-17T10:30:00Z", output_hash: "abc123"}`
- **State Anchor**: `{checkpoint: "mechanics-analysis", frame_count: 5, focus: "integration-guide"}`

## 3. Mentions: Explicit Injections

### Core Constraint
"Mentions are explicit injections. Manual context insertions that don't fit the current chain default to a new branch."

### Mention Strategy

#### Context Injection Patterns
```
@docs/explanation/agentos/design-rationale.md
@docs/reference/agentos/cursor-mechanics.md
@docs/reference/agentos/spec-active-state.md
```

#### Explicit Injection Rules
- **Chain Fitting**: If mention fits current decision chain, integrate it
- **Branch Creation**: If mention doesn't fit, create new branch automatically
- **Injection Recording**: Tag as `mention_injected` with anchor: `{type: "mention", file: "path.md", line: 42}`

### Mention Integration Workflow
1. **Pre-Injection Assessment**: Evaluate if mention fits current chain
2. **Chain Integration**: If fits, integrate with existing trace
3. **Branch Creation**: If doesn't fit, `/branch "mention-{timestamp}" "Mention injection"`
4. **Evidence Anchoring**: Record mention anchor in trace

## 4. Semantic Search: Candidate Suggestions

### Core Constraint
"Semantic search suggests candidates but is not authoritative; record search anchors and tag provenance as `search_suggested`."

### Search Integration

#### Provenance Tracking
```
Search Query: "decision trace mechanics"
Results: 3 candidates
- docs/reference/agentos/spec-active-state.md (confidence: 0.89)
- docs/explanation/decisions/2026-01-16-restructuring-process-design.md (confidence: 0.76)
- docs/explanation/agentos/design-rationale.md (confidence: 0.64)

Selected: docs/reference/agentos/spec-active-state.md
Anchor: {type: "semantic_search", query: "decision trace mechanics", selected_file: "spec-active-state.md", confidence: 0.89, provenance: "search_suggested"}
```

#### Search Evidence Recording
- **Query Anchoring**: Record full search query and parameters
- **Result Ranking**: Include confidence scores for all candidates
- **Selection Rationale**: Document why specific result was chosen
- **Provenance Tagging**: Always tag as `search_suggested` to distinguish from authoritative sources

### Search Validation Framework
- **Confidence Thresholds**: Only suggest results above 0.7 confidence
- **Multiple Candidates**: Present top 3-5 results for user selection
- **Fallback Strategy**: If no high-confidence results, suggest manual search

## 5. Tools/MCP: Evidence Production

### Core Constraint
"Tools/MCP produce evidence; record tool anchors (command + hash/excerpt) and tie them to decisions via `anchors_used`."

### MCP Server Integration

#### Evidence Anchoring Format
```
Tool Execution: mcp-server-db.query
Command: "SELECT * FROM decision_traces WHERE date > '2026-01-15'"
Output Hash: "def456"
Excerpt: "Found 12 traces with mechanics applications"
Anchor: {tool: "mcp-db", command_hash: "cmd789", output_hash: "def456", excerpt: "12 traces found", anchors_used: ["trace-001", "trace-002"]}
```

#### MCP Evidence Workflow
1. **Tool Execution**: Run MCP server operations
2. **Output Capture**: Hash full output, extract relevant excerpts
3. **Anchor Creation**: Create tool anchor with command and output references
4. **Decision Integration**: Tie anchors to specific decisions via `anchors_used` field

### Tool Evidence Categories
- **Database Evidence**: Query results from project databases
- **API Evidence**: External API responses and data
- **File System Evidence**: Directory structures, file metadata
- **External Service Evidence**: Web service responses, cloud resource data

## Integration Workflow

### Complete Mechanics Application
1. **Setup Rules**: Configure project rules for mechanics enforcement
2. **Establish State**: `/checkpoint "mechanics-integration-start"`
3. **Search Context**: Use semantic search to find relevant mechanics docs
4. **Inject Evidence**: @ mention key documents for explicit context
5. **Execute Tools**: Run MCP servers to gather additional evidence
6. **Record Decisions**: Use `/trace` to document mechanics applications
7. **Branch as Needed**: Use `/branch` for complex integrations
8. **Validate Integration**: Check all anchors and provenance recorded

### Quality Assurance
- **Anchor Completeness**: Every decision references its evidence sources
- **Provenance Clarity**: Clear distinction between rule-injected, mention-injected, search-suggested, and tool-evidence
- **Trace Integrity**: Decision traces maintain complete provenance chains
- **State Consistency**: Checkpoints enable resumable workflows
- **Integration Quality**: Mechanics constraints properly enforced across all features
