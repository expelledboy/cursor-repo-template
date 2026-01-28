---
doc_status: stable
purpose: Define OpenCode-specific mechanics for configuration, agents, skills, and permissions.
intent: facts
governed_by:
  docs/domains/dev.md: Authority for dev domain docs
related:
  docs/dev/facts/agent-mechanics.md: Universal constraints this doc extends
  docs/dev/facts/cursor-mechanics.md: Comparable mechanics for Cursor runtime
---

# Fact: OpenCode Runtime Mechanics

This document defines mechanics specific to the **OpenCode** agent runtime. For universal constraints shared by all runtimes, see `docs/dev/facts/agent-mechanics.md`.

## Configuration System

### Config File Format

OpenCode uses JSON or JSONC (JSON with comments) configuration:

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "model": "anthropic/claude-sonnet-4-5",
  "theme": "opencode",
  "instructions": ["CONTRIBUTING.md", "docs/guidelines.md"]
}
```

### Config Locations and Precedence

Configs are **merged** (not replaced). Later sources override earlier for conflicting keys:

1. **Remote** (`.well-known/opencode`) - Organizational defaults
2. **Global** (`~/.config/opencode/opencode.json`) - User preferences
3. **Custom** (`OPENCODE_CONFIG` env var) - Custom overrides
4. **Project** (`opencode.json` in project root) - Project-specific
5. **`.opencode/` directories** - Agents, commands, plugins, skills
6. **Inline** (`OPENCODE_CONFIG_CONTENT` env var) - Runtime overrides

### Variable Substitution

Config supports variables:
- `{env:VARIABLE_NAME}` - Environment variables
- `{file:path/to/file}` - File contents

## Rules System

### AGENTS.md

OpenCode uses `AGENTS.md` at project root as the primary rules mechanism:

- Always loaded into context
- Plain Markdown, no frontmatter required
- Run `/init` to auto-generate from project analysis
- Commit to git for team sharing

```markdown
# Project Instructions

## Code Style
- Use TypeScript for all new files
- Prefer functional components in React

## Architecture
- Follow the repository pattern
```

### Instructions Array

Additional instruction files via `opencode.json`:

```json
{
  "instructions": [
    "CONTRIBUTING.md",
    "docs/guidelines.md",
    ".cursor/rules/*.md",
    "https://example.com/remote-rules.md"
  ]
}
```

- Supports file paths, glob patterns, and remote URLs
- Remote instructions fetched with 5-second timeout
- Combined with AGENTS.md content

### Claude Code Compatibility

OpenCode reads Claude Code conventions as fallbacks:
- `CLAUDE.md` (if no `AGENTS.md`)
- `~/.claude/CLAUDE.md` (if no `~/.config/opencode/AGENTS.md`)
- `~/.claude/skills/`

Disable with `OPENCODE_DISABLE_CLAUDE_CODE=1`.

## Multi-Agent Architecture

### Agent Types

| Type | Description | Tool Access |
|------|-------------|-------------|
| **Primary** | Main conversation handlers | Configurable |
| **Subagent** | Specialized assistants invoked by primary agents | Configurable |

### Built-in Agents

| Agent | Type | Description |
|-------|------|-------------|
| `build` | Primary | Default agent, all tools enabled |
| `plan` | Primary | Read-only, requires approval for edits/bash |
| `general` | Subagent | Full tools for multi-step tasks |
| `explore` | Subagent | Fast, read-only codebase exploration |

### Agent Switching

- **Primary agents**: Press `Tab` key to cycle
- **Subagents**: `@mention` in chat (e.g., `@general help me search`)
- **Automatic**: Primary agents invoke subagents based on task

### Custom Agents

Define in `opencode.json` or `.opencode/agents/<name>.md`:

```yaml
---
description: Reviews code for best practices
mode: subagent
model: anthropic/claude-sonnet-4-5
tools:
  write: false
  edit: false
---

You are a code reviewer. Focus on security and maintainability.
```

## Skills System

### Skill Locations

| Location | Scope |
|----------|-------|
| `.opencode/skills/<name>/SKILL.md` | Project |
| `~/.config/opencode/skills/<name>/SKILL.md` | User (global) |
| `.claude/skills/<name>/SKILL.md` | Project (Claude compatibility) |
| `~/.claude/skills/<name>/SKILL.md` | User (Claude compatibility) |

### Skill File Format

```yaml
---
name: my-skill              # Required, lowercase with hyphens
description: "When to use"  # Required, 1-1024 characters
license: MIT                # Optional
compatibility: opencode     # Optional
metadata:                   # Optional key-value pairs
  audience: developers
---

# Skill content
```

### Skill Loading

- Native `skill` tool presents available skills to agent
- Agent loads skill by calling `skill({ name: "skill-name" })`
- Content loaded on-demand, not at startup

### Skill Permissions

Control skill access per-agent:

```json
{
  "permission": {
    "skill": {
      "*": "allow",
      "internal-*": "deny",
      "experimental-*": "ask"
    }
  }
}
```

## Compaction Configuration

Unlike Cursor, OpenCode compaction is **user-configurable**:

```json
{
  "compaction": {
    "auto": true,    // Auto-compact when context full (default: true)
    "prune": true    // Remove old tool outputs to save tokens (default: true)
  }
}
```

## Permission System

### Permission Levels

| Level | Behavior |
|-------|----------|
| `allow` | Execute without approval |
| `deny` | Disabled entirely |
| `ask` | Prompt user for approval |

### Global Permissions

```json
{
  "permission": {
    "edit": "ask",
    "bash": "ask",
    "webfetch": "allow"
  }
}
```

### Per-Agent Permissions

Override globals for specific agents:

```json
{
  "agent": {
    "build": {
      "permission": {
        "edit": "allow",
        "bash": {
          "*": "ask",
          "git status": "allow",
          "npm test": "allow"
        }
      }
    }
  }
}
```

### Bash Command Patterns

Fine-grained bash permissions with glob patterns:

```json
{
  "permission": {
    "bash": {
      "*": "ask",
      "git diff": "allow",
      "git log*": "allow",
      "npm *": "allow"
    }
  }
}
```

Last matching rule wins.

## Built-in Tools

| Tool | Description |
|------|-------------|
| `bash` | Execute shell commands |
| `edit` | Modify files with exact string replacement |
| `write` | Create or overwrite files |
| `read` | Read file contents |
| `grep` | Search file contents with regex |
| `glob` | Find files by pattern |
| `list` | List directory contents |
| `patch` | Apply patches to files |
| `skill` | Load skills on-demand |
| `todowrite` | Create/update task lists |
| `todoread` | Read task list state |
| `webfetch` | Fetch web content |
| `question` | Ask user questions during execution |
| `lsp` | LSP integration (experimental) |

### Tool Configuration

Disable or require approval per-tool:

```json
{
  "tools": {
    "write": false,
    "bash": false
  }
}
```

## Session State

### Todo Tools

Built-in `todowrite`/`todoread` tools for task tracking within a session:

- Creates task lists with status tracking
- Persists within the conversation
- Disabled for subagents by default

### External State

For multi-session state persistence, use external mechanisms:
- This governance system provides `docs/work/objective-graph.yaml`
- Git commits for checkpointing
- Plan files for documentation

## Commands

Define reusable workflows in `.opencode/commands/` or via config:

```json
{
  "command": {
    "test": {
      "template": "Run tests with coverage",
      "description": "Run tests with coverage report",
      "agent": "build",
      "model": "anthropic/claude-haiku-4-5"
    }
  }
}
```

Invoke with `/test` in chat.

## Integration Points

### MCP Servers

Configure external tools:

```json
{
  "mcp": {
    "jira": {
      "type": "remote",
      "url": "https://jira.example.com/mcp",
      "enabled": true
    }
  }
}
```

### Formatters

Auto-format code after edits:

```json
{
  "formatter": {
    "prettier": {
      "command": ["npx", "prettier", "--write", "$FILE"],
      "extensions": [".js", ".ts", ".jsx", ".tsx"]
    }
  }
}
```

### Plugins

Extend with custom tools, hooks, and integrations:

```json
{
  "plugin": ["opencode-helicone-session", "@my-org/custom-plugin"]
}
```

## Runtime Interfaces

| Interface | Description |
|-----------|-------------|
| TUI | Terminal-based interface |
| CLI | `opencode run "prompt"` for scripts |
| Web | Browser-based via `opencode web` |
| IDE | VS Code extension |
| Server | HTTP API via `opencode serve` |
