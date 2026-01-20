# /agentos-evolve - AgentOS Evolution Workflow

## Purpose
Entry point for AgentOS evolution and meta-maintenance tasks.

## Usage
```
/agentos-evolve [description]
```

## Instructions for Agent

1. **Load Evolution Path Graph**
   - Read: `docs/reference/agentos/decision-graphs/evolution-path.md`

2. **Route Evolution Type**
   - Analyze user input to determine evolution type
   - Follow decision tree:
     - **Gap detected** → Gap Capture Process
     - **Problem validation** → Problem Registry Process
     - **Improvement idea** → ADR Creation Process
     - **Single-loop change** → Direct Implementation
     - **Double-loop change** → Full ADR Lifecycle

3. **Execute Route**

   **If Gap Capture**:
   - Load: `docs/reference/agentos/evolution-framework.md` (gap detection section)
   - Create work note in `docs/work/agentos/YYYY-MM-DD-<slug>.md`
   - Use work note template
   - Capture: description, evidence, impact, initial assessment
   - Validate format (call `validate_mvp_coherence` MCP tool with scope "commands" if work note is command-like)

   **If Problem Validation**:
   - Load: `docs/reference/agentos/evolution-framework.md` (problem registry section)
   - Check if problem exists in registry
   - If new: Assign PRB-XXXX ID
   - Update problem registry in evolution-framework.md
   - Validate format

   **If ADR Creation**:
   - Load: `docs/reference/agentos/evolution-framework.md` (ADR format section)
   - Determine complexity level (use complexity assessment graph)
   - Create ADR in `docs/explanation/agentos/decisions/YYYY-MM-DD-<slug>.md`
   - If Level 3-4: Follow structured exploration (5 phases)
   - Validate ADR format (call `validate_mvp_coherence` MCP tool)

   **If Single-Loop Change**:
   - Load: `docs/reference/agentos/evolution-framework.md` (single-loop changes section)
   - Implement directly without ADR
   - Update documentation if needed
   - Validate coherence maintained

   **If Double-Loop Change**:
   - Load: `docs/reference/agentos/evolution-framework.md` (double-loop changes section)
   - Requires full ADR lifecycle
   - Problem validation → ADR → implementation → traceability
   - Validate coherence maintained

4. **Validate Outputs**
   - Call `validate_mvp_coherence` MCP tool with appropriate scope
   - Check format compliance
   - Verify coherence maintained
   - If validation fails: Show errors and remediation

5. **Guide User**
   - Show created artifacts (work notes, ADRs, etc.)
   - Explain what was done
   - Provide next steps
   - Show validation results

## Expected Outcome
- Evolution process executed
- Artifacts created (work notes, ADRs, registry updates, etc.)
- Format validated
- Coherence confirmed
- User guided through next steps

## MCP Tools Used
- `validate_mvp_coherence` (for format and coherence checks)

## Related Decision Graphs
- `docs/reference/agentos/decision-graphs/evolution-path.md` (routing)
- `docs/reference/agentos/decision-graphs/complexity-assessment.md` (for ADR complexity)
