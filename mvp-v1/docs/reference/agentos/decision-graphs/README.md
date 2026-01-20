# AgentOS Decision Graphs

**Status**: Initial Version
**Date**: 2026-01-14

Decision graphs are **documentation specifications** that guide deterministic agent behavior. They are markdown files that the agent reads and follows, not executable code.

## Available Graphs

### Task Classification (`task-classification.md`)
**Purpose**: Classify incoming tasks into task types

**Output**: Task type (Execution, Coordination, Architecture, Direct)

**Process**: 3-step decision tree checking objective clarity, stakeholder involvement, and technical complexity

**Use Case**: First decision when starting any task

---

### Complexity Assessment (`complexity-assessment.md`)
**Purpose**: Determine task complexity level (1-4)

**Output**: Complexity level (1-4) with workflow variation

**Process**: Multi-dimensional analysis (scope, decisions, risk, effort, dependencies) with escalation rules

**Use Case**: After task classification, to determine appropriate rigor level

---

### Validation Strategy (`validation-strategy.md`)
**Purpose**: Select appropriate validation approach

**Output**: Validation strategy with specific gates

**Process**: Check CI → tests → commands → manual validation, considering complexity level

**Use Case**: During planning phase, to determine verification gates for task plan header

---

### Evolution Path (`evolution-path.md`)
**Purpose**: Route AgentOS meta-maintenance tasks to appropriate evolution processes

**Output**: Evolution process route (gap capture, problem validation, ADR creation, etc.)

**Process**: Check for gaps → problems → improvements → single-loop vs double-loop changes

**Use Case**: For AgentOS self-improvement and meta-maintenance tasks

---

## How Decision Graphs Work

1. **Agent reads the graph** markdown file
2. **Follows the decision tree** step by step
3. **Evaluates conditions** based on task context
4. **Returns decision** with confidence level
5. **Loads appropriate directives** based on decision

## Graph Format

Each graph follows this structure:
- **Purpose**: What decision it makes
- **Decision Tree**: Step-by-step process
- **Output**: What it produces
- **Examples**: Concrete examples for clarity

## Adding New Graphs

To add a new decision graph:

1. Create markdown file in this directory
2. Follow the format of existing graphs
3. Update this README
4. Reference in commands that use it

## Integration

Decision graphs are used by:
- `/agentos-start` command (classification + complexity)
- Future commands (validation strategy, evolution path, etc.)
