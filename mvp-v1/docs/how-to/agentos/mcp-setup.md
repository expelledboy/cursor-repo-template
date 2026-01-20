# MCP Server Setup Guide

**Status**: Initial
**Date**: 2026-01-14
**Purpose**: Guide for setting up AgentOS MCP validation server in Cursor.

---

## Overview

The AgentOS MCP server exposes validation tools to Cursor, enabling the agent to run coherence checks directly.

**Available Tools**:
- `validate_decision_graph` - Validate decision graph structure
- `validate_command` - Validate command file format
- `validate_rule` - Validate rule file format
- `validate_mvp_coherence` - Comprehensive MVP coherence check

---

## Prerequisites

- Python 3.8+ installed
- Cursor IDE with MCP support
- AgentOS MVP files in `mvp/` directory

---

## Installation

### Step 1: Verify MCP Server Script

Check that the MCP server script exists and is executable:

```bash
ls -l scripts/agentos/mcp_server.py
chmod +x scripts/agentos/mcp_server.py
```

### Step 2: Test MCP Server (CLI)

Test the server directly:

```bash
# Test decision graph validation
python3 scripts/agentos/mcp_server.py validate_decision_graph docs/reference/agentos/decision-graphs/task-classification.md

# Test command validation
python3 scripts/agentos/mcp_server.py validate_command .cursor/commands/agentos-start.md

# Test rule validation
python3 scripts/agentos/mcp_server.py validate_rule .cursor/rules/agentos-core.mdc

# Test comprehensive validation
python3 scripts/agentos/mcp_server.py validate_mvp_coherence all
```

Expected output: JSON validation results.

### Step 3: Configure Cursor MCP

Add MCP server configuration to Cursor settings.

**Option A: Cursor Settings UI**
1. Open Cursor Settings (`Cmd+,` or `Ctrl+,`)
2. Navigate to "Features" → "Model Context Protocol"
3. Add new MCP server:
   - **Name**: `agentos-validation`
   - **Command**: `python3`
   - **Args**: `["scripts/agentos/mcp_server.py"]`
   - **Working Directory**: (leave empty or set to repo root)

**Option B: Cursor Config File**

Edit `~/.cursor/mcp.json` (or equivalent):

```json
{
  "mcpServers": {
    "agentos-validation": {
      "command": "python3",
      "args": ["scripts/agentos/mcp_server.py"],
      "cwd": "/path/to/repo"
    }
  }
}
```

**Note**: Adjust paths based on your setup. If running from `mvp/` directory, use:
```json
{
  "mcpServers": {
    "agentos-validation": {
      "command": "python3",
      "args": ["../scripts/agentos/mcp_server.py"],
      "cwd": "/path/to/repo/mvp"
    }
  }
}
```

### Step 4: Verify MCP Connection

1. Restart Cursor
2. Open Cursor Chat
3. Try using `/agentos-validate` command
4. Check if MCP tools are available (agent should mention MCP tool calls)

---

## Usage

### Via Commands

Use the `/agentos-validate` command:

```
/agentos-validate
/agentos-validate all
/agentos-validate graphs
/agentos-validate commands
/agentos-validate rules
```

### Via Direct MCP Tool Calls

The agent can call MCP tools directly:

- `validate_decision_graph` with `{"graph_path": "docs/reference/agentos/decision-graphs/task-classification.md"}`
- `validate_command` with `{"command_path": ".cursor/commands/agentos-start.md"}`
- `validate_rule` with `{"rule_path": ".cursor/rules/agentos-core.mdc"}`
- `validate_mvp_coherence` with `{"scope": "all"}`

---

## Output Format

All tools return JSON following this schema:

```json
{
  "status": "pass" | "fail" | "warning",
  "message": "Summary message",
  "details": [
    {
      "severity": "critical" | "warning" | "info",
      "message": "Issue description",
      "file": "path/to/file",
      "line": 12,
      "column": 5,
      "remediation": "How to fix",
      "context": "Code snippet"
    }
  ],
  "metadata": {
    "execution_time": 0.123,
    "scope": "decision_graph:path/to/file",
    "version": "1.0.0",
    "timestamp": "2026-01-14T12:00:00Z"
  }
}
```

---

## Troubleshooting

### MCP Server Not Found

**Error**: `Command not found` or `MCP server unavailable`

**Solutions**:
1. Check Python path: `which python3`
2. Verify script exists: `ls -l scripts/agentos/mcp_server.py`
3. Check script permissions: `chmod +x scripts/agentos/mcp_server.py`
4. Test script directly: `python3 scripts/agentos/mcp_server.py validate_mvp_coherence all`
5. Verify Cursor MCP config path and working directory

### Path Issues

**Error**: `File does not exist` or `Cannot read file`

**Solutions**:
1. Ensure paths are relative to MVP root (no `mvp/` prefix)
2. Check working directory in MCP config
3. Verify file paths exist: `ls -la docs/reference/agentos/decision-graphs/`

### JSON Parse Errors

**Error**: `Invalid JSON` or `Parse error`

**Solutions**:
1. Check Python version: `python3 --version` (need 3.8+)
2. Verify script syntax: `python3 -m py_compile scripts/agentos/mcp_server.py`
3. Check for encoding issues (files should be UTF-8)

### MCP Tools Not Available

**Error**: Agent doesn't mention MCP tools or can't call them

**Solutions**:
1. Restart Cursor after MCP config changes
2. Check Cursor MCP logs (if available)
3. Verify MCP server name matches config
4. Try manual MCP tool call in chat

---

## Fallback (MCP Unavailable)

If MCP is not configured or unavailable, commands will:

1. Show manual validation steps
2. Provide CLI commands to run manually
3. Explain how to set up MCP
4. Continue with manual validation guidance

Example fallback output:

```
MCP server not available. Run manually:

python3 scripts/agentos/mcp_server.py validate_mvp_coherence all

To set up MCP, see: docs/how-to/agentos/mcp-setup.md
```

---

## Next Steps

After setup:

1. Test validation tools via `/agentos-validate`
2. Integrate validation into workflow
3. Use validation results for remediation
4. Report issues or improvements

---

## Related Documentation

- `docs/reference/agentos/validation-contract.md` - Validation principles
- `docs/reference/agentos/cursor-implementation-spec.md` - Cursor integration details
- `.cursor/commands/agentos-validate.md` - Validation command usage
