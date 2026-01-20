# /agentos - Main Orchestrator Command

## Purpose
Main entry point for all AgentOS workflows. Orchestrates all Cursor features together for maximum synergy and power.

## Usage

### Natural Language Requirement
```
/agentos
I want to add user authentication with OAuth
```

### Structured YAML (Optional)
```
/agentos
```yaml
task:
  objective: Add user authentication with OAuth
  scope:
    domains: [auth, security]
  success_criteria:
    - OAuth flow works end-to-end
    - Tests pass
```
```

## Instructions for Agent

### Phase 1: Initial Orchestration Setup

#### 1.1. Load Core Orchestration Rules
- Load: `.cursor/rules/core.mdc` (alwaysApply - already loaded)
- Load: `.cursor/rules/orchestration.mdc` (orchestration patterns)
- Understand feature synergy patterns
- Understand complexity-based orchestration selection

#### 1.2. Understand Requirement Semantically
- Read requirement for meaning, not just structure
- Extract key concepts:
  - **Domain**: What area is this about? (auth, testing, docs, etc.)
  - **Objective**: What needs to be accomplished?
  - **Scope**: What's affected? (files, components, systems)
  - **Type**: Implementation? Coordination? Architecture? Direct?
- If structured YAML provided, understand the semantic meaning behind the structure

#### 1.3. Leverage File Context (globs)
- Check what files are currently open
- Understand domain from file patterns:
  - `src/auth/**` → Authentication domain
  - `tests/**` → Testing domain
  - `docs/**` → Documentation domain
- File context triggers `globs` rules automatically
- Use file context to inform initial orchestration

### Phase 2: Parallel Pattern Discovery (Level 2+)

#### 2.1. Launch Pattern Discovery Subagents in Parallel
For Level 2+ tasks, launch subagents simultaneously:

**Launch `/pattern-searcher` subagent**:
- Input: requirement, domain (if known), task_type (if known)
- Purpose: Find similar requirements and task patterns

**Launch `/code-pattern-searcher` subagent**:
- Input: requirement, domain, file_context (if available)
- Purpose: Find code patterns and implementation approaches

**Launch `/doc-pattern-searcher` subagent**:
- Input: requirement, domain
- Purpose: Find documentation patterns and reference materials

#### 2.2. Wait for All Subagent Results
- Wait for all three subagents to complete
- Collect results from all subagents
- Document subagents launched in task plan header

#### 2.3. Synthesize Pattern Discovery Results
- Combine results from all subagents
- Identify common patterns across all sources
- Extract best patterns for routing
- Document patterns found in task plan header

**For Level 1 tasks**: Skip parallel pattern discovery, use basic semantic understanding only.

### Phase 3: Task Classification

#### 3.1. Classify Task Semantically
- Load: `docs/reference/agentos/decisions/task-classification.md`
- Use synthesized patterns (if available) to inform classification
- Match semantic patterns to task types:
  - Execution: Implementation-focused, clear objective
  - Coordination: Stakeholder alignment needed
  - Architecture: System-wide, structural changes
  - Direct: Simple, isolated changes
- Use semantic search if classification unclear (Level 1: skip, Level 2+: use)
- Document classification reasoning

### Phase 4: Complexity Assessment (via Subagent for Level 2+)

#### 4.1. Assess Complexity
**For Level 1 (estimated)**: Quick semantic assessment
- Assess complexity dimensions semantically
- Determine complexity level (1-4)
- Document reasoning

**For Level 2+**: Launch `/complexity-assessor` subagent
- Input: requirement, task_type (from classification), domain, context
- Wait for subagent results
- Use subagent assessment
- Document subagent used

#### 4.2. Select Orchestration Pattern Based on Complexity
- Level 1: Streamlined orchestration (minimal subagents, basic rules)
- Level 2: Standard orchestration (2-3 subagents, full rules)
- Level 3: Enhanced orchestration (3+ subagents, cascading rules)
- Level 4: Maximum orchestration (all subagents, full cascading, multi-layer validation)

### Phase 5: Workflow Selection (via Subagent for Level 2+)

#### 5.1. Select Workflow
**For Level 1**: Direct workflow selection
- Load: `docs/reference/agentos/decisions/workflow-selection.md`
- Match task type + complexity → workflow
- Load workflow documentation

**For Level 2+**: Launch `/workflow-selector` subagent
- Input: task_type, complexity_level, domain, patterns_found (from Phase 2)
- Wait for subagent results
- Use subagent selection
- Load workflow documentation from subagent result
- Document subagent used

### Phase 6: Generate Plan with Orchestration Metadata

#### 6.1. Create Task Plan Header
Create structured plan header including orchestration metadata:

```yaml
plan:
  task_id: TASK-YYYYMMDD-XXXXXX
  orchestration:
    complexity_level: [1-4]
    orchestration_pattern: [selected pattern from orchestration.mdc]
    subagents_launched: [list of subagents launched]
    rules_cascaded: [list of cascading rules triggered]
    semantic_searches: [list of search queries used]
    pattern_library_used: [patterns consulted, if Level 3+]
  semantic_understanding:
    requirement_meaning: [what I understood from the requirement]
    patterns_matched: [semantic patterns I recognized]
    similar_patterns_found: [results from pattern discovery subagents]
    context_used: [file patterns, domain rules that informed understanding]
  type: [from semantic classification]
  objective: [from requirement]
  complexity: [from complexity assessment]
  workflow: [from workflow selection]
  steps: [structured execution steps from workflow]
  success_criteria: [from requirement]
  loaded_docs: [list of all documentation loaded]
  rules_loaded: [list of rules that matched: alwaysApply, description keywords, globs patterns]
```

#### 6.2. Generate Execution Steps
- Load workflow documentation: `docs/reference/agentos/workflows/<workflow-name>.md`
- Generate execution steps from workflow
- Assign validation methods to each step
- Link success criteria to validation

### Phase 7: Validation (Level 2+)

#### 7.1. Validate Plan Structure (MCP)
- Call MCP tool: `validate_plan` (if available)
- Check plan structure against schema
- Document validation results

#### 7.2. Validate Coherence (via Subagent for Level 3+)
**For Level 3+**: Launch `/validator` subagent
- Input: validation_type=plan, object_to_validate=plan, context=task context
- Wait for subagent results
- Use subagent validation
- Document subagent used

**For Level 2**: Use MCP validation only

**For Level 1**: Skip validation, proceed directly

### Phase 8: Present to User

#### 8.1. Show Orchestration Summary
- Show complexity level and orchestration pattern selected
- Show subagents launched (if any)
- Show rules cascaded
- Show semantic searches used (if any)
- Show pattern library consulted (if Level 3+)

#### 8.2. Show Semantic Understanding
- Show requirement meaning understood
- Show patterns matched
- Show similar patterns found
- Show context used

#### 8.3. Show Task Plan
- Show task plan header with orchestration metadata
- Show execution steps
- Show validation results (if performed)

#### 8.4. Request Confirmation
- Request confirmation or adjustments
- Suggest next command: `/agentos-start` (if confirmed)

## Expected Outcome

```yaml
plan:
  task_id: TASK-20260114-ABC123
  orchestration:
    complexity_level: 3
    orchestration_pattern: "Enhanced Orchestration"
    subagents_launched:
      - /pattern-searcher
      - /code-pattern-searcher
      - /doc-pattern-searcher
      - /complexity-assessor
      - /workflow-selector
    rules_cascaded:
      - alwaysApply: core.mdc
      - description: auth (matched "authentication")
      - globs: ["src/auth/**"] (file context)
    semantic_searches:
      - "tasks like OAuth authentication"
      - "auth implementation patterns"
    pattern_library_used: ["oauth-integration-pattern"]
  semantic_understanding:
    requirement_meaning: "User wants to add OAuth authentication, which is a security-sensitive implementation task"
    patterns_matched: ["implementation-focused", "security domain", "clear objective"]
    similar_patterns_found: "Found 3 similar authentication tasks via pattern discovery subagents"
    context_used: ["auth domain rule loaded", "security patterns from globs"]
  type: execution
  objective: Add user authentication with OAuth
  complexity: 3
  workflow: execution-enhanced
  steps: [execution steps from workflow]
  success_criteria:
    - OAuth flow works end-to-end
    - Tests pass
  loaded_docs:
    - docs/reference/agentos/workflows/execution-enhanced.md
    - docs/reference/agentos/decisions/task-classification.md
  rules_loaded:
    - alwaysApply: core.mdc
    - description: auth (matched "authentication")
    - globs: ["src/auth/**"] (file context)
```

## MCP Tools Used
- `validate_plan` - Validate plan structure (Level 2+)
- `validate_requirement` - Validate requirement structure (if available)
- `validate_coherence` - Check system coherence (Level 3+)

## Subagents Used
- `/pattern-searcher` - Pattern discovery (Level 2+)
- `/code-pattern-searcher` - Code pattern discovery (Level 2+)
- `/doc-pattern-searcher` - Documentation pattern discovery (Level 2+)
- `/complexity-assessor` - Complexity assessment (Level 2+)
- `/workflow-selector` - Workflow selection (Level 2+)
- `/validator` - Validation (Level 3+)

## Fallback (MCP/Subagents Unavailable)
- Use manual validation checklist
- Continue with semantic understanding workflow
- Document that MCP/subagent validation was skipped
- Proceed with best-effort orchestration

## Key Principles
- Orchestrate all features together for maximum synergy
- Adapt orchestration to task complexity
- Launch subagents in parallel when possible
- Cascade rules for exponential context enrichment
- Learn patterns and reuse them
- Self-orchestrate for maximum efficiency

## Next Command
After completion, proceed to: `/agentos-start`
