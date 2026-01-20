# AgentOS MVP-v3: Meta Semantic System

**Status**: Initial Implementation
**Date**: 2026-01-14

Self-describing semantic system that leverages Cursor's full feature interplay for intelligent requirement understanding and routing.

---

## Key Features

1. **Semantic Understanding**: Requirements understood by meaning, not syntax
2. **Feature Interplay**: Rules (alwaysApply + description + globs) work together
3. **Self-Description**: System describes itself so Cursor can understand it
4. **Pattern Discovery**: Semantic search finds similar requirements/patterns
5. **Context Awareness**: File context (globs) informs domain understanding
6. **Two-Layer Validation**: Semantic routing + MCP structure validation
7. **Self-Awareness**: Monitors semantic understanding quality and feature usage

---

## Quick Start

### 1. Setup

```bash
# Copy Cursor configuration
cp -r mvp-v3/.cursor .cursor

# Or create symlink
ln -s mvp-v3/.cursor .cursor
```

### 2. Use

In Cursor chat:

```
/agentos
I want to add user authentication with OAuth
```

The system will:
- Understand requirement semantically
- Use semantic search to find similar patterns
- Leverage file context (if files open)
- Layer rules (alwaysApply + description + globs)
- Route based on semantic understanding
- Validate structure (MCP)

---

## Structure

```
mvp-v3/
├── .cursor/
│   ├── rules/
│   │   ├── core.mdc                    # Self-describing meta-core
│   │   └── domains/                    # Domain-specific rules
│   │       ├── auth.mdc               # Auth domain (description + globs)
│   │       ├── testing.mdc            # Testing domain
│   │       └── docs.mdc                # Documentation domain
│   └── commands/
│       └── agentos.md                  # Semantic entry point
├── docs/
│   └── reference/
│       └── agentos/
│           ├── core-contract.md        # Core invariants
│           ├── self-awareness.md       # Self-awareness integration
│           ├── decisions/              # Semantic decision graphs (markdown)
│           │   ├── task-classification.md
│           │   ├── complexity-assessment.md
│           │   └── workflow-selection.md
│           └── workflows/              # Workflow definitions
│               └── execution-standard.md
├── schemas/                            # Structure validation (MCP)
│   ├── requirement.yaml
│   └── plan.yaml
└── scripts/
    └── agentos/
        └── mcp_server.py               # Structure validation + semantic metadata
```

---

## Differences from MVP-v2

| Aspect | MVP-v2 | MVP-v3 |
|--------|--------|--------|
| **Decision Graphs** | YAML with pseudo-code | Markdown with semantic patterns |
| **Requirement Intake** | Force YAML structure | Natural language → semantic understanding |
| **Routing** | Code evaluation | Semantic pattern matching |
| **Rules** | Single core rule | Orchestrated (alwaysApply + description + globs) |
| **Search** | Not integrated | Semantic search for pattern discovery |
| **File Context** | Not used | Globs inform domain understanding |
| **Self-Description** | Template-based | Self-describing semantic system |
| **Self-Awareness** | Not integrated | Monitors semantic understanding quality |

---

## How It Works

### Semantic Understanding Flow

1. **Requirement Intake**: Natural language or structured YAML
2. **Semantic Understanding**: Understand meaning, not syntax
3. **Semantic Search**: Find similar patterns (if unclear)
4. **File Context**: Understand domain from open files (globs)
5. **Rule Layering**: Combine alwaysApply + description + globs
6. **Semantic Routing**: Match patterns to workflow types
7. **Structure Validation**: MCP validates structure (semantic routes)

### Feature Interplay

- **alwaysApply rule**: Core semantic patterns always available
- **description rules**: Domain patterns load on keyword match
- **globs rules**: File patterns load on file context
- **Semantic search**: Finds similar patterns when unclear
- **MCP**: Validates structure (semantic understanding routes)

---

## Documentation

- `docs/reference/agentos/core-contract.md` - Core invariants
- `docs/reference/agentos/self-awareness.md` - Self-awareness integration
- `docs/reference/agentos/decisions/` - Semantic decision graphs
- `docs/reference/agentos/workflows/` - Workflow definitions

---

## Next Steps

1. Test semantic understanding with natural language requirements
2. Test feature interplay (rules loading together)
3. Test semantic search pattern discovery
4. Test file context domain awareness
5. Test two-layer validation
6. Test self-awareness monitoring

---

## Dependencies

For MCP server:
```bash
pip install pyyaml jsonschema
```

For Cursor:
- Cursor IDE with MCP support
- `.cursor/` directory configured
