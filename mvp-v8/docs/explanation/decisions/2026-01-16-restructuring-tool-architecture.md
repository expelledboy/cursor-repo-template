---
title: "Decision: Restructuring Tool Architecture"
status: accepted
created_date: 2026-01-16
purpose: "Technology choices for deterministic restructuring infrastructure"
domain: docs
related:
  - docs/explanation/architecture/restructuring-system-rationale.md
implementations:
  - scripts/docs/index.py
  - scripts/docs/mod.just
---

# Decision: Restructuring Tool Architecture

## Problem

Need deterministic infrastructure that supports agent intelligence without constraining decision-making or creating maintenance overhead.

## Alternatives Considered

- **Monolithic AI Tool**: Single intelligent system handling all operations
- **GUI Interface**: Visual restructuring application
- **Manual Scripts**: Ad-hoc shell scripts for each operation
- **Full Automation**: AI-driven restructuring without agent oversight

## Decision

Justfile orchestration + Python utilities with stdout-based communication and path-aware execution.

## Technology Rationale

### Justfile Orchestration
- **Declarative Syntax**: Clear task definitions enable agent customization
- **Cross-Platform**: Works on all development environments
- **Extensible**: Easy addition of new restructuring operations
- **Composable**: Tasks can reference each other for complex workflows

### Python Utilities
- **Rapid Development**: Fast iteration for tool enhancements
- **Rich Ecosystem**: Access to file operations, data processing, validation libraries
- **Scripting Flexibility**: Handles complex logic without justfile limitations
- **Path Resolution**: Robust handling of relative/absolute paths

### Stdout Communication
- **Agent Parseable**: Text output enables intelligent agent processing
- **Streaming Support**: Real-time feedback during long operations
- **Tool Agnostic**: Any tool can consume output from any other
- **Debuggable**: Clear text output for troubleshooting

### Path-Aware Execution
- **Context Independence**: Tools work from any directory
- **Project Portability**: Handles different project structures
- **Symbolic Link Support**: Works with complex file system layouts
- **Cross-Platform Paths**: Consistent behavior across operating systems

## Trade-offs

- **Gained**: Agent extensibility, rapid tool evolution, robust execution
- **Lost**: Additional complexity vs monolithic solutions
- **Risk**: Path resolution edge cases, stdout parsing complexity
- **Risk**: Justfile learning curve for new contributors

## Implementation

- **Justfile**: Task orchestration in `scripts/docs/mod.just`
- **Python Scripts**: Core logic in `scripts/docs/index.py`
- **Path Resolution**: Dynamic project root detection
- **Error Handling**: Comprehensive validation and user feedback
- **Extensibility**: Modular design for adding new operations

## Validation Criteria

- Tools execute reliably across different project structures
- Agent can parse and act on tool outputs effectively
- Path resolution works in all execution contexts
- Error messages guide users to correct actions
- New operations can be added without breaking existing functionality

## See Also
- [Restructuring Tools Reference](docs/how-to/docs/restructuring-tools.md) - Command reference for restructuring tools
- [Documentation Tools](scripts/docs/index.py) - Python implementation of restructuring utilities
- [Justfile Module](scripts/docs/mod.just) - Justfile orchestration for restructuring workflows
- [Restructuring System Rationale](docs/explanation/architecture/restructuring-system-rationale.md) - Architectural rationale