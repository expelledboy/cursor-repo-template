---
doc_status: stable
purpose: Define Cursor-specific mechanics for rules, skills, and context management.
intent: facts
governed_by:
  docs/domains/dev.md: Authority for dev domain docs
related:
  docs/dev/facts/agent-mechanics.md: Universal constraints this doc extends
  docs/dev/facts/opencode-mechanics.md: Comparable mechanics for OpenCode runtime
---

# Fact: Cursor Runtime Mechanics

This document defines mechanics specific to the **Cursor** IDE agent runtime. For universal constraints shared by all runtimes, see `docs/dev/facts/agent-mechanics.md`.

## Rules System

### Rule Locations

| Location | Scope | Notes |
|----------|-------|-------|
| `.cursor/rules/` | Project | Version-controlled, shared with team |
| `~/.cursor/rules/` | User | Personal preferences, all projects |
| Team Rules (dashboard) | Organization | Managed via cursor.com dashboard |

### Rule File Format

Rules are Markdown files (`.md` or `.mdc`) with optional YAML frontmatter:

```yaml
---
description: "When to apply this rule (for agent-decided)"
globs: ["src/**/*.ts"]  # File patterns (for path-based)
alwaysApply: false      # true = every session
---

# Rule content in Markdown
```

### Rule Trigger Types

| Type | Frontmatter | Behavior |
|------|-------------|----------|
| `Always Apply` | `alwaysApply: true` | Applied to every chat session |
| `Apply Intelligently` | `description` only | Agent decides based on description |
| `Apply to Specific Files` | `globs` patterns | Applied when active file matches glob |
| `Apply Manually` | No triggers | Only when @-mentioned in chat |

### Rule Precedence

When rules conflict, precedence is: **Team Rules → Project Rules → User Rules**

All applicable rules are merged; earlier sources take precedence for conflicting keys.

## AGENTS.md Support

Cursor supports `AGENTS.md` as a simple alternative to `.cursor/rules/`:

- Place at project root for project-wide instructions
- **Nested support**: `AGENTS.md` in subdirectories combines with parent
- Always loaded (equivalent to `alwaysApply: true`)
- Plain Markdown, no frontmatter required

```
project/
  AGENTS.md              # Global instructions
  frontend/
    AGENTS.md            # Frontend-specific (combines with root)
  backend/
    AGENTS.md            # Backend-specific (combines with root)
```

## Skills System

### Skill Locations

Skills are discovered from multiple locations:

| Location | Scope |
|----------|-------|
| `.cursor/skills/<name>/SKILL.md` | Project |
| `~/.cursor/skills/<name>/SKILL.md` | User (global) |
| `.claude/skills/<name>/SKILL.md` | Project (Claude compatibility) |
| `~/.claude/skills/<name>/SKILL.md` | User (Claude compatibility) |
| `.codex/skills/<name>/SKILL.md` | Project (Codex compatibility) |

### Skill File Format

```yaml
---
name: my-skill              # Required, must match folder name
description: "When to use"  # Required, used for agent decisions
license: MIT                # Optional
disable-model-invocation: false  # Optional, true = manual only
---

# Skill content loaded on-demand
```

### Skill Loading Behavior

- Skills are discovered at startup
- Content is loaded **on-demand** when agent decides relevance
- Manual invocation via `/skill-name` in chat
- `disable-model-invocation: true` makes skill manual-only (like a slash command)

### Skill Directories

Skills can include optional subdirectories:

```
.cursor/skills/deploy-app/
├── SKILL.md           # Main instructions
├── scripts/           # Executable code
├── references/        # Additional docs (loaded on-demand)
└── assets/            # Static resources
```

## Commands and Hooks

### Commands

Store reusable workflows in `.cursor/commands/` as Markdown files:

- Invoked via `/command-name` in chat
- Can include multi-step instructions
- Checked into git for team sharing

### Hooks

Configure pre/post agent actions in `.cursor/hooks.json`:

```json
{
  "version": 1,
  "hooks": {
    "stop": [{ "command": "bun run .cursor/hooks/grind.ts" }]
  }
}
```

Hooks can return `followup_message` to continue agent loops.

## Plan Mode

- Toggle with `Shift+Tab` in agent input
- Agent researches, asks questions, creates plan before coding
- Plans save to `.cursor/plans/` for documentation and resumption
- Useful for complex tasks; skip for quick changes

## Context Management

### Agent Context Discovery

Cursor's agent finds context on-demand via:

- **Instant grep**: Millisecond text search
- **Semantic search**: Find by meaning, not just keywords
- **@-mentions**: `@file`, `@Branch`, `@Past Chats`

**Best practice**: Tag files you know; let agent find the rest.

### Compaction Behavior

Cursor compaction is **implicit and not user-configurable**:

- Long conversations accumulate noise
- Agent may lose focus or get distracted
- Start a new conversation when effectiveness decreases
- Use `@Past Chats` to reference previous work efficiently

### Parallel Agents

- **Git worktrees**: Each agent runs in isolated worktree
- **Multi-model**: Run same prompt across models, compare results
- Worktree changes merge back to working branch via "Apply"

## Integration Points

### MCP Servers

Connect external tools via Model Context Protocol:
- Slack, Datadog, Sentry, databases
- Configured in Cursor settings

### Bugbot

Automated PR review:
- Runs on push to source control
- Advanced analysis for issues and improvements

### Cloud Agents

- Start from cursor.com/agents, editor, or mobile
- Run in remote sandboxes
- Create branches and open PRs autonomously
- Notify via Slack, email, or web
