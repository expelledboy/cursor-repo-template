# AgentOS v5 Design: Programmatic Synergy Maximization

**Status**: Concrete Design
**Date**: 2026-01-14
**Source**: Refactoring Council Round 3 (Programmatic Focus)

---

## Core Principle

v5 maximizes Cursor feature synergies through **programmatic patterns** (rules, commands, decision graphs) that create novel behavioral effects.

---

## 1. Recursive Rule Loading

**What**: Rules that trigger rules that trigger rules (with depth limits).

**Implementation**:
*   `.cursor/rules/recursive-loader.mdc`:
    *   Detects ambiguity/vagueness in user input.
    *   Loads `ambiguity-resolver.mdc` rule.
    *   Ambiguity-resolver may trigger domain rules.
    *   Domain rules may trigger related rules.
    *   Creates a **Rule Cascade** with depth tracking.

**Behavioral Effect**: Context Expansion → Compression → Focus cycles.

**Synergy**: Rules × Rules × Commands (rules trigger commands that load more rules).

---

## 2. Subagent Pipelines

**What**: Subagents chain together, each enriching the next.

**Implementation**:
*   Subagents output structured JSON (standardized schema).
*   Commands read Subagent A's output.
*   Commands launch Subagent B with A's output as enriched context.
*   Creates a **Pipeline**: Pattern → Code → Validation.

**Behavioral Effect**: Specialized processors chain together, creating a "thought chain."

**Synergy**: Commands × Subagents × Semantic Search (each subagent uses search, results chain to next).

**Example Pipeline**:
```
/pattern-searcher → Finds "OAuth pattern"
  ↓ (output: pattern JSON)
/code-pattern-searcher → Searches for OAuth code with pattern context
  ↓ (output: code locations)
/validator → Validates OAuth security with code context
  ↓ (output: validation results)
Frontal Lobe synthesizes all outputs
```

---

## 3. Evolutionary Decision Graphs

**What**: Decision graphs that evolve based on execution outcomes.

**Implementation**:
*   Decision graphs stored in git (version-controlled).
*   `/agentos-evolve` command:
    1.  Analyzes past N tasks (from pattern library).
    2.  Finds routing failures: "Route X → Y fails 80% of the time."
    3.  Proposes decision graph mutation.
    4.  User approves → Graph updates → Git commit.
*   Creates a **Learning Loop**.

**Behavioral Effect**: System gets smarter over time by evolving its routing logic.

**Synergy**: Commands × MCP × Pattern Library (analyze outcomes, validate changes, learn patterns).

---

## 4. Adaptive Context Management

**What**: Self-compressing context when token limit approached.

**Implementation**:
*   `.cursor/rules/context-monitor.mdc`:
    *   Monitors context usage (estimated).
    *   When >80% full, triggers compression phase.
    *   Launches `/summarizer` subagent on loaded docs.
    *   Replaces loaded docs with summaries.
    *   Continues with compressed context.

**Behavioral Effect**: System prevents context overflow by self-regulating.

**Synergy**: Rules × Subagents × Commands (rule triggers command that launches subagent for compression).

---

## 5. Multi-Dimensional Pattern Matching

**What**: Pattern matching across semantic, structural, temporal, outcome dimensions.

**Implementation**:
*   Launch 4 subagents in parallel:
    *   `/semantic-matcher` (meaning similarity)
    *   `/structural-matcher` (organization similarity)
    *   `/temporal-matcher` (timing similarity)
    *   `/outcome-matcher` (result similarity)
*   Frontal Lobe synthesizes all outputs into **Multi-Dimensional Match Score**.
*   Routing uses combined score.

**Behavioral Effect**: Better routing decisions from multiple perspectives.

**Synergy**: Commands × Subagents × Semantic Search (parallel searches across dimensions, synthesized).

---

## File Structure

```
mvp-v5/
├── .cursor/
│   ├── rules/
│   │   ├── core.mdc                    # (From v4, enhanced)
│   │   ├── recursive-loader.mdc       # (New) Recursive rule loading
│   │   ├── context-monitor.mdc        # (New) Context compression
│   │   └── ...
│   ├── commands/
│   │   ├── agentos.md                  # (Enhanced) Pipeline orchestrator
│   │   ├── agentos-evolve.md           # (New) Decision graph evolution
│   │   └── ...
│   └── agents/
│       ├── pattern-searcher.md          # (Enhanced) Multi-dimensional
│       ├── semantic-matcher.md         # (New) Semantic dimension
│       ├── structural-matcher.md       # (New) Structural dimension
│       ├── temporal-matcher.md         # (New) Temporal dimension
│       ├── outcome-matcher.md          # (New) Outcome dimension
│       ├── summarizer.md               # (New) Context compression
│       └── ...
├── docs/
│   └── reference/
│       └── agentos/
│           ├── decisions/
│           │   ├── task-classification.md  # (Evolvable)
│           │   └── ...
│           └── pipelines/              # (New) Subagent pipeline definitions
│               └── pattern-to-code-to-validation.md
└── schemas/
    └── subagent-output.yaml            # (New) Standardized subagent JSON schema
```

---

## Implementation Priority

1.  **Subagent Pipelines** (Highest Impact): Chains subagents together.
2.  **Multi-Dimensional Matching** (High Impact): Better routing.
3.  **Recursive Rule Loading** (Medium Impact): Context expansion/compression.
4.  **Adaptive Context Management** (Medium Impact): Prevents overflow.
5.  **Evolutionary Decision Graphs** (Lower Priority): Requires pattern library maturity.

---

## Key Synergy Patterns

1.  **Pipeline Synergy**: Commands → Subagents → Commands (circular).
2.  **Recursive Synergy**: Rules → Rules → Rules (cascading).
3.  **Multi-Dimensional Synergy**: Subagents × Subagents × Commands (parallel synthesis).
4.  **Evolutionary Synergy**: Commands × MCP × Pattern Library (learning loop).
5.  **Adaptive Synergy**: Rules × Subagents × Commands (self-regulation).
