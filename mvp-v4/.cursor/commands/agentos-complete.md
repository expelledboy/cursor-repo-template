# /agentos-complete - Task Lifecycle: Complete

## Purpose
Complete task phase. Orchestrates features for task completion and pattern learning.

## Lifecycle Entrypoint
- Covers: completion → documentation → pattern learning → reporting
- Handoff: task complete

## Instructions for Agent

### 1. Load Phase Rules
- Load: `.cursor/rules/core.mdc` (alwaysApply - already loaded)
- Load: `.cursor/rules/orchestration.mdc` (orchestration patterns)
- Load: `.cursor/rules/patterns/pattern-library.mdc` (pattern library, Level 3+)

### 2. Review Task Completion
- Review verification results from `/agentos-verify`
- Review all success criteria
- Review orchestration metadata
- Review semantic understanding

### 3. Orchestrate Features for Completion

#### Level 1: Streamlined
- Brief completion report
- Skip pattern learning
- Document completion

#### Level 2: Standard
- Standard completion report
- Basic pattern learning (if applicable)
- Document completion

#### Level 3: Enhanced
- Comprehensive completion report
- Pattern learning and library update
- Document completion and patterns learned

#### Level 4: Maximum
- Formal completion report
- Extensive pattern learning and library update
- Document completion, patterns learned, and improvements

### 4. Update Documentation
- Update relevant documentation (reference, how-to, explanation)
- Document changes made
- Document patterns learned (Level 3+)
- Ensure coherence maintained

### 5. Learn Patterns (Level 3+)
- Extract patterns from successful task
- Update pattern library with learned patterns
- Document pattern characteristics:
  - Task type patterns
  - Complexity patterns
  - Workflow patterns
  - Domain patterns
  - Orchestration patterns

### 6. Generate Completion Report
Create structured completion report:

```yaml
completion_report:
  task_id: [task ID]
  status: [completed/failed/partial]
  success_criteria_met: [list of criteria met]
  orchestration_summary:
    complexity_level: [1-4]
    orchestration_pattern: [pattern used]
    subagents_used: [list of subagents]
    rules_cascaded: [list of rules]
    semantic_searches: [list of searches]
  patterns_learned: [list of patterns learned, Level 3+]
  documentation_updated: [list of docs updated]
  coherence_maintained: [yes/no]
  next_steps: [any follow-up tasks]
```

### 7. Present Completion
- Show completion report
- Show patterns learned (Level 3+)
- Show documentation updates
- Show orchestration summary
- Task complete

## Canonical Entrypoints
- `docs/reference/agentos/core-contract.md`
- `docs/reference/agentos/meta-orchestration.md`
- `.cursor/rules/patterns/pattern-library.mdc` (Level 3+)

## Pattern Learning (Level 3+)

When learning patterns:
1. Extract successful orchestration patterns
2. Extract semantic understanding patterns
3. Extract workflow patterns
4. Extract domain patterns
5. Update pattern library
6. Document pattern characteristics

## Next Steps

Task complete. Ready for next task:
- Use `/agentos` for new task
- Review pattern library for similar tasks (Level 3+)
