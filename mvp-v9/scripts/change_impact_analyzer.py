#!/usr/bin/env python3
"""
Change Impact Analyzer - AgentOS v9
Analyzes relationship-aware change impact patterns using shared data orchestrator.
Direct data access for change impact analysis - no subprocess overhead.

DOE Registry - Bidirectional Linkages:
@directive docs/reference/agentos/architecture.md

# DOE Layer Declaration
DOE_LAYER = "orchestration"
DOE_RESPONSIBILITY = "Analyze relationship-aware change impacts"
DOE_GOVERNANCE = "docs/reference/agentos/doe-framework.md"
DOE_PRECEDENCE = 3
"""

import sys
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime

# Import data orchestrator
try:
    from data_orchestrator import DataOrchestrator
except ImportError:
    try:
        from .data_orchestrator import DataOrchestrator
    except ImportError:
        print("Error: Could not import data orchestrator")
        sys.exit(1)

class ChangeImpactAnalyzer:
    """Analyzes change impact using shared data orchestrator."""

    def __init__(self, orchestrator: DataOrchestrator):
        self.orchestrator = orchestrator

    def analyze_change_impact(self, change_description: str, affected_files: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Analyze change impact on relationship network using direct data access.
        Reveals how changes affect documentation integration patterns.
        """
        data = self.orchestrator.get_structured_data()

        result = {
            "analysis_timestamp": datetime.now().isoformat(),
            "script_role": "impact_analysis_using_shared_data",
            "change_description": change_description,
            "affected_files_provided": affected_files or [],
            "impact_analysis": {},
            "analysis_status": "processing"
        }

        try:
            # Analyze current system state for impact baseline
            result["impact_analysis"]["baseline_state"] = self._analyze_baseline_state(data)

            # Analyze potential relationship impacts
            result["impact_analysis"]["relationship_impacts"] = self._analyze_relationship_impacts(data, change_description)

            # Analyze authority flow impacts
            result["impact_analysis"]["authority_impacts"] = self._analyze_authority_impacts(data)

            # If specific files provided, analyze their specific impacts
            if affected_files:
                result["impact_analysis"]["file_specific_impacts"] = self._analyze_file_impacts(data, affected_files)

            # Calculate overall impact assessment
            result["impact_analysis"]["overall_assessment"] = self._calculate_overall_impact(result["impact_analysis"])

            result["analysis_status"] = "complete"

        except Exception as e:
            result["analysis_status"] = "error"
            result["error"] = str(e)

        return result

    def _analyze_baseline_state(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze current system state as baseline for impact assessment."""
        coherence = data['coherence_metrics']
        relationships = data['relationships']

        return {
            "current_coherence": coherence['connection_coverage'],
            "total_relationships": coherence['total_relationships'],
            "isolated_documents": coherence['isolated_documents'],
            "relationship_types": len([rt for rt, rels in relationships.items() if rels]),
            "authority_distribution": coherence['authority_distribution']
        }

    def _analyze_relationship_impacts(self, data: Dict[str, Any], change_description: str) -> Dict[str, Any]:
        """Analyze how the change might impact relationship patterns."""
        relationships = data['relationships']
        coherence = data['coherence_metrics']

        # Analyze change keywords to predict relationship impacts
        change_lower = change_description.lower()

        potential_impacts = {
            "relationship_types_affected": [],
            "coherence_change_prediction": "stable",
            "isolation_risk_increase": 0,
            "integration_opportunities": []
        }

        # Predict impacts based on change description
        if any(word in change_lower for word in ['add', 'create', 'new', 'implement']):
            potential_impacts["relationship_types_affected"].extend(['depends_on', 'implements'])
            potential_impacts["coherence_change_prediction"] = "improving"
            potential_impacts["integration_opportunities"].append("new_relationships_possible")

        if any(word in change_lower for word in ['remove', 'delete', 'deprecate']):
            potential_impacts["relationship_types_affected"].extend(['supersedes', 'governed_by'])
            potential_impacts["coherence_change_prediction"] = "degrading"
            potential_impacts["isolation_risk_increase"] = 1

        if any(word in change_lower for word in ['refactor', 'restructure', 'reorganize']):
            potential_impacts["relationship_types_affected"].extend(['related', 'references'])
            potential_impacts["coherence_change_prediction"] = "restructuring"

        return potential_impacts

    def _analyze_authority_impacts(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze potential authority flow impacts."""
        authority_flow = data['authority_flow']

        return {
            "current_authority_violations": len(authority_flow['invalid_flows']),
            "authority_flow_stability": "stable" if len(authority_flow['invalid_flows']) == 0 else "vulnerable",
            "hierarchy_levels_affected": len(data['authority_hierarchy']['levels']),
            "authority_impact_risk": "low" if len(authority_flow['invalid_flows']) == 0 else "medium"
        }

    def _analyze_file_impacts(self, data: Dict[str, Any], affected_files: List[str]) -> Dict[str, Any]:
        """Analyze impacts specific to affected files."""
        file_impacts = {}

        for file_path in affected_files:
            if file_path in data['documents']:
                doc_data = data['documents'][file_path]

                # Get document's current relationship context
                relationships = self.orchestrator.get_document_context(file_path)

                file_impacts[file_path] = {
                    "exists": True,
                    "current_relationships": len(relationships.get('relationships', {})),
                    "authority_level": doc_data.get('authority_level', 'unknown'),
                    "is_isolated": len(relationships.get('relationships', {})) == 0,
                    "impact_sensitivity": self._calculate_impact_sensitivity(relationships)
                }
            else:
                file_impacts[file_path] = {
                    "exists": False,
                    "impact_prediction": "new_file_creation"
                }

        return file_impacts

    def _calculate_impact_sensitivity(self, relationships: Dict[str, Any]) -> str:
        """Calculate how sensitive a document is to changes."""
        rel_count = len(relationships.get('relationships', {}))

        if rel_count == 0:
            return "high_isolation_risk"
        elif rel_count <= 2:
            return "medium_coupling"
        else:
            return "low_well_connected"

    def _calculate_overall_impact(self, impact_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate overall change impact assessment."""
        baseline = impact_analysis['baseline_state']
        relationship_impacts = impact_analysis['relationship_impacts']
        authority_impacts = impact_analysis['authority_impacts']

        # Calculate impact score (0-100, higher = more impactful)
        impact_score = 0

        # Baseline coherence affects impact
        if baseline['current_coherence'] < 0.5:
            impact_score += 30  # Low coherence = higher impact potential

        # Authority stability affects impact
        if authority_impacts['authority_impact_risk'] == "medium":
            impact_score += 20

        # Relationship prediction affects impact
        if relationship_impacts['coherence_change_prediction'] == "improving":
            impact_score += 10
        elif relationship_impacts['coherence_change_prediction'] == "degrading":
            impact_score += 25

        # Isolation risk increases impact
        impact_score += relationship_impacts['isolation_risk_increase'] * 15

        impact_score = min(100, max(0, impact_score))

        # Determine impact level
        if impact_score >= 70:
            impact_level = "high"
        elif impact_score >= 40:
            impact_level = "medium"
        else:
            impact_level = "low"

        return {
            "impact_score": impact_score,
            "impact_level": impact_level,
            "requires_detailed_analysis": impact_score > 50,
            "monitoring_recommended": impact_level in ["medium", "high"]
        }

def main():
    """CLI interface for change impact analysis - maintains backwards compatibility."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Change Impact Analyzer - analyzes relationship-aware change impacts"
    )

    parser.add_argument(
        "command",
        choices=["analyze"],
        help="Command to execute"
    )

    parser.add_argument(
        "change_description",
        help="Description of the change to analyze"
    )

    parser.add_argument(
        "--files", "-f",
        nargs="*",
        help="Specific files affected by the change"
    )

    parser.add_argument(
        "--output", "-o",
        choices=["json", "text"],
        default="json",
        help="Output format (default: json)"
    )

    args = parser.parse_args()

    # Load data using orchestrator
    orchestrator = DataOrchestrator()
    success = orchestrator.load_all_data()

    if not success:
        print("Error: Failed to load data")
        sys.exit(1)

    # Analyze using shared data
    analyzer = ChangeImpactAnalyzer(orchestrator)
    result = analyzer.analyze_change_impact(args.change_description, args.files)

    if args.output == "json":
        print(json.dumps(result, indent=2))
    else:
        print("Change Impact Analysis Complete")
        print("=" * 50)
        print(f"Change: {result['change_description']}")
        print(f"Timestamp: {result['analysis_timestamp']}")
        print(f"Status: {result['analysis_status']}")
        assessment = result['impact_analysis'].get('overall_assessment', {})
        print(f"Impact Level: {assessment.get('impact_level', 'unknown')}")
        print(f"Impact Score: {assessment.get('impact_score', 0)}")
        if args.files:
            print(f"Files Analyzed: {len(args.files)}")
        print("\nChange impact patterns analyzed for AI insights.")

if __name__ == "__main__":
    main()