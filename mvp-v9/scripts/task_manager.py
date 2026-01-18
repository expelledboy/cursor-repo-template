#!/usr/bin/env python3
"""
Active Task Engine for AgentOS v9

Manages task branches for deterministic context reloading.
Provides navigation between active learning objectives.

DOE Registry - Bidirectional Linkages:
@directive docs/reference/agentos/architecture.md

# DOE Layer Declaration
DOE_LAYER = "execution"
DOE_RESPONSIBILITY = "Task branch management and learning workflow orchestration"
DOE_GOVERNANCE = "docs/reference/agentos/doe-framework.md"
DOE_PRECEDENCE = 4
"""

import argparse
import yaml
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional

class ActiveTaskEngine:
    """Manages active task branches with context preservation."""

    def __init__(self):
        self.tasks_dir = Path("docs/local/tasks")
        self.tasks_file = self.tasks_dir / "active-tasks.yaml"
        self.current_task_file = self.tasks_dir / "current-task.yaml"
        self._ensure_tasks_dir()

    def _ensure_tasks_dir(self):
        """Ensure tasks directory exists."""
        self.tasks_dir.mkdir(parents=True, exist_ok=True)

    def create_task_branch(self, task_name: str, objective: str, task_type: str = "learning") -> str:
        """Create a new task branch with context."""
        tasks = self._load_tasks_state()

        task_id = f"{task_type}-{datetime.now().strftime('%Y%m%d-%H%M%S')}"

        task_data = {
            "task_id": task_id,
            "task_name": task_name,
            "objective": objective,
            "task_type": task_type,
            "created_at": datetime.now().isoformat(),
            "status": "active",
            "iterations": [],
            "context_snapshot": {},
            "validation_status": "pending",
            # Advanced task management features
            "hierarchy": {
                "parent_task": None,
                "sub_objectives": [],
                "completed_sub_objectives": []
            },
            "dependencies": {
                "blocking_tasks": [],  # Tasks that must complete before this one
                "blocked_by": [],      # Tasks this one is waiting for
                "prerequisites": []    # Non-task prerequisites
            },
            "prioritization": {
                "priority_level": "medium",  # high, medium, low
                "priority_score": 5,         # 1-10 scale
                "reprioritization_history": []
            },
            "alternative_routes": {
                "explored_routes": [],
                "deprecated_routes": [],
                "selected_route": None
            },
            "progress_diary": {
                "assessment_findings": [],
                "improvements_made": [],
                "challenges_encountered": [],
                "lessons_learned": []
            }
        }

        tasks["active_tasks"][task_id] = task_data
        self._save_tasks_state(tasks)

        # Set as current task
        self._set_current_task(task_id)

        return task_id

    def switch_to_task(self, task_id: str) -> bool:
        """Switch context to a different task branch."""
        tasks = self._load_tasks_state()

        if task_id not in tasks["active_tasks"]:
            return False

        # Save current task context before switching
        current_task_id = self._get_current_task_id()
        if current_task_id:
            self._snapshot_task_context(current_task_id)

        # Switch to new task
        self._set_current_task(task_id)

        # Load task context
        self._load_task_context(task_id)

        return True

    def list_active_tasks(self) -> Dict[str, Any]:
        """List all active task branches."""
        tasks = self._load_tasks_state()
        return tasks["active_tasks"]

    def record_iteration(self, task_id: str, iteration_data: Dict[str, Any]) -> bool:
        """Record a learning iteration for a task."""
        tasks = self._load_tasks_state()

        if task_id not in tasks["active_tasks"]:
            return False

        iteration = {
            "timestamp": datetime.now().isoformat(),
            "data": iteration_data,
            "iteration_type": iteration_data.get("type", "general"),
            "user_feedback": iteration_data.get("user_feedback", ""),
            "ai_agent_response": iteration_data.get("ai_agent_response", ""),
            "alignment_status": iteration_data.get("alignment_status", "pending")
        }

        if "iterations" not in tasks["active_tasks"][task_id]:
            tasks["active_tasks"][task_id]["iterations"] = []

        tasks["active_tasks"][task_id]["iterations"].append(iteration)

        # Update user alignment status if provided
        if "user_alignment_complete" in iteration_data:
            tasks["active_tasks"][task_id]["validation_status"] = "user_aligned" if iteration_data["user_alignment_complete"] else "iterating"

        self._save_tasks_state(tasks)

        return True

    def add_sub_objective(self, task_id: str, sub_objective: str, description: str = "") -> bool:
        """Add a sub-objective to a task."""
        tasks = self._load_tasks_state()

        if task_id not in tasks["active_tasks"]:
            return False

        sub_obj_data = {
            "id": f"{task_id}-sub-{len(tasks['active_tasks'][task_id]['hierarchy']['sub_objectives'])}",
            "objective": sub_objective,
            "description": description,
            "created_at": datetime.now().isoformat(),
            "status": "pending"
        }

        tasks["active_tasks"][task_id]["hierarchy"]["sub_objectives"].append(sub_obj_data)
        self._save_tasks_state(tasks)
        return True

    def complete_sub_objective(self, task_id: str, sub_objective_id: str) -> bool:
        """Mark a sub-objective as completed."""
        tasks = self._load_tasks_state()

        if task_id not in tasks["active_tasks"]:
            return False

        task = tasks["active_tasks"][task_id]

        # Find and move sub-objective to completed
        for i, sub_obj in enumerate(task["hierarchy"]["sub_objectives"]):
            if sub_obj["id"] == sub_objective_id:
                sub_obj["completed_at"] = datetime.now().isoformat()
                sub_obj["status"] = "completed"
                task["hierarchy"]["completed_sub_objectives"].append(sub_obj)
                task["hierarchy"]["sub_objectives"].pop(i)
                break

        self._save_tasks_state(tasks)
        return True

    def add_blocking_dependency(self, task_id: str, blocking_task_id: str, reason: str = "") -> bool:
        """Add a blocking dependency to a task."""
        tasks = self._load_tasks_state()

        if task_id not in tasks["active_tasks"]:
            return False

        dependency_data = {
            "blocking_task_id": blocking_task_id,
            "reason": reason,
            "added_at": datetime.now().isoformat(),
            "status": "active"
        }

        # Add to this task's blocked_by list
        tasks["active_tasks"][task_id]["dependencies"]["blocked_by"].append(dependency_data)

        # Add to blocking task's blocking_tasks list
        if blocking_task_id in tasks["active_tasks"]:
            blocking_data = {
                "blocked_task_id": task_id,
                "reason": reason,
                "added_at": datetime.now().isoformat()
            }
            tasks["active_tasks"][blocking_task_id]["dependencies"]["blocking_tasks"].append(blocking_data)

        self._save_tasks_state(tasks)
        return True

    def deprecate_alternative_route(self, task_id: str, route_description: str, deprecation_reason: str) -> bool:
        """Deprecate an alternative route that was explored."""
        tasks = self._load_tasks_state()

        if task_id not in tasks["active_tasks"]:
            return False

        route_data = {
            "description": route_description,
            "deprecated_at": datetime.now().isoformat(),
            "reason": deprecation_reason
        }

        tasks["active_tasks"][task_id]["alternative_routes"]["deprecated_routes"].append(route_data)
        self._save_tasks_state(tasks)
        return True

    def reprioritize_task(self, task_id: str, new_priority: str, reason: str) -> bool:
        """Change task priority with historical tracking."""
        tasks = self._load_tasks_state()

        if task_id not in tasks["active_tasks"]:
            return False

        old_priority = tasks["active_tasks"][task_id]["prioritization"]["priority_level"]
        old_score = tasks["active_tasks"][task_id]["prioritization"]["priority_score"]

        # Update priority
        tasks["active_tasks"][task_id]["prioritization"]["priority_level"] = new_priority
        tasks["active_tasks"][task_id]["prioritization"]["priority_score"] = self._priority_to_score(new_priority)

        # Record history
        history_entry = {
            "changed_at": datetime.now().isoformat(),
            "old_priority": old_priority,
            "new_priority": new_priority,
            "old_score": old_score,
            "new_score": tasks["active_tasks"][task_id]["prioritization"]["priority_score"],
            "reason": reason
        }

        tasks["active_tasks"][task_id]["prioritization"]["reprioritization_history"].append(history_entry)
        self._save_tasks_state(tasks)
        return True

    def _priority_to_score(self, priority: str) -> int:
        """Convert priority level to numeric score."""
        priority_map = {"low": 3, "medium": 5, "high": 8}
        return priority_map.get(priority, 5)

    def record_progress_diary(self, task_id: str, diary_type: str, entry: str) -> bool:
        """Record an entry in the progress diary."""
        tasks = self._load_tasks_state()

        if task_id not in tasks["active_tasks"]:
            return False

        diary_entry = {
            "timestamp": datetime.now().isoformat(),
            "type": diary_type,
            "entry": entry
        }

        diary_types = {
            "assessment": "assessment_findings",
            "improvement": "improvements_made",
            "challenge": "challenges_encountered",
            "lesson": "lessons_learned"
        }

        if diary_type in diary_types:
            tasks["active_tasks"][task_id]["progress_diary"][diary_types[diary_type]].append(diary_entry)

        self._save_tasks_state(tasks)
        return True

    def validate_task_completion(self, task_id: str) -> Dict[str, Any]:
        """Validate that a task meets completion criteria."""
        tasks = self._load_tasks_state()

        if task_id not in tasks["active_tasks"]:
            return {"valid": False, "error": "Task not found"}

        task = tasks["active_tasks"][task_id]

        validation = {
            "task_id": task_id,
            "has_iterations": len(task.get("iterations", [])) > 0,
            "has_context": bool(task.get("context_snapshot")),
            "user_alignment_complete": task.get("validation_status") == "user_aligned",
            "valid": False
        }

        # Deterministic validation: task must have iterations and user alignment
        validation["valid"] = (
            validation["has_iterations"] and
            validation["has_context"] and
            validation["user_alignment_complete"]
        )

        return validation

    def complete_task(self, task_id: str) -> bool:
        """Mark a task as completed."""
        tasks = self._load_tasks_state()

        if task_id not in tasks["active_tasks"]:
            return False

        tasks["active_tasks"][task_id]["status"] = "completed"
        tasks["active_tasks"][task_id]["completed_at"] = datetime.now().isoformat()

        self._save_tasks_state(tasks)
        return True

    def _load_tasks_state(self) -> Dict[str, Any]:
        """Load tasks state from file."""
        if not self.tasks_file.exists():
            return {"active_tasks": {}}

        try:
            with open(self.tasks_file, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f) or {"active_tasks": {}}
        except Exception:
            return {"active_tasks": {}}

    def _save_tasks_state(self, tasks: Dict[str, Any]):
        """Save tasks state to file."""
        with open(self.tasks_file, 'w', encoding='utf-8') as f:
            yaml.safe_dump(tasks, f, sort_keys=False)

    def _get_current_task_id(self) -> Optional[str]:
        """Get the currently active task ID."""
        if not self.current_task_file.exists():
            return None

        try:
            with open(self.current_task_file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                return data.get("current_task_id")
        except Exception:
            return None

    def _set_current_task(self, task_id: str):
        """Set the currently active task."""
        current_data = {"current_task_id": task_id, "switched_at": datetime.now().isoformat()}
        with open(self.current_task_file, 'w', encoding='utf-8') as f:
            yaml.safe_dump(current_data, f)

    def _snapshot_task_context(self, task_id: str):
        """Take a snapshot of current task context for lossy scenario recovery."""
        tasks = self._load_tasks_state()
        if task_id in tasks["active_tasks"]:
            # Enhanced context snapshot for lossy scenarios
            task = tasks["active_tasks"][task_id]
            iterations = task.get("iterations", [])

            # Analyze iteration patterns and learning progress
            iteration_analysis = self._analyze_iteration_patterns(iterations)

            # Capture current state comprehensively
            context_snapshot = {
                "timestamp": datetime.now().isoformat(),
                "snapshot_type": "enhanced_context_preservation",
                "task_metadata": {
                    "objective": task.get("objective", ""),
                    "iterations_count": len(iterations),
                    "last_iteration_timestamp": iterations[-1]["timestamp"] if iterations else None,
                    "user_alignment_status": task.get("validation_status", "unknown")
                },
                "iteration_analysis": iteration_analysis,
                "recovery_context": {
                    "can_resume_from_last_iteration": len(iterations) > 0,
                    "suggested_next_action": self._suggest_next_action(iterations, task.get("validation_status")),
                    "context_loss_risk": self._assess_context_loss_risk(iterations)
                }
            }

            # Store compressed context for efficient recovery
            tasks["active_tasks"][task_id]["context_snapshot"] = context_snapshot
            self._save_tasks_state(tasks)

    def _load_task_context(self, task_id: str):
        """Load task context (placeholder for future context reloading)."""
        # This would reload directive states, validation gates, etc.
        pass

    def _analyze_iteration_patterns(self, iterations: list) -> dict:
        """Analyze patterns in learning iterations for context preservation."""
        if not iterations:
            return {"pattern": "no_iterations", "insights": []}

        # Analyze feedback patterns
        feedback_patterns = []
        alignment_progression = []

        for iteration in iterations:
            data = iteration.get("data", {})
            if data.get("type") == "user_feedback":
                feedback_patterns.append({
                    "alignment_status": data.get("alignment_status", "unknown"),
                    "feedback_length": len(data.get("user_feedback", ""))
                })
                alignment_progression.append(data.get("alignment_status", "unknown"))

        return {
            "total_iterations": len(iterations),
            "feedback_patterns": feedback_patterns,
            "alignment_progression": alignment_progression,
            "iteration_frequency": self._calculate_iteration_frequency(iterations),
            "insights": self._extract_iteration_insights(iterations)
        }

    def _suggest_next_action(self, iterations: list, validation_status: str) -> str:
        """Suggest next action based on iteration history and validation status."""
        if validation_status == "user_aligned":
            return "validate_completion_and_complete_task"

        if not iterations:
            return "await_first_iteration"

        last_iteration = iterations[-1]
        data = last_iteration.get("data", {})

        if data.get("alignment_status") == "pending":
            return "provide_additional_guidance"
        elif data.get("alignment_status") == "partial":
            return "continue_iteration_with_refinements"
        else:
            return "await_user_feedback"

    def _assess_context_loss_risk(self, iterations: list) -> str:
        """Assess risk of context loss based on iteration patterns."""
        if not iterations:
            return "low"

        # Analyze time gaps between iterations
        timestamps = [datetime.fromisoformat(iteration["timestamp"]) for iteration in iterations]
        if len(timestamps) > 1:
            gaps = [(timestamps[i] - timestamps[i-1]).total_seconds() / 3600 for i in range(1, len(timestamps))]  # hours
            avg_gap = sum(gaps) / len(gaps)

            if avg_gap > 24:  # More than a day between iterations
                return "high"
            elif avg_gap > 6:  # More than 6 hours
                return "medium"
            else:
                return "low"
        else:
            return "low"

    def _calculate_iteration_frequency(self, iterations: list) -> float:
        """Calculate average iterations per day."""
        if len(iterations) < 2:
            return 0.0

        timestamps = [datetime.fromisoformat(iteration["timestamp"]) for iteration in iterations]
        time_span = (timestamps[-1] - timestamps[0]).total_seconds() / 86400  # days

        return len(iterations) / max(time_span, 1)  # iterations per day

    def _extract_iteration_insights(self, iterations: list) -> list:
        """Extract insights from iteration patterns."""
        insights = []

        if len(iterations) >= 3:
            # Check for feedback consistency
            alignment_statuses = [i.get("data", {}).get("alignment_status") for i in iterations]
            if alignment_statuses.count("pending") > len(alignment_statuses) * 0.7:
                insights.append("frequent_pending_status_suggests_guidance_needed")

            # Check for rapid progression
            if "complete" in alignment_statuses and alignment_statuses.index("complete") <= len(alignment_statuses) * 0.3:
                insights.append("rapid_alignment_progression")

        return insights

# CLI Interface
def main():
    parser = argparse.ArgumentParser(description='Active Task Engine for AgentOS v9')
    subparsers = parser.add_subparsers(dest='command')

    # Create task
    create_parser = subparsers.add_parser('create', help='Create new task branch')
    create_parser.add_argument('name', help='Task name')
    create_parser.add_argument('objective', help='Task objective')
    create_parser.add_argument('--type', default='learning', help='Task type')

    # Switch task
    switch_parser = subparsers.add_parser('switch', help='Switch to task branch')
    switch_parser.add_argument('task_id', help='Task ID to switch to')

    # List tasks
    subparsers.add_parser('list', help='List active task branches')

    # Record iteration
    record_parser = subparsers.add_parser('record-iteration', help='Record learning iteration')
    record_parser.add_argument('task_id', help='Task ID')
    record_parser.add_argument('data', help='Iteration data as JSON string')

    # Validate completion
    validate_parser = subparsers.add_parser('validate', help='Validate task completion')
    validate_parser.add_argument('task_id', help='Task ID to validate')

    # Complete task
    complete_parser = subparsers.add_parser('complete', help='Mark task as completed')
    complete_parser.add_argument('task_id', help='Task ID to complete')

    # Record learning feedback
    feedback_parser = subparsers.add_parser('feedback', help='Record learning feedback for alignment')
    feedback_parser.add_argument('task_id', help='Task ID')
    feedback_parser.add_argument('--message', required=True, help='User feedback message')
    feedback_parser.add_argument('--alignment', choices=['pending', 'partial', 'complete'], default='pending', help='Alignment status')

    # Advanced task management commands
    sub_obj_parser = subparsers.add_parser('add-sub-objective', help='Add sub-objective to task')
    sub_obj_parser.add_argument('task_id', help='Task ID')
    sub_obj_parser.add_argument('objective', help='Sub-objective description')
    sub_obj_parser.add_argument('--description', help='Detailed description')

    complete_sub_parser = subparsers.add_parser('complete-sub-objective', help='Mark sub-objective as completed')
    complete_sub_parser.add_argument('task_id', help='Task ID')
    complete_sub_parser.add_argument('sub_objective_id', help='Sub-objective ID')

    dependency_parser = subparsers.add_parser('add-dependency', help='Add blocking dependency')
    dependency_parser.add_argument('task_id', help='Task ID to add dependency to')
    dependency_parser.add_argument('blocking_task_id', help='Task ID that blocks this one')
    dependency_parser.add_argument('--reason', help='Reason for dependency')

    deprecate_parser = subparsers.add_parser('deprecate-route', help='Deprecate alternative route')
    deprecate_parser.add_argument('task_id', help='Task ID')
    deprecate_parser.add_argument('route_description', help='Description of deprecated route')
    deprecate_parser.add_argument('--reason', required=True, help='Reason for deprecation')

    prioritize_parser = subparsers.add_parser('reprioritize', help='Change task priority')
    prioritize_parser.add_argument('task_id', help='Task ID')
    prioritize_parser.add_argument('priority', choices=['low', 'medium', 'high'], help='New priority level')
    prioritize_parser.add_argument('--reason', required=True, help='Reason for reprioritization')

    diary_parser = subparsers.add_parser('record-diary', help='Record progress diary entry')
    diary_parser.add_argument('task_id', help='Task ID')
    diary_parser.add_argument('diary_type', choices=['assessment', 'improvement', 'challenge', 'lesson'], help='Type of diary entry')
    diary_parser.add_argument('entry', help='Diary entry content')

    args = parser.parse_args()

    engine = ActiveTaskEngine()

    if args.command == 'create':
        task_id = engine.create_task_branch(args.name, args.objective, args.type)
        print(f"Created task branch: {task_id}")

    elif args.command == 'switch':
        if engine.switch_to_task(args.task_id):
            print(f"Switched to task: {args.task_id}")
        else:
            print(f"Task not found: {args.task_id}")

    elif args.command == 'add-sub-objective':
        if engine.add_sub_objective(args.task_id, args.objective, args.description or ""):
            print(f"Added sub-objective to task: {args.task_id}")
        else:
            print(f"Task not found: {args.task_id}")

    elif args.command == 'complete-sub-objective':
        if engine.complete_sub_objective(args.task_id, args.sub_objective_id):
            print(f"Completed sub-objective in task: {args.task_id}")
        else:
            print(f"Failed to complete sub-objective")

    elif args.command == 'add-dependency':
        if engine.add_blocking_dependency(args.task_id, args.blocking_task_id, args.reason or ""):
            print(f"Added dependency: {args.blocking_task_id} blocks {args.task_id}")
        else:
            print(f"Failed to add dependency")

    elif args.command == 'deprecate-route':
        if engine.deprecate_alternative_route(args.task_id, args.route_description, args.reason):
            print(f"Deprecated alternative route in task: {args.task_id}")
        else:
            print(f"Task not found: {args.task_id}")

    elif args.command == 'reprioritize':
        if engine.reprioritize_task(args.task_id, args.priority, args.reason):
            print(f"Reprioritized task {args.task_id} to {args.priority}")
        else:
            print(f"Task not found: {args.task_id}")

    elif args.command == 'record-diary':
        if engine.record_progress_diary(args.task_id, args.diary_type, args.entry):
            print(f"Recorded {args.diary_type} diary entry for task: {args.task_id}")
        else:
            print(f"Task not found: {args.task_id}")

    elif args.command == 'list':
        tasks = engine.list_active_tasks()
        if tasks:
            print("Active task branches:")
            for task_id, task_data in tasks.items():
                status = task_data.get('status', 'unknown')
                objective = task_data.get('objective', 'no objective')
                print(f"  {task_id}: {status} - {objective}")
        else:
            print("No active task branches")

    elif args.command == 'record-iteration':
        import json
        try:
            data = json.loads(args.data)
            if engine.record_iteration(args.task_id, data):
                print(f"Recorded iteration for task: {args.task_id}")
            else:
                print(f"Task not found: {args.task_id}")
        except json.JSONDecodeError:
            print("Invalid JSON data")

    elif args.command == 'validate':
        validation = engine.validate_task_completion(args.task_id)
        if validation["valid"]:
            print(f"✅ Task {args.task_id} is complete and valid")
        else:
            print(f"❌ Task {args.task_id} validation failed:")
            for key, value in validation.items():
                if key.startswith('has_') and not value:
                    print(f"  - Missing: {key.replace('has_', '')}")

    elif args.command == 'complete':
        if engine.complete_task(args.task_id):
            print(f"Marked task as completed: {args.task_id}")
        else:
            print(f"Task not found: {args.task_id}")

    elif args.command == 'feedback':
        feedback_data = {
            "type": "user_feedback",
            "user_feedback": args.message,
            "alignment_status": args.alignment,
            "user_alignment_complete": args.alignment == "complete"
        }

        if engine.record_iteration(args.task_id, feedback_data):
            print(f"Recorded feedback for task: {args.task_id}")
            print(f"Alignment status: {args.alignment}")

            # Provide guidance based on alignment status
            if args.alignment == "pending":
                print("Guidance: Consider what specific aspects need refinement")
            elif args.alignment == "partial":
                print("Guidance: Good progress - continue iterating on remaining gaps")
            elif args.alignment == "complete":
                print("Guidance: Alignment achieved - validate task completion")
        else:
            print(f"Task not found: {args.task_id}")

if __name__ == '__main__':
    main()