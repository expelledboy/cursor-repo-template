---
title: "Self-Improvement Execution"
description: "Execute improvements identified through assessment and learning"
usage: "/improve"
---

# @directive docs/reference/agentos/authenticity-validation.md
# @directive docs/reference/agentos/behavior-spec.md

# Self-Improvement Execution Command

Implements concrete improvements identified through assessment and learning workflows, maintaining detailed progress tracking and validation.

## Purpose
This command transforms learning insights into actual system improvements, tracking what changes were made, why they were necessary, and their effectiveness.

## Workflow Integration
- Reviews current learning tasks for actionable improvements
- Creates improvement tasks with specific implementation steps
- Executes changes through appropriate scripts and validation
- Records detailed improvement diary with rationale and outcomes
- Suggests next steps: `/reflect` for progress review, `/assess` for impact validation

## Task Management Features
- **Improvement Tracking**: Records exactly what was improved and why
- **Implementation Steps**: Breaks improvements into verifiable sub-tasks
- **Validation Gates**: Ensures improvements work as intended
- **Rollback Capability**: Tracks changes for potential reversion
- **Dependency Management**: Handles blocking relationships for complex improvements

## Progress Diary Integration
Each improvement records:
- Assessment findings that drove the improvement
- Specific changes implemented
- Rationale for each change
- Validation results and effectiveness measures
- Unexpected challenges encountered and resolved

## Related Commands
- `/assess` - Identify areas needing improvement
- `/learn` - Develop understanding of required improvements
- `/reflect` - Review improvement effectiveness and lessons learned
- `/prioritize` - Manage improvement prioritization when multiple options exist

---

*This command integrates with `scripts/task_manager.py` for improvement tracking and maintains bidirectional alignment with `docs/reference/agentos/authenticity-validation.md` for authentic self-improvement processes.*