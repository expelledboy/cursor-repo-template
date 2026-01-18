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

## Basic Usage

### Analyze a Codebase
```bash
./src/agentos.py analyze [path]
```

Analyzes the structure of a codebase and provides metrics:

- Total files and directories
- File type distribution
- Basic structural information

**Example**:
```bash
./src/agentos.py analyze .
```

**Output**:
```json
{
  "path": "/path/to/project",
  "type": "directory",
  "structure": {
    "total_files": 42,
    "total_dirs": 8,
    "file_types": {
      ".py": 25,
      ".md": 5,
      ".json": 3
    }
  }
}
```

### Validate a Project
```bash
./src/agentos.py validate [path]
```

Performs basic validation checks on a project structure:

- Directory/file existence
- Common project file detection
- Basic structural validation

**Example**:
```bash
./src/agentos.py validate /path/to/project
```

**Output**:
```json
{
  "path": "/path/to/project",
  "checks": [
    {
      "name": "directory_exists",
      "status": "pass",
      "message": "Target directory exists"
    },
    {
      "name": "project_files",
      "status": "pass",
      "message": "Found project files: ['README.md', 'package.json']"
    }
  ]
}
```

### Show Version
```bash
./src/agentos.py --version
```

Displays the current version of AgentOS v9.

### Collect Self-Determination Evidence
```bash
./src/agentos.py self-determination
```

Collects structured evidence for self-determination analysis (DOE E Layer operation):

- Gathers basic system facts (file counts, directory presence)
- Collects relationship graph evidence
- Validates directive structure presence
- Produces orchestration-ready evidence

**Output** (Evidence Collection):
```json
{
  "evidence_collection": {
    "collection_type": "self-determination",
    "timestamp": "2026-01-18T19:44:18.027177",
    "doe_layer": "execution",
    "doe_responsibility": "Collect structured evidence for self-determination analysis",
    "evidence_quality": "doe_compliant"
  },
  "system_facts": {
    "docs_count": 11,
    "scripts_count": 13,
    "src_count": 1,
    "total_files": 64,
    "directories_present": {
      "docs": true,
      "scripts": true,
      "src": true
    }
  },
  "relationship_evidence": {
    "renderer_status": "executed",
    "relationship_count": 12,
    "renderer_output_length": 423,
    "evidence_collected": true
  },
  "directive_evidence": {
    "docs_directory_exists": true,
    "core_docs_present": false,
    "validation_status": "evidence_collected"
  },
  "orchestration_ready": true
}
```

**Next Step**: Use orchestration layer analysis to interpret this evidence.
Performs comprehensive self-determination analysis with relationship graph orchestration:

- Renders relationship graph for all documentation
- Validates directive orchestration completeness
- Checks core documentation presence
- Provides orchestration status assessment

**Output**:
```json
{
  "analysis_type": "self-determination",
  "relationship_graph": {
    "status": "rendered",
    "output": "AGENTOS V9 RELATIONSHIP GRAPH\n========================================\n\nTotal relationships: 0\n\nCore directive loading validation:\n\u2713 Relationship graph rendered with 0 connections\n\u2713 Orchestration ready for directive validation"
  },
  "directive_validation": {
    "docs_found": 2,
    "core_docs_present": false,
    "status": "validated"
  },
  "meta_analysis": {
    "capability": "on-demand",
    "ai_agent_analysis_required": true,
    "analysis_types_available": [
      "system_coherence_assessment",
      "gap_identification",
      "evolution_opportunities",
      "authenticity_validation",
      "relationship_analysis"
    ]
  },
  "orchestration_status": "complete"
}
```

### Perform Learning Observation Capture
```bash
./src/agentos.py learn "observation text"
```

Captures learning observations for AI agent analysis:

- Stores observation without intelligent assumptions
- Creates task branch for learning objective
- Indicates AI agent analysis required
- Prepares for user alignment workflow

**Examples**:

**Text Observation**:
```bash
./src/agentos.py learn "validation script fails when files are missing"
```

**File Analysis**:
```bash
./src/agentos.py learn --file docs/work/analysis/result.md
```

**Output**:
```json
{
  "learning_type": "manual_capture",
  "observation": "validation script fails when files are missing",
  "capture_timestamp": "9.0.0",
  "ai_agent_analysis_required": true,
  "user_alignment_required": true,
  "next_steps": [
    "AI agent will analyze observation content",
    "AI agent will determine categorization (problem/discovery)",
    "AI agent will generate meaningful artifact content",
    "User will provide alignment feedback",
    "Iterate until user alignment achieved"
  ]
}
```

## Task Management

### Create Learning Task Branch
```bash
python3 scripts/task_manager.py create "task_name" "learning_objective"
```

Creates a new navigable task branch for learning objectives.

### Switch Between Task Branches
```bash
python3 scripts/task_manager.py switch task-id
```

Navigate to different learning task branches while preserving context.

### List Active Task Branches
```bash
python3 scripts/task_manager.py list
```

View all active learning task branches and their status.

### Record Learning Iteration
```bash
python3 scripts/task_manager.py record-iteration task-id '{"observation": "details", "ai_analysis": "categorization", "user_feedback": "alignment_status"}'
```

Track learning iteration history and progress.

### Validate Task Completion
```bash
python3 scripts/task_manager.py validate task-id
```

Perform deterministic validation that learning task meets completion criteria.

### Complete Learning Task
```bash
python3 scripts/task_manager.py complete task-id
```

Mark learning task as completed with full context preservation.

### Record Learning Feedback
```bash
python3 scripts/task_manager.py feedback task-id --message "your feedback here" --alignment pending|partial|complete
```

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