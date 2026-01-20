# /agentos-validate - Validate MVP Coherence

## Purpose
Run MVP coherence validation checks using MCP tools.

## Usage
```
/agentos-validate
/agentos-validate all
/agentos-validate graphs
/agentos-validate commands
/agentos-validate rules
```

## Instructions for Agent

1. **Determine Scope**
   - If no input or "all": Validate everything (graphs, commands, rules)
   - If "graphs": Validate decision graphs only
   - If "commands": Validate commands only
   - If "rules": Validate rules only

2. **Call MCP Tool**
   - Tool: `validate_mvp_coherence`
   - Input: `{"scope": "all" | "graphs" | "commands" | "rules"}`
   - If MCP unavailable: Proceed to fallback (step 6)

3. **Parse Results**
   - Parse JSON response per schema
   - Extract: status, message, details[], metadata

4. **Display Results**
   - **Overall Status**: Show pass/fail/warning badge
   - **Summary Message**: Display validation summary
   - **Detailed Issues**: Group by severity:
     - **Critical Issues** (red): Must fix
     - **Warning Issues** (yellow): Should fix
     - **Info Issues** (blue): Nice to fix
   - **For Each Issue**:
     - Severity badge
     - File path (relative to mvp/)
     - Line number (if available)
     - Column number (if available)
     - Issue message
     - Remediation guidance
     - Context snippet (3-5 lines around issue)

5. **Group by File**
   - Group issues by file path
   - Show file path once, then list all issues for that file
   - Makes it easier to fix multiple issues in one file

6. **Fallback (MCP Unavailable)**
   If MCP server not configured or tool call fails:
   - List manual validation steps
   - Provide commands to run manually:
     ```bash
     python3 scripts/agentos/mcp_server.py validate_mvp_coherence all
     ```
   - Explain how to set up MCP (link to installation guide)
   - Continue with manual validation guidance

7. **Provide Remediation**
   - For each file with issues, provide fix steps
   - Link to relevant documentation if needed
   - Suggest running specific validation tool for detailed check

8. **Document Results**
   - Save validation results in context
   - Reference in task plan header if part of task
   - Note any critical issues that block progress

## Expected Outcome
- Validation results displayed with detailed errors
- Clear remediation guidance grouped by file
- Results documented for reference
- Fallback guidance if MCP unavailable

## MCP Tool Used
- `validate_mvp_coherence` (with scope parameter)

## Example Output Format

```
## Validation Results

**Status**: ⚠️ Warning (2 warnings, 0 critical)

**Summary**: MVP coherence validation passed with 2 warning(s)

### Issues by File

#### `.cursor/commands/agentos-start.md`
- **Warning** (line 12): Referenced decision graph does not exist: `validation-strategy.md`
  - **Remediation**: Create decision graph at `docs/reference/agentos/decision-graphs/validation-strategy.md`
  - **Context**:
    ```
    11.   - Read: `docs/reference/agentos/decision-graphs/complexity-assessment.md`
    12.   - Read: `docs/reference/agentos/decision-graphs/validation-strategy.md`
    13.   - If meta-maintenance task: Read `docs/reference/agentos/decision-graphs/evolution-path.md`
    ```

#### `docs/reference/agentos/decision-graphs/task-classification.md`
- **Warning** (line 16): Referenced file does not exist: `docs/reference/agentos/alignment-mechanisms.md`
  - **Remediation**: Create file at `docs/reference/agentos/alignment-mechanisms.md` or fix reference
```
