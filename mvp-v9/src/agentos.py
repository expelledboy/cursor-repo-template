#!/usr/bin/env python3
"""
AgentOS v9 - Implementation-First AI Development Framework

A minimal, working CLI tool that prioritizes functionality over documentation.
Built following intelligence-first design principles from v8 learnings.

DOE Registry - Bidirectional Linkages:
@directive docs/reference/agentos/behavior-spec.md
@directive docs/reference/agentos/architecture.md
@directive docs/reference/agentos/learning-system.md
@directive docs/how-to/agentos/usage.md
"""

import sys
import argparse
import json
from pathlib import Path

class AgentOS:
    """Core AgentOS class implementing minimal working functionality."""

    def __init__(self):
        self.version = "9.0.0"
        self.working_dir = Path.cwd()

    def analyze(self, target_path: str = ".") -> dict:
        """Perform genuine analysis of codebase structure."""
        target = Path(target_path)
        if not target.exists():
            return {"error": f"Path {target_path} does not exist"}

        analysis = {
            "path": str(target.absolute()),
            "type": "directory" if target.is_dir() else "file",
            "structure": {}
        }

        if target.is_dir():
            # Analyze directory structure
            files = []
            dirs = []
            for item in target.rglob("*"):
                if item.is_file():
                    files.append(str(item.relative_to(target)))
                elif item.is_dir():
                    dirs.append(str(item.relative_to(target)))

            analysis["structure"] = {
                "total_files": len(files),
                "total_dirs": len(dirs),
                "file_types": self._analyze_file_types(files)
            }

        return analysis

    def _analyze_file_types(self, files: list) -> dict:
        """Analyze file type distribution."""
        types = {}
        for file in files:
            ext = Path(file).suffix.lower()
            types[ext] = types.get(ext, 0) + 1
        return types

    def validate(self, target_path: str = ".") -> dict:
        """Perform basic validation of codebase."""
        target = Path(target_path)

        validation = {
            "path": str(target.absolute()),
            "checks": []
        }

        # Check for basic structure
        if target.is_dir():
            validation["checks"].append({
                "name": "directory_exists",
                "status": "pass",
                "message": "Target directory exists"
            })

            # Check for common project files
            project_files = ["README.md", "package.json", "requirements.txt", "Cargo.toml"]
            found_files = [f for f in project_files if (target / f).exists()]

            validation["checks"].append({
                "name": "project_files",
                "status": "pass" if found_files else "warn",
                "message": f"Found project files: {found_files}" if found_files else "No standard project files found"
            })
        else:
            validation["checks"].append({
                "name": "file_exists",
                "status": "pass",
                "message": "Target file exists"
            })

        return validation

    def self_determine(self) -> dict:
        """Collect self-determination evidence for orchestration layer analysis."""
        import subprocess
        from datetime import datetime

        # DOE Layer Declaration - E Layer Evidence Collection
        DOE_LAYER = "execution"
        DOE_RESPONSIBILITY = "Collect structured evidence for self-determination analysis"
        DOE_GOVERNANCE = "docs/reference/agentos/execution-layer.md"
        DOE_PRECEDENCE = 4

        result = {
            "evidence_collection": {
                "collection_type": "self-determination",
                "timestamp": datetime.now().isoformat(),
                "doe_layer": DOE_LAYER,
                "doe_responsibility": DOE_RESPONSIBILITY,
                "evidence_quality": "doe_compliant"
            },
            "system_facts": {},
            "relationship_evidence": {},
            "directive_evidence": {},
            "orchestration_ready": False
        }

        try:
            # Collect basic system facts
            docs_dir = Path(__file__).parent.parent / "docs"
            scripts_dir = Path(__file__).parent.parent / "scripts"
            src_dir = Path(__file__).parent.parent / "src"

            result["system_facts"] = {
                "docs_count": len(list(docs_dir.rglob("*.md"))) if docs_dir.exists() else 0,
                "scripts_count": len(list(scripts_dir.glob("*.py"))) if scripts_dir.exists() else 0,
                "src_count": len(list(src_dir.glob("*.py"))) if src_dir.exists() else 0,
                "total_files": len(list(Path(__file__).parent.parent.rglob("*"))),
                "directories_present": {
                    "docs": docs_dir.exists(),
                    "scripts": scripts_dir.exists(),
                    "src": src_dir.exists()
                }
            }

            # Collect relationship evidence
            renderer_script = Path(__file__).parent.parent / "scripts" / "relationship_renderer.py"
            if renderer_script.exists():
                process = subprocess.run(
                    [sys.executable, str(renderer_script)],
                    capture_output=True,
                    text=True,
                    cwd=Path(__file__).parent.parent
                )

                if process.returncode == 0:
                    # Parse relationship counts from output
                    output = process.stdout.strip()
                    relationship_count = 0
                    if "Total relationships:" in output:
                        try:
                            relationship_count = int(output.split("Total relationships:")[1].split("\n")[0].strip())
                        except:
                            relationship_count = 0

                    result["relationship_evidence"] = {
                        "renderer_status": "executed",
                        "relationship_count": relationship_count,
                        "renderer_output_length": len(output),
                        "evidence_collected": True
                    }
                else:
                    result["relationship_evidence"] = {
                        "renderer_status": "error",
                        "error": process.stderr.strip(),
                        "evidence_collected": False
                    }
            else:
                result["relationship_evidence"] = {
                    "renderer_status": "missing",
                    "error": "relationship_renderer.py not found",
                    "evidence_collected": False
                }

            # Collect directive evidence
            if docs_dir.exists():
                core_docs = self._check_core_docs(docs_dir)
                result["directive_evidence"] = {
                    "docs_directory_exists": True,
                    "core_docs_present": core_docs,
                    "validation_status": "evidence_collected"
                }
            else:
                result["directive_evidence"] = {
                    "docs_directory_exists": False,
                    "core_docs_present": False,
                    "validation_status": "evidence_unavailable"
                }

            # Collect meta-analysis with gap detection integration
            gap_detector_script = Path(__file__).parent.parent / "scripts" / "gap_detector.py"
            if gap_detector_script.exists():
                gap_process = subprocess.run(
                    [sys.executable, str(gap_detector_script), "status"],
                    capture_output=True,
                    text=True,
                    cwd=Path(__file__).parent.parent
                )

                if gap_process.returncode == 0 and "System Active: True" in gap_process.stdout:
                    result["meta_analysis"] = {
                        "gap_detection_integration": {
                            "status": "integrated",
                            "gap_detector_available": True,
                            "ai_agent_framework_ready": True,
                            "analysis_types_supported": [
                                "relationship_pattern_analysis",
                                "impact_assessment",
                                "prioritization_ranking",
                                "root_cause_identification",
                                "remediation_planning"
                            ],
                            "integration_timestamp": datetime.now().isoformat(),
                            "evidence_collection_capable": True
                        },
                        "self_improvement_capabilities": {
                            "learning_opportunities": "gap analysis results can feed learning system",
                            "pattern_recognition": "recurring gap types inform system improvements",
                            "validation_enhancement": "gap detection improves overall validation",
                            "meta_analysis_ready": True
                        }
                    }
                else:
                    result["meta_analysis"] = {
                        "gap_detection_integration": {
                            "status": "degraded",
                            "gap_detector_available": False,
                            "error": "gap detector not responding",
                            "integration_timestamp": datetime.now().isoformat(),
                            "evidence_collection_capable": False
                        }
                    }
            else:
                result["meta_analysis"] = {
                    "gap_detection_integration": {
                        "status": "missing",
                        "gap_detector_available": False,
                        "error": "gap_detector.py script not found",
                        "integration_timestamp": datetime.now().isoformat(),
                        "evidence_collection_capable": False
                    }
                }

            # Mark orchestration ready
            result["orchestration_ready"] = True

        except Exception as e:
            result["evidence_collection"]["error"] = str(e)
            result["orchestration_ready"] = False

        return result

    def learn(self, observation: str = "", file_path: str = "") -> dict:
        """Capture learning observation for AI agent analysis."""
        result = {
            "learning_type": "manual_capture",
            "observation": observation,
            "file_path": file_path,
            "capture_timestamp": str(self.version),
            "ai_agent_analysis_required": True,
            "user_alignment_required": True,
            "next_steps": [
                "AI agent will analyze observation content",
                "AI agent will determine categorization (problem/discovery)",
                "AI agent will generate meaningful artifact content",
                "User will provide alignment feedback",
                "Iterate until user alignment achieved"
            ]
        }

        if not observation and not file_path:
            result["error"] = "No observation or file provided for learning capture"
            return result

        # Scripts only capture and structure - no intelligence assumptions
        result["capture_status"] = "successful"
        result["awaiting_ai_analysis"] = True

        return result

        # Analyze the observation for learning potential
        if observation:
            result["analysis"] = self._analyze_observation(observation)
        elif file_path:
            result["analysis"] = self._analyze_file_observation(file_path)
        else:
            result["analysis"] = {
                "error": "No observation or file provided for learning"
            }
            return result

        # Categorize as problem or discovery
        result["categorization"] = self._categorize_learning(result["analysis"])

        # Generate draft artifacts (not authoritative yet)
        if result["categorization"]["category"] in ["problem", "discovery"]:
            result["generated_artifacts"] = self._generate_learning_artifacts(
                result["categorization"]
            )

        result["guidance"] = self._get_user_alignment_guidance()

        return result

    def _analyze_observation(self, observation: str) -> dict:
        """Analyze a text observation for learning potential."""
        analysis = {
            "content": observation,
            "issues_identified": [],
            "patterns_found": [],
            "insights": [],
            "actionable": False
        }

        # Simple pattern recognition
        if any(word in observation.lower() for word in ["fail", "error", "issue", "problem", "bug"]):
            analysis["issues_identified"].append("error_pattern")
            analysis["actionable"] = True

        if any(word in observation.lower() for word in ["improve", "better", "enhance", "optimize"]):
            analysis["patterns_found"].append("improvement_opportunity")
            analysis["actionable"] = True

        if any(word in observation.lower() for word in ["discover", "find", "learn", "realize"]):
            analysis["insights"].append("discovery_pattern")
            analysis["actionable"] = True

        return analysis

    def _analyze_file_observation(self, file_path: str) -> dict:
        """Analyze a file for learning potential."""
        analysis = {
            "file_path": file_path,
            "file_exists": False,
            "content_preview": "",
            "issues_identified": [],
            "actionable": False
        }

        file = Path(file_path)
        if file.exists():
            analysis["file_exists"] = True
            try:
                content = file.read_text()
                analysis["content_preview"] = content[:500] + "..." if len(content) > 500 else content
                # Simple content analysis
                if "error" in content.lower() or "fail" in content.lower():
                    analysis["issues_identified"].append("error_in_file")
                    analysis["actionable"] = True
            except Exception as e:
                analysis["error"] = str(e)

        return analysis

    def _categorize_learning(self, analysis: dict) -> dict:
        """Categorize learning as problem or discovery."""
        categorization = {
            "category": "unknown",
            "confidence": 0.0,
            "rationale": "",
            "recommended_fields": {}
        }

        if analysis.get("actionable", False):
            if analysis.get("issues_identified"):
                categorization["category"] = "problem"
                categorization["confidence"] = 0.8
                categorization["rationale"] = "Issues identified suggest a problem to solve"
                issues = analysis.get('issues_identified', [])
                issue_title = issues[0] if issues else "Unknown"
                categorization["recommended_fields"] = {
                    "title": f"Problem: {issue_title}",
                    "status": "draft",
                    "evidence_sources": ["manual_observation"],
                    "impact_assessment": {"severity": "unknown", "scope": "unknown"}
                }
            elif analysis.get("insights") or analysis.get("patterns_found"):
                categorization["category"] = "discovery"
                categorization["confidence"] = 0.8
                categorization["rationale"] = "Insights or patterns suggest a discovery"
                insights = analysis.get('insights', [])
                patterns = analysis.get('patterns_found', [])
                discovery_title = insights[0] if insights else (patterns[0] if patterns else "Unknown")
                categorization["recommended_fields"] = {
                    "title": f"Discovery: {discovery_title}",
                    "status": "draft",
                    "evidence_sources": ["manual_observation"],
                    "validation_evidence": ["observation_analysis"]
                }

        return categorization

    def _generate_learning_artifacts(self, categorization: dict) -> list:
        """Generate draft artifacts for learning (not authoritative)."""
        artifacts = []

        category = categorization["category"]
        recommended = categorization["recommended_fields"]

        if category == "problem":
            artifact = {
                "type": "problem_draft",
                "filename": f"docs/work/agentos/problems/draft-{recommended['title'].lower().replace(' ', '-').replace(':', '')}.md",
                "content_preview": f"""---
title: "{recommended['title']}"
status: draft
created_date: {self.version}
domain: agentos
type: problem
evidence_sources: {recommended['evidence_sources']}
---

# {recommended['title']}

## Context
[Generated from manual learning observation]

## Observation
[To be filled based on user alignment]

## Impact Assessment
- **Severity**: {recommended['impact_assessment']['severity']}
- **Scope**: {recommended['impact_assessment']['scope']}

## Root Cause Analysis
[To be developed with user input]

## Potential Solutions
[To be determined through user alignment process]
""",
                "user_alignment_required": True
            }
            artifacts.append(artifact)

        elif category == "discovery":
            artifact = {
                "type": "discovery_draft",
                "filename": f"docs/work/agentos/discoveries/draft-{recommended['title'].lower().replace(' ', '-').replace(':', '')}.md",
                "content_preview": f"""---
title: "{recommended['title']}"
status: draft
created_date: {self.version}
domain: agentos
type: discovery
evidence_sources: {recommended['evidence_sources']}
---

# {recommended['title']}

## Context
[Generated from manual learning observation]

## Observation
[To be filled based on user alignment]

## Key Insights
[To be developed with user input]

## Validation Evidence
{chr(10).join(f"- {evidence}" for evidence in recommended['validation_evidence'])}

## Implications
[To be determined through user alignment process]

## Recommendations
[To be developed through iterative alignment]
""",
                "user_alignment_required": True
            }
            artifacts.append(artifact)

        return artifacts

    def _get_user_alignment_guidance(self) -> dict:
        """Provide guidance for user alignment process."""
        return {
            "alignment_questions": [
                "What specific aspects of this learning are most/least accurate?",
                "What additional context would strengthen this learning?",
                "How does this align with your experience or observations?",
                "What specific changes would make this more actionable?"
            ],
            "iteration_process": "Provide feedback, and I'll refine the learning until we achieve alignment",
            "authoritative_promotion": "Once aligned, the learning can be promoted to authoritative status",
            "multiple_lessons": "If this contains multiple distinct learnings, let me know and I'll separate them"
        }

    def get_importance_rankings(self, limit: int = 10, min_score: float = 0.0) -> dict:
        """Get importance rankings for self-reflection and gap analysis."""
        import subprocess
        import sys

        result = {
            "analysis_type": "importance_rankings",
            "limit": limit,
            "min_score": min_score,
            "rankings": [],
            "status": "analyzing"
        }

        try:
            # Use data orchestrator to get importance rankings
            sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
            from data_orchestrator import DataOrchestrator

            orchestrator = DataOrchestrator()
            data_loaded = orchestrator.load_all_data()

            if data_loaded:
                rankings = orchestrator.get_importance_rankings(limit=limit, min_score=min_score)
                result["rankings"] = rankings
                result["total_rankings"] = len(rankings)
                result["status"] = "success"
            else:
                result["status"] = "data_loading_failed"
                result["error"] = "Could not load AgentOS data"

        except ImportError as e:
            result["status"] = "import_error"
            result["error"] = f"Could not import data orchestrator: {e}"
        except Exception as e:
            result["status"] = "error"
            result["error"] = str(e)

        return result

    def _check_core_docs(self, docs_dir: Path) -> bool:
        """Check if core documentation files exist."""
        core_files = [
            "reference/agentos/architecture.md",
            "reference/agentos/behavior-spec.md",
            "README.md"
        ]

        return all((docs_dir / file).exists() for file in core_files)

def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="AgentOS v9 - Implementation-first AI development framework",
        prog="agentos"
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"AgentOS v{AgentOS().version}"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Analyze command
    analyze_parser = subparsers.add_parser(
        "analyze",
        help="Analyze codebase structure and patterns"
    )
    analyze_parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Path to analyze (default: current directory)"
    )

    # Validate command
    validate_parser = subparsers.add_parser(
        "validate",
        help="Validate project structure and configuration"
    )
    validate_parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Path to validate (default: current directory)"
    )

    # Self-determination command
    self_parser = subparsers.add_parser(
        "self-determination",
        help="Perform self-determination analysis with relationship graph"
    )

    # Learn command
    learn_parser = subparsers.add_parser(
        "learn",
        help="Perform learning analysis from observation or file"
    )
    learn_parser.add_argument(
        "observation",
        nargs="?",
        help="Text observation to learn from"
    )
    learn_parser.add_argument(
        "--file", "-f",
        help="File path to analyze for learning"
    )

    # Importance command
    importance_parser = subparsers.add_parser(
        "importance",
        help="Analyze and display document importance rankings"
    )
    importance_parser.add_argument(
        "--limit", "-l",
        type=int,
        default=10,
        help="Limit number of results (default: 10)"
    )
    importance_parser.add_argument(
        "--min-score", "-m",
        type=float,
        default=0.0,
        help="Minimum importance score to include (default: 0.0)"
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    agentos = AgentOS()

    try:
        if args.command == "analyze":
            result = agentos.analyze(args.path)
            print(json.dumps(result, indent=2))

        elif args.command == "validate":
            result = agentos.validate(args.path)
            print(json.dumps(result, indent=2))

        elif args.command == "self-determination":
            result = agentos.self_determine()
            print(json.dumps(result, indent=2))

        elif args.command == "learn":
            observation = args.observation or ""
            file_path = getattr(args, 'file', None) or ""
            result = agentos.learn(observation, file_path)
            print(json.dumps(result, indent=2))

        elif args.command == "importance":
            result = agentos.get_importance_rankings(
                limit=getattr(args, 'limit', 10),
                min_score=getattr(args, 'min_score', 0.0)
            )
            print(json.dumps(result, indent=2))

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()