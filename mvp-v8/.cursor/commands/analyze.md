---
title: "/analyze - Context Analysis & Task Planning"
description: "Analyze recent conversation context to identify tasks, problems, and planning needs"
usage: "/analyze"
---

# `/analyze` - Context Analysis & Task Planning

**Purpose**: Analyze the recent conversation context to identify tasks, problems, learning opportunities, and planning needs. Performs intelligent context mining to understand what needs to be done based on what was just discussed.

**When to Use**:
- After discussing a task or problem that needs planning
- When you've described work that needs to be organized
- After identifying issues that need systematic resolution
- When you want to extract actionable items from conversation

## Context-Aware Analysis Workflow

The command analyzes recent conversation context to identify tasks and planning needs:

### How It Works

1. **Context Mining**: Analyzes recent chat messages (last 10-20 messages)
2. **Pattern Recognition**: Identifies tasks, problems, discoveries, and planning needs
3. **Task Synthesis**: Creates structured task plans from context
4. **DOE Alignment**: Validates planning against AgentOS requirements
5. **Recommendations**: Suggests next steps and improvements

### Context Analysis Patterns

#### Task Identification
- **Explicit requests**: "I need to...", "Let's implement...", "We should..."
- **Problem statements**: "The issue is...", "This doesn't work...", "We need to fix..."
- **Feature requests**: "Add feature...", "Implement...", "Create..."
- **Research questions**: "How do we...", "What about...", "Should we..."

#### Planning Elements Extraction
- **Objectives**: What needs to be achieved
- **Operations**: Steps or actions mentioned
- **Constraints**: Requirements, limitations, dependencies
- **Risks**: Potential issues or destructive operations

#### Learning Opportunities
- **Success patterns**: Effective approaches that worked
- **Failure analysis**: Problems encountered and lessons
- **Process insights**: Workflow improvements identified
- **System gaps**: Missing capabilities or tools

### Analysis Output

#### Task Plan Synthesis
```
📋 IDENTIFIED TASK PLAN
Task Type: [Inferred from context]
Objective: [Extracted measurable goal]
Operations: [Concrete steps identified]
Files: [Affected files mentioned]
Risks: [Potential issues flagged]
```

#### DOE Alignment Check
```
🔍 DOE ALIGNMENT AUDIT
✅ Directives: [Required docs identified and accessible]
✅ Gates: [Verification gates defined for task type]
✅ Safety: [Destructive operations identified with rollback plans]
✅ Evidence: [Sources authoritative and current]
⚠️ Gaps: [Missing planning elements or improvement opportunities]
```

#### Recommendations
```
💡 RECOMMENDED NEXT STEPS
1. [Immediate action items]
2. [Planning completions needed]
3. [Verification gates to run]
4. [Learning captures suggested]
```

### Usage Examples

**After discussing a feature:**
```
User: We need to add user authentication to handle logins securely.

Assistant: [analyzes context] → /analyze

Output:
📋 IDENTIFIED TASK PLAN
Task Type: Implementation / Feature
Objective: Users can securely log in to the application
Operations: Implement authentication system, add login/logout endpoints
Files: src/auth.py, tests/auth_test.py
Risks: Database schema changes (destructive - backup needed)
```

**After identifying a problem:**
```
User: The validation scripts are failing because of missing dependencies.

Assistant: [analyzes context] → /analyze

Output:
📋 IDENTIFIED TASK PLAN
Task Type: Maintenance
Objective: Validation scripts run successfully without dependency errors
Operations: Identify missing dependencies, add to requirements, test execution
Files: scripts/validate.py, requirements.txt
Risks: Potential breaking changes to existing scripts
```

### Context Window Considerations

#### Analysis Scope
- **Recent messages**: Last 10-20 messages for immediate context
- **Conversation thread**: Current topic and discussion flow
- **Artifact references**: Files, commands, or docs mentioned
- **User intent**: Goals and objectives expressed

#### Boundary Handling
- **Context limits**: Respects token constraints in analysis
- **Progressive analysis**: Can analyze broader context if needed
- **Reference linking**: Connects to existing artifacts and plans
- **State preservation**: Maintains analysis state across calls

### Integration with Planning System

#### Task Plan Enhancement
- **Gap filling**: Identifies missing planning elements
- **Risk assessment**: Flags potential issues from context
- **Dependency mapping**: Links related tasks and artifacts
- **Priority setting**: Suggests task sequencing and importance

#### Learning System Integration
- **Automatic capture**: Suggests `/learn` calls for insights found
- **Pattern recognition**: Identifies recurring issues or successes
- **Knowledge building**: Contributes to system improvement
- **Feedback loops**: Informs future context analysis

### Success Criteria

#### Effective Context Analysis
- **Task identification accuracy**: Correctly identifies intended tasks
- **Planning completeness**: Captures all essential planning elements
- **Risk awareness**: Identifies potential issues and constraints
- **Actionability**: Provides clear, executable next steps

#### User Experience
- **Context understanding**: Accurately interprets conversation intent
- **Helpful synthesis**: Creates useful task plans from discussion
- **Non-disruptive**: Doesn't require changing conversation flow
- **Progressive refinement**: Can be called multiple times for deeper analysis

## Related Documentation
- `docs/reference/agentos/architecture.md#doe-integrated-flow`
- `docs/reference/agentos/task-plan-spec.md`
- `docs/reference/agentos/self-awareness-framework.md`