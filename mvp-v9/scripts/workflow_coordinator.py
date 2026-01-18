#!/usr/bin/env python3
"""
Workflow Analyzer - AgentOS v9
Analyzes command-based workflow execution patterns using shared data orchestrator.
Direct data access for workflow coordination analysis - no subprocess overhead.

DOE Registry - Bidirectional Linkages:
@directive docs/reference/agentos/architecture.md
@directive docs/reference/agentos/learning-system.md

# DOE Layer Declaration
DOE_LAYER = "orchestration"
DOE_RESPONSIBILITY = "Analyze workflow coordination patterns and orchestration potential"
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

class WorkflowAnalyzer:
    """Analyzes workflow execution patterns using shared data orchestrator."""

    def __init__(self, orchestrator: DataOrchestrator):
        self.orchestrator = orchestrator

    def analyze_workflow_patterns(self) -> Dict[str, Any]:
        """
        Analyze workflow execution patterns using direct data access.
        Reveals command-based workflow coordination opportunities.
        """
        data = self.orchestrator.get_structured_data()

        result = {
            "analysis_timestamp": datetime.now().isoformat(),
            "script_role": "workflow_analysis_using_shared_data",
            "workflow_execution_insights": {},
            "analysis_status": "processing"
        }

        try:
            # Analyze documentation workflow patterns
            result["workflow_execution_insights"]["documentation_workflows"] = self._analyze_documentation_workflows(data)

            # Analyze relationship-based workflows
            result["workflow_execution_insights"]["relationship_workflows"] = self._analyze_relationship_workflows(data)

            # Analyze authority-based execution patterns
            result["workflow_execution_insights"]["authority_execution"] = self._analyze_authority_execution(data)

            # Analyze multi-step task orchestration potential
            result["workflow_execution_insights"]["orchestration_potential"] = self._analyze_orchestration_potential(data)

            result["analysis_status"] = "complete"

        except Exception as e:
            result["analysis_status"] = "error"
            result["error"] = str(e)

        return result

    def _analyze_documentation_workflows(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze documentation workflow patterns."""
        documents = data['documents']
        coherence = data['coherence_metrics']

        workflow_analysis = {
            "documentation_lifecycle": {},
            "authority_progression": {},
            "relationship_maturation": {},
            "workflow_efficiency": {}
        }

        # Analyze documentation lifecycle
        status_counts = {}
        type_counts = {}

        for doc_path, doc_data in documents.items():
            status = doc_data.get('status', 'unknown')
            status_counts[status] = status_counts.get(status, 0) + 1

            # Infer document type from path
            doc_type = self._infer_document_type(doc_path)
            type_counts[doc_type] = type_counts.get(doc_type, 0) + 1

        workflow_analysis["documentation_lifecycle"] = {
            "status_distribution": status_counts,
            "type_distribution": type_counts,
            "maturity_progression": self._calculate_maturity_progression(status_counts)
        }

        # Authority progression analysis
        authority_distribution = coherence['authority_distribution']
        workflow_analysis["authority_progression"] = {
            "authority_levels_utilized": len(authority_distribution),
            "authority_distribution": authority_distribution,
            "hierarchy_completeness": len(authority_distribution) / 7.0  # 7 authority levels total
        }

        # Relationship maturation
        relationships = data['relationships']
        workflow_analysis["relationship_maturation"] = {
            "relationship_types_active": len([rt for rt, rels in relationships.items() if rels]),
            "relationship_coverage": coherence['connection_coverage'],
            "relationship_maturity_score": self._calculate_relationship_maturity(relationships, len(documents))
        }

        # Workflow efficiency
        workflow_analysis["workflow_efficiency"] = {
            "documentation_density": len(documents),
            "relationship_density": coherence['total_relationships'] / max(len(documents), 1),
            "authority_flow_efficiency": len(data['authority_flow']['valid_flows']) / max(len(data['authority_flow']['valid_flows']) + len(data['authority_flow']['invalid_flows']), 1),
            "overall_efficiency_score": self._calculate_workflow_efficiency(workflow_analysis)
        }

        return workflow_analysis

    def _infer_document_type(self, doc_path: str) -> str:
        """Infer document type from path."""
        path_parts = doc_path.split('/')

        if len(path_parts) >= 2:
            category = path_parts[1]

            type_mappings = {
                'reference': 'reference',
                'how-to': 'procedural',
                'explanation': 'explanatory',
                'tutorials': 'tutorial',
                'work': 'working',
                'archive': 'archival'
            }

            return type_mappings.get(category, 'unknown')

        return 'root'

    def _calculate_maturity_progression(self, status_counts: Dict[str, int]) -> Dict[str, Any]:
        """Calculate documentation maturity progression."""
        total_docs = sum(status_counts.values())

        if total_docs == 0:
            return {"maturity_level": "empty", "progression_score": 0}

        # Maturity weights (higher = more mature)
        maturity_weights = {
            'draft': 1,
            'review': 2,
            'approved': 3,
            'published': 4,
            'archived': 5
        }

        weighted_sum = sum(count * maturity_weights.get(status, 0) for status, count in status_counts.items())
        avg_maturity = weighted_sum / total_docs

        maturity_levels = ["nascent", "developing", "mature", "optimized"]
        maturity_index = min(int(avg_maturity), len(maturity_levels) - 1)

        return {
            "maturity_level": maturity_levels[maturity_index],
            "progression_score": avg_maturity,
            "maturity_distribution": status_counts
        }

    def _calculate_relationship_maturity(self, relationships: Dict[str, Any], doc_count: int) -> float:
        """Calculate relationship maturity score."""
        if doc_count == 0:
            return 0.0

        # Maturity based on relationship diversity and coverage
        type_diversity = len([rt for rt, rels in relationships.items() if rels])
        total_relationships = sum(len(targets) for rel_data in relationships.values() for targets in rel_data.values())

        diversity_score = min(1.0, type_diversity / 8.0)  # 8 relationship types possible
        coverage_score = min(1.0, total_relationships / (doc_count * 2))  # Ideal: 2 relationships per doc

        return (diversity_score + coverage_score) / 2.0

    def _calculate_workflow_efficiency(self, workflow_analysis: Dict[str, Any]) -> float:
        """Calculate overall workflow efficiency score."""
        lifecycle = workflow_analysis["documentation_lifecycle"]
        progression = workflow_analysis["relationship_maturation"]
        authority = workflow_analysis["authority_progression"]

        # Component scores (0-1 scale)
        maturity_score = min(1.0, lifecycle["maturity_progression"]["progression_score"] / 4.0)
        relationship_score = progression["relationship_maturity_score"]
        authority_score = authority["hierarchy_completeness"]

        # Weighted average
        return (maturity_score * 0.4 + relationship_score * 0.4 + authority_score * 0.2)

    def _analyze_relationship_workflows(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze relationship-based workflow patterns."""
        relationships = data['relationships']

        workflow_patterns = {
            "relationship_chains": {},
            "dependency_networks": {},
            "workflow_complexity": {},
            "execution_paths": []
        }

        # Analyze relationship chains
        for rel_type, rel_data in relationships.items():
            chain_analysis = {
                "total_links": sum(len(targets) for targets in rel_data.values()),
                "unique_sources": len(rel_data),
                "average_chain_length": sum(len(targets) for targets in rel_data.values()) / max(len(rel_data), 1),
                "most_connected_source": max(rel_data.keys(), key=lambda k: len(rel_data[k])) if rel_data else None
            }
            workflow_patterns["relationship_chains"][rel_type] = chain_analysis

        # Analyze dependency networks
        workflow_patterns["dependency_networks"] = self._analyze_dependency_networks(relationships)

        # Workflow complexity analysis
        workflow_patterns["workflow_complexity"] = {
            "relationship_type_entropy": self._calculate_relationship_entropy(relationships),
            "network_density": self._calculate_network_density(relationships, len(data['documents'])),
            "centrality_distribution": self._analyze_centrality(relationships)
        }

        return workflow_patterns

    def _analyze_dependency_networks(self, relationships: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze dependency networks in relationships."""
        networks = {}

        for rel_type, rel_data in relationships.items():
            network = {
                "nodes": [],
                "edges": [],
                "strongly_connected": [],
                "weakly_connected": []
            }

            # Build network graph
            nodes_set = set()
            for source, targets in rel_data.items():
                nodes_set.add(source)
                for target in targets:
                    nodes_set.add(target)
                    network["edges"].append((source, target))

            network["nodes"] = list(nodes_set)

            # Analyze connectivity (simplified)
            node_count = len(network["nodes"])
            edge_count = len(network["edges"])

            if node_count > 1:
                # Calculate basic connectivity metrics
                network["connectivity_ratio"] = float(edge_count / (node_count * (node_count - 1) / 2)) if node_count > 1 else 0.0
                network["average_degree"] = float((2 * edge_count) / node_count) if node_count > 0 else 0.0

            networks[rel_type] = network

        return networks

    def _calculate_relationship_entropy(self, relationships: Dict[str, Any]) -> float:
        """Calculate relationship type entropy (diversity measure)."""
        total_links = sum(len(targets) for rel_data in relationships.values() for targets in rel_data.values())

        if total_links == 0:
            return 0.0

        entropy = 0.0
        for rel_data in relationships.values():
            rel_links = sum(len(targets) for targets in rel_data.values())
            if rel_links > 0:
                p = rel_links / total_links
                entropy -= p * (p ** 0.5)  # Simplified entropy

        return entropy

    def _calculate_network_density(self, relationships: Dict[str, Any], node_count: int) -> float:
        """Calculate overall network density."""
        if node_count <= 1:
            return 0.0

        total_possible_edges = node_count * (node_count - 1) / 2
        total_actual_edges = sum(len(targets) for rel_data in relationships.values() for targets in rel_data.values())

        return total_actual_edges / total_possible_edges if total_possible_edges > 0 else 0.0

    def _analyze_centrality(self, relationships: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze centrality distribution in relationship network."""
        centrality = {}

        # Count connections for each node
        for rel_data in relationships.values():
            for source, targets in rel_data.items():
                centrality[source] = centrality.get(source, 0) + len(targets)
                for target in targets:
                    centrality[target] = centrality.get(target, 0) + 1  # Incoming connection

        if not centrality:
            return {"most_central": None, "average_centrality": 0, "centrality_distribution": {}}

        # Calculate centrality statistics
        centrality_values = list(centrality.values())
        most_central = max(centrality.items(), key=lambda x: x[1])

        return {
            "most_central_node": most_central[0],
            "highest_centrality": most_central[1],
            "average_centrality": sum(centrality_values) / len(centrality_values),
            "centrality_range": max(centrality_values) - min(centrality_values)
        }

    def _analyze_authority_execution(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze authority-based execution patterns."""
        authority_flow = data['authority_flow']
        authority_hierarchy = data['authority_hierarchy']

        execution_analysis = {
            "authority_flow_patterns": {},
            "execution_hierarchy": {},
            "authority_compliance": {},
            "workflow_authorization": {}
        }

        # Authority flow patterns
        execution_analysis["authority_flow_patterns"] = {
            "valid_execution_paths": len(authority_flow['valid_flows']),
            "blocked_execution_paths": len(authority_flow['invalid_flows']),
            "authority_flow_efficiency": len(authority_flow['valid_flows']) / max(len(authority_flow['valid_flows']) + len(authority_flow['invalid_flows']), 1)
        }

        # Execution hierarchy
        execution_analysis["execution_hierarchy"] = {
            "hierarchy_depth": len(authority_hierarchy['levels']),
            "authority_levels_active": len(authority_hierarchy['validation_rules']),
            "hierarchy_utilization": len(authority_hierarchy['validation_rules']) / max(len(authority_hierarchy['levels']), 1)
        }

        # Authority compliance
        compliance_score = execution_analysis["authority_flow_patterns"]["authority_flow_efficiency"]
        execution_analysis["authority_compliance"] = {
            "compliance_score": compliance_score,
            "compliance_level": "high" if compliance_score > 0.9 else "medium" if compliance_score > 0.7 else "low",
            "violation_impact": "minimal" if len(authority_flow['invalid_flows']) == 0 else "moderate" if len(authority_flow['invalid_flows']) < 3 else "significant"
        }

        # Workflow authorization patterns
        execution_analysis["workflow_authorization"] = self._analyze_workflow_authorization(data)

        return execution_analysis

    def _analyze_workflow_authorization(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze workflow authorization patterns."""
        documents = data['documents']
        authority_distribution = data['coherence_metrics']['authority_distribution']

        authorization_patterns = {
            "authority_level_distribution": authority_distribution,
            "authorization_boundaries": {},
            "workflow_clearance_levels": []
        }

        # Identify authorization boundaries (gaps in authority levels)
        used_levels = sorted(authority_distribution.keys())
        all_levels = list(range(1, 8))  # Authority levels 1-7

        missing_levels = [level for level in all_levels if level not in used_levels]
        authorization_patterns["authorization_boundaries"] = {
            "missing_authority_levels": missing_levels,
            "authority_gaps": len(missing_levels),
            "authority_continuity": len(missing_levels) == 0
        }

        # Define workflow clearance levels based on authority
        clearance_mapping = {
            range(1, 3): "basic_workflow_clearance",
            range(3, 5): "intermediate_workflow_clearance",
            range(5, 8): "advanced_workflow_clearance"
        }

        for level_range, clearance in clearance_mapping.items():
            if any(level in level_range for level in used_levels):
                authorization_patterns["workflow_clearance_levels"].append(clearance)

        return authorization_patterns

    def _analyze_orchestration_potential(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze multi-step task orchestration potential."""
        coherence = data['coherence_metrics']
        relationships = data['relationships']

        orchestration_analysis = {
            "orchestration_readiness": {},
            "multi_step_potential": {},
            "task_coordination_capacity": {},
            "workflow_automation_potential": {}
        }

        # Orchestration readiness
        orchestration_analysis["orchestration_readiness"] = {
            "relationship_network_maturity": coherence['connection_coverage'] > 0.5,
            "authority_flow_stability": len(data['authority_flow']['invalid_flows']) == 0,
            "data_consistency": data['metadata']['data_integrity']['data_valid'],
            "orchestration_score": self._calculate_orchestration_score(data)
        }

        # Multi-step potential
        orchestration_analysis["multi_step_potential"] = {
            "relationship_chain_depth": self._calculate_chain_depth(relationships),
            "parallel_execution_paths": len([rt for rt, rels in relationships.items() if len(rels) > 2]),
            "sequential_dependencies": len([rt for rt, rels in relationships.items() if rt in ['depends_on', 'governed_by']]),
            "complexity_score": self._calculate_workflow_complexity(relationships, len(data['documents']))
        }

        # Task coordination capacity
        orchestration_analysis["task_coordination_capacity"] = {
            "coordination_nodes": len(data['documents']) - coherence['isolated_documents'],
            "coordination_density": coherence['total_relationships'] / max(len(data['documents']), 1),
            "bottleneck_identification": self._identify_coordination_bottlenecks(relationships),
            "scalability_potential": "high" if coherence['connection_coverage'] > 0.7 else "medium" if coherence['connection_coverage'] > 0.4 else "low"
        }

        return orchestration_analysis

    def _calculate_orchestration_score(self, data: Dict[str, Any]) -> float:
        """Calculate orchestration readiness score."""
        coherence = data['coherence_metrics']
        authority_flow = data['authority_flow']

        # Component scores
        connectivity_score = coherence['connection_coverage']
        authority_score = 1.0 if len(authority_flow['invalid_flows']) == 0 else 0.5
        consistency_score = 1.0 if data['metadata']['data_integrity']['data_valid'] else 0.3

        return (connectivity_score + authority_score + consistency_score) / 3.0

    def _calculate_chain_depth(self, relationships: Dict[str, Any]) -> int:
        """Calculate maximum relationship chain depth."""
        # Simplified chain depth calculation
        max_depth = 0

        for rel_data in relationships.values():
            for targets in rel_data.values():
                max_depth = max(max_depth, len(targets))

        return max_depth

    def _calculate_workflow_complexity(self, relationships: Dict[str, Any], doc_count: int) -> float:
        """Calculate workflow complexity score."""
        if doc_count == 0:
            return 0.0

        # Complexity based on relationship diversity and density
        type_count = len([rt for rt, rels in relationships.items() if rels])
        total_relationships = sum(len(targets) for rel_data in relationships.values() for targets in rel_data.values())

        type_complexity = min(1.0, type_count / 8.0)  # 8 possible relationship types
        density_complexity = min(1.0, total_relationships / (doc_count * 3))  # Ideal: 3 relationships per doc

        return (type_complexity + density_complexity) / 2.0

    def _identify_coordination_bottlenecks(self, relationships: Dict[str, Any]) -> List[str]:
        """Identify potential coordination bottlenecks."""
        bottlenecks = []

        # Check for nodes with too many dependencies
        for rel_type, rel_data in relationships.items():
            for source, targets in rel_data.items():
                if len(targets) > 5:  # Arbitrary threshold
                    bottlenecks.append(f"high_dependency_node: {source} ({len(targets)} {rel_type} relationships)")

        # Check for relationship types with low utilization
        for rel_type, rel_data in relationships.items():
            total_links = sum(len(targets) for targets in rel_data.values())
            if total_links == 0:
                bottlenecks.append(f"unused_relationship_type: {rel_type}")

        return bottlenecks

def main():
    """CLI interface for workflow analysis - maintains backwards compatibility."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Workflow Analyzer - analyzes command-based workflow execution patterns"
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
    analyzer = WorkflowAnalyzer(orchestrator)
    result = analyzer.analyze_workflow_patterns()

    if args.output == "json":
        print(json.dumps(result, indent=2))
    else:
        print("Workflow Execution Pattern Analysis")
        print("=" * 50)
        print(f"Timestamp: {result['analysis_timestamp']}")
        print(f"Status: {result['analysis_status']}")
        insights = result['workflow_execution_insights']
        print(f"Documentation Types: {len(insights['documentation_workflows']['documentation_lifecycle']['type_distribution'])}")
        print(f"Relationship Types: {len(insights['relationship_workflows']['relationship_chains'])}")
        print(f"Authority Levels: {insights['authority_execution']['execution_hierarchy']['authority_levels_active']}")
        print("\nCommand-based workflow patterns analyzed for AI orchestration.")

if __name__ == "__main__":
    main()