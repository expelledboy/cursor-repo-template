# AgentOS Cursor Configuration

**Status**: Initial Setup
**Date**: 2026-01-14

This directory contains the minimal Cursor configuration for AgentOS MVP.

## Structure

```
.cursor/
├── rules/
│   └── agentos-core.mdc      # Core rule (always loads)
└── commands/
    └── agentos-start.md      # Start new task command
```

## Rules

### `agentos-core.mdc`
- **Type**: alwaysApply
- **Purpose**: Loads core AgentOS contract and provides basic instructions
- **Loads**: `mvp/docs/reference/agentos/coherence-contract.md`
- **Provides**: Task plan header template, core principles, semantic search guidance

### Domain-Specific Rules (description)
- **`agentos-security.mdc`**: Security, auth, encryption tasks
- **`agentos-testing.mdc`**: Testing, validation, verification tasks
- **`agentos-refactoring.mdc`**: Refactoring, restructuring tasks

### File Pattern Rules (globs)
- **`agentos-docs.mdc`**: Documentation files (docs/**/*.md)

## Commands

### `/agentos-start`
- **Purpose**: Begin new task workflow
- **Process**: Loads task classification graph, creates task plan header, loads directives
- **Outcome**: Classified task with plan header ready for execution

## Decision Graphs

Located in `mvp/docs/reference/agentos/decision-graphs/`:

- `task-classification.md` - Determines task type (Execution, Coordination, Architecture, Direct)
- `complexity-assessment.md` - Determines complexity level (1-4) using 5 dimensions

## Usage

1. **Start a task**: Type `/agentos-start` in Cursor chat
2. **Describe your task**: The agent will classify it and create a plan header
3. **Confirm or clarify**: Review the task plan header and proceed

## Iteration Plan

This is the minimal starting configuration. We'll iterate by:
1. Testing task classification accuracy
2. Adding complexity assessment graph
3. Adding validation strategy graph
4. Refining rules based on usage patterns
