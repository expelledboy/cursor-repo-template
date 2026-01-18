---
title: "Learning Workflow"
description: "Create and manage learning tasks for authentic evolution"
usage: "/learn"
---

# @directive docs/reference/agentos/learning-system.md
# @directive docs/reference/agentos/behavior-spec.md

# Learning Workflow Command

Creates learning tasks from assessment findings and manages the authentic evolution process.

## Purpose
This command transforms assessment insights into actionable learning objectives, tracking progress through detailed iterations and maintaining a comprehensive learning diary.

## Workflow Integration
- Analyzes current assessment task for findings and gaps
- Creates learning tasks with specific objectives and sub-objectives
- Tracks learning progress through detailed iteration recording
- Manages dependencies and blocking relationships between learning tasks
- Suggests next steps: `/improve` for implementation, `/reflect` for progress review

## Task Management Features
- **Sub-objectives**: Break complex learning into manageable components
- **Dependencies**: Track blocking relationships between learning tasks
- **Prioritization**: Dynamic reprioritization based on assessment insights
- **Deprecation**: Mark alternative approaches as deprecated when better paths found
- **Completion Tracking**: Validate learning outcomes against objectives

## Progress Diary Integration
Each learning interaction records:
- Learning objectives established
- Sub-objectives completed or deferred
- Dependencies identified and managed
- Prioritization decisions made
- Alternative routes explored and deprecated

## Related Commands
- `/assess` - Generate findings that drive learning objectives
- `/improve` - Implement learnings through concrete changes
- `/reflect` - Review learning progress and effectiveness
- `/prioritize` - Manage task prioritization and dependencies

---

*This command integrates with `scripts/task_manager.py` for comprehensive learning workflow management and maintains bidirectional alignment with `docs/reference/agentos/learning-system.md` for authentic task-based learning processes.*