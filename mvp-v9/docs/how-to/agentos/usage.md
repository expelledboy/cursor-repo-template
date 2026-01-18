---
title: "Using AgentOS v9"
status: stable
created_date: 2026-01-18
purpose: "Basic usage guide for AgentOS v9 functionality"
domain: agentos
authority_level: 4
doe_layer: directive
doe_responsibility: "Define usage patterns and operational procedures"
doe_governance: "Governed by behavior-spec.md and doe-framework.md"
doe_precedence: 4
depends_on: ["docs/reference/agentos/architecture.md"]
governed_by: ["docs/reference/agentos/doe-framework.md", "docs/reference/agentos/behavior-spec.md"]
implementations: ["src/agentos.py"]
---

# Using AgentOS v9

## Prerequisites

- AgentOS v9 installed and accessible
- Python 3.8+ available
- Basic understanding of DOE framework (Directive-Orchestration-Execution)

## Codebase Analysis

### Command Syntax
```bash
./src/agentos.py analyze [path]
```

### Parameters
- `path`: Directory or file path to analyze (default: current directory)

### Steps
1. Execute analysis command on target path
2. Review structural metrics in JSON output
3. Identify file type distributions and patterns

### Verification
- Command completes without errors
- JSON output contains file counts and type distributions
- Path information matches target location

## Project Validation

### Command Syntax
```bash
./src/agentos.py validate [path]
```

### Parameters
- `path`: Directory path to validate (default: current directory)

### Steps
1. Execute validation command on target path
2. Review validation results in JSON output
3. Confirm all required project files present

### Verification
- Command completes successfully
- JSON output shows validation status
- Core project files detected (README, docs structure)

## Evidence Collection

### Command Syntax
```bash
./src/agentos.py self-determination
```

### Steps
1. Execute self-determination command
2. Collect evidence from JSON output
3. Provide evidence to orchestration layer for analysis

### Verification
- Command produces structured JSON evidence
- Evidence meets DOE standards (timestamp, layer declaration)
- Orchestration-ready flag set to true

## Learning Analysis

### Manual Observation Capture
```bash
./src/agentos.py learn "observation text"
```

### Parameters
- `observation text`: Text describing issue, improvement, or discovery

### Steps
1. Execute learn command with observation text
2. AI agent analyzes and categorizes observation
3. Review generated draft artifacts
4. Provide alignment feedback iteratively

### File-Based Learning Analysis
```bash
./src/agentos.py learn --file [path]
```

### Parameters
- `--file path`: Path to file containing observation text

### Steps
1. Execute learn command with file path
2. AI agent analyzes file content
3. Review categorization and draft artifacts
4. Provide alignment feedback until complete
## Task Management

### Create Learning Task Branch
```bash
python3 scripts/task_manager.py create "task_name" "learning_objective"
```

### Parameters
- `task_name`: Identifier for the task
- `learning_objective`: Description of what should be learned

### Steps
1. Execute create command with task name and objective
2. Task branch created with context preservation
3. Learning workflow initialized

### Verification
- Command completes successfully
- Task appears in active task list
- Context preservation confirmed

### Switch Between Task Branches
```bash
python3 scripts/task_manager.py switch task-id
```

### Parameters
- `task-id`: Identifier of task to switch to

### Steps
1. Execute switch command with target task ID
2. Current context saved automatically
3. Target task context loaded

### Verification
- Command completes without errors
- Task switch confirmed in status output

### Record Learning Iteration
```bash
python3 scripts/task_manager.py record-iteration task-id "iteration_data"
```

### Parameters
- `task-id`: Task identifier
- `iteration_data`: JSON string with observation, analysis, and feedback

### Steps
1. Execute record command with iteration details
2. Learning progress tracked in task history

### Verification
- Iteration recorded successfully
- Task history updated

### Provide Learning Feedback
```bash
python3 scripts/task_manager.py feedback task-id --message "feedback text" --alignment pending|partial|complete
```

### Parameters
- `task-id`: Task identifier
- `--message`: User feedback text
- `--alignment`: Current alignment status

### Steps
1. Execute feedback command with alignment assessment
2. AI agent receives feedback for iteration
3. Process continues until complete alignment achieved

### Verification
- Feedback recorded in task history
- Alignment status updated appropriately

## System Validation

### Core Functionality Validation
```bash
python3 scripts/validate.py
```

### Steps
1. Execute validation script
2. Review all system component validations
3. Confirm DOE framework compliance

### Verification
- All validation checks pass
- System integrity confirmed
- No critical errors reported

### Self-Determination Evidence Collection
```bash
./src/agentos.py self-determination
```

### Steps
1. Execute self-determination command
2. Collect system evidence from output
3. Use evidence for orchestration analysis

### Verification
- Structured evidence produced
- DOE compliance maintained
- Orchestration layer can consume output

Record user feedback during learning alignment process:

**Examples**:

**Initial Feedback**:
```bash
python3 scripts/task_manager.py feedback learning-20260118-160000 --message "The categorization is accurate but I need more specific recommendations" --alignment partial
```

**Final Alignment**:
```bash
python3 scripts/task_manager.py feedback learning-20260118-160000 --message "This captures the learning perfectly - no further changes needed" --alignment complete
```

**Guidance Provided**: The command provides contextual guidance based on alignment status to help users provide valuable feedback.

Performs learning analysis from manual observations or files:

- Analyzes text for issues, improvements, and discoveries
- Categorizes as problem or discovery
- Generates draft artifacts (not authoritative)
- Provides user alignment guidance for refinement

**Examples**:

**Text Observation**:
```bash
./src/agentos.py learn "The validation script fails when files are missing"
```

**File Analysis**:
```bash
./src/agentos.py learn --file docs/work/analysis/result.md
```

**Output**:
```json
{
  "learning_type": "manual",
  "observation": "The validation script fails when files are missing",
  "analysis": {
    "content": "The validation script fails when files are missing",
    "issues_identified": ["error_pattern"],
    "actionable": true
  },
  "categorization": {
    "category": "problem",
    "confidence": 0.8,
    "rationale": "Issues identified suggest a problem to solve",
    "recommended_fields": {
      "title": "Problem: error_pattern",
      "status": "draft"
    }
  },
  "generated_artifacts": [
    {
      "type": "problem_draft",
      "filename": "docs/work/agentos/problems/draft-problem-error-pattern.md",
      "user_alignment_required": true
    }
  ],
  "guidance": {
    "alignment_questions": [
      "What specific aspects of this learning are most/least accurate?",
      "What additional context would strengthen this learning?",
      "How does this align with your experience or observations?",
      "What specific changes would make this more actionable?"
    ],
    "iteration_process": "Provide feedback, and I'll refine the learning until we achieve alignment",
    "authoritative_promotion": "Once aligned, the learning can be promoted to authoritative status",
    "multiple_lessons": "If this contains multiple distinct learnings, let me know and I'll separate them"
  }
}
```

## State Management

### Save Context
```bash
python3 scripts/state_manager.py save <type> '<metadata_json>'
```

Saves a context with metadata for later retrieval:

**Example**:
```bash
python3 scripts/state_manager.py save analyze '{"key_insights": ["found_patterns"], "context_summary": "analysis_complete"}'
```

### List Active Contexts
```bash
python3 scripts/state_manager.py list
```

Shows currently active contexts with timestamps.

### Transfer Context
```bash
python3 scripts/state_manager.py transfer <context_id> <target_operation>
```

Transfers context metadata to a new operation for continuity.

## Common Workflows

### System Self-Assessment
1. Run self-determination analysis to check orchestration validity
2. Review relationship graph for documentation connections
3. Validate core documentation presence
4. Address any orchestration issues identified

### Quick Project Assessment
1. Analyze the codebase structure
2. Validate project configuration
3. Run self-determination analysis
4. Review all JSON outputs for comprehensive insights

### Development with Context Continuity
1. Save current operation context before starting work
2. Run analysis and validation as needed
3. Transfer context between related operations
4. List active contexts to maintain awareness of ongoing work

### Learning from Issues
1. Create task branch: `task_manager.py create "analyze_issue" "understand validation failures"`
2. Capture observation: `/learn "validation script fails when files missing"`
3. AI agent analyzes and provides categorization + content
4. Provide alignment feedback through iterations
5. Record iterations: `task_manager.py record-iteration task-id '{"feedback": "accurate analysis"}'`
6. Validate completion: `task_manager.py validate task-id`
7. Complete task: `task_manager.py complete task-id`

### Development Iteration
1. Run analysis before making changes
2. Implement modifications
3. Run validation to ensure structure integrity
4. Run self-determination to verify orchestration
5. Save context for future reference
6. If issues or insights arise, trigger learning: `/learn "specific observation"`
7. Analyze again to see structural changes

## Error Handling

The tool provides clear error messages for common issues:

- Non-existent paths: `"error": "Path /invalid/path does not exist"`
- Permission issues: Standard Python error messages
- Invalid arguments: Automatic help display

## Integration

AgentOS v9 is designed to be:
- **Scriptable**: JSON output for automation
- **Composable**: Can be used in larger workflows
- **Context-Aware**: State management preserves continuity across operations
- **Orchestration-Valid**: Self-determination ensures directive loading validity
- **Extensible**: New commands and scripts can be added following the established patterns