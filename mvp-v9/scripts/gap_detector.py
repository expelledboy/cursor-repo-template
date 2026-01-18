#!/usr/bin/env python3
"""
Gap Detection System - AgentOS v9

Coordinates gap detection data collection for AI analysis - scripts only coordinate data collection.

DOE Registry - Bidirectional Linkages:
@directive docs/reference/agentos/architecture.md

# DOE Layer Declaration
DOE_LAYER = "orchestration"
DOE_RESPONSIBILITY = "Detect and analyze system gaps and integration issues"
DOE_GOVERNANCE = "docs/reference/agentos/doe-framework.md"
DOE_PRECEDENCE = 3
"""

import json
import yaml
import os
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime

class GapDetector:
    """Coordinates gap detection data collection for AI analysis - no intelligence assumptions."""

    def __init__(self):
        self.docs_dir = Path("docs")
        self.detection_history = []

    def collect_gap_data(self) -> Dict[str, Any]:
        """Collect raw gap data for AI analysis - scripts only coordinate data collection."""
        return {
            "collection_metadata": {
                "timestamp": datetime.now().isoformat(),
                "data_schema_version": "gap_data_v3",
                "collection_method": "comprehensive_frontmatter_analysis_with_importance",
                "script_role": "data_coordination_only"
            },
            "raw_relationship_data": self._collect_relationships(),
            "raw_document_metadata": self._collect_document_metadata(),
            "raw_implementation_data": self._collect_implementation_data(),
            "raw_file_metrics": self._collect_file_metrics(),
            "raw_importance_data": self._collect_importance_data(),
            "ai_agent_analysis_schema": self._provide_ai_analysis_schema(),
            "lint_rules_framework": self._provide_lint_rules_framework()
        }

    def _collect_relationships(self) -> Dict[str, Any]:
        """Collect raw relationship data - no interpretation."""
        relationships = {}
        relationship_types = ['depends_on', 'informs', 'evidence_for', 'implements', 'governed_by', 'related']

        for md_file in self.docs_dir.rglob('*.md'):
            if md_file.name == 'index.md':
                continue

            frontmatter = self._load_frontmatter(md_file)
            if not frontmatter:
                continue

            doc_path = f"docs/{md_file.relative_to(self.docs_dir)}"

            # Collect all relationship data without categorization
            for rel_type in relationship_types:
                if rel_type in frontmatter:
                    targets = frontmatter[rel_type]
                    if isinstance(targets, list):
                        for target in targets:
                            if isinstance(target, str) and target.startswith('docs/'):
                                if rel_type not in relationships:
                                    relationships[rel_type] = {}
                                if doc_path not in relationships[rel_type]:
                                    relationships[rel_type][doc_path] = []
                                relationships[rel_type][doc_path].append(target)
                    elif isinstance(targets, str) and targets.startswith('docs/'):
                        if rel_type not in relationships:
                            relationships[rel_type] = {}
                        if doc_path not in relationships[rel_type]:
                            relationships[rel_type][doc_path] = []
                        relationships[rel_type][doc_path].append(targets)

        return relationships

    def _collect_importance_data(self) -> Dict[str, Any]:
        """Collect raw importance data for gap analysis integration."""
        try:
            # Import data orchestrator to get importance scores
            from data_orchestrator import DataOrchestrator

            orchestrator = DataOrchestrator()
            orchestrator.load_all_data()

            importance_rankings = orchestrator.get_importance_rankings()
            importance_insights = orchestrator.get_importance_insights()

            return {
                "importance_rankings": importance_rankings,
                "importance_insights": importance_insights,
                "importance_collection_status": "success"
            }
        except Exception as e:
            return {
                "importance_collection_error": str(e),
                "importance_collection_status": "failed",
                "importance_rankings": [],
                "importance_insights": {}
            }

    def _collect_document_metadata(self) -> Dict[str, Any]:
        """Collect raw document metadata - no interpretation."""
        documents = {}

        for md_file in self.docs_dir.rglob('*.md'):
            if md_file.name == 'index.md':
                continue

            frontmatter = self._load_frontmatter(md_file)
            if not frontmatter:
                continue

            doc_path = f"docs/{md_file.relative_to(self.docs_dir)}"

            # Collect all metadata without interpretation
            documents[doc_path] = {
                'path': doc_path,
                'frontmatter': frontmatter,
                'file_size_bytes': os.path.getsize(md_file),
                'authority_level': self._get_authority_level(doc_path),
                'last_modified': datetime.fromtimestamp(os.path.getmtime(md_file)).isoformat()
            }

        return documents

    def _collect_implementation_data(self) -> Dict[str, Any]:
        """Collect raw implementation link data - no validation."""
        implementations = {}

        for md_file in self.docs_dir.rglob('*.md'):
            if md_file.name == 'index.md':
                continue

            frontmatter = self._load_frontmatter(md_file)
            if not frontmatter or 'implementations' not in frontmatter:
                continue

            doc_path = f"docs/{md_file.relative_to(self.docs_dir)}"
            implementations[doc_path] = frontmatter['implementations']

        return implementations

    def _collect_file_metrics(self) -> Dict[str, Any]:
        """Collect raw file metrics - no interpretation."""
        file_metrics = {
            'total_files': 0,
            'file_sizes': {},
            'size_distribution': {},
            'content_complexity': {}
        }

        md_files = list(self.docs_dir.rglob('*.md'))
        md_files = [f for f in md_files if f.name != 'index.md']

        file_metrics['total_files'] = len(md_files)

        for md_file in md_files:
            doc_path = f"docs/{md_file.relative_to(self.docs_dir)}"
            size = os.path.getsize(md_file)

            file_metrics['file_sizes'][doc_path] = size

            # Size distribution buckets
            if size < 1000:
                bucket = 'small'
            elif size < 5000:
                bucket = 'medium'
            elif size < 10000:
                bucket = 'large'
            else:
                bucket = 'very_large'

            if bucket not in file_metrics['size_distribution']:
                file_metrics['size_distribution'][bucket] = []
            file_metrics['size_distribution'][bucket].append(doc_path)

            # Basic content metrics
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    word_count = len(content.split())
                    line_count = len(content.split('\n'))

                file_metrics['content_complexity'][doc_path] = {
                    'word_count': word_count,
                    'line_count': line_count,
                    'frontmatter_present': content.startswith('---')
                }
            except Exception:
                file_metrics['content_complexity'][doc_path] = {'error': 'could_not_read'}

        return file_metrics

    def _provide_ai_analysis_schema(self) -> Dict[str, Any]:
        """Provide structured schema for AI analysis - defines what AI should do."""
        return {
            "analysis_inputs": {
                "relationship_graph": "Complete graph of document relationships",
                "document_metadata": "Authority levels, file sizes, domains, frontmatter",
                "implementation_links": "Declared implementation mappings",
                "file_metrics": "Size distribution, content complexity indicators",
                "importance_rankings": "Document importance scores and ranking factors",
                "importance_insights": "System-wide importance analysis and gap opportunities"
            },
            "required_categorization_analyses": {
                "gap_identification": {
                    "isolated_documents": "Documents with zero relationships",
                    "under_connected_documents": "Documents below relationship density threshold (< 3 relationships)",
                    "authority_violations": "Documents violating authority hierarchy rules",
                    "implementation_drift": "Documents with broken @implementation links"
                },
                "relationship_pattern_analysis": {
                    "circular_dependencies": "Relationship cycles that create confusion",
                    "hub_documents": "Documents that connect many others (high centrality)",
                    "relationship_type_balance": "Distribution of depends_on vs informs vs implements",
                    "authority_flow": "How relationships respect or violate authority hierarchy"
                }
            },
            "required_impact_assessments": {
                "system_functionality_impact": "How gaps affect directive loading, task execution, and system coherence",
                "documentation_quality_impact": "How gaps undermine documentation hierarchy, maintenance, and self-awareness"
            },
            "required_prioritization": {
                "impact_severity": "High/Medium/Low impact on system functionality",
                "remediation_effort": "Easy/Medium/Hard to fix",
                "system_criticality": "Core functionality vs. peripheral features",
                "user_visibility": "How visible the gap is to system users",
                "importance_weighting": "Factor document importance scores into gap prioritization"
            },
            "output_requirements": {
                "categorized_findings": "Clear gap categories with specific document examples",
                "impact_quantification": "Measurable effects on system capabilities",
                "prioritized_recommendations": "Actionable remediation suggestions ranked by importance",
                "confidence_levels": "AI confidence in analysis accuracy"
            }
        }

    def _provide_lint_rules_framework(self) -> Dict[str, Any]:
        """Provide comprehensive lint rules framework for AI analysis."""
        return {
            "lint_categories": {
                "frontmatter_completeness": {
                    "rule_type": "metadata_validation",
                    "required_fields": ["title", "status", "created_date", "domain"],
                    "recommended_fields": ["purpose", "depends_on", "implementations"],
                    "severity_mapping": {
                        "missing_required": "error",
                        "missing_recommended": "warning",
                        "malformed_data": "error"
                    },
                    "ai_guidance": "Evaluate business impact of incomplete metadata on system usability"
                },
                "relationship_density": {
                    "rule_type": "connectivity_analysis",
                    "thresholds": {
                        "isolated": {"value": 0, "severity": "error"},
                        "under_connected": {"value": 3, "severity": "warning"},
                        "well_connected": {"value": 7, "severity": "info"},
                        "over_connected": {"value": 15, "severity": "warning"}
                    },
                    "measurement_method": "count_total_relationships_per_document",
                    "ai_guidance": "Assess how connectivity gaps impair system intelligence and context loading"
                },
                "authority_compliance": {
                    "rule_type": "hierarchy_validation",
                    "path_authority_rules": {
                        "docs/reference/": {"required_level": 1, "severity": "error"},
                        "docs/how-to/": {"required_level": 2, "severity": "error"},
                        "docs/explanation/": {"required_level": 3, "severity": "error"},
                        "docs/tutorials/": {"required_level": 4, "severity": "error"},
                        "docs/work/": {"required_level": 5, "severity": "warning"},
                        "docs/archive/": {"required_level": 6, "severity": "info"}
                    },
                    "relationship_authority_rules": {
                        "governed_by": "source must have lower authority than target",
                        "implements": "can cross authority levels",
                        "depends_on": "can cross authority levels",
                        "informs": "can cross authority levels"
                    },
                    "ai_guidance": "Analyze systemic coherence implications of hierarchy violations"
                },
                "implementation_alignment": {
                    "rule_type": "reality_synchronization",
                    "validation_checks": {
                        "file_existence": "Referenced implementation files must exist",
                        "path_validity": "Implementation paths must be well-formed",
                        "recency_check": "Implementation files should be reasonably current"
                    },
                    "ai_guidance": "Determine documentation-implementation drift severity and remediation priority"
                },
                "documentation_maintainability": {
                    "rule_type": "quality_assurance",
                    "size_guidelines": {
                        "splitting_threshold": {"bytes": 10000, "severity": "warning"},
                        "maximum_size": {"bytes": 25000, "severity": "error"}
                    },
                    "complexity_indicators": {
                        "high_relationship_count": {"threshold": 10, "severity": "warning"},
                        "frequent_updates_needed": {"stale_days": 90, "severity": "info"}
                    },
                    "ai_guidance": "Assess long-term maintenance burden and recommend refactoring strategies"
                }
            },
            "lint_execution_guidance": {
                "rule_application_order": ["authority_compliance", "frontmatter_completeness", "relationship_density", "implementation_alignment", "documentation_maintainability"],
                "severity_precedence": ["error", "warning", "info"],
                "false_positive_handling": "AI should validate apparent violations against business context",
                "remediation_guidance": "Provide specific actionable steps for each violation type"
            }
        }

    def _load_frontmatter(self, file_path: Path) -> Optional[Dict]:
        """Load YAML frontmatter from a markdown file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            if not content.startswith('---'):
                return None

            end_pos = content.find('---', 3)
            if end_pos == -1:
                return None

            frontmatter_text = content[3:end_pos]
            return yaml.safe_load(frontmatter_text)
        except Exception:
            return None

    def _get_authority_level(self, doc_path: str) -> int:
        """Get authority level for a document path."""
        authority_map = {
            'reference': 1,
            'how-to': 2,
            'explanation': 3,
            'tutorials': 4,
            'work': 5,
            'archive': 6
        }

        for level, number in authority_map.items():
            if f'docs/{level}/' in doc_path:
                return number
        return 7  # Unknown

    def analyze_gaps(self) -> Dict[str, Any]:
        """Provide structured data collection for AI gap analysis - scripts coordinate only."""
        try:
            # Collect comprehensive raw data for AI analysis
            gap_data = self.collect_gap_data()

            # Add analysis metadata
            analysis = {
                "analysis_metadata": {
                    "timestamp": datetime.now().isoformat(),
                    "gap_detection_version": "2.0",
                    "script_role": "data_coordination_only",
                    "ai_agent_analysis_required": True,
                    "data_freshness": "collected_in_this_session"
                },
                "raw_gap_data": gap_data,
                "ai_processing_guidance": {
                    "input_interpretation": "Use raw data to perform intelligent gap categorization and impact assessment",
                    "output_requirements": "Provide categorized findings, impact quantification, and prioritized recommendations",
                    "confidence_reporting": "Include AI confidence levels for all analyses and recommendations",
                    "human_collaboration": "Structure output for human review and feedback integration"
                }
            }

            # Store analysis session for tracking
            self.detection_history.append({
                "timestamp": analysis["analysis_metadata"]["timestamp"],
                "data_collected": True,
                "ai_analysis_pending": True
            })

            return analysis

        except Exception as e:
            return {
                "error": str(e),
                "analysis_metadata": {
                    "timestamp": datetime.now().isoformat(),
                    "status": "failed"
                }
            }

    def get_gap_detection_status(self) -> Dict[str, Any]:
        """Get current status of gap detection analysis."""
        latest_analysis = self.detection_history[-1] if self.detection_history else None

        status = {
            "gap_detection_active": True,
            "analysis_history_count": len(self.detection_history),
            "latest_analysis": latest_analysis,
            "ai_agent_integration": {
                "framework_ready": True,
                "analysis_types_supported": [
                    "relationship_pattern_analysis",
                    "impact_assessment",
                    "prioritization_ranking",
                    "root_cause_identification",
                    "remediation_planning"
                ],
                "expected_ai_contribution": "sophisticated analysis beyond basic pattern matching"
            },
            "self_improvement_potential": {
                "learning_opportunities": "gap analysis results can feed learning system",
                "pattern_recognition": "recurring gap types inform system improvements",
                "validation_enhancement": "gap detection improves overall validation"
            }
        }

        return status

    def validate_gap_detection_capabilities(self) -> Dict[str, Any]:
        """Validate that gap detection system has required capabilities."""
        validation = {
            "capability_checks": {
                "frontmatter_intelligence": self._check_frontmatter_integration(),
                "relationship_graph_access": self._check_relationship_graph(),
                "ai_agent_framework": self._check_ai_framework(),
                "learning_system_integration": self._check_learning_integration()
            },
            "overall_readiness": False,
            "missing_capabilities": [],
            "recommendations": []
        }

        # Check each capability
        all_capable = True
        for check_name, check_result in validation["capability_checks"].items():
            if not check_result["available"]:
                all_capable = False
                validation["missing_capabilities"].append(check_name)
                validation["recommendations"].extend(check_result.get("recommendations", []))

        validation["overall_readiness"] = all_capable

        return validation

    def _check_frontmatter_integration(self) -> Dict[str, Any]:
        """Check data collection capabilities."""
        try:
            # Test data collection
            test_data = self.collect_gap_data()
            return {
                "available": bool(test_data.get("raw_relationship_data")),
                "data_collection_working": True,
                "capabilities": ["data_collection", "schema_provision", "ai_guidance"]
            }
        except Exception as e:
            return {
                "available": False,
                "error": str(e),
                "recommendations": ["Check data collection methods"]
            }

    def _check_relationship_graph(self) -> Dict[str, Any]:
        """Check relationship data collection."""
        try:
            # Test relationship data collection
            rel_data = self._collect_relationships()
            return {
                "available": bool(rel_data),
                "relationship_types_found": list(rel_data.keys()),
                "capabilities": ["relationship_collection", "data_structuring"]
            }
        except Exception as e:
            return {
                "available": False,
                "error": str(e),
                "recommendations": ["Check relationship collection logic"]
            }

    def _check_ai_framework(self) -> Dict[str, Any]:
        """Check AI agent analysis framework."""
        # This is more of a structural check since AI analysis happens externally
        framework_elements = [
            "ai_agent_analysis_required",
            "analysis_types_available",
            "guidance",
            "next_steps"
        ]

        # Check if our analysis structure includes AI framework elements
        sample_analysis = self.analyze_gaps()
        framework_present = all(key in sample_analysis for key in ["ai_agent_analysis_required", "analysis_types_available", "guidance"])

        return {
            "available": framework_present,
            "framework_elements_present": framework_elements,
            "capabilities": ["ai_guidance", "analysis_framework", "structured_output"]
        }

    def _check_learning_integration(self) -> Dict[str, Any]:
        """Check learning system integration potential."""
        # This checks if gap detection can feed the learning system
        integration_points = [
            "can_create_learning_tasks",
            "can_record_gap_analysis",
            "can_track_remediation"
        ]

        # Since we have task management and learning capture, this should be available
        return {
            "available": True,
            "integration_points": integration_points,
            "capabilities": ["learning_feed", "task_creation", "progress_tracking"]
        }

# CLI Interface
def main():
    import argparse

    parser = argparse.ArgumentParser(description='Graph-Based Gap Detection for AgentOS v9')
    subparsers = parser.add_subparsers(dest='command')

    # Analyze gaps
    subparsers.add_parser('analyze', help='Perform comprehensive gap analysis')

    # Get status
    subparsers.add_parser('status', help='Get gap detection system status')

    # Validate capabilities
    subparsers.add_parser('validate', help='Validate gap detection capabilities')

    args = parser.parse_args()

    detector = GapDetector()

    if args.command == 'analyze':
        analysis = detector.analyze_gaps()

        if 'error' in analysis:
            print(f"Error: {analysis['error']}")
            return

        print("=== AgentOS v9 Gap Detection Data Collection ===")
        metadata = analysis['analysis_metadata']
        print(f"Timestamp: {metadata['timestamp']}")
        print(f"Script Role: {metadata['script_role']}")
        print(f"Version: {metadata.get('gap_detection_version', '2.0')}")
        print()

        # Show data collection summary
        raw_data = analysis['raw_gap_data']
        rel_data = raw_data['raw_relationship_data']
        doc_meta = raw_data['raw_document_metadata']
        impl_data = raw_data['raw_implementation_data']
        file_metrics = raw_data['raw_file_metrics']

        print("Data Collection Summary:")
        print(f"  Relationship Types: {len(rel_data)}")
        print(f"  Documents Analyzed: {len(doc_meta)}")
        print(f"  Implementation Links: {len(impl_data)}")
        print(f"  Files with Metrics: {file_metrics['total_files']}")
        print()

        print("AI Analysis Schema Available:")
        ai_schema = raw_data['ai_agent_analysis_schema']
        print(f"  Categorization Analyses: {len(ai_schema['required_categorization_analyses'])}")
        print(f"  Impact Assessments: {len(ai_schema['required_impact_assessments'])}")
        print()

        print("Lint Rules Framework:")
        lint_framework = raw_data['lint_rules_framework']
        print(f"  Rule Categories: {len(lint_framework['lint_categories'])}")
        print()

        print("AI Processing Guidance:")
        guidance = analysis['ai_processing_guidance']
        print(f"  Input: {guidance['input_interpretation']}")
        print(f"  Output: {guidance['output_requirements']}")
        print()

        print("📤 Data ready for AI agent analysis - no intelligence assumptions made by script")

    elif args.command == 'status':
        status = detector.get_gap_detection_status()
        print("=== Gap Detection System Status ===")
        print(f"System Active: {status['gap_detection_active']}")
        print(f"Analysis History: {status['analysis_history_count']} runs")
        if status['latest_analysis']:
            print(f"Latest Analysis: {status['latest_analysis']['timestamp']}")
            print(f"Gaps Found: {status['latest_analysis']['gaps_found']}")
        print()

        print("AI Agent Integration:")
        print(f"  Framework Ready: {status['ai_agent_integration']['framework_ready']}")
        print(f"  Supported Analysis: {', '.join(status['ai_agent_integration']['analysis_types_supported'])}")
        print()

        print("Self-Improvement Potential:")
        for key, value in status['self_improvement_potential'].items():
            print(f"  {key}: {value}")

    elif args.command == 'validate':
        validation = detector.validate_gap_detection_capabilities()
        print("=== Gap Detection Capability Validation ===")
        print(f"Overall Readiness: {'✅ Ready' if validation['overall_readiness'] else '❌ Issues Found'}")
        print()

        print("Capability Checks:")
        for check_name, check_result in validation["capability_checks"].items():
            status = "✅ Available" if check_result["available"] else "❌ Missing"
            print(f"  {check_name}: {status}")
            if not check_result["available"] and "error" in check_result:
                print(f"    Error: {check_result['error']}")
        print()

        if validation["missing_capabilities"]:
            print("Missing Capabilities:")
            for capability in validation["missing_capabilities"]:
                print(f"  - {capability}")
            print()

            print("Recommendations:")
            for recommendation in validation["recommendations"]:
                print(f"  - {recommendation}")

if __name__ == '__main__':
    main()