# AgentOS MVP-v4: Accelerated Synergy System

**Status**: Initial Implementation
**Date**: 2026-01-14

Accelerated synergy system that maximizes Cursor feature interplay through subagent orchestration, command workflows, cascading rules, parallel pattern discovery, and meta-orchestration.

---

## Key Features

1. **Subagent Orchestration**: Commands launch specialized subagents in parallel for pattern discovery, code analysis, and validation
2. **Command Workflows**: Multiple commands form structured workflows that chain together, each orchestrating feature interplay
3. **Cascading Rules**: Rules explicitly trigger other rules, creating cascading context enrichment
4. **Parallel Pattern Discovery**: Multiple semantic searches run simultaneously via subagents
5. **Active File Context**: File context actively shapes behavior through globs rules and domain inference
6. **Meta-Orchestration**: System orchestrates its own feature usage based on task complexity and context
7. **Pattern Library**: Learned patterns become reusable rule components (Level 3+)

---

## Quick Start

### 1. Setup

```bash
# Copy Cursor configuration
cp -r mvp-v4/.cursor .cursor

# Or create symlink
ln -s mvp-v4/.cursor .cursor
```

### 2. Use

In Cursor chat:

```
/agentos
I want to add user authentication with OAuth
```

The system will:
- Orchestrate subagents in parallel for pattern discovery
- Cascade rules for exponential context enrichment
- Use semantic search across multiple dimensions
- Adapt orchestration to task complexity
- Learn patterns for future reuse (Level 3+)

---

## Structure

```
mvp-v4/
├── .cursor/
│   ├── rules/
│   │   ├── core.mdc                    # Meta-orchestration core
│   │   ├── orchestration.mdc           # Feature orchestration patterns
│   │   ├── domains/                    # Domain rules (description + globs)
│   │   │   ├── auth.mdc
│   │   │   ├── testing.mdc
│   │   │   └── docs.mdc
│   │   └── patterns/                   # Learned pattern library
│   │       └── pattern-library.mdc
│   ├── commands/
│   │   ├── agentos.md                  # Main orchestrator command
│   │   ├── agentos-start.md            # Task lifecycle: start
│   │   ├── agentos-plan.md             # Task lifecycle: plan
│   │   ├── agentos-execute.md          # Task lifecycle: execute
│   │   ├── agentos-verify.md           # Task lifecycle: verify
│   │   └── agentos-complete.md         # Task lifecycle: complete
│   └── agents/                         # Subagent definitions
│       ├── pattern-searcher.md         # Semantic pattern discovery
│       ├── code-pattern-searcher.md    # Code pattern discovery
│       ├── doc-pattern-searcher.md     # Documentation pattern discovery
│       ├── complexity-assessor.md      # Complexity assessment specialist
│       ├── workflow-selector.md        # Workflow selection specialist
│       └── validator.md                # Validation specialist
├── docs/
│   └── reference/
│       └── agentos/
│           ├── core-contract.md        # Core invariants
│           ├── synergy-patterns.md     # Feature synergy patterns
│           ├── meta-orchestration.md   # Self-orchestration system
│           ├── decisions/              # Semantic decision graphs
│           │   ├── task-classification.md
│           │   ├── complexity-assessment.md
│           │   └── workflow-selection.md
│           └── workflows/              # Workflow definitions
│               ├── execution-minimal.md
│               ├── execution-standard.md
│               ├── execution-enhanced.md
│               └── execution-maximum.md
├── schemas/
│   ├── requirement.yaml
│   ├── plan.yaml
│   └── pattern.yaml                    # Pattern library schema
└── scripts/
    └── agentos/
        └── mcp_server.py               # MCP server with pattern library support
```

---

## Differences from MVP-v3

| Aspect | MVP-v3 | MVP-v4 |
|--------|--------|--------|
| **Subagents** | Not integrated | Central orchestration mechanism |
| **Commands** | Single entry point | Multiple commands with workflows |
| **Rules** | Layered (alwaysApply + description + globs) | Cascading (rules trigger rules) |
| **Semantic Search** | Sequential | Parallel via subagents |
| **Pattern Library** | Not present | Learned patterns become reusable |
| **Meta-Orchestration** | Not present | System orchestrates its own feature usage |
| **Complexity Adaptation** | Basic | Complexity-based orchestration selection |
| **Feature Synergy** | Basic interplay | Maximum synergy with all features |

---

## How It Works

### Feature Orchestration Flow

1. **Requirement Intake**: Natural language or structured YAML
2. **Complexity Assessment**: Determine complexity level (1-4)
3. **Orchestration Selection**: Select orchestration pattern based on complexity
4. **Parallel Pattern Discovery**: Launch subagents in parallel (Level 2+)
5. **Cascading Rules**: Rules trigger other rules for context enrichment
6. **Semantic Routing**: Match patterns to workflow types
7. **Multi-Layer Validation**: Semantic + MCP + subagent validation
8. **Pattern Learning**: Learn patterns for future reuse (Level 3+)

### Feature Synergy Patterns

- **Parallel Pattern Discovery**: Commands × Subagents × Semantic Search (3x faster)
- **Cascading Rule Enrichment**: Rules × Rules × File Context (Exponential)
- **Command Workflow Chaining**: Commands × Commands × Rules (Structured workflows)
- **Two-Layer Validation**: Commands × MCP × Subagents (Multi-layer validation)
- **Context-Aware Orchestration**: File Context × Rules × Commands × Subagents (Context-aware)
- **Meta-Orchestration**: Complexity × Orchestration Pattern × All Features (Self-optimizing)

---

## Complexity-Based Orchestration

### Level 1: Streamlined
- Basic rule layering
- Skip subagents
- Minimal semantic search
- Basic MCP validation

### Level 2: Standard
- Full rule layering
- 2-3 subagents in parallel
- Standard semantic search
- Standard MCP validation

### Level 3: Enhanced
- Cascading rules
- 3+ subagents in parallel
- Multiple semantic searches
- Comprehensive MCP validation
- Pattern library consultation

### Level 4: Maximum
- Full cascading rules
- All relevant subagents in parallel
- Multi-dimensional semantic search
- Multi-layer validation
- Pattern library learning and reuse

---

## Documentation

- `docs/reference/agentos/core-contract.md` - Core invariants
- `docs/reference/agentos/meta-orchestration.md` - Meta-orchestration system
- `docs/reference/agentos/synergy-patterns.md` - Feature synergy patterns
- `docs/reference/agentos/decisions/` - Semantic decision graphs
- `docs/reference/agentos/workflows/` - Workflow definitions

---

## Dependencies

For MCP server:
```bash
pip install pyyaml jsonschema
```

For Cursor:
- Cursor IDE with MCP support
- `.cursor/` directory configured

---

## Next Steps

1. Test subagent orchestration with parallel launches
2. Test command workflow chaining
3. Test cascading rule triggers
4. Test parallel semantic search
5. Test pattern library learning and reuse (Level 3+)
6. Test meta-orchestration pattern selection
7. Test all features working together

---

## Success Criteria

1. **Subagent Integration**: Commands launch subagents in parallel for pattern discovery
2. **Command Workflows**: Multiple commands chain together with feature orchestration
3. **Cascading Rules**: Rules trigger other rules for exponential context enrichment
4. **Parallel Search**: Multiple semantic searches run simultaneously via subagents
5. **Pattern Library**: Learned patterns become reusable rule components (Level 3+)
6. **Meta-Orchestration**: System selects orchestration patterns based on complexity
7. **Feature Synergy**: All features work together for maximum power
