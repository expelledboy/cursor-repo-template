#!/usr/bin/env python3
"""
AgentOS v9 Validation Suite

Comprehensive validation of AgentOS v9 functionality and authenticity.
Tests all core components and ensures system integrity.

DOE Registry - Bidirectional Linkages:
@directive docs/reference/agentos/architecture.md

# DOE Layer Declaration
DOE_LAYER = "execution"
DOE_RESPONSIBILITY = "System validation and authenticity verification"
DOE_GOVERNANCE = "docs/reference/agentos/doe-framework.md"
DOE_PRECEDENCE = 4
"""

import sys
import subprocess
import json
from pathlib import Path

def run_command(cmd, cwd=None, timeout=30):
    """Run a command and return result."""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            cwd=cwd,
            timeout=timeout
        )
        return {
            "success": result.returncode == 0,
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
            "returncode": result.returncode
        }
    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "error": "Command timed out"
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

def validate_core_functionality():
    """Validate that core AgentOS functionality works."""
    print("🔍 Validating AgentOS v9 core functionality...")

    v9_dir = Path(__file__).parent.parent
    agentos_script = v9_dir / "src" / "agentos.py"

    checks = []

    # Check script exists and is executable
    if agentos_script.exists():
        checks.append({
            "name": "script_exists",
            "status": "pass",
            "message": "AgentOS script exists"
        })
    else:
        checks.append({
            "name": "script_exists",
            "status": "fail",
            "message": "AgentOS script not found"
        })
        return checks

    # Test version command
    version_result = run_command(f"python3 {agentos_script} --version", cwd=v9_dir)
    if version_result["success"] and "AgentOS v9" in version_result["stdout"]:
        checks.append({
            "name": "version_command",
            "status": "pass",
            "message": "Version command works"
        })
    else:
        checks.append({
            "name": "version_command",
            "status": "fail",
            "message": f"Version command failed: {version_result}"
        })

    # Test analyze command
    analyze_result = run_command(f"python3 {agentos_script} analyze .", cwd=v9_dir)
    if analyze_result["success"]:
        try:
            data = json.loads(analyze_result["stdout"])
            if "structure" in data and "total_files" in data["structure"]:
                checks.append({
                    "name": "analyze_command",
                    "status": "pass",
                    "message": "Analyze command works and returns valid JSON"
                })
            else:
                checks.append({
                    "name": "analyze_command",
                    "status": "fail",
                    "message": "Analyze command returns invalid structure"
                })
        except json.JSONDecodeError:
            checks.append({
                "name": "analyze_command",
                "status": "fail",
                "message": "Analyze command does not return valid JSON"
            })
    else:
        checks.append({
            "name": "analyze_command",
            "status": "fail",
            "message": f"Analyze command failed: {analyze_result}"
        })

    # Test validate command
    validate_result = run_command(f"python3 {agentos_script} validate .", cwd=v9_dir)
    if validate_result["success"]:
        try:
            data = json.loads(validate_result["stdout"])
            if "checks" in data:
                checks.append({
                    "name": "validate_command",
                    "status": "pass",
                    "message": "Validate command works and returns valid JSON"
                })
            else:
                checks.append({
                    "name": "validate_command",
                    "status": "fail",
                    "message": "Validate command returns invalid structure"
                })
        except json.JSONDecodeError:
            checks.append({
                "name": "validate_command",
                "status": "fail",
                "message": "Validate command does not return valid JSON"
            })
    else:
        checks.append({
            "name": "validate_command",
            "status": "fail",
            "message": f"Validate command failed: {validate_result}"
        })

    # Test self-determination command
    self_det_result = run_command(f"python3 {agentos_script} self-determination", cwd=v9_dir)
    if self_det_result["success"]:
        try:
            data = json.loads(self_det_result["stdout"])
            if ("evidence_collection" in data and
                "system_facts" in data and
                "relationship_evidence" in data and
                "directive_evidence" in data and
                "orchestration_ready" in data and
                data.get("evidence_collection", {}).get("doe_layer") == "execution"):
                checks.append({
                    "name": "self_determination_command",
                    "status": "pass",
                    "message": "Self-determination evidence collection works with DOE compliance"
                })
            else:
                checks.append({
                    "name": "self_determination_command",
                    "status": "fail",
                    "message": "Self-determination command returns invalid evidence structure"
                })
        except json.JSONDecodeError:
            checks.append({
                "name": "self_determination_command",
                "status": "fail",
                "message": "Self-determination command does not return valid JSON"
            })
    else:
        checks.append({
            "name": "self_determination_command",
            "status": "fail",
            "message": f"Self-determination command failed: {self_det_result}"
        })

    # Test state manager
    state_list_result = run_command(f"python3 scripts/state_manager.py list", cwd=v9_dir)
    if state_list_result["success"]:
        checks.append({
            "name": "state_manager",
            "status": "pass",
            "message": "State manager basic functionality works"
        })
    else:
        checks.append({
            "name": "state_manager",
            "status": "fail",
            "message": f"State manager failed: {state_list_result}"
        })

    # Test learn command
    learn_result = run_command(f"python3 src/agentos.py learn \"test learning observation\"", cwd=v9_dir)
    if learn_result["success"]:
        try:
            data = json.loads(learn_result["stdout"])
            if "learning_type" in data and "ai_agent_analysis_required" in data and "user_alignment_required" in data:
                checks.append({
                    "name": "learn_command",
                    "status": "pass",
                    "message": "Learn command correctly captures observations without intelligence assumptions"
                })
            else:
                checks.append({
                    "name": "learn_command",
                    "status": "fail",
                    "message": "Learn command does not properly indicate AI agent analysis requirement"
                })
        except json.JSONDecodeError:
            checks.append({
                "name": "learn_command",
                "status": "fail",
                "message": "Learn command does not return valid JSON"
            })
    else:
        checks.append({
            "name": "learn_command",
            "status": "fail",
            "message": f"Learn command failed: {learn_result}"
        })

    # Test task manager
    task_create_result = run_command(f"python3 scripts/task_manager.py create test-task \"test learning objective\"", cwd=v9_dir)
    if task_create_result["success"]:
        # Extract the actual task ID from the output (format: "Created task branch: learning-YYYYMMDD-HHMMSS")
        import re
        task_id_match = re.search(r'Created task branch: (\S+)', task_create_result["stdout"])
        if task_id_match:
            actual_task_id = task_id_match.group(1)

            checks.append({
                "name": "task_manager_create",
                "status": "pass",
                "message": "Task manager can create task branches"
            })

            # Test task listing
            task_list_result = run_command(f"python3 scripts/task_manager.py list", cwd=v9_dir)
            if task_list_result["success"] and "test objective" in task_list_result["stdout"]:
                checks.append({
                    "name": "task_manager_list",
                    "status": "pass",
                    "message": "Task manager can list active task branches"
                })
            else:
                checks.append({
                    "name": "task_manager_list",
                    "status": "fail",
                    "message": f"Task manager list failed: {task_list_result}"
                })

            # Test feedback recording with actual task ID
            feedback_result = run_command(f"python3 scripts/task_manager.py feedback {actual_task_id} --message \"test feedback\" --alignment partial", cwd=v9_dir)
            if feedback_result["success"] and "Recorded feedback" in feedback_result["stdout"]:
                checks.append({
                    "name": "task_manager_feedback",
                    "status": "pass",
                    "message": "Task manager can record learning feedback"
                })
            else:
                checks.append({
                    "name": "task_manager_feedback",
                    "status": "fail",
                    "message": f"Task manager feedback failed: {feedback_result}"
                })
        else:
            checks.append({
                "name": "task_manager_create",
                "status": "fail",
                "message": "Could not extract task ID from creation output"
            })
    else:
        checks.append({
            "name": "task_manager_create",
            "status": "fail",
            "message": f"Task manager create failed: {task_create_result}"
        })

    # Test DOE compliance in self-determination evidence
    self_det_result = run_command(f"python3 src/agentos.py self-determination", cwd=v9_dir)
    if self_det_result["success"]:
        try:
            data = json.loads(self_det_result["stdout"])

            # Check for DOE evidence collection compliance
            if ("evidence_collection" in data and
                data["evidence_collection"].get("doe_layer") == "execution" and
                data.get("orchestration_ready") is True):
                checks.append({
                    "name": "doe_evidence_collection",
                    "status": "pass",
                    "message": "Self-determination provides DOE-compliant evidence for orchestration analysis"
                })
            else:
                checks.append({
                    "name": "doe_evidence_collection",
                    "status": "fail",
                    "message": "Self-determination evidence does not meet DOE standards"
                })

            # Check for orchestration readiness
            if data.get("orchestration_ready") and "system_facts" in data and "relationship_evidence" in data:
                checks.append({
                    "name": "orchestration_readiness",
                    "status": "pass",
                    "message": "Self-determination evidence ready for orchestration layer analysis"
                })
            else:
                checks.append({
                    "name": "orchestration_readiness",
                    "status": "fail",
                    "message": "Self-determination evidence not orchestration-ready"
                })

        except json.JSONDecodeError:
            checks.append({
                "name": "doe_evidence_collection",
                "status": "fail",
                "message": f"Self-determination returned invalid JSON: {self_det_result['stdout'][:100]}..."
            })

    # Note: E layer API validation moved to separate test to avoid self-validation loops

    # Test data orchestrator importance API
    importance_result = run_command(f"python3 scripts/data_orchestrator.py importance --output json", cwd=v9_dir)
    if importance_result["success"]:
        try:
            importance_data = json.loads(importance_result["stdout"])
            if isinstance(importance_data, list) and len(importance_data) > 0:
                checks.append({
                    "name": "data_orchestrator_api",
                    "status": "pass",
                    "message": f"Data orchestrator importance API returns {len(importance_data)} items with proper JSON structure"
                })
            else:
                checks.append({
                    "name": "data_orchestrator_api",
                    "status": "fail",
                    "message": "Data orchestrator importance API returned empty or invalid data"
                })
        except json.JSONDecodeError:
            checks.append({
                "name": "data_orchestrator_api",
                "status": "fail",
                "message": "Data orchestrator importance API returned invalid JSON"
            })
    else:
        checks.append({
            "name": "data_orchestrator_api",
            "status": "fail",
            "message": "Data orchestrator importance API not accessible"
        })

    # Test E layer API understanding validation
    e_layer_scripts = [
        "scripts/validate.py",
        "scripts/task_manager.py",
        "scripts/state_manager.py",
        "scripts/relationship_renderer.py",
        "scripts/relationship_tree_visualizer.py"
    ]

    api_understanding_checks = 0
    for script in e_layer_scripts:
        # Test that script exists and is executable
        script_result = run_command(f"python3 {script} --help", cwd=v9_dir)
        if script_result["success"] and "usage:" in script_result["stdout"].lower():
            api_understanding_checks += 1
        else:
            checks.append({
                "name": f"e_layer_api_{script.split('/')[-1].replace('.py', '')}",
                "status": "fail",
                "message": f"E layer script {script} API not accessible"
            })

    if api_understanding_checks == len(e_layer_scripts):
        checks.append({
            "name": "e_layer_api_discovery",
            "status": "pass",
            "message": f"E layer API understanding validated for {api_understanding_checks} scripts"
        })

    # Test data orchestrator importance API
    importance_result = run_command(f"python3 scripts/data_orchestrator.py importance --output json", cwd=v9_dir)
    if importance_result["success"]:
        try:
            importance_data = json.loads(importance_result["stdout"])
            if isinstance(importance_data, list) and len(importance_data) > 0:
                checks.append({
                    "name": "data_orchestrator_api",
                    "status": "pass",
                    "message": f"Data orchestrator importance API returns {len(importance_data)} items with proper JSON structure"
                })
            else:
                checks.append({
                    "name": "data_orchestrator_api",
                    "status": "fail",
                    "message": "Data orchestrator importance API returned empty or invalid data"
                })
        except json.JSONDecodeError:
            checks.append({
                "name": "data_orchestrator_api",
                "status": "fail",
                "message": "Data orchestrator importance API returned invalid JSON"
            })
    else:
        checks.append({
            "name": "data_orchestrator_api",
            "status": "fail",
            "message": "Data orchestrator importance API not accessible"
        })

    # Test frontmatter intelligence
    fm_result = run_command(f"python3 scripts/frontmatter_intelligence.py gaps", cwd=v9_dir)
    if fm_result["success"] and "Isolated Documents" in fm_result["stdout"]:
        checks.append({
            "name": "frontmatter_intelligence",
            "status": "pass",
            "message": "Frontmatter intelligence can analyze relationship gaps"
        })
    else:
        checks.append({
            "name": "frontmatter_intelligence",
            "status": "fail",
            "message": f"Frontmatter intelligence failed: {fm_result}"
        })

    # Test frontmatter intelligence awareness
    awareness_result = run_command(f"python3 scripts/frontmatter_intelligence.py awareness docs/reference/agentos/architecture.md", cwd=v9_dir)
    if awareness_result["success"] and "Authority Level:" in awareness_result["stdout"]:
        checks.append({
            "name": "frontmatter_awareness",
            "status": "pass",
            "message": "Frontmatter intelligence provides agent self-awareness"
        })
    else:
        checks.append({
            "name": "frontmatter_awareness",
            "status": "fail",
            "message": f"Frontmatter awareness failed: {awareness_result}"
        })

    # Test meta-analysis mode validation
    self_det_result = run_command(f"python3 src/agentos.py self-determination", cwd=v9_dir)
    if self_det_result["success"]:
        try:
            data = json.loads(self_det_result["stdout"])
            if "meta_analysis" in data and "gap_detection_integration" in data["meta_analysis"]:
                checks.append({
                    "name": "meta_analysis_gap_integration",
                    "status": "pass",
                    "message": "Meta-analysis includes gap detection integration"
                })
            else:
                checks.append({
                    "name": "meta_analysis_gap_integration",
                    "status": "fail",
                    "message": "Meta-analysis missing gap detection integration"
                })
        except json.JSONDecodeError:
            checks.append({
                "name": "meta_analysis_gap_integration",
                "status": "fail",
                "message": "Self-determination does not return valid JSON"
            })
    else:
        checks.append({
            "name": "meta_analysis_gap_integration",
            "status": "fail",
            "message": f"Self-determination failed: {self_det_result}"
        })

    # Test gap detector functionality
    gap_result = run_command(f"python3 scripts/gap_detector.py status", cwd=v9_dir)
    if gap_result["success"] and "System Active: True" in gap_result["stdout"]:
        checks.append({
            "name": "gap_detector_status",
            "status": "pass",
            "message": "Gap detector provides status information"
        })
    else:
        checks.append({
            "name": "gap_detector_status",
            "status": "fail",
            "message": f"Gap detector status failed: {gap_result}"
        })

    # Test evolution analyzer (refactored to use data orchestrator)
    evolution_result = run_command(f"python3 scripts/evolution_planner.py analyze", cwd=v9_dir)
    if evolution_result["success"] and '"analysis_status": "complete"' in evolution_result["stdout"]:
        checks.append({
            "name": "evolution_analyzer",
            "status": "pass",
            "message": "Evolution analyzer provides structured evolution insights using shared data"
        })
    else:
        checks.append({
            "name": "evolution_analyzer",
            "status": "fail",
            "message": f"Evolution analyzer failed: {evolution_result['returncode']}"
        })

    # Test change impact analyzer
    impact_result = run_command(f"python3 scripts/change_impact_analyzer.py analyze \"test change\"", cwd=v9_dir)
    if impact_result["success"] and '"analysis_status": "complete"' in impact_result["stdout"]:
        checks.append({
            "name": "change_impact_analyzer",
            "status": "pass",
            "message": "Change impact analyzer reveals relationship-aware change impact patterns"
        })
    else:
        checks.append({
            "name": "change_impact_analyzer",
            "status": "fail",
            "message": f"Change impact analyzer failed: {impact_result['returncode']}"
        })

    # Test memory bank integrator
    memory_result = run_command(f"python3 scripts/memory_bank_integrator.py analyze", cwd=v9_dir)
    if memory_result["success"] and '"analysis_status": "complete"' in memory_result["stdout"]:
        checks.append({
            "name": "memory_bank_integrator",
            "status": "pass",
            "message": "Memory bank integrator reveals context optimization patterns"
        })
    else:
        checks.append({
            "name": "memory_bank_integrator",
            "status": "fail",
            "message": f"Memory bank integrator failed: {memory_result['returncode']}"
        })

    # Test workflow coordinator
    workflow_result = run_command(f"python3 scripts/workflow_coordinator.py analyze", cwd=v9_dir)
    if workflow_result["success"] and '"analysis_status": "complete"' in workflow_result["stdout"]:
        checks.append({
            "name": "workflow_coordinator",
            "status": "pass",
            "message": "Workflow coordinator reveals command-based execution patterns"
        })
    else:
        checks.append({
            "name": "workflow_coordinator",
            "status": "fail",
            "message": f"Workflow coordinator failed: {workflow_result['returncode']}"
        })

    return checks

def main():
    """Main validation entry point."""
    print("🚀 AgentOS v9 Validation")
    print("=" * 40)

    checks = validate_core_functionality()

    passed = sum(1 for check in checks if check["status"] == "pass")
    total = len(checks)

    print(f"\n📊 Results: {passed}/{total} checks passed")

    for check in checks:
        status_icon = "✅" if check["status"] == "pass" else "❌"
        print(f"{status_icon} {check['name']}: {check['message']}")

    if passed == total:
        print("\n🎉 All validation checks passed! AgentOS v9 is authentic.")
        return 0
    else:
        print(f"\n⚠️  {total - passed} validation checks failed. Implementation needs attention.")
        return 1

if __name__ == "__main__":
    sys.exit(main())