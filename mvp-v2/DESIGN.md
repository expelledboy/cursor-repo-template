# AgentOS MVP-v2 Design

**Status**: Design
**Date**: 2026-01-14
**Purpose**: Clean, structured AgentOS engine optimized for Cursor's capabilities.

---

## Core Principles

1. **Structured Requirements**: Requirements come in as structured data, not unstructured text blobs
2. **Cursor-Optimized**: Leverages Cursor's rules, commands, globs, and MCP optimally
3. **Small but Powerful**: Minimal surface area, maximum leverage
4. **Documentation-Driven**: Behavior lives in docs, not code

---

## Architecture

### 1. Structured Requirement Intake

**Problem**: Requirements come as unstructured text blobs
**Solution**: Structured intake forms that guide requirement capture

**Components**:
- Requirement templates (by task type)
- Structured fields (objective, scope, constraints, success criteria)
- Validation at intake (not after)

### 2. Cursor-Optimized Engine

**Leverages**:
- **Rules**: Context loading via alwaysApply, description, globs
- **Commands**: Entry points that trigger structured workflows
- **MCP**: Validation and coherence checking
- **Semantic Search**: Automatic pattern discovery

**Key Insight**: Rules load docs → Commands trigger workflows → Docs define behavior

### 3. Minimal Surface Area

**Core Components**:
1. **Requirement Intake** (structured forms)
2. **Decision Engine** (documentation-based routing)
3. **Validation Layer** (MCP tools)
4. **Execution Framework** (workflow orchestration)

**Everything Else**: Documentation that guides behavior

---

## Requirement Structure

### Task Requirement Template

```yaml
task:
  id: auto-generated
  type: execution | coordination | architecture | meta
  objective: clear, single sentence
  scope:
    files: [list of affected files/patterns]
    domains: [list of domains]
  constraints:
    time: optional
    dependencies: [list]
    risks: [list]
  success_criteria:
    - measurable outcome 1
    - measurable outcome 2
  context:
    background: optional
    related_tasks: [list]
```

### Why Structured?

1. **Clarity**: Forces clear thinking about requirements
2. **Validation**: Can validate structure at intake
3. **Routing**: Structured data enables deterministic routing
4. **Traceability**: Links requirements to outcomes

---

## Cursor Integration Strategy

### Rules (Context Loading)

**Single Core Rule** (`alwaysApply`):
- Loads core contract
- Provides task plan header template
- Minimal, focused

**Domain Rules** (`description` keywords):
- Security → security-specific context
- Testing → testing-specific context
- Refactoring → refactoring-specific context

**File Rules** (`globs` patterns):
- `docs/**/*.md` → documentation workflow
- `**/*.py` → Python-specific guidance
- `.cursor/**` → Cursor config guidance

### Commands (Entry Points)

**Single Entry Command**: `/agentos`
- Takes structured requirement
- Routes to appropriate workflow
- Returns structured plan

**Workflow Commands** (internal):
- `/agentos-classify` → Classification workflow
- `/agentos-plan` → Planning workflow
- `/agentos-execute` → Execution workflow
- `/agentos-validate` → Validation workflow

### MCP Tools (Validation)

**Coherence Tools**:
- `validate_requirement` → Validate requirement structure
- `validate_plan` → Validate execution plan
- `validate_coherence` → Check system coherence

---

## Decision Engine

### Structure

**Decision graphs are YAML**, not markdown prose:

```yaml
decision_graph:
  name: task_classification
  steps:
    - id: check_objective
      condition: objective.clarity == "clear"
      route: execution
      load: docs/reference/agentos/workflows/execution.md
    - id: check_stakeholders
      condition: stakeholders.count > 1
      route: coordination
      load: docs/reference/agentos/workflows/coordination.md
```

**Why YAML?**
- Structured, parseable
- Enables deterministic routing
- Can be validated
- Clearer than prose

---

## Workflow

### 1. Requirement Intake

```
User: /agentos
Requirement: [structured YAML or guided form]

→ Validate structure
→ Extract fields
→ Route to classification
```

### 2. Classification

```
→ Load classification graph (YAML)
→ Apply decision steps
→ Determine task type
→ Load appropriate workflow docs
```

### 3. Planning

```
→ Load workflow docs
→ Generate execution plan
→ Validate plan structure
→ Return structured plan
```

### 4. Execution

```
→ Follow plan steps
→ Validate each step
→ Update requirement status
→ Report progress
```

### 5. Validation

```
→ Run coherence checks (MCP)
→ Validate outcomes against success criteria
→ Report results
```

---

## File Structure

```
mvp-v2/
├── .cursor/
│   ├── rules/
│   │   └── core.mdc              # Single alwaysApply rule
│   └── commands/
│       └── agentos.md             # Single entry command
├── docs/
│   └── reference/
│       └── agentos/
│           ├── core-contract.md   # Core invariants
│           ├── workflows/         # Workflow definitions
│           └── decisions/         # Decision graphs (YAML)
├── schemas/
│   ├── requirement.yaml           # Requirement schema
│   ├── plan.yaml                  # Plan schema
│   └── decision-graph.yaml        # Decision graph schema
└── scripts/
    └── agentos/
        └── mcp_server.py          # MCP validation tools
```

---

## Key Differences from MVP

1. **Structured Requirements**: YAML templates vs unstructured text
2. **YAML Decision Graphs**: Structured, parseable vs markdown prose
3. **Single Entry Point**: `/agentos` vs multiple commands
4. **Validation at Intake**: Structure validation before routing
5. **Schemas**: JSON Schema validation for all structured data
6. **Minimal Rules**: One core rule vs many domain rules

---

## Next Steps

1. Create requirement schema
2. Create decision graph schema
3. Implement single entry command
4. Create YAML decision graphs
5. Implement MCP validation tools
6. Test end-to-end workflow
