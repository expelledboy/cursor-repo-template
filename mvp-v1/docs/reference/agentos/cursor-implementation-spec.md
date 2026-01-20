# AgentOS Cursor Implementation Specification

**Status**: Design
**Date**: 2026-01-14
**Purpose**: Defines how to implement AgentOS MVP using Cursor IDE's actual capabilities.

---

## 1. How Cursor Actually Works

### 1.1. Rules (`.cursor/rules/*.mdc`)

**What They Are**: Markdown files with YAML frontmatter that contain instructions loaded into the AI's context.

**How They Work**:
- **Frontmatter**: YAML metadata defining when the rule loads
  - `description: "keywords"` → Loads when keywords match user input
  - `alwaysApply: true` → Always loads (no keyword needed)
  - `globs: ["pattern"]` → Loads when file paths match pattern
- **Content**: Markdown instructions that guide AI behavior
- **Limitation**: Rules cannot execute code or enforce behavior - they only provide context/instructions

**Example**:
```mdc
---
description: agentos, core behavior, routing
---
- Load these core directives:
  - `docs/reference/agentos/coherence-contract.md`
- Always include task plan header
- Do not treat Cursor memories as authoritative
```

### 1.2. Commands (`.cursor/commands/*.md`)

**What They Are**: Markdown files that describe what the agent should do when the command is invoked.

**How They Work**:
- User types `/command-name` in chat
- Cursor loads the command file into context
- Agent reads the instructions and follows them
- Commands reference canonical docs - they don't contain the actual behavior

**Example**:
```markdown
# /agentos-init

## Purpose
Load core AgentOS system and provide readiness report.

## Canonical entrypoints
- docs/reference/agentos/coherence-contract.md
- docs/reference/agentos/evolution-framework.md

## Expected outcome
- Core directives loaded
- System readiness report provided
```

### 1.3. Background Agents

**What They Are**: Cursor feature for running tasks asynchronously in the cloud.

**Limitation**: Not something you program or control - it's a Cursor feature you use, not customize.

### 1.4. Semantic Search

**What It Is**: Built into Cursor's codebase indexing - automatically understands code context.

**Limitation**: Not something you program - it just works automatically. You can't create custom semantic search workflows.

### 1.5. MCP (Model Context Protocol)

**What It Is**: Protocol for connecting Cursor to external tools (databases, APIs, documentation sources).

**How It Works**: You create MCP servers that expose tools/resources to Cursor.

**Use Case**: For validation scripts, external APIs, not for internal behavior control.

---

## 2. Corrected Implementation Approach

### 2.1. Core Principle

**AgentOS behavior is defined in documentation, not in executable code.**

- Rules load documentation and instructions into context
- Commands provide entrypoints that reference canonical docs
- The AI agent follows the instructions consistently
- Determinism comes from consistent instruction-following, not code execution

### 2.2. Decision Graphs as Documentation

Decision graphs are **documentation specifications** that the agent follows, not executable code:

```markdown
# Task Classification Decision Tree

## Step 1: Check Objective Clarity
- If clear objective → Route to execution patterns
- If unclear → Check stakeholder involvement

## Step 2: Check Stakeholder Involvement
- If multiple stakeholders → Route to coordination frameworks
- If single stakeholder → Check complexity

## Step 3: Check Complexity
- If simple → Route to direct execution
- If complex → Route to architectural patterns
```

The agent reads this documentation and follows it deterministically.

---

## 3. Rules Implementation

### 3.1. Core Rule (alwaysApply)

**File**: `.cursor/rules/agentos/core.mdc`

```mdc
---
description: agentos core
alwaysApply: true
---

# AgentOS Core Instructions

## Always Load These Core Contracts
- `docs/reference/agentos/coherence-contract.md`
- `docs/reference/agentos/evolution-framework.md`
- `docs/reference/agentos/validation-contract.md`

## Always Follow These Principles
- Maintain coherence across documentation, implementation, and behavior surfaces
- Follow authority order: reference > how-to > explanation > tutorials > work > archive
- Require explicit confirmation for destructive actions
- Always include task plan header with required fields

## Task Plan Header Template
- Task type:
- Primary objective:
- Required directives:
- Allowed domains:
- Verification gates:
- Loaded core docs:
```

### 3.2. Semantic Rules (description)

**File**: `.cursor/rules/agentos/refactoring.mdc`

```mdc
---
description: refactor, refactoring, restructure
---

# Refactoring Task Instructions

## Load Additional Directives
- `docs/reference/agentos/architectural-patterns.md` (registry mapping section)
- `docs/reference/agentos/validation-contract.md` (validation gates)

## Follow Refactoring Protocol
1. Assess impact on registry mappings
2. Determine complexity level (1-4)
3. Select appropriate validation gates
4. Update registry mappings after refactoring
5. Run validation to confirm coherence maintained
```

**File**: `.cursor/rules/agentos/security.mdc`

```mdc
---
description: security, auth, encrypt, authentication
---

# Security Task Instructions

## Load Security Directives
- `docs/reference/agentos/coherence-contract.md` (safety policy section)

## Follow Security Protocol
1. Check for secrets in code (block if found)
2. Require explicit confirmation for security boundary changes
3. Load threat modeling considerations
4. Validate against safety policy constraints
```

### 3.3. Structural Rules (globs)

**File**: `.cursor/rules/agentos/docs.mdc`

```mdc
---
description: documentation
globs: ["docs/**/*.md", "docs/**/*.md"]
---

# Documentation File Instructions

## Load Documentation Directives
- `docs/reference/agentos/alignment-mechanisms.md` (registry mapping)
- `docs/reference/agentos/evolution-framework.md` (ADR format)

## Follow Documentation Protocol
1. Verify authority order compliance
2. Check registry mappings for code references
3. Validate structure against documentation standards
4. Update registry if documentation changes affect code
```

---

## 4. Commands Implementation

### 4.1. Lifecycle Commands

**File**: `.cursor/commands/agentos-init.md`

```markdown
# /agentos-init - Initialize AgentOS System

## Purpose
Load core AgentOS contracts and provide system readiness report.

## Instructions for Agent
1. Load all Tier 1 (Core) directives from `docs/reference/agentos/`
2. Read `docs/reference/agentos/coherence-contract.md`
3. Read `docs/reference/agentos/evolution-framework.md`
4. Read `docs/reference/agentos/validation-contract.md`
5. Provide readiness report confirming:
   - Core contracts loaded
   - Agent operating according to AgentOS
   - Ready for task workflow

## Expected Outcome
System readiness report with confirmation of operational status.
```

**File**: `.cursor/commands/agentos-start.md`

```markdown
# /agentos-start - Begin New Task

## Purpose
Intake, classify, route, and plan a new task.

## Instructions for Agent
1. Load task classification decision tree from `docs/reference/agentos/alignment-mechanisms.md`
2. Follow intake → classify → route → plan sequence
3. Create task plan header with all required fields
4. Load appropriate directives based on task type and complexity
5. Document routing decisions in task plan header

## Expected Outcome
Task plan header with routing decisions and directive loading plan.
```

### 4.2. Decision Graph Commands

**File**: `.cursor/commands/agentos-decide.md`

```markdown
# /agentos-decide - Execute Decision Graph

## Purpose
Manually trigger decision graph execution for specific decisions.

## Usage
`/agentos-decide <graph-name> [context]`

## Available Graphs
- `task-classification` - Classify task type
- `complexity-assessment` - Determine complexity level (1-4)
- `validation-strategy` - Select validation approach
- `evolution-path` - Route evolution activities

## Instructions for Agent
1. Load decision graph documentation from `docs/reference/agentos/decision-graphs/<graph-name>.md`
2. Follow the decision tree steps
3. Evaluate conditions based on provided context
4. Return decision result with confidence level
5. If confidence < threshold, request user clarification

## Example
`/agentos-decide complexity-assessment "implement user authentication with OAuth"`

Expected: Complexity Level 3 (moderate scope, security considerations, integration complexity)
```

**Note**: Decision graphs are markdown documentation files, not executable code. The agent reads and follows them.

---

## 5. Decision Graph Documentation Format

### 5.1. Graph Structure (Markdown)

**File**: `docs/reference/agentos/decision-graphs/task-classification.md`

```markdown
# Task Classification Decision Graph

**Purpose**: Deterministically classify incoming tasks into task types.

## Decision Tree

### Step 1: Check Objective Clarity
**Condition**: Does the task have a clear, unambiguous primary objective?

**If YES**:
- Route to: Execution patterns
- Load: `docs/reference/agentos/alignment-mechanisms.md` (execution section)
- Confidence: 0.95

**If NO**:
- Proceed to Step 2

### Step 2: Check Stakeholder Involvement
**Condition**: Are multiple stakeholders involved or is coordination required?

**If YES**:
- Route to: Coordination frameworks
- Load: `docs/reference/agentos/evolution-framework.md` (stakeholder coordination)
- Confidence: 0.90

**If NO**:
- Proceed to Step 3

### Step 3: Check Technical Complexity
**Condition**: Does the task involve architectural decisions or system-wide changes?

**If YES**:
- Route to: Architectural patterns
- Load: `docs/reference/agentos/architectural-patterns.md`
- Confidence: 0.85

**If NO**:
- Route to: Direct execution
- Load: `docs/reference/agentos/alignment-mechanisms.md` (minimal workflow)
- Confidence: 0.95

## Fallback
If classification is unclear after all steps:
- Request user clarification
- Load: `docs/reference/agentos/coherence-contract.md` (ambiguity resolution)
```

### 5.2. Complexity Assessment Graph

**File**: `docs/reference/agentos/decision-graphs/complexity-assessment.md`

```markdown
# Complexity Assessment Decision Graph

**Purpose**: Determine task complexity level (1-4) using multi-dimensional analysis.

## Assessment Dimensions

### Dimension 1: Scope
- **Level 1**: Single component, isolated change
- **Level 2**: Multiple components, limited dependencies
- **Level 3**: System-wide, multiple dependencies
- **Level 4**: Cross-system, enterprise impact

### Dimension 2: Decision Complexity
- **Level 1**: Obvious solution, no tradeoffs
- **Level 2**: Simple decisions, few options
- **Level 3**: Complex tradeoffs, multiple viable options
- **Level 4**: Strategic decisions, policy implications

### Dimension 3: Risk
- **Level 1**: Low risk, easily reversible
- **Level 2**: Moderate risk, some impact
- **Level 3**: High risk, significant impact
- **Level 4**: Critical risk, mission-critical impact

## Decision Process

1. Assess each dimension independently
2. Take maximum level across all dimensions
3. Apply escalation rules:
   - If max=1 but risk≥3 → Level 2
   - If max=4 but scope≤2 and effort≤2 → Level 3
4. Return final complexity level with rationale

## Workflow Variations by Level
- **Level 1**: Minimal rigor, skip optional steps
- **Level 2**: Standard rigor, all steps required
- **Level 3**: Enhanced rigor, comprehensive verification
- **Level 4**: Maximum rigor, formal reviews
```

---

## 6. MCP Integration (External Tools Only)

### 6.1. Validation MCP Server

**Purpose**: Connect validation scripts to Cursor for automated checking.

**MCP Server Configuration** (`cursor-settings.json`):
```json
{
  "mcpServers": {
    "agentos-validation": {
      "command": "python",
      "args": ["scripts/agentos/mcp_server.py"]
    }
  }
}
```

**MCP Tools Exposed**:
- `validate_registry` - Check docs↔code mapping integrity
- `validate_traceability` - Verify problem→decision→artifact links
- `validate_behavior` - Check runtime contract compliance

**Note**: MCP is for external tool integration, not for internal behavior control. The validation scripts run externally and report results back to Cursor.

---

## 7. Deterministic Behavior Through Documentation

### 7.1. How Determinism Works

**Not through code execution**, but through:
1. **Consistent Documentation**: Same decision graphs always provide same guidance
2. **Explicit Instructions**: Rules and commands provide clear, unambiguous instructions
3. **Canonical Sources**: Single source of truth for each concept
4. **Authority Order**: Clear hierarchy prevents conflicts

### 7.2. Documentation Reduction Strategy

**Replace verbose explanations with structured decision trees**:

**Before** (500 words):
```
When routing a task, you must first assess the objective clarity. If the objective is clear and unambiguous, you can proceed directly to execution patterns. However, if the objective is unclear, you need to check stakeholder involvement. If multiple stakeholders are involved, you should route to coordination frameworks. If only a single stakeholder is involved, check the technical complexity...
```

**After** (50 lines of structured decision tree):
```markdown
# Task Classification Decision Tree

## Step 1: Check Objective Clarity
- Clear? → Execution patterns
- Unclear? → Step 2

## Step 2: Check Stakeholder Involvement
- Multiple? → Coordination frameworks
- Single? → Step 3
...
```

The agent follows the structured tree deterministically, reducing need for verbose explanations.

---

## 8. Implementation Roadmap

### Phase 1: Core Rules (Week 1)
- [ ] Create alwaysApply core rule
- [ ] Create description rules for common keywords
- [ ] Create globs rules for file patterns
- [ ] Test rule loading and context injection

### Phase 2: Decision Graph Documentation (Week 2)
- [ ] Write task classification decision tree
- [ ] Write complexity assessment decision tree
- [ ] Write validation strategy decision tree
- [ ] Write evolution path decision tree
- [ ] Test agent following decision trees

### Phase 3: Commands (Week 3)
- [ ] Create lifecycle phase commands
- [ ] Create decision graph command
- [ ] Test command invocation and instruction following
- [ ] Validate agent behavior consistency

### Phase 4: MCP Integration (Week 4)
- [ ] Create validation MCP server
- [ ] Expose validation tools via MCP
- [ ] Test MCP tool invocation
- [ ] Integrate validation results into workflow

### Phase 5: Documentation Reduction (Week 5-6)
- [ ] Measure decision tree effectiveness
- [ ] Replace verbose explanations with structured trees
- [ ] Validate agent behavior remains consistent
- [ ] Achieve 70%+ documentation reduction

---

## 9. Success Criteria

### Determinism Metrics
- **Instruction Consistency**: 100% same instructions produce same agent behavior
- **Decision Tree Accuracy**: 95%+ correct routing using decision trees
- **Documentation Reduction**: 70%+ reduction in procedural documentation

### Quality Metrics
- **Routing Accuracy**: 90%+ correct task classification
- **Validation Coverage**: 95%+ of changes validated
- **Coherence Maintenance**: 100% of detected gaps captured

---

## 10. Key Corrections from Initial Spec

### What Was Wrong
1. **Decision graphs as executable code** → They're documentation the agent follows
2. **Rules executing behavior** → Rules just load instructions into context
3. **Subagents as programmable** → Background agents are a Cursor feature, not customizable
4. **Semantic search as API** → It's automatic, not programmable
5. **MCP for internal control** → MCP is for external tools only

### What's Correct
1. **Rules load documentation and instructions** → Agent follows them consistently
2. **Commands provide entrypoints** → They reference canonical docs
3. **Decision graphs are structured documentation** → Agent reads and follows them
4. **Determinism through consistent instruction-following** → Not code execution
5. **Documentation reduction through structured trees** → Less verbose, more actionable

---

## 11. Related Documents

- `docs/reference/agentos/coherence-contract.md`: Core coherence invariants
- `docs/reference/agentos/evolution-framework.md`: Evolution protocols
- `docs/reference/agentos/validation-contract.md`: Validation requirements
- `docs/reference/agentos/architectural-patterns.md`: Implementation patterns
- `docs/reference/agentos/alignment-mechanisms.md`: Operational mechanisms
- `docs/reference/agentos/cursor-mechanics.md`: Cursor adapter constraints

---

This specification correctly reflects how Cursor actually works: rules load instructions, commands provide entrypoints, decision graphs are documentation the agent follows, and determinism comes from consistent instruction-following, not code execution.
