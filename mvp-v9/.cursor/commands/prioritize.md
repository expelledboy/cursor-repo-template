---
title: "Task Prioritization Management"
description: "Manage complex task hierarchies with sub-objectives, dependencies, and dynamic prioritization"
usage: "/prioritize"
---

# @directive docs/reference/agentos/learning-system.md
# @directive docs/reference/agentos/task-plan-spec.md

# Task Prioritization Management Command

Provides sophisticated task management capabilities for complex self-determination workflows, including sub-objectives, blocking dependencies, deprecation of alternative routes, and dynamic reprioritization.

## Purpose
This command enables complex task management for authentic self-determination, allowing hierarchical task structures with dependencies and dynamic adaptation based on new insights.

## Workflow Integration
- Analyzes current task landscape and dependencies
- Creates hierarchical task structures with sub-objectives
- Manages blocking relationships and prerequisite validation
- Handles deprecation of alternative approaches when better paths emerge
- Implements dynamic reprioritization based on assessment findings
- Suggests workflow adjustments: `/assess` for priority reassessment, `/learn` for dependency management

## Advanced Task Management Features

### Hierarchical Objectives
- **Main Objectives**: High-level self-determination goals
- **Sub-objectives**: Break down complex objectives into manageable components
- **Completion Tracking**: Mark sub-objectives complete while maintaining main objective progress

### Dependency Management
- **Blocking Dependencies**: Tasks that must complete before others can proceed
- **Prerequisite Validation**: Ensure all dependencies are met before task execution
- **Dependency Chains**: Manage complex dependency relationships across task hierarchies

### Alternative Route Management
- **Route Exploration**: Track multiple approaches to the same objective
- **Deprecation Tracking**: Mark alternative routes as deprecated when better approaches found
- **Route Selection**: Choose optimal paths based on assessment insights and learning outcomes

### Dynamic Prioritization
- **Assessment-Driven**: Reprioritize based on new evidence and findings
- **Resource Allocation**: Adjust task focus based on available capacity and urgency
- **Impact-Based**: Prioritize tasks with highest self-determination impact

## Progress Diary Integration
Detailed tracking for all prioritization decisions:
- Sub-objectives established and their completion status
- Dependencies identified and blocking relationships managed
- Alternative routes explored and deprecated routes documented
- Prioritization decisions with rationale and expected impact
- Workflow adjustments and their justification

## Related Commands
- `/assess` - Generate evidence for prioritization decisions
- `/learn` - Understand dependencies and prerequisite relationships
- `/improve` - Implement prioritization-driven task reorganizations
- `/reflect` - Review prioritization effectiveness and adjustment patterns

---

*This command integrates with `scripts/task_manager.py` for advanced hierarchical task management and maintains bidirectional alignment with `docs/reference/agentos/learning-system.md` for complex task-based learning workflows.*