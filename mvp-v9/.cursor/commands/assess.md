---
title: "Self-Assessment"
description: "Begin authentic self-determination assessment workflow"
usage: "/assess"
---

# @directive docs/reference/agentos/behavior-spec.md
# @directive docs/reference/agentos/self-awareness.md

# Self-Assessment Command

Initiates the authentic self-determination assessment workflow for AgentOS v9.

## Purpose
This command creates a comprehensive self-assessment task that collects evidence, guides human analysis, and establishes the foundation for authentic self-improvement.

## Workflow Integration
- Creates assessment task with full context snapshot
- Automatically collects system, alignment, gap, and validation evidence
- Guides human analysis of findings through structured workflow
- Records detailed progress diary for self-determination journey
- Suggests next steps: `/learn` for evolution planning, `/improve` for implementation

## Task Management
- **Task Type**: self_determination
- **Task Name**: assessment-{timestamp}
- **Objective**: Complete authentic self-assessment of AgentOS v9 state
- **Iterations**: Evidence collection, human analysis, findings documentation

## Progress Diary
Each interaction records:
- Assessment phase completed
- Evidence analyzed
- Human insights gained
- Next workflow suggestions

## Related Commands
- `/learn` - Create learning tasks from assessment findings
- `/improve` - Implement improvements identified in assessment
- `/reflect` - Review assessment progress and insights

---

*This command integrates with `scripts/task_manager.py` for comprehensive task tracking and maintains bidirectional alignment with `docs/reference/agentos/behavior-spec.md` for authentic self-determination processes.*