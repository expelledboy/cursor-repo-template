---
title: "AgentOS v9 Architecture"
status: stable
created_date: 2026-01-18
purpose: "Core architecture and design principles for AgentOS v9"
domain: agentos
authority_level: 1
doe_layer: directive
doe_responsibility: "Define core architecture and design principles"
doe_governance: "Governed by doe-framework.md"
doe_precedence: 3
governed_by: ["docs/reference/agentos/doe-framework.md"]
informs: ["docs/how-to/agentos/usage.md"]
implementations: ["src/agentos.py", "scripts/task_manager.py", "scripts/agentos_data_models.py", "scripts/change_impact_analyzer.py", "scripts/evolution_planner.py", "scripts/frontmatter_intelligence.py", "scripts/gap_detector.py", "scripts/memory_bank_integrator.py", "scripts/validate.py", "scripts/workflow_coordinator.py"]
---

# AgentOS v9 Architecture

## Overview

AgentOS v9 implements a minimal, working AI development framework built on intelligence-first design principles learned from v8's failure.

## Core Components

### AgentOS Class
Main class providing core functionality:

- **analyze()**: Performs structural analysis of codebases
- **validate()**: Basic project structure validation
- **self_determine()**: Performs self-determination analysis with relationship graph orchestration
- **learn()**: Performs learning analysis from manual observations or files

### Context & Navigation Components
- **FrontmatterIntelligence**: Analyzes document relationships for intelligent context loading
- **ActiveTaskEngine**: Manages task branches with navigation and state preservation
- **CursorModeAdapter**: Detects and adapts to Cursor IDE mode constraints

### CLI Interface
Command-line interface providing:

- `analyze` command: Analyze codebase structure
- `validate` command: Validate project configuration
- `self-determination` command: Perform self-determination analysis with relationship graph
- `learn` command: Perform learning analysis from observations or files
- `--version` flag: Display version information

## Design Principles Applied

### Implementation First
- Built working code before extensive documentation
- Functionality verified before documenting capabilities
- Minimal viable implementation as foundation

### Intelligence-First Architecture
- Clear separation between automation (scripts) and cognition (AI)
- Scripts provide structured guidance and basic operations
- AI reasoning handles analysis and decision-making

### Authenticity Focus
- Implementation matches documented capabilities
- No aspirational features without working code
- Regular verification of documentation-implementation alignment
- Relationship graph ensures directive orchestration validity

## File Structure
```
mvp-v9/
├── src/
│   └── agentos.py           # Core implementation
├── scripts/
│   ├── relationship_renderer.py      # Relationship graph orchestration
│   ├── state_manager.py              # Lightweight state management
│   ├── task_manager.py               # Active task engine with navigation
│   ├── frontmatter_intelligence.py   # Relationship intelligence for context loading
│   ├── cursor_mode_adapter.py        # Cursor mode-aware behavior
│   └── validate.py                   # Authenticity validation
├── docs/
│   ├── reference/
│   │   └── agentos/
│   │       └── architecture.md
│   └── how-to/
│       └── agentos/
│           └── usage.md
├── docs/local/               # State persistence (gitignored)
└── README.md                 # Essential usage documentation
```

## Current Capabilities

| Component | Analysis | Validation | State | Learning | Context | Cursor |
|-----------|----------|------------|-------|----------|---------|--------|
| AgentOS Class | Directory/file scanning, metrics | Project structure checks | Lightweight preservation | Manual capture + AI analysis | Frontmatter analysis | Mode-aware adaptation |
| Task Engine | - | - | Navigation state | Hierarchical branching | - | - |
| Scripts | Raw data coordination | Deterministic operations | Context transfer | - | Relationship graphs | - |

## Core Components Integration

### Relationship Graph Orchestration
- **Purpose**: Ensures directive loading and orchestration validity
- **Mechanism**: Renders relationship graphs from frontmatter connections
- **Validation**: Checks directive dependencies and orchestration completeness
- **Integration**: Core to self-determination analysis

### State Management System
- **Purpose**: Maintains consciousness across context jumps
- **Mechanism**: Lightweight YAML-based state with metadata transfer
- **Features**: Context preservation, insight transfer, operation continuity
- **Integration**: Supports all analysis and learning operations

### Self-Determination Analysis
- **Purpose**: On-demand meta-analysis with orchestration validation
- **Mechanism**: Combines relationship graph with directive validation
- **Output**: Comprehensive system state and orchestration assessment
- **Integration**: Provides foundation for all subsequent intelligence operations
- **AI Agent Integration**: Guides genuine meta-analysis without assumptions

### Active Task Learning System
- **Purpose**: Branch-based learning with deterministic navigation and context preservation
- **Mechanism**: Task branches for objective isolation, script state management, AI analysis
- **Output**: Structured learning tasks with complete context and iteration history
- **Integration**: Foundation for authentic, navigable learning workflows

## Extension Points

The architecture supports extension through:
- Additional methods in AgentOS class
- New CLI subcommands
- Enhanced analysis algorithms
- Expanded validation rules