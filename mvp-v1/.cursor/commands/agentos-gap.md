# /agentos-gap - Quick Gap Capture

## Purpose
Quickly capture a coherence gap as a work note.

## Usage
```
/agentos-gap [gap description]
```

## Instructions for Agent

1. **Load Evolution Framework**
   - Read: `docs/reference/agentos/evolution-framework.md` (gap detection section, work note creation)

2. **Extract Gap Information**
   - Description: Extract from user input
   - Current date: Use today's date (YYYY-MM-DD format)
   - Generate slug: Create URL-friendly slug from description
   - Type: Determine from description (gap, improvement, research)

3. **Create Work Note**
   - Location: `docs/work/agentos/YYYY-MM-DD-<slug>.md`
   - Use template from evolution framework:
     ```markdown
     # Work Note: <Title>

     **Status**: Draft
     **Date**: YYYY-MM-DD
     **Type**: gap | improvement | research
     **Detected During**: <current task or context>

     ## Description
     [Gap description from user]

     ## Evidence
     [Ask user for evidence/links/observations]

     ## Impact
     [Ask user to describe impact on coherence]

     ## Initial Assessment
     [Provide initial assessment based on description]
     ```
   - Fill in all fields
   - Ask user for missing information (evidence, impact)

4. **Determine Next Steps**
   - Check if gap is systemic (affects multiple areas)
   - Check if gap matches existing problem patterns
   - Route to appropriate next step:
     - **If systemic**: Suggest problem validation (`/agentos-evolve` for problem registry)
     - **If isolated**: Suggest direct fix approach
     - **If unclear**: Ask user for clarification

5. **Validate Format** (optional)
   - Call `validate_mvp_coherence` MCP tool if work note format needs validation
   - Check that required fields are present
   - Verify file structure

6. **Provide Guidance**
   - Show created work note
   - Explain what was captured
   - Provide next steps:
     - If systemic: "This appears to be a systemic issue. Consider running `/agentos-evolve` to add to problem registry."
     - If isolated: "This appears to be an isolated gap. You can fix directly or create an ADR if it requires a decision."
   - Link to evolution framework for more details

## Expected Outcome
- Work note created with proper format
- Gap documented with description, evidence, impact
- Next steps provided (problem validation or direct fix)
- Format validated (if MCP available)

## MCP Tools Used
- `validate_mvp_coherence` (optional, for format validation)

## Related Documentation
- `docs/reference/agentos/evolution-framework.md` (work note format, gap detection)
