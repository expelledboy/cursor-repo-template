#!/usr/bin/env python3
"""
AgentOS MVP-v4 MCP Server
Structure validation tools with semantic metadata and pattern library support.

Exposes 4 validation tools:
- validate_requirement: Validate requirement structure + semantic metadata
- validate_plan: Validate plan structure + semantic metadata
- validate_coherence: Check system coherence
- validate_pattern: Validate pattern library entry structure
"""

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    import yaml
    from jsonschema import validate, ValidationError
except ImportError:
    print("Error: Missing dependencies. Install: pip install pyyaml jsonschema", file=sys.stderr)
    sys.exit(1)

# MVP-v4 root
SCRIPT_DIR = Path(__file__).parent
MVP_ROOT = SCRIPT_DIR.parent.parent

# Load schemas
REQUIREMENT_SCHEMA_PATH = MVP_ROOT / "schemas" / "requirement.yaml"
PLAN_SCHEMA_PATH = MVP_ROOT / "schemas" / "plan.yaml"
PATTERN_SCHEMA_PATH = MVP_ROOT / "schemas" / "pattern.yaml"


def load_yaml_schema(path: Path) -> Dict:
    """Load YAML schema file."""
    if not path.exists():
        return {}
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def create_result(status: str, message: str, details: List[Dict], scope: str, semantic_metadata: Optional[Dict] = None) -> Dict:
    """Create standardized validation result with semantic metadata."""
    result = {
        "status": status,
        "message": message,
        "details": details,
        "metadata": {
            "execution_time": 0.0,
            "scope": scope,
            "version": "3.0.0",
            "timestamp": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
        }
    }

    if semantic_metadata:
        result["semantic_metadata"] = semantic_metadata

    return result


def extract_semantic_metadata(requirement: Dict) -> Dict:
    """Extract semantic metadata from requirement."""
    metadata = {
        "domains_detected": [],
        "objective_type": None,
        "scope_indicators": [],
        "complexity_hints": []
    }

    if "task" in requirement:
        task = requirement["task"]

        # Extract domains
        if "scope" in task and "domains" in task["scope"]:
            metadata["domains_detected"] = task["scope"].get("domains", [])

        # Extract objective type hints
        if "objective" in task:
            objective = task["objective"].lower()
            if any(word in objective for word in ["implement", "add", "create", "build"]):
                metadata["objective_type"] = "implementation"
            elif any(word in objective for word in ["coordinate", "align", "consensus"]):
                metadata["objective_type"] = "coordination"
            elif any(word in objective for word in ["refactor", "redesign", "architecture"]):
                metadata["objective_type"] = "architecture"
            elif any(word in objective for word in ["fix", "typo", "update"]):
                metadata["objective_type"] = "direct"

        # Extract scope indicators
        if "scope" in task:
            if "files" in task["scope"]:
                file_count = len(task["scope"]["files"])
                if file_count == 1:
                    metadata["scope_indicators"].append("single_file")
                elif file_count <= 3:
                    metadata["scope_indicators"].append("limited_scope")
                else:
                    metadata["scope_indicators"].append("multiple_files")

        # Extract complexity hints
        if "constraints" in task:
            constraints = task["constraints"]
            if "risks" in constraints and len(constraints["risks"]) > 0:
                metadata["complexity_hints"].append("has_risks")
            if "dependencies" in constraints and len(constraints["dependencies"]) > 0:
                metadata["complexity_hints"].append("has_dependencies")
            if "time" in constraints:
                time_str = constraints["time"].lower()
                if "month" in time_str:
                    metadata["complexity_hints"].append("extensive_effort")
                elif "week" in time_str:
                    metadata["complexity_hints"].append("substantial_effort")

    return metadata


def validate_requirement(requirement_yaml: str) -> Dict:
    """Validate requirement structure against schema and extract semantic metadata."""
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

        # Extract semantic metadata
        semantic_metadata = extract_semantic_metadata(requirement)

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

        result = create_result(status, message, details, scope, semantic_metadata)
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


def extract_plan_semantic_metadata(plan: Dict) -> Dict:
    """Extract semantic metadata from plan."""
    metadata = {
        "workflow_type": None,
        "complexity_level": None,
        "rules_mentioned": [],
        "semantic_understanding_present": False
    }

    if "plan" in plan:
        plan_data = plan["plan"]

        # Extract workflow type
        if "workflow" in plan_data:
            workflow = plan_data["workflow"]
            if "execution" in workflow:
                metadata["workflow_type"] = "execution"
            elif "coordination" in workflow:
                metadata["workflow_type"] = "coordination"
            elif "architecture" in workflow:
                metadata["workflow_type"] = "architecture"
            elif "direct" in workflow:
                metadata["workflow_type"] = "direct"

        # Extract complexity level
        if "complexity" in plan_data:
            metadata["complexity_level"] = plan_data["complexity"]

        # Check for semantic understanding
        if "semantic_understanding" in plan_data:
            metadata["semantic_understanding_present"] = True
            semantic = plan_data["semantic_understanding"]
            if "patterns_matched" in semantic:
                metadata["patterns_matched"] = semantic["patterns_matched"]
            if "similar_patterns_found" in semantic:
                metadata["similar_patterns_found"] = semantic["similar_patterns_found"]

        # Extract rules loaded
        if "rules_loaded" in plan_data:
            metadata["rules_mentioned"] = plan_data["rules_loaded"]

    return metadata


def validate_plan(plan_yaml: str) -> Dict:
    """Validate plan structure and extract semantic metadata."""
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

        # Extract semantic metadata
        semantic_metadata = extract_plan_semantic_metadata(plan)

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

            # Check semantic understanding presence
            if "semantic_understanding" not in plan_data:
                details.append({
                    "severity": "warning",
                    "message": "Missing 'semantic_understanding' field",
                    "remediation": "Add semantic understanding to plan header"
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

        result = create_result(status, message, details, scope, semantic_metadata)
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

    if not PLAN_SCHEMA_PATH.exists():
        details.append({
            "severity": "warning",
            "message": f"Plan schema not found: {PLAN_SCHEMA_PATH}",
            "remediation": "Create plan schema"
        })

    # Check decision graphs exist (markdown, not YAML)
    decisions_dir = MVP_ROOT / "docs" / "reference" / "agentos" / "decisions"
    if decisions_dir.exists():
        required_graphs = ["task-classification.md", "complexity-assessment.md", "workflow-selection.md"]
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
        workflows = list(workflows_dir.glob("*.md"))
        if len(workflows) == 0:
            details.append({
                "severity": "warning",
                "message": "No workflow documentation found",
                "remediation": "Create workflow documentation"
            })

    # Check domain rules exist
    domain_rules_dir = MVP_ROOT / ".cursor" / "rules" / "domains"
    if domain_rules_dir.exists():
        domain_rules = list(domain_rules_dir.glob("*.mdc"))
        if len(domain_rules) == 0:
            details.append({
                "severity": "info",
                "message": "No domain rules found",
                "remediation": "Create domain rules for common domains"
            })

    # Check pattern schema exists (MVP-v4)
    if not PATTERN_SCHEMA_PATH.exists():
        details.append({
            "severity": "info",
            "message": f"Pattern schema not found: {PATTERN_SCHEMA_PATH}",
            "remediation": "Create pattern schema for pattern library validation"
        })

    # Check subagents exist (MVP-v4)
    subagents_dir = MVP_ROOT / ".cursor" / "agents"
    if subagents_dir.exists():
        subagents = list(subagents_dir.glob("*.md"))
        if len(subagents) == 0:
            details.append({
                "severity": "info",
                "message": "No subagent definitions found",
                "remediation": "Create subagent definitions for parallel execution"
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


def validate_pattern(pattern_yaml: str) -> Dict:
    """Validate pattern library entry structure against schema."""
    start_time = time.time()
    details = []
    scope = "pattern:validation"

    try:
        pattern = yaml.safe_load(pattern_yaml)
        if not pattern:
            return create_result(
                "fail",
                "Pattern is empty or invalid YAML",
                [{
                    "severity": "critical",
                    "message": "Pattern must be valid YAML",
                    "remediation": "Check YAML syntax"
                }],
                scope
            )

        # Load schema
        schema = load_yaml_schema(PATTERN_SCHEMA_PATH)
        if not schema:
            # Schema not found, do basic validation
            if "pattern" not in pattern:
                details.append({
                    "severity": "critical",
                    "message": "Missing 'pattern' field",
                    "remediation": "Add 'pattern:' field to pattern entry"
                })
            else:
                pattern_data = pattern["pattern"]
                required_fields = ["id", "type", "semantic_indicators", "orchestration_pattern", "workflow_used"]
                for field in required_fields:
                    if field not in pattern_data:
                        details.append({
                            "severity": "critical",
                            "message": f"Missing required field: pattern.{field}",
                            "remediation": f"Add 'pattern.{field}:' to pattern entry"
                        })
        else:
            # Validate against schema
            try:
                validate(instance=pattern, schema=schema)
            except ValidationError as e:
                details.append({
                    "severity": "critical",
                    "message": f"Schema validation failed: {e.message}",
                    "remediation": f"Fix validation error at: {'.'.join(str(p) for p in e.path)}"
                })

        # Additional semantic checks
        if "pattern" in pattern:
            pattern_data = pattern["pattern"]

            # Check semantic indicators
            if "semantic_indicators" in pattern_data:
                indicators = pattern_data["semantic_indicators"]
                if not isinstance(indicators, list) or len(indicators) == 0:
                    details.append({
                        "severity": "critical",
                        "message": "pattern.semantic_indicators must be a non-empty list",
                        "remediation": "Add semantic indicators as YAML list"
                    })

            # Check success rate range
            if "success_rate" in pattern_data:
                success_rate = pattern_data["success_rate"]
                if not isinstance(success_rate, (int, float)) or success_rate < 0 or success_rate > 1:
                    details.append({
                        "severity": "warning",
                        "message": "pattern.success_rate must be between 0.0 and 1.0",
                        "remediation": "Set success_rate to value between 0.0 and 1.0"
                    })

        # Determine status
        critical_issues = [d for d in details if d["severity"] == "critical"]
        if critical_issues:
            status = "fail"
            message = f"Pattern validation failed: {len(critical_issues)} critical issue(s)"
        elif details:
            status = "warning"
            message = f"Pattern validation passed with {len(details)} warning(s)"
        else:
            status = "pass"
            message = "Pattern validation passed"

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
                "remediation": "Check pattern format"
            }],
            scope
        )


# CLI interface
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: mcp_server.py <tool> [args...]")
        print("Tools: validate_requirement, validate_plan, validate_coherence, validate_pattern")
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

    elif tool == "validate_pattern":
        if len(sys.argv) < 3:
            print("Usage: mcp_server.py validate_pattern <pattern_yaml_file>")
            sys.exit(1)
        with open(sys.argv[2], 'r') as f:
            pattern_yaml = f.read()
        result = validate_pattern(pattern_yaml)

    else:
        print(f"Unknown tool: {tool}")
        sys.exit(1)

    print(json.dumps(result, indent=2))
