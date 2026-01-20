# Workflow Selection (Semantic)

**Purpose**: Select specific workflow based on semantic understanding of task type and complexity level.

**Status**: Stable
**Date**: 2026-01-14

---

## How I Select Workflows

I match semantic understanding of task type and complexity to appropriate workflows. I understand the meaning of the combination, not just the values.

---

## Execution Workflows

**When**: Task type is `execution` (semantically understood as implementation-focused)

### Level 1 → `execution-minimal`
- **Semantic Match**: Simple, quick implementation tasks
- **Load**: `docs/reference/agentos/workflows/execution-minimal.md`
- **Indicators**: Single file, quick fix, minimal scope

### Level 2 → `execution-standard`
- **Semantic Match**: Standard implementation tasks
- **Load**: `docs/reference/agentos/workflows/execution-standard.md`
- **Indicators**: Multiple files, standard scope, moderate complexity

### Level 3 → `execution-enhanced`
- **Semantic Match**: Complex implementation tasks
- **Load**: `docs/reference/agentos/workflows/execution-enhanced.md`
- **Indicators**: System-wide, security-sensitive, comprehensive

### Level 4 → `execution-maximum`
- **Semantic Match**: Enterprise implementation tasks
- **Load**: `docs/reference/agentos/workflows/execution-maximum.md`
- **Indicators**: Critical, enterprise-wide, extensive verification

**When Unclear**: Use semantic search for "execution workflows for [complexity description]"

---

## Coordination Workflows

**When**: Task type is `coordination` (semantically understood as stakeholder alignment)

### Level 1-2 → `coordination-standard`
- **Semantic Match**: Standard coordination needs
- **Load**: `docs/reference/agentos/workflows/coordination-standard.md`
- **Indicators**: Few stakeholders, simple alignment

### Level 3-4 → `coordination-enhanced`
- **Semantic Match**: Complex coordination needs
- **Load**: `docs/reference/agentos/workflows/coordination-enhanced.md`
- **Indicators**: Multiple stakeholders, complex alignment, enterprise coordination

**When Unclear**: Use semantic search for "coordination workflows for [stakeholder description]"

---

## Architecture Workflows

**When**: Task type is `architecture` (semantically understood as structural/system-wide changes)

### Level 1-2 → `architecture-standard`
- **Semantic Match**: Standard architectural changes
- **Load**: `docs/reference/agentos/workflows/architecture-standard.md`
- **Indicators**: Limited scope, contained impact

### Level 3-4 → `architecture-enhanced`
- **Semantic Match**: Complex architectural changes
- **Load**: `docs/reference/agentos/workflows/architecture-enhanced.md`
- **Indicators**: System-wide, strategic decisions, enterprise impact

**When Unclear**: Use semantic search for "architectural workflows for [change description]"

---

## Direct Workflows

**When**: Task type is `direct` (semantically understood as simple, isolated changes)

### All Levels → `direct-minimal`
- **Semantic Match**: Simple, isolated changes
- **Load**: `docs/reference/agentos/workflows/direct-minimal.md`
- **Indicators**: Single file, quick change, minimal impact

**Note**: Direct tasks are typically Level 1, so workflow is always minimal rigor.

---

## Semantic Matching Process

1. **Understand task type semantically**
   - What does the task type mean? (execution = implementation, coordination = alignment, etc.)
   - What are the semantic implications?

2. **Understand complexity semantically**
   - What does the complexity level mean? (1 = minimal, 4 = maximum)
   - What are the semantic implications?

3. **Match combination semantically**
   - Execution + Level 3 = Complex implementation = execution-enhanced
   - Architecture + Level 4 = Enterprise architecture = architecture-enhanced
   - Understand the meaning of the combination

4. **Use semantic search when unclear**
   - Search for: "workflows for [task type] tasks at [complexity] level"
   - Find similar workflow selections
   - Learn from past matches

---

## Integration with Other Decision Graphs

This selection happens **after**:
1. Task classification (semantic understanding of task type)
2. Complexity assessment (semantic understanding of complexity level)

Then:
- Workflow documentation provides execution guidance
- Workflow steps guide implementation
- Validation gates defined by workflow

---

## Fallback

If workflow selection is unclear:
1. Use semantic search for similar task type + complexity combinations
2. Default to standard workflow for task type
3. Document uncertainty in task plan header
4. Load workflow documentation and proceed
