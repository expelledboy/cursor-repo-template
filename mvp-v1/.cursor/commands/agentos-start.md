# /agentos-start - Begin AgentOS Task

## Purpose
Start a new task following AgentOS workflow: intake → classify → assess complexity → route → plan

## Instructions for Agent

1. **Load Decision Graphs**
   - Read: `docs/reference/agentos/decision-graphs/task-classification.md`
   - Read: `docs/reference/agentos/decision-graphs/complexity-assessment.md`
   - Read: `docs/reference/agentos/decision-graphs/validation-strategy.md` (for verification gates)
   - If meta-maintenance task: Read `docs/reference/agentos/decision-graphs/evolution-path.md`

2. **Classify Task**
   - Follow task classification decision tree
   - **If classification unclear**: Use Cursor's semantic search to find similar tasks/patterns
   - Search codebase for similar implementations to inform classification
   - Determine task type: Execution, Coordination, Architecture, or Direct
   - Document search terms and results if semantic search was used

3. **Assess Complexity**
   - Follow complexity assessment decision tree
   - Evaluate 5 dimensions (scope, decisions, risk, effort, dependencies)
   - Determine complexity level (1-4)
   - Apply escalation rules if needed

4. **Determine Validation Strategy** (if not meta-maintenance)
   - Follow validation strategy decision tree
   - **Use Cursor's codebase indexing** to discover available validation tools
   - Check CI availability → tests → commands → manual
   - Search codebase for existing validation patterns
   - Select appropriate verification gates
   - Document in task plan header

5. **Route Evolution Path** (if meta-maintenance task)
   - Follow evolution path decision tree
   - Determine: gap capture, problem validation, ADR creation, or direct implementation
   - Load appropriate evolution framework sections

6. **Create Task Plan Header**
   Use this template:
   ```
   ## Task Plan Header
   - Task type: [from classification]
   - Complexity level: [from assessment]
   - Primary objective: [user's stated goal]
   - Required directives: [based on task type and complexity]
   - Workflow variation: [minimal/standard/enhanced/maximum]
   - Verification gates: [to be determined]
   ```

7. **Load Appropriate Directives**
   - Tier 1 (Core): `docs/reference/agentos/coherence-contract.md`
   - Task-type specific: Based on classification graph
   - Complexity-specific: Based on workflow variation

8. **Confirm with User**
   - Show task plan header
   - Explain classification and complexity rationale
   - Ask for confirmation or clarification if needed

## Expected Outcome
- Task classified using decision graph
- Complexity level determined
- Validation strategy selected (if applicable)
- Evolution path routed (if meta-maintenance)
- Task plan header created with workflow variation and verification gates
- Appropriate directives loaded
- Ready to proceed with planning

## Next Steps
After task plan header is confirmed, proceed with detailed planning and execution.
