#!/usr/bin/env python3
"""
AgentOS MVP-v2 MCP Server
Structured validation tools for requirement and plan validation.

Exposes 3 validation tools:
- validate_requirement: Validate requirement structure (YAML schema)
- validate_plan: Validate plan structure
- validate_coherence: Check system coherence
"""

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

try:
    import yaml
    from jsonschema import validate, ValidationError
except ImportError:
    print("Error: Missing dependencies. Install: pip install pyyaml jsonschema", file=sys.stderr)
    sys.exit(1)

# MVP-v2 root
SCRIPT_DIR = Path(__file__).parent
MVP_ROOT = SCRIPT_DIR.parent.parent

# Load schemas
REQUIREMENT_SCHEMA_PATH = MVP_ROOT / "schemas" / "requirement.yaml"
DECISION_GRAPH_SCHEMA_PATH = MVP_ROOT / "schemas" / "decision-graph.yaml"


def load_yaml_schema(path: Path) -> Dict:
    """Load YAML schema file."""
    if not path.exists():
        return {}
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def create_result(status: str, message: str, details: List[Dict], scope: str) -> Dict:
    """Create standardized validation result."""
    return {
        "status": status,
        "message": message,
        "details": details,
        "metadata": {
            "execution_time": 0.0,
            "scope": scope,
            "version": "2.0.0",
            "timestamp": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
        }
    }


def validate_requirement(requirement_yaml: str) -> Dict:
    """Validate requirement structure against schema."""
    start_time = time.time()
    details = []
    scope = "requirement:validation"

    try:
        # Parse YAML
        requirement = yaml.safe_load(requirement_yaml)
        if not requirement:
            return create_result(
                "fail",
                "Requirement is empty or invalid YAML",
                [{
                    "severity": "critical",
                    "message": "Requirement must be valid YAML",
                    "remediation": "Check YAML syntax"
                }],
                scope
            )

        # Load schema
        schema = load_yaml_schema(REQUIREMENT_SCHEMA_PATH)
        if not schema:
            # Schema not found, do basic validation
            if "task" not in requirement:
                details.append({
                    "severity": "critical",
                    "message": "Missing 'task' field",
                    "remediation": "Add 'task:' field to requirement"
                })
            else:
                task = requirement["task"]
                required_fields = ["type", "objective", "scope", "success_criteria"]
                for field in required_fields:
                    if field not in task:
                        details.append({
                            "severity": "critical",
                            "message": f"Missing required field: task.{field}",
                            "remediation": f"Add 'task.{field}:' to requirement"
                        })
        else:
            # Validate against schema
            try:
                validate(instance=requirement, schema=schema)
            except ValidationError as e:
                details.append({
                    "severity": "critical",
                    "message": f"Schema validation failed: {e.message}",
                    "remediation": f"Fix validation error at: {'.'.join(str(p) for p in e.path)}"
                })

        # Additional semantic checks
        if "task" in requirement:
            task = requirement["task"]

            # Check objective length
            if "objective" in task:
                obj_len = len(task["objective"])
                if obj_len < 10:
                    details.append({
                        "severity": "warning",
                        "message": f"Objective too short ({obj_len} chars, minimum 10)",
                        "remediation": "Make objective more specific"
                    })
                elif obj_len > 200:
                    details.append({
                        "severity": "warning",
                        "message": f"Objective too long ({obj_len} chars, maximum 200)",
                        "remediation": "Split into multiple tasks or simplify"
                    })

            # Check domains
            if "scope" in task and "domains" in task["scope"]:
                if len(task["scope"]["domains"]) == 0:
                    details.append({
                        "severity": "critical",
                        "message": "At least one domain required",
                        "remediation": "Add domains to task.scope.domains"
                    })

        # Determine status
        critical_issues = [d for d in details if d["severity"] == "critical"]
        if critical_issues:
            status = "fail"
            message = f"Requirement validation failed: {len(critical_issues)} critical issue(s)"
        elif details:
            status = "warning"
            message = f"Requirement validation passed with {len(details)} warning(s)"
        else:
            status = "pass"
            message = "Requirement validation passed"

        result = create_result(status, message, details, scope)
        result["metadata"]["execution_time"] = time.time() - start_time
        return result

    except yaml.YAMLError as e:
        return create_result(
            "fail",
            f"YAML parse error: {str(e)}",
            [{
                "severity": "critical",
                "message": f"Invalid YAML: {str(e)}",
                "remediation": "Fix YAML syntax"
            }],
            scope
        )
    except Exception as e:
        return create_result(
            "fail",
            f"Validation error: {str(e)}",
            [{
                "severity": "critical",
                "message": f"Unexpected error: {str(e)}",
                "remediation": "Check requirement format"
            }],
            scope
        )


def validate_plan(plan_yaml: str) -> Dict:
    """Validate plan structure."""
    start_time = time.time()
    details = []
    scope = "plan:validation"

    try:
        plan = yaml.safe_load(plan_yaml)
        if not plan:
            return create_result(
                "fail",
                "Plan is empty or invalid YAML",
                [{
                    "severity": "critical",
                    "message": "Plan must be valid YAML",
                    "remediation": "Check YAML syntax"
                }],
                scope
            )

        # Basic structure checks
        required_fields = ["task_id", "type", "objective", "workflow", "steps", "success_criteria"]
        if "plan" not in plan:
            details.append({
                "severity": "critical",
                "message": "Missing 'plan' field",
                "remediation": "Add 'plan:' field"
            })
        else:
            plan_data = plan["plan"]
            for field in required_fields:
                if field not in plan_data:
                    details.append({
                        "severity": "critical",
                        "message": f"Missing required field: plan.{field}",
                        "remediation": f"Add 'plan.{field}:' to plan"
                    })

            # Check steps structure
            if "steps" in plan_data:
                steps = plan_data["steps"]
                if not isinstance(steps, list):
                    details.append({
                        "severity": "critical",
                        "message": "plan.steps must be a list",
                        "remediation": "Format steps as YAML list"
                    })
                else:
                    for i, step in enumerate(steps):
                        if not isinstance(step, dict):
                            details.append({
                                "severity": "critical",
                                "message": f"plan.steps[{i}] must be an object",
                                "remediation": "Format each step as YAML object"
                            })
                        else:
                            if "id" not in step:
                                details.append({
                                    "severity": "warning",
                                    "message": f"plan.steps[{i}] missing 'id' field",
                                    "remediation": "Add 'id:' to each step"
                                })
                            if "action" not in step:
                                details.append({
                                    "severity": "warning",
                                    "message": f"plan.steps[{i}] missing 'action' field",
                                    "remediation": "Add 'action:' to each step"
                                })

        # Determine status
        critical_issues = [d for d in details if d["severity"] == "critical"]
        if critical_issues:
            status = "fail"
            message = f"Plan validation failed: {len(critical_issues)} critical issue(s)"
        elif details:
            status = "warning"
            message = f"Plan validation passed with {len(details)} warning(s)"
        else:
            status = "pass"
            message = "Plan validation passed"

        result = create_result(status, message, details, scope)
        result["metadata"]["execution_time"] = time.time() - start_time
        return result

    except yaml.YAMLError as e:
        return create_result(
            "fail",
            f"YAML parse error: {str(e)}",
            [{
                "severity": "critical",
                "message": f"Invalid YAML: {str(e)}",
                "remediation": "Fix YAML syntax"
            }],
            scope
        )


def validate_coherence(scope: str = "all") -> Dict:
    """Comprehensive coherence check."""
    start_time = time.time()
    details = []

    # Check schemas exist
    if not REQUIREMENT_SCHEMA_PATH.exists():
        details.append({
            "severity": "warning",
            "message": f"Requirement schema not found: {REQUIREMENT_SCHEMA_PATH}",
            "remediation": "Create requirement schema"
        })

    if not DECISION_GRAPH_SCHEMA_PATH.exists():
        details.append({
            "severity": "warning",
            "message": f"Decision graph schema not found: {DECISION_GRAPH_SCHEMA_PATH}",
            "remediation": "Create decision graph schema"
        })

    # Check decision graphs exist
    decisions_dir = MVP_ROOT / "docs" / "reference" / "agentos" / "decisions"
    if decisions_dir.exists():
        required_graphs = ["task-classification.yaml", "complexity-assessment.yaml", "workflow-selection.yaml"]
        for graph in required_graphs:
            graph_path = decisions_dir / graph
            if not graph_path.exists():
                details.append({
                    "severity": "critical",
                    "message": f"Required decision graph missing: {graph}",
                    "remediation": f"Create decision graph at {graph_path}"
                })

    # Check workflows exist
    workflows_dir = MVP_ROOT / "docs" / "reference" / "agentos" / "workflows"
    if workflows_dir.exists():
        # At least one workflow should exist
        workflows = list(workflows_dir.glob("*.md"))
        if len(workflows) == 0:
            details.append({
                "severity": "warning",
                "message": "No workflow documentation found",
                "remediation": "Create workflow documentation"
            })

    # Determine status
    critical_issues = [d for d in details if d["severity"] == "critical"]
    if critical_issues:
        status = "fail"
        message = f"Coherence validation failed: {len(critical_issues)} critical issue(s), {len([d for d in details if d['severity'] == 'warning'])} warning(s)"
    elif details:
        status = "warning"
        message = f"Coherence validation passed with {len(details)} warning(s)"
    else:
        status = "pass"
        message = "Coherence validation passed"

    result = create_result(status, message, details, f"coherence:{scope}")
    result["metadata"]["execution_time"] = time.time() - start_time
    return result


# CLI interface
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: mcp_server.py <tool> [args...]")
        print("Tools: validate_requirement, validate_plan, validate_coherence")
        sys.exit(1)

    tool = sys.argv[1]

    if tool == "validate_requirement":
        if len(sys.argv) < 3:
            print("Usage: mcp_server.py validate_requirement <requirement_yaml_file>")
            sys.exit(1)
        with open(sys.argv[2], 'r') as f:
            requirement_yaml = f.read()
        result = validate_requirement(requirement_yaml)

    elif tool == "validate_plan":
        if len(sys.argv) < 3:
            print("Usage: mcp_server.py validate_plan <plan_yaml_file>")
            sys.exit(1)
        with open(sys.argv[2], 'r') as f:
            plan_yaml = f.read()
        result = validate_plan(plan_yaml)

    elif tool == "validate_coherence":
        scope = sys.argv[2] if len(sys.argv) > 2 else "all"
        result = validate_coherence(scope)

    else:
        print(f"Unknown tool: {tool}")
        sys.exit(1)

    print(json.dumps(result, indent=2))
