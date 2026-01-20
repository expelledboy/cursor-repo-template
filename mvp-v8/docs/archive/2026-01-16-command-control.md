---
title: "Command-Driven Workflow Control"
created_date: 2026-01-16
purpose: "Cursor commands provide deterministic entry points for complex reasoning workflows"
domain: agentos
type: research
status: superseded
superseded_by: docs/reference/agentos/cursor-integration-specs.md
superseded_date: 2026-01-18
superseded_reason: Distilled into Reference
---

# Command-Driven Workflow Control

## Observation
Cursor commands provide deterministic entry points for complex reasoning workflows, enabling standardized processes across teams.

## Key Insights
- **Command Types**: Project (.cursor/commands/), global (~/.cursor/commands/), team (dashboard-managed)
- **Trigger Mechanism**: / prefix in chat input with automatic completion
- **Parameter Support**: Additional context can be passed after command name
- **Team Enforcement**: Team admins can create enforced commands for organization-wide compliance
- **Markdown Format**: Commands stored as plain markdown files with descriptive content
- **Official Documentation**: https://cursor.com/docs/context/commands

## Technical Grounding
- **Command Storage**: Commands stored as markdown files in `.cursor/commands/` (project) or `~/.cursor/commands/` (global)
- **Trigger Syntax**: `/command-name` prefix in chat input triggers command execution
- **Auto-completion**: Cursor provides automatic command name completion
- **Parameter Passing**: Additional context can follow command name (e.g., `/refine batch-1`)
- **Command Format**: Markdown files with title, description, and usage instructions
- **Team Commands**: Dashboard-managed commands for organization-wide enforcement
- **Integration**: Commands integrate with Cursor's chat interface and can trigger complex workflows
- **Examples**: `/refine` (documentation restructuring), `/trace` (trace revelation), `/checkpoint` (state management)

## Implications
- Complex operations become accessible through simple, memorable command interfaces
- Workflow control becomes predictable and team-standardized
- User experience improves through consistent interaction patterns
- Advanced features become discoverable and usable
- Process consistency increases across development workflows

## Used In
- [Command-Based UX Enhancement](docs/explanation/decisions/2026-01-16-command-ux.md)