#!/usr/bin/env python3
"""
Self-Determination Analyzer - AgentOS v9
Orchestration layer analysis of self-determination evidence.

DOE Declaration:
- DOE_LAYER: orchestration
- DOE_RESPONSIBILITY: Analyze self-determination evidence for system insights
- DOE_GOVERNANCE: docs/reference/agentos/orchestration-layer.md
- DOE_PRECEDENCE: 3
"""

import sys
import json
import argparse
from pathlib import Path
from typing import Dict, Any

# DOE Layer Declaration
DOE_LAYER = "orchestration"
DOE_RESPONSIBILITY = "Analyze self-determination evidence for system insights"
DOE_GOVERNANCE = "docs/reference/agentos/orchestration-layer.md"
DOE_PRECEDENCE = 3

class SelfDeterminationAnalyzer:
    """Analyze self-determination evidence to provide system insights."""

    def __init__(self):
        self.evidence = {}

    def load_evidence(self, evidence_file: str = "") -> bool:
        """Load evidence from file or collect it directly."""
        if evidence_file:
            try:
                with open(evidence_file, 'r') as f:
                    self.evidence = json.load(f)
                return True
            except Exception as e:
                print(f"Error loading evidence file: {e}", file=sys.stderr)
                return False
        else:
            # Collect evidence directly
            try:
                import subprocess
                result = subprocess.run(
                    [sys.executable, str(Path(__file__).parent / ".." / "src" / "agentos.py"), "self-determination"],
                    capture_output=True, text=True, cwd=Path(__file__).parent.parent
                )
                if result.returncode == 0:
                    self.evidence = json.loads(result.stdout)
                    return True
                else:
                    print(f"Error collecting evidence: {result.stderr}", file=sys.stderr)
                    return False
            except Exception as e:
                print(f"Error collecting evidence: {e}", file=sys.stderr)
                return False

    def analyze_system_coherence(self) -> Dict[str, Any]:
        """Analyze overall system coherence from evidence."""
        if not self.evidence:
            return {"error": "No evidence loaded"}

        facts = self.evidence.get("system_facts", {})
        rel_evidence = self.evidence.get("relationship_evidence", {})
        dir_evidence = self.evidence.get("directive_evidence", {})

        coherence_score = 0
        findings = []

        # Check directory completeness
        dirs_present = facts.get("directories_present", {})
        if all(dirs_present.values()):
            coherence_score += 25
            findings.append("All core directories present (docs, scripts, src)")
        else:
            findings.append(f"Missing directories: {[k for k, v in dirs_present.items() if not v]}")

        # Check file counts
        docs_count = facts.get("docs_count", 0)
        scripts_count = facts.get("scripts_count", 0)
        if docs_count > 0 and scripts_count > 0:
            coherence_score += 25
            findings.append(f"Documentation ({docs_count} files) and scripts ({scripts_count} files) present")
        else:
            findings.append("Missing documentation or implementation files")

        # Check relationship evidence
        if rel_evidence.get("evidence_collected"):
            relationship_count = rel_evidence.get("relationship_count", 0)
            coherence_score += 25
            findings.append(f"Relationship graph evidence collected ({relationship_count} relationships)")
        else:
            findings.append("Relationship evidence collection failed")

        # Check directive evidence
        if dir_evidence.get("docs_directory_exists"):
            coherence_score += 25
            findings.append("Directive structure validation completed")
        else:
            findings.append("Directive structure validation failed")

        return {
            "coherence_score": coherence_score,
            "max_score": 100,
            "findings": findings,
            "recommendations": self._generate_recommendations(coherence_score)
        }

    def _generate_recommendations(self, coherence_score: int) -> list:
        """Generate recommendations based on coherence score."""
        if coherence_score >= 75:
            return ["System coherence excellent - maintain current practices"]
        elif coherence_score >= 50:
            return ["Review missing directories or files", "Verify relationship configurations"]
        else:
            return ["Critical: System structure incomplete", "Immediate review of core directories required"]

    def analyze_evolutionary_readiness(self) -> Dict[str, Any]:
        """Analyze evolutionary readiness based on evidence."""
        if not self.evidence:
            return {"error": "No evidence loaded"}

        facts = self.evidence.get("system_facts", {})
        total_files = facts.get("total_files", 0)

        # Simple evolutionary readiness assessment
        readiness_score = min(100, total_files * 2)  # Rough heuristic

        return {
            "evolutionary_readiness_score": readiness_score,
            "assessment_factors": {
                "total_files": total_files,
                "documentation_coverage": facts.get("docs_count", 0),
                "implementation_coverage": facts.get("scripts_count", 0) + facts.get("src_count", 0)
            },
            "insights": [
                f"System contains {total_files} total files",
                "Evolution potential correlates with file complexity and coverage"
            ]
        }

    def generate_comprehensive_analysis(self) -> Dict[str, Any]:
        """Generate comprehensive analysis from evidence."""
        return {
            "analysis_type": "orchestration_layer_self_determination_analysis",
            "evidence_timestamp": self.evidence.get("evidence_collection", {}).get("timestamp"),
            "system_coherence": self.analyze_system_coherence(),
            "evolutionary_readiness": self.analyze_evolutionary_readiness(),
            "doe_compliance": {
                "orchestration_layer": DOE_LAYER,
                "evidence_consumed": bool(self.evidence),
                "analysis_provided": True
            }
        }


def main():
    parser = argparse.ArgumentParser(description="Analyze self-determination evidence")
    parser.add_argument("--evidence-file", help="JSON file containing self-determination evidence")
    parser.add_argument("--output", choices=["json", "text"], default="json", help="Output format")
    args = parser.parse_args()

    analyzer = SelfDeterminationAnalyzer()

    if not analyzer.load_evidence(args.evidence_file):
        print("Failed to load evidence", file=sys.stderr)
        sys.exit(1)

    analysis = analyzer.generate_comprehensive_analysis()

    if args.output == "json":
        print(json.dumps(analysis, indent=2))
    else:
        print("Self-Determination Analysis Results")
        print("=" * 40)
        coherence = analysis.get("system_coherence", {})
        print(f"Coherence Score: {coherence.get('coherence_score', 0)}/100")
        print("\nFindings:")
        for finding in coherence.get("findings", []):
            print(f"- {finding}")
        print("\nRecommendations:")
        for rec in coherence.get("recommendations", []):
            print(f"- {rec}")


if __name__ == "__main__":
    main()