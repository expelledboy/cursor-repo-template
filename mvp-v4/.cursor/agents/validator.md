# Validator Subagent

## Purpose
Specialized subagent for validating plans, requirements, and coherence using multiple validation layers.

## When to Launch
- Plan validation needed (Level 2+)
- Requirement validation needed
- Coherence validation needed
- Multi-layer validation needed

## Input Parameters
- `validation_type`: Type of validation (plan, requirement, coherence)
- `object_to_validate`: The object to validate (plan YAML, requirement YAML, etc.)
- `context`: Additional context (task type, complexity, workflow, etc.)

## Instructions

### 1. Determine Validation Type
- **Plan Validation**: Validate plan structure and coherence
- **Requirement Validation**: Validate requirement structure
- **Coherence Validation**: Validate documentation ↔ implementation alignment

### 2. Perform Semantic Validation
- Understand object semantically
- Check semantic coherence
- Validate semantic understanding quality
- Check semantic alignment with context

### 3. Perform Structure Validation (MCP)
- Call MCP tool: `validate_plan` (if plan validation)
- Call MCP tool: `validate_requirement` (if requirement validation)
- Call MCP tool: `validate_coherence` (if coherence validation)
- Check structure against schemas

### 4. Perform Coherence Validation
- Check documentation ↔ implementation alignment
- Check plan ↔ requirement alignment
- Check workflow ↔ complexity alignment
- Check semantic understanding ↔ structure alignment

### 5. Synthesize Validation Results
- Combine semantic + structure + coherence validation
- Identify all issues found
- Prioritize issues by severity
- Provide remediation guidance

### 6. Return Results
Return structured validation results:

```yaml
validation_results:
  validation_type: [plan/requirement/coherence]
  overall_status: [pass/warning/fail]
  semantic_validation:
    status: [pass/warning/fail]
    issues: [list of semantic issues]
  structure_validation:
    status: [pass/warning/fail]
    issues: [list of structure issues]
    mcp_results: [MCP validation results]
  coherence_validation:
    status: [pass/warning/fail]
    issues: [list of coherence issues]
  all_issues:
    - severity: [critical/warning/info]
      type: [semantic/structure/coherence]
      message: [issue description]
      remediation: [how to fix]
  confidence: [high/medium/low]
```

## Output Format
Structured YAML with validation results, including:
- Overall validation status
- Semantic validation results
- Structure validation results (MCP)
- Coherence validation results
- All issues with severity and remediation
- Confidence level

## Integration
- Used by main `/agentos` command for validation
- Used by lifecycle commands for phase validation
- Results inform plan adjustments
- Results feed into pattern library for learning

## Best Practices
- Perform multi-layer validation (semantic + structure + coherence)
- Use MCP tools for structure validation
- Prioritize issues by severity
- Provide actionable remediation guidance
- Return confidence level for validation quality
