#!/usr/bin/env python3
"""
Evolution Analyzer - AgentOS v9
Analyzes evolution patterns using shared data orchestrator.
Direct data access - no subprocess overhead, structured analysis.

DOE Registry - Bidirectional Linkages:
@directive docs/reference/agentos/architecture.md

# DOE Layer Declaration
DOE_LAYER = "orchestration"
DOE_RESPONSIBILITY = "Evolution pattern analysis using shared data"
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

class EvolutionAnalyzer:
    """Analyzes evolution patterns using shared data orchestrator."""

    def __init__(self, orchestrator: DataOrchestrator):
        self.orchestrator = orchestrator

    def analyze_evolution_patterns(self) -> Dict[str, Any]:
        """
        Analyze evolution patterns using direct data access.
        Reveals documentation integration patterns for AI analysis.
        """
        data = self.orchestrator.get_structured_data()

        result = {
            "analysis_timestamp": datetime.now().isoformat(),
            "script_role": "pattern_analysis_using_shared_data",
            "evolution_insights": {},
            "analysis_status": "processing"
        }

        try:
            # Analyze integration patterns directly from loaded data
            result["evolution_insights"]["relationship_structure"] = self._analyze_relationship_structure(data)
            result["evolution_insights"]["gap_patterns"] = self._analyze_gap_patterns(data)
            result["evolution_insights"]["authority_evolution"] = self._analyze_authority_evolution(data)
            result["evolution_insights"]["coherence_trends"] = self._analyze_coherence_trends(data)

            result["analysis_status"] = "complete"

        except Exception as e:
            result["analysis_status"] = "error"
            result["error"] = str(e)

        return result

    def _analyze_relationship_structure(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze the structure of relationships for evolution insights."""
        relationships = data['relationships']
        coherence = data['coherence_metrics']

        # Count relationships by type
        rel_counts = {}
        for rel_type, rel_data in relationships.items():
            rel_counts[rel_type] = sum(len(targets) for targets in rel_data.values())

        return {
            "relationship_types_used": rel_counts,
            "total_relationships": sum(rel_counts.values()),
            "connection_coverage": coherence['connection_coverage'],
            "isolated_documents": coherence['isolated_documents'],
            "evolution_readiness": "connected" if coherence['connection_coverage'] > 0.5 else "fragmented"
        }

    def _analyze_gap_patterns(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze gap patterns that indicate evolution opportunities."""
        relationships = data['relationships']
        documents = data['documents']

        gaps = {
            "missing_relationships": [],
            "orphaned_references": [],
            "authority_violations": []
        }

        # Find documents with no relationships (potential gaps)
        connected_docs = set()
        for rel_data in relationships.values():
            for source, targets in rel_data.items():
                connected_docs.add(source)
                connected_docs.update(targets)

        all_docs = set(documents.keys())
        isolated_docs = all_docs - connected_docs

        gaps["missing_relationships"] = list(isolated_docs)

        # Check for orphaned references (relationships to non-existent docs)
        for rel_type, rel_data in relationships.items():
            for source, targets in rel_data.items():
                for target in targets:
                    if target not in all_docs:
                        gaps["orphaned_references"].append({
                            "source": source,
                            "target": target,
                            "relationship": rel_type
                        })

        return {
            "gaps_identified": len(gaps["missing_relationships"]) + len(gaps["orphaned_references"]),
            "gap_details": gaps,
            "evolution_opportunity": "high" if len(gaps["missing_relationships"]) > 2 else "medium"
        }

    def _analyze_authority_evolution(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze authority flow patterns for evolution insights."""
        authority_flow = data['authority_flow']
        authority_hierarchy = data['authority_hierarchy']

        return {
            "authority_flows_valid": len(authority_flow['valid_flows']),
            "authority_violations": len(authority_flow['invalid_flows']),
            "hierarchy_levels": len(authority_hierarchy['levels']),
            "authority_maturity": "high" if len(authority_flow['invalid_flows']) == 0 else "needs_attention"
        }

    def _analyze_coherence_trends(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze coherence trends that indicate system evolution state."""
        coherence = data['coherence_metrics']
        relationships = data['relationships']

        # Calculate relationship density
        total_docs = coherence['total_documents']
        total_relationships = coherence['total_relationships']
        relationship_density = total_relationships / max(total_docs, 1)

        return {
            "relationship_density": relationship_density,
            "coherence_score": coherence['connection_coverage'],
            "system_maturity_indicator": self._calculate_maturity_indicator(coherence, relationship_density),
            "evolution_velocity": "stable" if coherence['connection_coverage'] > 0.6 else "evolving"
        }

    def _calculate_maturity_indicator(self, coherence: Dict[str, Any], density: float) -> str:
        """Calculate a maturity indicator based on coherence and density."""
        coverage = coherence['connection_coverage']

        if coverage > 0.8 and density > 1.0:
            return "mature"
        elif coverage > 0.5 and density > 0.5:
            return "developing"
        elif coverage > 0.2:
            return "emerging"
        else:
            return "nascent"

def main():
    """CLI interface for evolution analysis - maintains backwards compatibility."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Evolution Analyzer - analyzes evolution patterns using shared data"
    )

    parser.add_argument(
        "command",
        choices=["analyze"],
        help="Command to execute"
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
    analyzer = EvolutionAnalyzer(orchestrator)
    result = analyzer.analyze_evolution_patterns()

    if args.output == "json":
        print(json.dumps(result, indent=2))
    else:
        print("Evolution Pattern Analysis Complete")
        print("=" * 50)
        print(f"Timestamp: {result['analysis_timestamp']}")
        print(f"Status: {result['analysis_status']}")
        insights = result['evolution_insights']
        print(f"Relationship Types: {len(insights['relationship_structure']['relationship_types_used'])}")
        print(f"Gaps Identified: {insights['gap_patterns']['gaps_identified']}")
        print(f"Authority Maturity: {insights['authority_evolution']['authority_maturity']}")
        print(f"System Maturity: {insights['coherence_trends']['system_maturity_indicator']}")
        print("\nEvolution patterns analyzed for AI insights.")

if __name__ == "__main__":
    main()