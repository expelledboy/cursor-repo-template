# AgentOS MVP-v2

**Status**: Initial Implementation
**Date**: 2026-01-14

Clean, structured AgentOS engine optimized for Cursor's capabilities.

---

## Key Features

1. **Structured Requirements**: YAML-based requirement intake (no unstructured blobs)
2. **YAML Decision Graphs**: Structured, parseable routing logic
3. **Single Entry Point**: `/agentos` command handles all workflows
4. **Schema Validation**: JSON Schema validation for all structured data
5. **Cursor-Optimized**: Leverages rules, commands, globs, and MCP optimally

---

## Quick Start

### 1. Setup

```bash
# Copy Cursor configuration
cp -r mvp-v2/.cursor .cursor

# Or create symlink
ln -s mvp-v2/.cursor .cursor
```

### 2. Use

In Cursor chat:

```
/agentos
```yaml
task:
  type: execution
  objective: Add user authentication with OAuth
  scope:
    domains: [auth, security]
  success_criteria:
    - OAuth flow works end-to-end
    - Tests pass
```

Or use guided form:

```
/agentos
I want to add user authentication
```

---

## Structure

```
mvp-v2/
├── .cursor/
│   ├── rules/
│   │   └── core.mdc              # Single alwaysApply rule
│   └── commands/
│       └── agentos.md             # Single entry command
├── docs/
│   └── reference/
│       └── agentos/
│           ├── core-contract.md   # Core invariants
│           ├── decisions/        # YAML decision graphs
│           └── workflows/        # Workflow definitions
├── schemas/
│   ├── requirement.yaml           # Requirement schema
│   └── decision-graph.yaml       # Decision graph schema
└── scripts/
    └── agentos/
        └── mcp_server.py          # MCP validation tools
```

---

## Differences from MVP

| Feature | MVP | MVP-v2 |
|---------|-----|--------|
| Requirements | Unstructured text | Structured YAML |
| Decision Graphs | Markdown prose | YAML structured |
| Entry Point | Multiple commands | Single `/agentos` |
| Validation | After routing | At intake |
| Schemas | None | JSON Schema |
| Rules | Multiple domain rules | Single core rule |

---

## Documentation

- `DESIGN.md` - Architecture and design decisions
- `docs/reference/agentos/core-contract.md` - Core invariants
- `docs/reference/agentos/decisions/` - Decision graphs (YAML)
- `docs/reference/agentos/workflows/` - Workflow definitions

---

## Next Steps

1. Test requirement intake
2. Test decision graph routing
3. Create additional workflows
4. Add MCP integration
5. Iterate based on usage
