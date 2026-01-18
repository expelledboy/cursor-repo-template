# AgentOS v9 Documentation Map

Read this first. Authority order: reference → how-to → explanation → tutorials → work → archive.

## AgentOS Framework

### Reference (Stable Facts & Contracts)
- [AgentOS v9 Architecture](reference/agentos/architecture.md) - Core architecture and design principles
- [State Management System](reference/agentos/state-management.md) - Lightweight context preservation
- [Relationship Graph Orchestration](reference/agentos/relationship-orchestration.md) - Directive loading validation
- [Active Task Learning System](reference/agentos/learning-system.md) - Task-based learning with navigation

### How-to (Step-by-Step Procedures)
- [Using AgentOS v9](how-to/agentos/usage.md) - Complete usage guide with examples

## Cursor Integration

### Rule-Based Mode Adaptation
- `.cursor/rules/agentos/mode-awareness.mdc` - Core mode detection and behavioral adaptation
- `.cursor/rules/agentos/objective-directive-loader.mdc` - Active objective directive loading
- `.cursor/rules/agentos/relationship-precedence.mdc` - Frontmatter relationship precedence
- `.cursor/rules/agentos/agent-mode-execution.mdc` - Full execution capabilities
- `.cursor/rules/agentos/ask-mode-analysis.mdc` - Analysis and guidance capabilities

## Development Tools

### Reference
- Tool stack and environment setup guidance

## Your Project Domains

Add your project-specific domains here following the same structure.

## Work Notes (Non-Authoritative)

Located in `docs/work/` with dated filenames and Status fields.

## Testing & Validation

Run these commands to ensure system integrity:

```bash
# Core functionality validation
python3 scripts/validate.py

# Self-determination evidence collection
./src/agentos.py self-determination

# State management check
python3 scripts/state_manager.py list

# Learning workflow
./src/agentos.py learn "observation text"
python3 scripts/task_manager.py create "task-name" "objective"
python3 scripts/task_manager.py feedback task-id --message "feedback" --alignment complete

# Context intelligence
python3 scripts/frontmatter_intelligence.py context docs/path.md
python3 scripts/frontmatter_intelligence.py awareness docs/path.md
```