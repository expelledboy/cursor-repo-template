#!/usr/bin/env python3
"""
AgentOS MVP MCP Server
Minimal validation tools for MVP coherence checking.

Exposes 4 validation tools via MCP protocol:
- validate_decision_graph: Validate decision graph structure
- validate_command: Validate command file format
- validate_rule: Validate rule file format
- validate_mvp_coherence: Comprehensive MVP coherence check
"""

import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

# MVP root (this script runs from mvp/scripts/agentos/)
# Handle both cases: running from repo root or mvp/ directory
_script_dir = Path(__file__).parent
if _script_dir.name == "agentos" and _script_dir.parent.name == "scripts":
    # Running from mvp/scripts/agentos/
    MVP_ROOT = _script_dir.parent.parent
else:
    # Running from repo root
    MVP_ROOT = Path(__file__).parent.parent.parent / "mvp"

# JSON Schema for tool output
OUTPUT_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "required": ["status", "message", "details", "metadata"],
    "properties": {
        "status": {"type": "string", "enum": ["pass", "fail", "warning"]},
        "message": {"type": "string"},
        "details": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["severity", "message"],
                "properties": {
                    "severity": {"type": "string", "enum": ["critical", "warning", "info"]},
                    "message": {"type": "string"},
                    "file": {"type": "string"},
                    "line": {"type": "integer"},
                    "column": {"type": "integer"},
                    "remediation": {"type": "string"},
                    "context": {"type": "string"}
                }
            }
        },
        "metadata": {
            "type": "object",
            "required": ["execution_time", "scope", "version", "timestamp"],
            "properties": {
                "execution_time": {"type": "number"},
                "scope": {"type": "string"},
                "version": {"type": "string"},
                "timestamp": {"type": "string"}
            }
        }
    }
}


def create_result(status: str, message: str, details: List[Dict], scope: str) -> Dict:
    """Create standardized validation result."""
    return {
        "status": status,
        "message": message,
        "details": details,
        "metadata": {
            "execution_time": 0.0,  # Will be set by caller
            "scope": scope,
            "version": "1.0.0",
            "timestamp": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
        }
    }


def validate_decision_graph(graph_path: str) -> Dict:
    """Validate decision graph structure and format."""
    start_time = time.time()
    details = []

    file_path = MVP_ROOT / graph_path
    scope = f"decision_graph:{graph_path}"

    # Check file exists
    if not file_path.exists():
        return create_result(
            "fail",
            f"Decision graph not found: {graph_path}",
            [{
                "severity": "critical",
                "message": f"File does not exist: {graph_path}",
                "file": graph_path,
                "remediation": f"Create the file at {graph_path} or check the path"
            }],
            scope
        )

    # Read file
    try:
        content = file_path.read_text()
        lines = content.split('\n')
    except Exception as e:
        return create_result(
            "fail",
            f"Error reading decision graph: {str(e)}",
            [{
                "severity": "critical",
                "message": f"Cannot read file: {str(e)}",
                "file": graph_path,
                "remediation": "Check file permissions and encoding"
            }],
            scope
        )

    # Check required sections (accept ##, #, or **Purpose**: format)
    if "## Purpose" not in content and "# Purpose" not in content and "**Purpose**" not in content:
        details.append({
            "severity": "critical",
            "message": "Missing required section: Purpose",
            "file": graph_path,
            "remediation": "Add section: ## Purpose or **Purpose**:"
        })
    if "## Decision Tree" not in content and "# Decision Tree" not in content:
        details.append({
            "severity": "critical",
            "message": "Missing required section: Decision Tree",
            "file": graph_path,
            "remediation": "Add section: ## Decision Tree"
        })

    # Check decision tree structure (accept both # and ##)
    if "## Decision Tree" in content or "# Decision Tree" in content:
        # Look for decision steps
        tree_section = False
        step_count = 0
        for i, line in enumerate(lines, 1):
            if "## Decision Tree" in line or "# Decision Tree" in line:
                tree_section = True
            if tree_section and re.match(r'^### Step \d+:', line):
                step_count += 1
            if tree_section and (line.startswith("## ") or line.startswith("# ")) and "Decision Tree" not in line:
                break

        if step_count == 0:
            details.append({
                "severity": "warning",
                "message": "Decision tree has no steps",
                "file": graph_path,
                "line": content.find("Decision Tree"),
                "remediation": "Add decision steps (### Step 1:, Step 2:, etc.)"
            })

    # Check referenced files exist
    doc_refs = re.findall(r'`([^`]+\.md)`', content)
    for ref in doc_refs:
        ref_path = MVP_ROOT / ref
        if not ref_path.exists():
            line_num = next((i for i, line in enumerate(lines, 1) if ref in line), None)
            details.append({
                "severity": "warning",
                "message": f"Referenced file does not exist: {ref}",
                "file": graph_path,
                "line": line_num,
                "remediation": f"Create file at {ref} or fix reference"
            })

    # Determine status
    critical_issues = [d for d in details if d["severity"] == "critical"]
    if critical_issues:
        status = "fail"
        message = f"Decision graph validation failed: {len(critical_issues)} critical issue(s)"
    elif details:
        status = "warning"
        message = f"Decision graph validation passed with {len(details)} warning(s)"
    else:
        status = "pass"
        message = "Decision graph validation passed"

    result = create_result(status, message, details, scope)
    result["metadata"]["execution_time"] = time.time() - start_time
    return result


def validate_command(cmd_path: str) -> Dict:
    """Validate command file format."""
    start_time = time.time()
    details = []

    file_path = MVP_ROOT / cmd_path
    scope = f"command:{cmd_path}"

    # Check file exists
    if not file_path.exists():
        return create_result(
            "fail",
            f"Command file not found: {cmd_path}",
            [{
                "severity": "critical",
                "message": f"File does not exist: {cmd_path}",
                "file": cmd_path,
                "remediation": f"Create the file at {cmd_path}"
            }],
            scope
        )

    # Read file
    try:
        content = file_path.read_text()
        lines = content.split('\n')
    except Exception as e:
        return create_result(
            "fail",
            f"Error reading command: {str(e)}",
            [{
                "severity": "critical",
                "message": f"Cannot read file: {str(e)}",
                "file": cmd_path,
                "remediation": "Check file permissions"
            }],
            scope
        )

    # Check required sections
    required_sections = ["Purpose", "Instructions for Agent", "Expected Outcome"]
    for section in required_sections:
        if f"## {section}" not in content:
            line_num = next((i for i, line in enumerate(lines, 1) if section.lower() in line.lower()), None)
            details.append({
                "severity": "critical",
                "message": f"Missing required section: {section}",
                "file": cmd_path,
                "line": line_num or 1,
                "remediation": f"Add section: ## {section}"
            })

    # Check references to decision graphs
    graph_refs = re.findall(r'`docs/reference/agentos/decision-graphs/([^`]+\.md)`', content)
    for graph_ref in graph_refs:
        graph_path = MVP_ROOT / "docs/reference/agentos/decision-graphs" / graph_ref
        if not graph_path.exists():
            line_num = next((i for i, line in enumerate(lines, 1) if graph_ref in line), None)
            details.append({
                "severity": "warning",
                "message": f"Referenced decision graph does not exist: {graph_ref}",
                "file": cmd_path,
                "line": line_num,
                "remediation": f"Create decision graph at docs/reference/agentos/decision-graphs/{graph_ref}"
            })

    # Check references to docs
    doc_refs = re.findall(r'`docs/reference/agentos/([^`]+\.md)`', content)
    for doc_ref in doc_refs:
        doc_path = MVP_ROOT / "docs/reference/agentos" / doc_ref
        if not doc_path.exists():
            line_num = next((i for i, line in enumerate(lines, 1) if doc_ref in line), None)
            details.append({
                "severity": "warning",
                "message": f"Referenced doc does not exist: {doc_ref}",
                "file": cmd_path,
                "line": line_num,
                "remediation": f"Create doc at docs/reference/agentos/{doc_ref}"
            })

    # Determine status
    critical_issues = [d for d in details if d["severity"] == "critical"]
    if critical_issues:
        status = "fail"
        message = f"Command validation failed: {len(critical_issues)} critical issue(s)"
    elif details:
        status = "warning"
        message = f"Command validation passed with {len(details)} warning(s)"
    else:
        status = "pass"
        message = "Command validation passed"

    result = create_result(status, message, details, scope)
    result["metadata"]["execution_time"] = time.time() - start_time
    return result


def validate_rule(rule_path: str) -> Dict:
    """Validate rule file format."""
    start_time = time.time()
    details = []

    file_path = MVP_ROOT / rule_path
    scope = f"rule:{rule_path}"

    # Check file exists
    if not file_path.exists():
        return create_result(
            "fail",
            f"Rule file not found: {rule_path}",
            [{
                "severity": "critical",
                "message": f"File does not exist: {rule_path}",
                "file": rule_path,
                "remediation": f"Create the file at {rule_path}"
            }],
            scope
        )

    # Read file
    try:
        content = file_path.read_text()
        lines = content.split('\n')
    except Exception as e:
        return create_result(
            "fail",
            f"Error reading rule: {str(e)}",
            [{
                "severity": "critical",
                "message": f"Cannot read file: {str(e)}",
                "file": rule_path,
                "remediation": "Check file permissions"
            }],
            scope
        )

    # Check frontmatter
    if not content.startswith("---"):
        details.append({
            "severity": "critical",
            "message": "Missing YAML frontmatter (should start with ---)",
            "file": rule_path,
            "line": 1,
            "remediation": "Add YAML frontmatter at start of file"
        })
    else:
        # Parse frontmatter
        frontmatter_end = content.find("---", 3)
        if frontmatter_end == -1:
            details.append({
                "severity": "critical",
                "message": "Incomplete YAML frontmatter (missing closing ---)",
                "file": rule_path,
                "line": 1,
                "remediation": "Add closing --- after frontmatter"
            })
        else:
            frontmatter = content[3:frontmatter_end].strip()
            # Check for description or alwaysApply
            if "description:" not in frontmatter and "alwaysApply:" not in frontmatter and "globs:" not in frontmatter:
                details.append({
                    "severity": "warning",
                    "message": "Frontmatter missing description, alwaysApply, or globs",
                    "file": rule_path,
                    "line": 2,
                    "remediation": "Add description:, alwaysApply: true, or globs: to frontmatter"
                })

    # Check referenced files
    doc_refs = re.findall(r'`([^`]+\.md)`', content)
    for ref in doc_refs:
        ref_path = MVP_ROOT / ref
        if not ref_path.exists():
            line_num = next((i for i, line in enumerate(lines, 1) if ref in line), None)
            details.append({
                "severity": "warning",
                "message": f"Referenced file does not exist: {ref}",
                "file": rule_path,
                "line": line_num,
                "remediation": f"Create file at {ref} or fix reference"
            })

    # Determine status
    critical_issues = [d for d in details if d["severity"] == "critical"]
    if critical_issues:
        status = "fail"
        message = f"Rule validation failed: {len(critical_issues)} critical issue(s)"
    elif details:
        status = "warning"
        message = f"Rule validation passed with {len(details)} warning(s)"
    else:
        status = "pass"
        message = "Rule validation passed"

    result = create_result(status, message, details, scope)
    result["metadata"]["execution_time"] = time.time() - start_time
    return result


def validate_mvp_coherence(scope: str = "all") -> Dict:
    """Comprehensive MVP coherence check."""
    start_time = time.time()
    all_details = []

    if scope in ["all", "graphs"]:
        # Validate all decision graphs
        graphs_dir = MVP_ROOT / "docs/reference/agentos/decision-graphs"
        if graphs_dir.exists():
            for graph_file in graphs_dir.glob("*.md"):
                if graph_file.name != "README.md":
                    graph_path = graph_file.relative_to(MVP_ROOT)
                    result = validate_decision_graph(str(graph_path))
                    all_details.extend(result["details"])

    if scope in ["all", "commands"]:
        # Validate all commands
        commands_dir = MVP_ROOT / ".cursor/commands"
        if commands_dir.exists():
            for cmd_file in commands_dir.glob("*.md"):
                cmd_path = cmd_file.relative_to(MVP_ROOT)
                result = validate_command(str(cmd_path))
                all_details.extend(result["details"])

    if scope in ["all", "rules"]:
        # Validate all rules
        rules_dir = MVP_ROOT / ".cursor/rules"
        if rules_dir.exists():
            for rule_file in rules_dir.rglob("*.mdc"):
                rule_path = rule_file.relative_to(MVP_ROOT)
                result = validate_rule(str(rule_path))
                all_details.extend(result["details"])

    # Determine overall status
    critical_issues = [d for d in all_details if d["severity"] == "critical"]
    warnings = [d for d in all_details if d["severity"] == "warning"]

    if critical_issues:
        status = "fail"
        message = f"MVP coherence validation failed: {len(critical_issues)} critical issue(s), {len(warnings)} warning(s)"
    elif warnings:
        status = "warning"
        message = f"MVP coherence validation passed with {len(warnings)} warning(s)"
    else:
        status = "pass"
        message = "MVP coherence validation passed"

    result = create_result(status, message, all_details, f"mvp_coherence:{scope}")
    result["metadata"]["execution_time"] = time.time() - start_time
    return result


# MCP Protocol Handler (simplified - actual implementation depends on MCP library)
def handle_mcp_request(request: Dict) -> Dict:
    """Handle MCP tool call request."""
    tool_name = request.get("name")
    arguments = request.get("arguments", {})

    if tool_name == "validate_decision_graph":
        graph_path = arguments.get("graph_path", "")
        return validate_decision_graph(graph_path)

    elif tool_name == "validate_command":
        cmd_path = arguments.get("command_path", "")
        return validate_command(cmd_path)

    elif tool_name == "validate_rule":
        rule_path = arguments.get("rule_path", "")
        return validate_rule(rule_path)

    elif tool_name == "validate_mvp_coherence":
        scope = arguments.get("scope", "all")
        return validate_mvp_coherence(scope)

    else:
        return {
            "status": "fail",
            "message": f"Unknown tool: {tool_name}",
            "details": [{
                "severity": "critical",
                "message": f"Tool not found: {tool_name}",
                "remediation": "Use one of: validate_decision_graph, validate_command, validate_rule, validate_mvp_coherence"
            }],
            "metadata": {
                "execution_time": 0.0,
                "scope": "unknown",
                "version": "1.0.0",
                "timestamp": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
            }
        }


# CLI interface for testing
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: mcp_server.py <tool> [args...]")
        print("Tools: validate_decision_graph, validate_command, validate_rule, validate_mvp_coherence")
        sys.exit(1)

    tool = sys.argv[1]

    if tool == "validate_decision_graph":
        if len(sys.argv) < 3:
            print("Usage: mcp_server.py validate_decision_graph <graph_path>")
            sys.exit(1)
        result = validate_decision_graph(sys.argv[2])

    elif tool == "validate_command":
        if len(sys.argv) < 3:
            print("Usage: mcp_server.py validate_command <command_path>")
            sys.exit(1)
        result = validate_command(sys.argv[2])

    elif tool == "validate_rule":
        if len(sys.argv) < 3:
            print("Usage: mcp_server.py validate_rule <rule_path>")
            sys.exit(1)
        result = validate_rule(sys.argv[2])

    elif tool == "validate_mvp_coherence":
        scope = sys.argv[2] if len(sys.argv) > 2 else "all"
        result = validate_mvp_coherence(scope)

    else:
        print(f"Unknown tool: {tool}")
        sys.exit(1)

    print(json.dumps(result, indent=2))
