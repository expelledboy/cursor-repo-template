#!/usr/bin/env python3
"""
Memory Bank Analyzer - AgentOS v9
Analyzes context optimization patterns using shared data orchestrator.
Direct data access for memory optimization analysis - no subprocess overhead.

DOE Registry - Bidirectional Linkages:
@directive docs/reference/agentos/architecture.md
@directive docs/reference/agentos/learning-system.md

# DOE Layer Declaration
DOE_LAYER = "orchestration"
DOE_RESPONSIBILITY = "Analyze memory optimization patterns and context efficiency"
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

class MemoryBankAnalyzer:
    """Analyzes memory optimization patterns using shared data orchestrator."""

    def __init__(self, orchestrator: DataOrchestrator):
        self.orchestrator = orchestrator

    def analyze_memory_patterns(self) -> Dict[str, Any]:
        """
        Analyze context optimization patterns using direct data access.
        Reveals memory bank optimization opportunities.
        """
        data = self.orchestrator.get_structured_data()

        result = {
            "analysis_timestamp": datetime.now().isoformat(),
            "script_role": "memory_analysis_using_shared_data",
            "memory_optimization_insights": {},
            "analysis_status": "processing"
        }

        try:
            # Analyze documentation structure for memory optimization
            result["memory_optimization_insights"]["documentation_structure"] = self._analyze_documentation_structure(data)

            # Analyze relationship patterns for context optimization
            result["memory_optimization_insights"]["relationship_patterns"] = self._analyze_relationship_patterns(data)

            # Analyze file metrics for optimization opportunities
            result["memory_optimization_insights"]["file_optimization"] = self._analyze_file_optimization(data)

            # Analyze coherence patterns for memory efficiency
            result["memory_optimization_insights"]["coherence_optimization"] = self._analyze_coherence_optimization(data)

            result["analysis_status"] = "complete"

        except Exception as e:
            result["analysis_status"] = "error"
            result["error"] = str(e)

        return result

    def _analyze_documentation_structure(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze documentation structure for memory optimization."""
        documents = data['documents']
        file_metrics = data['file_metrics']

        structure_analysis = {
            "total_documents": len(documents),
            "authority_distribution": {},
            "domain_distribution": {},
            "file_size_distribution": {},
            "memory_efficiency_indicators": {}
        }

        # Analyze authority distribution
        for doc_path, doc_data in documents.items():
            authority = doc_data.get('authority_level', 7)
            structure_analysis["authority_distribution"][authority] = structure_analysis["authority_distribution"].get(authority, 0) + 1

        # Analyze domain distribution
        for doc_path, doc_data in documents.items():
            domain = doc_path.split('/')[1] if len(doc_path.split('/')) > 1 else 'root'
            structure_analysis["domain_distribution"][domain] = structure_analysis["domain_distribution"].get(domain, 0) + 1

        # Analyze file sizes for memory optimization
        if file_metrics:
            sizes = [metrics.get('size_bytes', 0) for metrics in file_metrics.values() if isinstance(metrics, dict)]
            if sizes:
                structure_analysis["file_size_distribution"] = {
                    "average_size": sum(sizes) / len(sizes),
                    "largest_file": max(sizes),
                    "smallest_file": min(sizes),
                    "size_variance": max(sizes) - min(sizes)
                }

        # Memory efficiency indicators
        coherence = data['coherence_metrics']
        structure_analysis["memory_efficiency_indicators"] = {
            "relationship_coverage_ratio": coherence['connection_coverage'],
            "documents_per_relationship": len(documents) / max(coherence['total_relationships'], 1),
            "authority_hierarchy_depth": len(structure_analysis["authority_distribution"]),
            "domain_fragmentation": len(structure_analysis["domain_distribution"])
        }

        return structure_analysis

    def _analyze_relationship_patterns(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze relationship patterns for context optimization."""
        relationships = data['relationships']
        coherence = data['coherence_metrics']

        pattern_analysis = {
            "relationship_types_used": {},
            "connectivity_patterns": {},
            "context_loading_efficiency": {},
            "optimization_opportunities": []
        }

        # Count relationship types
        for rel_type, rel_data in relationships.items():
            pattern_analysis["relationship_types_used"][rel_type] = sum(len(targets) for targets in rel_data.values())

        # Analyze connectivity patterns
        pattern_analysis["connectivity_patterns"] = {
            "total_relationships": coherence['total_relationships'],
            "isolated_documents": coherence['isolated_documents'],
            "connection_density": coherence['connection_coverage'],
            "relationship_type_diversity": len([rt for rt, count in pattern_analysis["relationship_types_used"].items() if count > 0])
        }

        # Context loading efficiency
        pattern_analysis["context_loading_efficiency"] = {
            "average_relationships_per_document": coherence['total_relationships'] / max(len(data['documents']), 1),
            "strongly_connected_ratio": (len(data['documents']) - coherence['isolated_documents']) / max(len(data['documents']), 1),
            "relationship_type_specialization": len(pattern_analysis["relationship_types_used"]) / max(coherence['total_relationships'], 1)
        }

        # Identify optimization opportunities
        if coherence['isolated_documents'] > 0:
            pattern_analysis["optimization_opportunities"].append("reduce_isolated_documents")

        if coherence['connection_coverage'] < 0.7:
            pattern_analysis["optimization_opportunities"].append("improve_relationship_coverage")

        if len(pattern_analysis["relationship_types_used"]) < 3:
            pattern_analysis["optimization_opportunities"].append("increase_relationship_type_diversity")

        return pattern_analysis

    def _analyze_file_optimization(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze file metrics for memory optimization."""
        file_metrics = data['file_metrics']

        optimization_analysis = {
            "file_size_analysis": {},
            "memory_usage_patterns": {},
            "optimization_recommendations": []
        }

        if file_metrics:
            # Analyze file sizes
            sizes = [metrics.get('size_bytes', 0) for metrics in file_metrics.values() if isinstance(metrics, dict) and 'size_bytes' in metrics]
            if sizes:
                optimization_analysis["file_size_analysis"] = {
                    "total_size": sum(sizes),
                    "average_size": sum(sizes) / len(sizes),
                    "size_distribution": self._categorize_sizes(sizes),
                    "largest_files": sorted([(path, metrics.get('size_bytes', 0)) for path, metrics in file_metrics.items()
                                           if isinstance(metrics, dict)], key=lambda x: x[1], reverse=True)[:3]
                }

            # Memory usage patterns
            optimization_analysis["memory_usage_patterns"] = {
                "files_with_frontmatter": len([m for m in file_metrics.values() if isinstance(m, dict) and m.get('has_frontmatter')]),
                "complexity_distribution": self._analyze_complexity(file_metrics),
                "authority_correlation": self._analyze_authority_file_correlation(data)
            }

        # Generate optimization recommendations
        if optimization_analysis.get("file_size_analysis", {}).get("size_distribution", {}).get("large", 0) > 2:
            optimization_analysis["optimization_recommendations"].append("consider_file_splitting")

        if optimization_analysis["memory_usage_patterns"].get("authority_correlation", {}).get("correlation_strength", 0) > 0.7:
            optimization_analysis["optimization_recommendations"].append("optimize_authority_based_loading")

        return optimization_analysis

    def _categorize_sizes(self, sizes: List[int]) -> Dict[str, int]:
        """Categorize file sizes."""
        categories = {"small": 0, "medium": 0, "large": 0, "very_large": 0}

        for size in sizes:
            if size < 1000:
                categories["small"] += 1
            elif size < 5000:
                categories["medium"] += 1
            elif size < 10000:
                categories["large"] += 1
            else:
                categories["very_large"] += 1

        return categories

    def _analyze_complexity(self, file_metrics: Dict[str, Any]) -> Dict[str, int]:
        """Analyze content complexity distribution."""
        complexity_counts = {"low": 0, "medium": 0, "high": 0}

        for metrics in file_metrics.values():
            if isinstance(metrics, dict):
                complexity = metrics.get('content_complexity', 'unknown')
                if complexity in complexity_counts:
                    complexity_counts[complexity] += 1

        return complexity_counts

    def _analyze_authority_file_correlation(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze correlation between authority levels and file characteristics."""
        documents = data['documents']
        file_metrics = data['file_metrics']

        correlation_data = []

        for doc_path, doc_data in documents.items():
            authority = doc_data.get('authority_level', 7)
            metrics = file_metrics.get(doc_path, {})

            if isinstance(metrics, dict) and 'size_bytes' in metrics:
                correlation_data.append({
                    "authority": authority,
                    "size": metrics['size_bytes'],
                    "complexity": metrics.get('content_complexity', 'unknown')
                })

        # Calculate correlation strength (simplified)
        if len(correlation_data) > 1:
            authority_sizes = [(item['authority'], item['size']) for item in correlation_data]
            # Simple correlation calculation
            correlation = self._calculate_correlation([a for a, s in authority_sizes], [s for a, s in authority_sizes])
        else:
            correlation = 0.0

        return {
            "correlation_strength": abs(correlation),
            "correlation_direction": "positive" if correlation > 0 else "negative",
            "sample_size": len(correlation_data)
        }

    def _calculate_correlation(self, x: List[float], y: List[float]) -> float:
        """Calculate Pearson correlation coefficient."""
        if len(x) != len(y) or len(x) < 2:
            return 0.0

        n = len(x)
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum(xi * yi for xi, yi in zip(x, y))
        sum_x2 = sum(xi ** 2 for xi in x)
        sum_y2 = sum(yi ** 2 for yi in y)

        numerator = n * sum_xy - sum_x * sum_y
        denominator = ((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2)) ** 0.5

        return numerator / denominator if denominator != 0 else 0.0

    def _analyze_coherence_optimization(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze coherence patterns for memory optimization."""
        coherence = data['coherence_metrics']
        authority_flow = data['authority_flow']

        optimization_analysis = {
            "coherence_efficiency": {},
            "authority_flow_optimization": {},
            "memory_access_patterns": {}
        }

        # Coherence efficiency
        optimization_analysis["coherence_efficiency"] = {
            "connection_efficiency": coherence['connection_coverage'],
            "relationship_utilization": coherence['total_relationships'] / max(len(data['documents']), 1),
            "authority_distribution_efficiency": len(coherence['authority_distribution']) / 7.0  # 7 authority levels
        }

        # Authority flow optimization
        optimization_analysis["authority_flow_optimization"] = {
            "flow_efficiency": len(authority_flow['valid_flows']) / max(len(authority_flow['valid_flows']) + len(authority_flow['invalid_flows']), 1),
            "violation_impact": len(authority_flow['invalid_flows']),
            "hierarchy_depth_utilization": len(coherence['authority_distribution']) / max(len(data['authority_hierarchy']['levels']), 1)
        }

        # Memory access patterns
        optimization_analysis["memory_access_patterns"] = {
            "isolated_content_ratio": coherence['isolated_documents'] / max(len(data['documents']), 1),
            "highly_connected_ratio": len([d for d in data['documents'].values() if len(self.orchestrator.get_document_context(list(data['documents'].keys())[list(data['documents'].values()).index(d)])['relationships']) > 2]) / max(len(data['documents']), 1),
            "context_loading_complexity": self._calculate_context_loading_complexity(data)
        }

        return optimization_analysis

    def _calculate_context_loading_complexity(self, data: Dict[str, Any]) -> float:
        """Calculate complexity of context loading based on relationship patterns."""
        relationships = data['relationships']

        # Complexity based on relationship type diversity and connectivity
        type_diversity = len([rt for rt, rels in relationships.items() if rels])
        total_relationships = sum(len(targets) for rel_data in relationships.values() for targets in rel_data.values())

        # Normalize complexity score (0-1)
        complexity = min(1.0, (type_diversity * 0.3) + (total_relationships * 0.01))
        return complexity

def main():
    """CLI interface for memory analysis - maintains backwards compatibility."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Memory Bank Analyzer - analyzes context optimization patterns"
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
    analyzer = MemoryBankAnalyzer(orchestrator)
    result = analyzer.analyze_memory_patterns()

    if args.output == "json":
        print(json.dumps(result, indent=2))
    else:
        print("Memory Bank Context Optimization Analysis")
        print("=" * 50)
        print(f"Timestamp: {result['analysis_timestamp']}")
        print(f"Status: {result['analysis_status']}")
        insights = result['memory_optimization_insights']
        print(f"Documentation Domains: {len(insights['documentation_structure']['domain_distribution'])}")
        print(f"Authority Levels: {len(insights['documentation_structure']['authority_distribution'])}")
        print(f"Relationship Types: {len(insights['relationship_patterns']['relationship_types_used'])}")
        print("\nContext optimization patterns analyzed for AI insights.")

if __name__ == "__main__":
    main()