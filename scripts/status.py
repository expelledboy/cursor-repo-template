#!/usr/bin/env python3
"""Agent OS status command.

@implements docs/system/model/system-kernel-bootup.md
@implements docs/system/decision/require-bootup-and-awareness-maintenance.md
"""

import subprocess
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def get_git_state():
    """Get branch name, commits ahead, and staged file count."""
    try:
        # Get branch name
        branch = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True,
            text=True,
            cwd=ROOT,
        ).stdout.strip()
        if not branch:
            branch = "detached"

        # Get commits ahead of upstream
        ahead_result = subprocess.run(
            ["git", "rev-list", "--count", "@{u}..HEAD"],
            capture_output=True,
            text=True,
            cwd=ROOT,
        )
        if ahead_result.returncode == 0:
            ahead = ahead_result.stdout.strip()
        else:
            ahead = "?"

        # Get staged file count
        staged_result = subprocess.run(
            ["git", "diff", "--cached", "--numstat"],
            capture_output=True,
            text=True,
            cwd=ROOT,
        )
        staged_lines = [l for l in staged_result.stdout.strip().split("\n") if l]
        staged = len(staged_lines)

        return branch, ahead, staged
    except Exception:
        return "unknown", "?", 0


def get_objective():
    """Get active objective from objective graph if it exists."""
    obj_path = ROOT / "docs" / "work" / "objective-graph.yaml"
    if not obj_path.exists():
        return None

    try:
        import yaml
        with open(obj_path) as f:
            data = yaml.safe_load(f)

        if not data:
            return None

        active_id = data.get("active_objective_id")
        if not active_id:
            return None

        # Find the active objective
        objectives = data.get("objectives", [])
        for obj in objectives:
            if obj.get("objective_id") == active_id:
                next_action = obj.get("next_action") or None
                if next_action:
                    return f"{active_id} → {next_action}"
                return active_id

        return active_id
    except Exception:
        return "error reading"


def main():
    # Timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Git state
    branch, ahead, staged = get_git_state()

    # Objective
    objective = get_objective()
    obj_str = objective if objective else "none"

    # Output: exactly 2 lines per system-kernel-bootup.md contract
    print(f"Agent OS | {timestamp} | {branch} +{ahead} | {staged} staged")
    print(f"Objective: {obj_str}")


if __name__ == "__main__":
    main()
