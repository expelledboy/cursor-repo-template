---
title: "Active Task Learning System"
status: stable
created_date: 2026-01-18
purpose: "Reference for AgentOS v9 active task learning capabilities with user alignment"
domain: agentos
authority_level: 1
doe_layer: directive
doe_responsibility: "Define learning system specifications and user alignment processes"
doe_governance: "Governed by doe-framework.md"
doe_precedence: 3
governed_by: ["docs/reference/agentos/doe-framework.md"]
governs: ["scripts/memory_bank_integrator.py", "scripts/workflow_coordinator.py", "scripts/task_manager.py"]
implementations: ["scripts/memory_bank_integrator.py", "scripts/workflow_coordinator.py", "scripts/task_manager.py"]
---

# @directive docs/reference/agentos/behavior-spec.md
# @directive docs/reference/agentos/self-awareness.md

# Active Task Learning System (Reference)

## Overview

AgentOS v9 implements an active task learning system that branches all learning operations and provides deterministic navigation between learning objectives. Scripts manage task state and workflow coordination while AI agents handle all intelligent analysis and content creation.

## Core Concepts

### Active Task Branching
- **Purpose**: Every learning operation creates a navigable task branch
- **Mechanism**: Task branches maintain complete learning context and history
- **Navigation**: Can always switch back to previous learning tasks
- **State**: Full context preservation across learning iterations

### Script Roles (No Intelligence Assumptions)
- **State Management**: Track task branches, context, and iteration history
- **Workflow Coordination**: Manage learning process flow and validation
- **Deterministic Operations**: Perform format checks, completeness validation, state transitions

### AI Agent Responsibilities
- **Categorization**: Determine problem vs discovery vs other learning types
- **Content Analysis**: Provide meaningful interpretation of observations
- **Artifact Creation**: Generate substantive learning content
- **User Alignment**: Handle feedback interpretation and refinement

### Advanced Task Management Features

#### Hierarchical Objectives
- **Main Objectives**: High-level learning goals (e.g., "improve self-determination")
- **Sub-objectives**: Break down complex objectives into manageable components
- **Completion Tracking**: Mark sub-objectives complete while maintaining main objective progress

#### Dependency Management
- **Blocking Dependencies**: Tasks that must complete before others can proceed
- **Prerequisite Validation**: Ensure all dependencies are met before task execution
- **Dependency Chains**: Manage complex interdependencies across learning workflows

#### Alternative Route Exploration
- **Route Exploration**: Track multiple approaches to the same learning objective
- **Deprecation Tracking**: Mark alternative routes as deprecated when better approaches found
- **Route Selection**: Choose optimal learning paths based on effectiveness

#### Dynamic Prioritization
- **Assessment-Driven**: Reprioritize learning tasks based on new evidence and findings
- **Resource Allocation**: Adjust learning focus based on available capacity and urgency
- **Impact-Based**: Prioritize learning with highest self-improvement impact

#### Progress Diary
- **Comprehensive Tracking**: Record all learning activities and insights
- **Assessment Findings**: Document what was discovered during assessments
- **Improvements Made**: Track specific changes implemented
- **Challenges Encountered**: Record obstacles and how they were overcome
- **Lessons Learned**: Capture insights for future learning cycles

## Technical Implementation

### Task Branch Structure
```yaml
active_tasks:
  learning-20260118-160000:
    task_id: learning-20260118-160000
    task_name: analyze_validation_failures
    objective: understand validation script failures
    task_type: learning
    created_at: "2026-01-18T16:00:00"
    status: active
    iterations: []
    context_snapshot:
      last_updated: "2026-01-18T16:00:00"
      snapshot_type: context_preservation
    validation_status: pending
```

### Task Operations

#### Create Task Branch
```bash
python3 scripts/task_manager.py create "analyze_validation_failures" "understand validation script failures"
```
- Creates new navigable task branch
- Sets as current active task
- Initializes context tracking

#### Switch Task Context
```bash
python3 scripts/task_manager.py switch learning-20260118-160000
```
- Saves current task context
- Loads target task context
- Maintains learning continuity

#### Record Learning Iteration
```bash
python3 scripts/task_manager.py record-iteration learning-20260118-160000 '{"observation": "validation fails on missing files", "ai_analysis": "categorized as problem", "user_feedback": "accurate categorization"}'
```
- Tracks iteration history
- Preserves learning progression
- Enables validation of completeness

#### Validate Task Completion
```bash
python3 scripts/task_manager.py validate learning-20260118-160000
```
- **Deterministic Checks**: Has iterations, has context, user alignment complete
- **Script-Only Validation**: Format compliance, structural completeness
- **AI Validation**: Semantic correctness (handled separately)

## Learning Workflow

### 1. Task Creation
- User creates learning task branch
- Script initializes task structure
- Context preservation begins

### 2. Observation Capture
- User provides learning observation
- Script captures without analysis
- Indicates AI agent analysis required

### 3. AI Agent Analysis
- AI determines categorization and content
- AI generates meaningful artifacts
- AI provides alignment guidance

### 4. User Alignment Iterations
- User provides feedback on AI analysis
- Script tracks iteration history
- Process continues until alignment achieved

### 5. Completion Validation
- Script validates structural completeness
- AI validates semantic correctness
- Task marked complete when both validations pass

## Integration with Learning Commands

### `/learn` Command Integration
```bash
# User triggers learning
/learn "validation script fails on missing files"

# Script captures observation
# AI agent analyzes and categorizes
# User provides alignment feedback
# Script tracks iterations
# Process completes with validation
```

### Task Branch Navigation
- Learning commands automatically create/switch task branches
- Users can navigate learning history via task manager
- Context preserved across learning sessions

## Deterministic Validation Types

### Script-Performed Validations
- **Task Structure**: Required fields present, proper YAML format
- **Iteration Tracking**: Iterations recorded, timestamps valid
- **Context Preservation**: Snapshots exist, properly formatted
- **Completion Criteria**: All required validations pass

### AI-Performed Validations
- **Content Accuracy**: Learning content correctly represents observations
- **Categorization Validity**: Problem vs discovery determination accurate
- **User Alignment**: Feedback properly incorporated, alignment achieved

## Safety & Determinism

### Task Branch Isolation
- Each learning task maintains separate context
- No cross-contamination between learning objectives
- Clear boundaries between active and completed tasks

### Validation Determinism
- Script validations return clear pass/fail results
- No ambiguous outcomes or probabilistic results
- Consistent validation across all learning tasks

### Context Preservation
- Automatic snapshots on task switches
- Complete iteration history maintained
- Reliable reloading of previous learning states

## Usage Patterns

### Problem Learning Workflow
1. Create task: `task_manager.py create "fix_validation" "resolve validation failures"`
2. Capture observation: `/learn "script fails when files missing"`
3. AI analyzes, categorizes as problem, generates content
4. User provides alignment feedback: `task_manager.py feedback learning-20260118-160000 --message "accurate categorization but need more context" --alignment partial`
5. Iterate based on feedback until alignment achieved
6. Script validates completion: `task_manager.py validate learning-20260118-160000`
7. Mark complete: `task_manager.py complete learning-20260118-160000`

### Discovery Learning Workflow
1. Create task branch for investigation
2. Capture observations as they're made
3. AI identifies patterns and insights
4. Iterate on discovery articulation
5. Validate and complete task

### Multi-Objective Learning
1. Create separate branches for different learning objectives
2. Switch between branches as focus changes
3. Context preserved for each objective
4. Navigate learning history as needed

## Extension Points

The active task learning system supports extension through:
- Additional task types beyond learning
- Custom validation rules for different objectives
- Enhanced context snapshot mechanisms
- Integration with external task management systems
- Advanced iteration tracking and analytics