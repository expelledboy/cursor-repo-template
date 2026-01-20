---
title: "AgentOS Architecture (DOE)"
status: stable
created_date: 2026-01-18
purpose: "Defines the Directive-Orchestration-Execution (DOE) operating model for AgentOS v8"
domain: agentos
---

# AgentOS Architecture (DOE)

## 1. Operating Model: DOE

AgentOS v8 follows the **Directive-Orchestration-Execution (DOE)** pattern to ensure coherence, reliability, and safety.

### **D: Directive (Source of Truth)**
*   **Definition**: Authoritative documentation that defines *what* should be done and *how* the system works.
*   **Role**: Anchors behavior to explicit, versioned truth. Prevents hallucination and drift.
*   **Artifacts**:
    *   `docs/reference/**`: Stable facts, schemas, contracts.
    *   `docs/how-to/**`: Procedural guides.
    *   `docs/explanation/**`: Rationale and decisions.

### **O: Orchestration (The "Brain")**
*   **Definition**: The cognitive process of routing tasks, planning work, and making decisions based on Directives.
*   **Role**: Maintains context, handles ambiguity, and ensures the correct sequence of operations.
*   **Artifacts**:
    *   **Agent Intelligence**: The LLM's reasoning capabilities.
    *   **Active State**: `docs/reference/agentos/spec-active-state.md` (Context persistence).
    *   **Routing Rules**: `.cursor/rules/*.mdc` (Context loading).

### **E: Execution (The "Hands")**
*   **Definition**: Deterministic tools and scripts that perform actions and produce evidence.
*   **Role**: Shifts reliability from the agent (stochastic) to code (deterministic). Ensures safety and repeatability.
*   **Artifacts**:
    *   **Tools**: `justfile` recipes, Python scripts (`scripts/`).
    *   **Commands**: Cursor commands (e.g., `/refine`, `/checkpoint`).
    *   **Validation**: Automated checks for correctness (e.g., `just docs::validate`).
    *   **Diagnostics**: Deterministic health checks and guidance (e.g., `just docs::doctor`).

## 2. The DOE Flow

Every robust operation in AgentOS follows this cycle:

1.  **Read Directive**: The agent loads the relevant authority (e.g., "How to restructure docs").
2.  **Orchestrate Plan**: The agent assesses the current state and plans the steps (e.g., "Inventory -> Batch -> Analyze").
3.  **Execute via Tools**: The agent invokes deterministic tools to perform the work (e.g., `just docs-inventory`).
4.  **Verify Outcome**: The tool provides evidence (output), and the agent validates it against the Directive.

## 3. Supporting Contracts: Traceability

To keep the DOE system coherent, we must maintain **Traceability** between Directives and Execution.

### The Registry
*   **Mechanism**: A bidirectional mapping between Documentation (D) and Implementation (E).
*   **Docs**: Frontmatter `implementations: [path/to/code]` field.
*   **Code**: Inline `# @directive docs/path/to/doc.md` comments.
*   **Enforcement**: `just docs::validate-registry` ensures these links remain valid.

**Rule**: Every architectural Decision and Specification (D) MUST be linked to its Implementation (E). This allows the Execution layer to "check" the documentation system.

## 4. Why DOE?

*   **Reliability**: Execution tools don't hallucinate. They either work or fail explicitly.
*   **Safety**: Validation gates in the Execution layer prevent destructive actions.
*   **Focus**: The Agent (Orchestrator) can focus on high-level reasoning, offloading rote tasks to the Execution layer.

## 5. DOE Integrated Flow

AgentOS v8 implements an **evolved, comprehensive DOE alignment system** that incorporates lessons from original AgentOS while maintaining simplicity. The system provides both **continuous monitoring** and **deep auditing** capabilities.

### Core Components

#### `/retrospect` Command (Enhanced)
**Purpose**: Comprehensive DOE alignment audit with continuous monitoring integration
**When**: Pre-execution, post-failure, continuous checkpoints, user request

**Complete Audit Checklist**:
0. **Task Plan Validation** ✅ - Complete header per behavior spec requirements
1. **Directives Loaded** ✅ - Required docs loaded for task type?
2. **Verification Gates** ✅ - Task-type gate exists and runnable?
3. **Safety Confirmed** ✅ - Destructive actions confirmed + extended safety checks
4. **Evidence Quality & Authority** ✅ - Sources authoritative per truth surface hierarchy
5. **Gaps Identified** ✅ - Known blockers with improvement suggestions
6. **Self-Monitoring Checkpoint** 👁️ - Contract compliance, objective alignment, gap awareness

#### Safe Execution Protocol (Expanded)
- **Destructive Actions**: Explicit confirmation + rollback plan required
- **Extended Safety**: Secrets detection, untrusted input validation, prompt injection prevention
- **Hard Errors**: Missing confirmation or safety violations block execution
- **Risk-Based**: Low/Med/High risk levels with appropriate validation

#### Task-Type Verification Gates (Complete Catalog)
| Task Type | Gate Command | Risk Level |
|-----------|--------------|------------|
| Documentation & Knowledge | `just docs::validate` | Low |
| Implementation / Feature | `just test` | High |
| Design/Architecture | `just docs::validate` | Medium |
| Testing & Verification | `just test` | High |
| Refactoring & Tech-Debt | `just test` | Medium |
| Discovery & Requirements | `just docs::validate` | Low |
| Planning & Estimation | `just docs::validate` | Low |
| Release/Deploy | build/smoke | High |
| Operations & Maintenance | smoke-test | Medium |
| Security & Compliance | lint/baseline | High |
| Incident Response & Debugging | diagnostic-check | Medium |
| AgentOS Meta-Maintenance | `just docs::validate` | High |

#### Continuous Self-Monitoring Integration
**Pre-Execution Checkpoint**: Task plan validation, directive loading, safety confirmation
**Mid-Execution Checkpoint**: Objective alignment, evidence quality, gap detection
**Post-Execution Checkpoint**: Performance assessment, contract compliance, improvement triggers

#### Decision Template (Enhanced)
For any decision-like documentation with evolution tracking:
```
## Decision: <Title>
- **Rationale**: <why this decision>
- **Evidence**: <supporting facts/links with authority levels>
- **Alternatives**: <options considered with tradeoffs>
- **Decision**: <what was chosen and why>
- **Implementation**: <where/how realized with validation>
- **Evolution**: <date + changes + lessons learned>
```

### Integration Points

- **Commands**: `/retrospect` provides continuous monitoring, `/learn` captures gaps, `/evolve` implements fixes
- **Rules**: `.cursor/rules/core.mdc` enforces DOE patterns and safety requirements
- **Validation**: `scripts/docs/index.py` provides comprehensive semantic validation
- **Safety**: Multi-layered protection with confirmation, authority validation, and extended checks

### Why This Works (Evolution from Original)

**Original AgentOS**: Comprehensive but complex (30+ files, 10+ mechanisms)
**v8 Evolution**: **Learned depth without complexity** (5 core files, 3 integrated pillars)

**Key Evolutions**:
- **Consolidated MAM + Self-Awareness**: Single `/retrospect` command with continuous checkpoints
- **Complete Gate Coverage**: All 12+ task types mapped vs original's partial implementation
- **Enhanced Safety**: Destructive + secrets + untrusted inputs + prompt injection
- **Authority Validation**: Truth surface enforcement vs basic pattern checks
- **Self-Improvement Integration**: `/learn` → `/evolve` workflow with proper gap categorization

**Result**: **Original AgentOS effectiveness with 90% less complexity**, achieved through systematic gap analysis and targeted enhancements rather than bloated feature addition.

## 6. Context Optimization
AgentOS v8 implements advanced context optimization to operate effectively within LLM token constraints while maintaining full functionality.

### Hierarchical Directive Loading
Directives load progressively based on operational needs:
- **Tier 1**: Core directives (DOE, safety, validation)
- **Tier 2**: Task-type specific directives
- **Tier 3**: Complexity-appropriate directives
- **Tier 4**: Phase-triggered directives

### Memory Bank Integration
Persistent context storage in `docs/local/` enables:
- **Active Context**: Current operation state
- **Operation History**: Continuity across commands
- **Validation Cache**: Cached results to prevent redundancy
- **State Snapshots**: Resumability for interrupted operations

### Selective Context Compression
Intelligent compression when context limits approach:
- **Directive Summarization**: Convert loaded docs to compact summaries
- **Operation History Condensation**: Summarize completed phases
- **Validation Result Caching**: Reference cached validation outcomes
- **Progressive Detail Reduction**: Reduce detail as context fills

### Complexity-Based Scaling
Operations adapt based on assessed complexity:
- **Level 1**: Minimal validation, compact documentation
- **Level 2**: Balanced validation, standard documentation
- **Level 3**: Enhanced validation, comprehensive documentation
- **Level 4**: Maximum validation, extensive documentation

See `docs/reference/agentos/context-optimization.md` for complete implementation details.

## 7. Related
- `docs/reference/agentos/behavior-spec.md` - Task lifecycle
- `docs/reference/agentos/verification-contract.md` - Gate requirements
- `docs/reference/agentos/context-optimization.md` - Context management
- `.cursor/commands/retrospect.md` - Audit command
- `.cursor/rules/core.mdc` - Integration rules
