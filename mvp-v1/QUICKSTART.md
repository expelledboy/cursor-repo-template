# AgentOS MVP Quick Start

**Status**: Initial Setup
**Date**: 2026-01-14

## Setup

1. **Copy Cursor Configuration** (one-time setup)
   ```bash
   # Option 1: Copy files
   cp -r mvp/.cursor .cursor

   # Option 2: Create symlink (if you want to keep everything in mvp/)
   ln -s mvp/.cursor .cursor
   ```

2. **Verify Setup**
   - Check that `.cursor/rules/agentos-core.mdc` exists
   - Check that `.cursor/commands/agentos-start.md` exists

## Usage

### Starting a New Task

1. **Open Cursor Chat** (`Ctrl+I` or `Cmd+I`)

2. **Type the command**:
   ```
   /agentos-start
   ```

3. **Describe your task**:
   ```
   I want to add user authentication to the app
   ```

4. **Agent will**:
   - Classify your task (using decision graph)
   - Assess complexity level (1-4)
   - Create a task plan header
   - Load appropriate directives
   - Show you the plan for confirmation

### Example Output

```
## Task Plan Header
- Task type: Execution
- Complexity level: 3
- Primary objective: Add user authentication to the app
- Required directives:
  - docs/reference/agentos/coherence-contract.md
  - docs/reference/agentos/alignment-mechanisms.md
- Workflow variation: Enhanced rigor
- Verification gates: [to be determined]

Classification rationale:
- Clear objective → Execution type
- System-wide change, security considerations → Level 3 complexity
- Requires comprehensive planning and verification
```

## Decision Graphs

The system uses four decision graphs:

1. **Task Classification** - Determines task type (Execution, Coordination, Architecture, Direct)
2. **Complexity Assessment** - Determines complexity level (1-4) using 5 dimensions
3. **Validation Strategy** - Selects appropriate verification gates (CI → tests → commands → manual)
4. **Evolution Path** - Routes AgentOS meta-maintenance tasks (gap → problem → ADR → implementation)

All are documented in `docs/reference/agentos/decision-graphs/`

## What Gets Loaded

### Always (via core rule)
- `docs/reference/agentos/coherence-contract.md`

### Based on Task Type
- Execution → `alignment-mechanisms.md` (execution section)
- Coordination → `evolution-framework.md` (stakeholder coordination)
- Architecture → `architectural-patterns.md`
- Direct → `alignment-mechanisms.md` (minimal workflow)

### Based on Complexity Level
- Level 1: Minimal rigor workflow
- Level 2: Standard rigor workflow
- Level 3: Enhanced rigor workflow
- Level 4: Maximum rigor workflow

## Testing the Setup

Try these test tasks:

1. **Simple task**:
   ```
   /agentos-start
   Fix typo in README.md
   ```
   Expected: Level 1, Direct execution

2. **Moderate task**:
   ```
   /agentos-start
   Add user authentication with OAuth
   ```
   Expected: Level 3, Execution type

3. **Complex task**:
   ```
   /agentos-start
   Refactor the entire authentication system to support multiple providers
   ```
   Expected: Level 3-4, Architecture type

## Troubleshooting

### Rule not loading?
- Check that `.cursor/rules/agentos-core.mdc` exists
- Try mentioning "agentos" in your request
- The rule uses `alwaysApply: true` so it should load automatically

### Command not found?
- Check that `.cursor/commands/agentos-start.md` exists
- Commands are markdown files, not executable scripts
- Type `/agentos-start` exactly as shown

### Classification seems wrong?
- The decision graphs are documentation - the agent reads and follows them
- If classification is off, we can refine the decision trees
- Check `docs/reference/agentos/decision-graphs/` for the logic

## Next Steps

After testing, we can iterate by:
1. Adding validation strategy decision graph
2. Adding evolution path decision graph
3. Refining existing graphs based on usage
4. Adding more commands for different phases

## Files Created

```
mvp/
├── .cursor/
│   ├── rules/
│   │   └── agentos-core.mdc          # Core rule (always loads)
│   ├── commands/
│   │   └── agentos-start.md          # Start task command
│   └── README.md                     # Configuration docs
├── docs/reference/agentos/
│   └── decision-graphs/
│       ├── README.md                 # Decision graphs overview
│       ├── task-classification.md    # Task type decision tree
│       └── complexity-assessment.md  # Complexity level decision tree
└── QUICKSTART.md                     # This file
```

Everything is sandboxed in `mvp/` directory for safe iteration!
