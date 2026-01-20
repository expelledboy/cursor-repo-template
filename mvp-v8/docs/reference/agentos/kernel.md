---
title: "AgentOS Kernel (v8)"
status: stable
created_date: 2026-01-16
purpose: "Core principles and components of the AgentOS v8 kernel"
domain: agentos
---

# AgentOS Kernel (v8)

## Core Principles

The Kernel implements the **[Directive-Orchestration-Execution (DOE)](docs/reference/agentos/architecture.md)** operating model.

- **Simplicity**: Essential features only
- **Performance**: Optional traces, lazy loading
- **Ergonomics**: Intuitive Cursor integration
- **Practicality**: Flexible governance

## Key Components

1. **Active State**: Simple YAML resumability
2. **Decision Flows**: Streamlined decision-making with external integration
3. **Optional Traces**: Record when needed with external evidence anchoring
4. **Cursor Commands**: `/checkpoint`, `/resume`, `/trace`
5. **External Knowledge**: Web URLs, MCP docs, Context7 integration

## Governance

- Trial-first approach
- Easy install approval
- Focus on user value over strict process