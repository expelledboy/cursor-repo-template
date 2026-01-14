# Using AgentOS Commands

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Learn how to use AgentOS commands to work through tasks systematically.

---

## Goal

By the end of this tutorial, you will:
- Understand what AgentOS commands are and when to use them
- Know how to use each command in sequence
- Understand how complexity levels affect your workflow
- Be able to complete a full task using the command sequence

## Prerequisites

- Cursor IDE (version 2.0 or higher)
- Basic familiarity with your project structure
- Understanding that commands are optional UI helpers (you can work without them)

## What Are AgentOS Commands?

AgentOS commands are Cursor chat commands that guide you through a structured task lifecycle. They help ensure you:
- Set up AgentOS in new repositories
- Verify AgentOS is properly loaded
- Capture requirements clearly
- Plan appropriately for task complexity
- Make design decisions when needed
- Execute systematically
- Verify your work
- Document outcomes

**Important**: Commands are optional UI helpers. The core behavior is defined in `docs/reference/agentos/`. Commands just make it easier to follow the workflow.

## Command Categories

### Setup Commands (One-time or Verification)
- `/agentos-bootstrap` - Initialize a new repository with AgentOS
- `/agentos-init` - Load core AgentOS system and self-validate

### Task Lifecycle Commands

AgentOS task commands follow a 6-step sequence that maps to the 8-step lifecycle:

```
1. /agentos-start   → Start a new task (intake, classify, route, complexity)
2. /agentos-plan    → Create your plan (with task plan header)
3. /agentos-design  → Design checkpoint (only if required by complexity)
4. /agentos-execute → Implement your changes
5. /agentos-verify  → Verify your work (run gates)
6. /agentos-complete → Finish and document (report, anneal)
```

## Setup Commands

### `/agentos-bootstrap` - Bootstrap a New Repository

**When to use**: When setting up AgentOS in a new or poorly documented repository (one-time setup).

**What it does**:
- Detects missing routing or directives
- Creates inventory of CI, task runners, configs, repo structure
- Extracts and documents workflows (install, test, build, deploy)
- Drafts reference and how-to docs for critical domains
- Creates routing (`docs/index.md` and domain rules)
- Defines registry scope
- Produces bootstrap summary for human validation

**How to use**:
1. Type `/agentos-bootstrap` in Cursor chat
2. Follow the bootstrap process steps
3. Validate against bootstrap gates
4. Get human ratification

**Output**: Bootstrap summary and initial AgentOS setup.

**Next**: After bootstrap gates pass, use `/agentos-init` to verify setup, then proceed with `/agentos-start` for tasks.

### `/agentos-init` - Initialize and Confirm AgentOS Readiness

**When to use**:
- After bootstrapping a new repository
- When you want to ensure AgentOS is properly loaded into context
- When you need confirmation the agent is operating according to AgentOS

**What it does**:
- Loads all Tier 1 (Core) AgentOS directives into context
- Loads AgentOS adapter rules
- Agent provides a system readiness report confirming:
  - Core directives are loaded
  - Agent is operating according to AgentOS
  - Ready for normal task workflow

**How to use**:
1. Type `/agentos-init` in Cursor chat
2. The agent loads core directives into context
3. Agent provides a readiness report
4. Review the report to confirm operational status

**Output**:
- System readiness report from the agent
- Confirmation that core directives are loaded
- Statement that agent is operating according to AgentOS
- Ready for normal workflow

**Next**: Proceed with `/agentos-start` for new tasks.

## Task Lifecycle Commands

## Step 1: Starting a Task with `/agentos-start`

**When to use**: At the beginning of any new task.

**What it does**:
- Captures your task request in one sentence
- Classifies the task type (e.g., "Implementation / Feature Build")
- Routes to appropriate domains and directives
- Determines complexity level (1-4)

**How to use**:
1. Type `/agentos-start` in Cursor chat
2. Describe your task in natural language

**Example**:
```
/agentos-start Add user authentication to the application
```

**What happens**:
- The agent captures: "Add user authentication to the application"
- Classifies: "Implementation / Feature Build"
- Determines complexity: Level 3 (subsystem impact, complex decisions)
- Creates initial task plan header
- Routes to authentication domain directives

**Output**: A task plan header with task type, primary objective, complexity level, and routing decisions.

**Next**: Use `/agentos-plan` to complete your plan.

## Step 2: Planning with `/agentos-plan`

**When to use**: After `/agentos-start`, before implementation.

**What it does**:
- Completes the task plan header with all required fields
- Defines verification gates
- Creates directive loading plan (what docs to load)
- Determines if design checkpoint is needed

**How to use**:
1. Type `/agentos-plan` in Cursor chat
2. The agent will complete the plan based on complexity level

**What happens** (varies by complexity):

**Level 1** (Quick fix):
- Minimal plan header
- Basic verification gates
- Direct execution path

**Level 2** (Standard):
- Standard plan header
- Standard verification gates
- Optional design checkpoint (if material decision exists)

**Level 3-4** (Complex):
- Comprehensive plan header
- Comprehensive verification gates
- **Mandatory** design checkpoint

**Output**: Complete task plan header with:
- Complexity level and rationale
- Required directives (what docs to load)
- Allowed domains
- Verification gates
- Design checkpoint status

**Next**:
- If design checkpoint required → `/agentos-design`
- Otherwise → `/agentos-execute`

## Step 3: Design Checkpoint with `/agentos-design`

**When to use**:
- **Required** for Level 3-4 tasks
- **Optional** for Level 1-2 if a material design decision exists

**What it does**:
- Performs structured exploration of design options
- Documents trade-offs
- Records decision rationale
- Uses design decision templates

**How to use**:
1. Type `/agentos-design` in Cursor chat
2. The agent guides you through structured exploration phases

**Example workflow**:
```
/agentos-design

The agent will:
1. Break down components affected
2. Explore 2-4 design options
3. Analyze trade-offs in tabular format
4. Document the chosen approach
5. Verify the decision aligns with constraints
```

**Output**: Design decision document with:
- Component breakdown
- Options explored
- Trade-off analysis
- Chosen approach and rationale

**Next**: `/agentos-execute`

## Step 4: Execution with `/agentos-execute`

**When to use**: After planning (and design checkpoint if required).

**What it does**:
- Implements changes using deterministic tools
- Follows safety policy (confirms destructive actions)
- Uses task runner/scripts/CI when available

**How to use**:
1. Type `/agentos-execute` in Cursor chat
2. The agent implements according to your plan

**What happens**:
- Agent uses deterministic tools (just, scripts, CI) when available
- Prompts for confirmation on destructive actions
- Implements systematically according to complexity level

**Output**: Implemented changes in your codebase.

**Next**: `/agentos-verify`

## Step 5: Verification with `/agentos-verify`

**When to use**: After implementation, before completion.

**What it does**:
- Runs verification gates (or lists commands if gates can't run)
- Validates against CI standards
- Does not truncate output

**How to use**:
1. Type `/agentos-verify` in Cursor chat
2. The agent runs your defined verification gates

**What happens**:
- Runs all verification gates defined in your plan
- Reports pass/fail/deferred status
- Shows full output (not truncated)

**Output**: Gate results showing:
- Which gates passed
- Which gates failed (if any)
- Which gates were deferred (if any)

**Next**: `/agentos-complete`

## Step 6: Completion with `/agentos-complete`

**When to use**: After verification, to finish the task.

**What it does**:
- Reports whether primary objective was met
- Reports gate status
- Records gaps as work notes (if any)
- Promotes relevant state to work notes (if needed)
- Cleans up local state

**How to use**:
1. Type `/agentos-complete` in Cursor chat
2. The agent generates completion report

**What happens**:
- Creates completion report
- Promotes only durable decisions and process gaps to `docs/work/`
- Discards ephemeral local state
- Records any gaps discovered

**Output**: Completion report with:
- Primary objective status (met/not met)
- Gate status summary
- Gaps recorded (if any)
- Next steps (if any)

**Next**: Start a new task with `/agentos-start` or end session.

## Complete Example: Adding a Feature

Let's walk through a complete example of adding a new feature:

### Scenario: Add user profile editing

**Step 1: Start**
```
/agentos-start Add user profile editing feature
```
**Result**:
- Task type: "Implementation / Feature Build"
- Complexity: Level 2 (multiple components, simple decisions)
- Routes to user/profile domain

**Step 2: Plan**
```
/agentos-plan
```
**Result**:
- Complete plan header
- Verification gates defined
- Design checkpoint: Optional (no material decisions)

**Step 3: Design** (skipped - Level 2, no material decisions)

**Step 4: Execute**
```
/agentos-execute
```
**Result**: Profile editing UI and API implemented

**Step 5: Verify**
```
/agentos-verify
```
**Result**: All gates passed (tests, lint, typecheck)

**Step 6: Complete**
```
/agentos-complete
```
**Result**:
- Report: Objective met, gates passed
- No gaps recorded
- Task complete

## Complexity Levels: What Changes?

The commands adapt their rigor based on complexity level:

### Level 1: Quick Fix (Hours)
- **Start**: Brief intake/classify/route
- **Plan**: Minimal header
- **Design**: Skip (unless material decision)
- **Execute**: Direct implementation
- **Verify**: Basic smoke tests
- **Complete**: Brief report

**Example**: Fix a typo in error message

## Setup Workflows

### New Repository Setup
```
/agentos-bootstrap
# Follow bootstrap process
# Get human ratification

/agentos-init
# Verify all validations pass

/agentos-start Add first feature
# Proceed with normal workflow
```

### Verify Existing Setup
```
/agentos-init
# Agent loads core directives and provides readiness report
# Review report to confirm agent is operating according to AgentOS
# If ready, proceed with tasks
```

## Common Task Workflows

### Level 2: Standard Enhancement (Days)
- **Start**: Standard intake/classify/route
- **Plan**: Standard header
- **Design**: Optional (if material decision)
- **Execute**: Planned implementation
- **Verify**: Standard gates
- **Complete**: Standard report

**Example**: Add a new API endpoint

### Level 3: Intermediate Feature (Weeks)
- **Start**: Comprehensive intake/classify/route
- **Plan**: Comprehensive header with checkpoints
- **Design**: **Mandatory** (structured exploration)
- **Execute**: Systematic implementation
- **Verify**: Comprehensive gates
- **Complete**: Detailed report

**Example**: Add authentication system

### Level 4: System Change (Weeks–Months)
- **Start**: Enterprise-level intake/classify/route
- **Plan**: Enterprise phased plan
- **Design**: **Mandatory** (may be multiple checkpoints)
- **Execute**: Phased with reviews
- **Verify**: Enterprise gates (phased)
- **Complete**: Enterprise report with lessons learned

**Example**: Migrate to new architecture

## Local State Management

During task execution, the agent may use local state in `docs/local/state/`:
- `task.md` - Current task summary
- `plan.md` - Working plan draft
- `decisions.md` - Task-local decisions
- `gaps.md` - Task-local gaps

**Important**:
- Local state is **ephemeral** (gitignored)
- Only **durable decisions** and **process gaps** are promoted to `docs/work/`
- All other state is discarded after task completion

## Common Workflows

### Quick Bug Fix (Level 1)
```
/agentos-start Fix typo in error message
/agentos-plan
/agentos-execute
/agentos-verify
/agentos-complete
```
(Design checkpoint skipped)

### Adding a Feature (Level 2)
```
/agentos-start Add user profile editing
/agentos-plan
/agentos-execute
/agentos-verify
/agentos-complete
```
(Design checkpoint optional)

### Complex Feature (Level 3)
```
/agentos-start Add authentication system
/agentos-plan
/agentos-design  ← Required for Level 3
/agentos-execute
/agentos-verify
/agentos-complete
```

### Architecture Change (Level 4)
```
/agentos-start Migrate to microservices
/agentos-plan
/agentos-design  ← Required, may have multiple checkpoints
/agentos-execute
/agentos-verify
/agentos-complete
```

## Troubleshooting

### Command not found
- Ensure you're in Cursor IDE (version 2.0+)
- Type `/` to see available commands
- Commands are in `.cursor/commands/`

### Agent skips a step
- Check complexity level (Level 1-2 may skip design checkpoint)
- Review task plan header to see what's required

### Verification gates fail
- Review the full output (not truncated)
- Fix issues and re-run `/agentos-verify`
- If gates can't run, agent will list commands and expected outcomes

### Want to skip commands
- Commands are optional! You can follow the lifecycle manually
- Core behavior is in `docs/reference/agentos/behavior-spec.md`
- Commands just make it easier to follow the workflow

## Next Steps

- Read `docs/reference/agentos/behavior-spec.md` for complete lifecycle details
- Read `docs/how-to/agentos/cursor-adapter.md` for adapter-specific guidance
- Read `docs/reference/agentos/complexity-determination.md` to understand complexity levels
- Try a simple Level 1 task to get familiar with the workflow

## Summary

AgentOS commands provide a structured way to set up and work through tasks:

### Setup (One-time or Verification)
1. **Bootstrap** with `/agentos-bootstrap` to initialize a new repository
2. **Init** with `/agentos-init` to load and validate the AgentOS system

### Task Lifecycle
1. **Start** with `/agentos-start` to capture and classify
2. **Plan** with `/agentos-plan` to prepare
3. **Design** with `/agentos-design` if required
4. **Execute** with `/agentos-execute` to implement
5. **Verify** with `/agentos-verify` to validate
6. **Complete** with `/agentos-complete` to finish

Commands adapt to complexity level, ensuring appropriate rigor for each task. They're optional helpers that make it easier to follow the AgentOS lifecycle systematically.
