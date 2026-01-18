#!/usr/bin/env python3
"""
Data Orchestrator - AgentOS v9 Central Data Coordination
Unified data loading and coordination for all AgentOS components.
Eliminates duplicate loading, subprocess overhead, and data marshalling issues.

DOE Registry - Bidirectional Linkages:
@directive docs/reference/agentos/behavior-spec.md

# DOE Layer Declaration
DOE_LAYER = "orchestration"
DOE_RESPONSIBILITY = "Central data coordination and DOE registry validation"
DOE_GOVERNANCE = "docs/reference/agentos/doe-framework.md"
DOE_PRECEDENCE = 3
"""

import sys
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime

# Import shared data models
try:
    from agentos_data_models import DocumentMetadata, RelationshipGraph, AuthorityHierarchy, FileMetrics
except ImportError:
    try:
        # Try relative import
        from .agentos_data_models import DocumentMetadata, RelationshipGraph, AuthorityHierarchy, FileMetrics
    except ImportError:
        print("Error: Could not import shared data models")
        sys.exit(1)

class DataOrchestrator:
    """
    Central coordinator for all AgentOS data loading and sharing.
    Loads data once, provides structured access to all components.
    """

    def __init__(self):
        self._data_loaded = False
        self._load_timestamp = None

        # Core data structures - loaded once, shared everywhere
        self.relationship_graph = RelationshipGraph()
        self.authority_hierarchy = AuthorityHierarchy()
        self.file_metrics_analyzer = FileMetrics()

        # Raw data collections
        self.documents: Dict[str, DocumentMetadata] = {}
        self.relationships: Dict[str, Dict[str, List[str]]] = {}
        self.file_metrics: Dict[str, Dict[str, Any]] = {}

        # Derived analysis data
        self.coherence_metrics: Optional[Dict[str, Any]] = None
        self.authority_flow: Optional[Dict[str, Any]] = None
        self.importance_scores: Optional[Dict[str, Dict[str, Any]]] = None

        # Configuration - directories to analyze
        self.project_root = Path(__file__).parent.parent
        self.docs_dir = self.project_root / "docs"
        self.src_dir = self.project_root / "src"
        self.scripts_dir = self.project_root / "scripts"

    def load_all_data(self, force_reload: bool = False) -> bool:
        """
        Load ALL AgentOS data once - documents, relationships, metrics.
        Returns True if data was loaded/refreshed, False if already loaded.
        """
        if self._data_loaded and not force_reload:
            return False

        try:
            # Load documents and relationships
            self._load_all_documents()
            self._load_all_relationships()

            # Calculate derived metrics
            self._calculate_coherence_metrics()
            self._calculate_authority_flow()
            self._calculate_file_metrics()
            self._calculate_importance_scores()

            self._data_loaded = True
            self._load_timestamp = datetime.now().isoformat()

            return True

        except Exception as e:
            print(f"❌ Data loading failed: {e}")
            self._data_loaded = False
            return False

    def get_structured_data(self) -> Dict[str, Any]:
        """
        Get all data in structured Python objects - no serialization needed.
        This is the primary interface for all analysis components.
        """
        if not self._data_loaded:
            raise RuntimeError("Data not loaded. Call load_all_data() first.")

        return {
            'metadata': {
                'load_timestamp': self._load_timestamp,
                'documents_count': len(self.documents),
                'relationships_count': sum(len(targets) for rel_data in self.relationships.values() for targets in rel_data.values()),
                'data_integrity': self._verify_data_integrity()
            },
            'documents': {path: doc.to_dict() for path, doc in self.documents.items()},
            'relationships': self.relationships,
            'relationship_graph': self.relationship_graph,
            'coherence_metrics': self.coherence_metrics,
            'authority_flow': self.authority_flow,
            'file_metrics': self.file_metrics,
            'importance_scores': self.importance_scores,
            'authority_hierarchy': {
                'levels': self.authority_hierarchy.levels,
                'validation_rules': {level: self.authority_hierarchy.validate_hierarchy(f'docs/{level}/test.md')
                                    for level in self.authority_hierarchy.levels.keys()}
            }
        }

    def get_importance_rankings(self, limit: Optional[int] = None, min_score: float = 0.0) -> List[Dict[str, Any]]:
        """
        Get importance rankings for self-reflection and gap analysis.
        Returns documents sorted by importance score (highest first).

        Args:
            limit: Maximum number of results to return (None = all)
            min_score: Minimum importance score to include (0-100)

        Returns:
            List of dicts with importance data, sorted by score descending
        """
        if not self._data_loaded or self.importance_scores is None:
            raise RuntimeError("Data not loaded or importance scores not calculated. Call load_all_data() first.")

        # Filter and sort by importance score
        rankings = []
        for doc_path, score_data in self.importance_scores.items():
            if score_data['importance_score'] >= min_score:
                ranking_entry = {
                    'doc_path': doc_path,
                    'title': self.documents[doc_path].title if doc_path in self.documents else 'Unknown',
                    'importance_score': score_data['importance_score'],
                    'authority_weight': score_data['authority_weight'],
                    'criticality_factor': score_data['criticality_factor'],
                    'connectivity_factor': score_data['connectivity_factor'],
                    'total_relationships': score_data['total_relationships'],
                    'ranking_factors': score_data['ranking_factors'],
                    'factors': score_data['factors']
                }
                rankings.append(ranking_entry)

        # Sort by importance score descending
        rankings.sort(key=lambda x: x['importance_score'], reverse=True)

        # Apply limit if specified
        if limit:
            rankings = rankings[:limit]

        return rankings

    def get_importance_insights(self, doc_path: Optional[str] = None) -> Dict[str, Any]:
        """
        Get importance insights for self-reflection.
        If doc_path is provided, returns insights for that document.
        Otherwise returns system-wide importance insights.

        Args:
            doc_path: Specific document path, or None for system insights

        Returns:
            Dict with importance insights and analysis
        """
        if not self._data_loaded or not self.importance_scores:
            raise RuntimeError("Data not loaded or importance scores not calculated. Call load_all_data() first.")

        if doc_path:
            # Specific document insights
            if doc_path not in self.importance_scores:
                return {'error': f'Document {doc_path} not found in importance analysis'}

            score_data = self.importance_scores[doc_path]
            doc_meta = self.documents.get(doc_path)

            return {
                'document': doc_path,
                'title': doc_meta.title if doc_meta else 'Unknown',
                'importance_score': score_data['importance_score'],
                'importance_percentile': self._calculate_percentile(doc_path),
                'ranking_factors': score_data['ranking_factors'],
                'improvement_suggestions': self._get_importance_improvements(doc_path),
                'system_context': {
                    'rank': self._get_document_rank(doc_path),
                    'total_documents': len(self.importance_scores),
                    'above_average': score_data['importance_score'] > self._get_average_importance()
                }
            }
        else:
            # System-wide insights
            rankings = self.get_importance_rankings()
            scores = [r['importance_score'] for r in rankings]

            return {
                'system_overview': {
                    'total_documents': len(rankings),
                    'average_importance': round(sum(scores) / len(scores), 2) if scores else 0,
                    'highest_score': max(scores) if scores else 0,
                    'lowest_score': min(scores) if scores else 0,
                    'importance_distribution': self._get_importance_distribution(scores)
                },
                'top_important_documents': rankings[:10],
                'gap_analysis_opportunities': self._identify_importance_gaps(rankings),
                'self_reflection_insights': self._generate_self_reflection_insights(rankings)
            }

    def _calculate_percentile(self, doc_path: str) -> float:
        """Calculate importance percentile for a document."""
        if self.importance_scores is None or doc_path not in self.importance_scores:
            return 0.0

        doc_score = self.importance_scores[doc_path]['importance_score']
        all_scores = [score_data['importance_score'] for score_data in self.importance_scores.values()]
        higher_scores = sum(1 for score in all_scores if score > doc_score)

        return round((higher_scores / len(all_scores)) * 100, 1)

    def _get_document_rank(self, doc_path: str) -> int:
        """Get the rank of a document by importance."""
        rankings = self.get_importance_rankings()
        for i, ranking in enumerate(rankings, 1):
            if ranking['doc_path'] == doc_path:
                return i
        return len(rankings) + 1

    def _get_average_importance(self) -> float:
        """Get average importance score across all documents."""
        if self.importance_scores is None:
            return 0.0
        scores = [score_data['importance_score'] for score_data in self.importance_scores.values()]
        return sum(scores) / len(scores) if scores else 0.0

    def _get_importance_distribution(self, scores: List[float]) -> Dict[str, int]:
        """Categorize importance score distribution."""
        distribution = {'very_high': 0, 'high': 0, 'medium': 0, 'low': 0, 'very_low': 0}

        for score in scores:
            if score >= 80:
                distribution['very_high'] += 1
            elif score >= 60:
                distribution['high'] += 1
            elif score >= 40:
                distribution['medium'] += 1
            elif score >= 20:
                distribution['low'] += 1
            else:
                distribution['very_low'] += 1

        return distribution

    def _identify_importance_gaps(self, rankings: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Identify documents that could benefit from importance improvements."""
        gaps = []

        for ranking in rankings:
            doc_path = ranking['doc_path']
            score = ranking['importance_score']
            relationships = ranking['total_relationships']

            # Flag low-importance, highly-connected documents
            if score < 30 and relationships > 5:
                gaps.append({
                    'doc_path': doc_path,
                    'issue': 'low_importance_high_connectivity',
                    'current_score': score,
                    'relationships': relationships,
                    'suggestion': 'Consider increasing criticality or authority level'
                })

            # Flag isolated high-authority documents
            elif score > 70 and relationships == 0:
                gaps.append({
                    'doc_path': doc_path,
                    'issue': 'isolated_high_importance',
                    'current_score': score,
                    'relationships': relationships,
                    'suggestion': 'Consider adding relationship links to increase system coherence'
                })

        return gaps[:10]  # Return top 10 gaps

    def _generate_self_reflection_insights(self, rankings: List[Dict[str, Any]]) -> List[str]:
        """Generate insights for system self-reflection."""
        insights = []

        # Check for authority concentration
        top_scores = [r['importance_score'] for r in rankings[:5]]
        if top_scores and top_scores[0] > top_scores[-1] * 1.5:
            insights.append("High authority concentration detected - consider distributing governance more evenly")

        # Check for connectivity vs authority balance
        authority_focused = sum(1 for r in rankings[:10] if r['authority_weight'] > 1.2)
        connectivity_focused = sum(1 for r in rankings[:10] if r['connectivity_factor'] > 1.1)

        if authority_focused > connectivity_focused + 3:
            insights.append("System appears authority-focused - consider increasing cross-document relationships")
        elif connectivity_focused > authority_focused + 3:
            insights.append("System appears connectivity-focused - ensure authority hierarchies are maintained")

        # Check for importance gaps
        score_range = max(r['importance_score'] for r in rankings) - min(r['importance_score'] for r in rankings)
        if score_range > 50:
            insights.append("Large importance score variance detected - review importance factor calibration")

        return insights

    def _get_importance_improvements(self, doc_path: str) -> List[str]:
        """Suggest improvements for a document's importance score."""
        if self.importance_scores is None or doc_path not in self.importance_scores:
            return []

        score_data = self.importance_scores[doc_path]
        suggestions = []

        # Check authority weight
        if score_data['authority_weight'] < 0.7:
            suggestions.append("Consider reviewing document authority level or DOE precedence")

        # Check criticality
        if score_data['criticality_factor'] <= 1.0:
            suggestions.append("Consider adding importance_factors.criticality in frontmatter")

        # Check connectivity
        if score_data['total_relationships'] < 2:
            suggestions.append("Consider adding more relationship links (governs, depends_on, etc.)")

        return suggestions

    def _load_all_documents(self) -> None:
        """Load all documents and implementation files into the system."""
        self.documents = {}

        # Load documentation files
        for md_file in self.docs_dir.rglob('*.md'):
            if md_file.name == 'index.md':
                continue

            frontmatter = self._load_frontmatter(md_file)
            doc_path = f"docs/{md_file.relative_to(self.docs_dir)}"

            # Create document metadata using shared model
            doc_metadata = DocumentMetadata(doc_path, frontmatter)
            self.documents[doc_path] = doc_metadata

            # Also add to relationship graph for coherence calculations
            self.relationship_graph.add_document(doc_path, frontmatter)

        # Load implementation files (Python files)
        for py_file in self.src_dir.rglob('*.py'):
            impl_path = f"src/{py_file.relative_to(self.src_dir)}"
            impl_metadata = self._load_implementation_file(py_file, impl_path)
            if impl_metadata:
                self.documents[impl_path] = impl_metadata
                self.relationship_graph.add_document(impl_path, impl_metadata.frontmatter)

        for py_file in self.scripts_dir.rglob('*.py'):
            impl_path = f"scripts/{py_file.relative_to(self.scripts_dir)}"
            impl_metadata = self._load_implementation_file(py_file, impl_path)
            if impl_metadata:
                self.documents[impl_path] = impl_metadata
                self.relationship_graph.add_document(impl_path, impl_metadata.frontmatter)

    def _load_all_relationships(self) -> None:
        """Load all relationships between documents."""
        relationship_types = [
            'depends_on', 'informs', 'evidence_for', 'implements',
            'governed_by', 'related', 'references', 'supersedes'
        ]

        self.relationships = {rel_type: {} for rel_type in relationship_types}

        for doc_path, doc_metadata in self.documents.items():
            if not doc_metadata.frontmatter:
                continue

            # Extract relationships from frontmatter
            for rel_type in relationship_types:
                if rel_type in doc_metadata.frontmatter:
                    targets = doc_metadata.frontmatter[rel_type]
                    if isinstance(targets, list):
                        for target in targets:
                            if isinstance(target, str) and target.startswith('docs/'):
                                self._add_relationship(rel_type, doc_path, target)
                    elif isinstance(targets, str) and targets.startswith('docs/'):
                        self._add_relationship(rel_type, doc_path, targets)

    def _add_relationship(self, rel_type: str, source: str, target: str) -> None:
        """Add a relationship to both orchestrator and graph."""
        # Add to orchestrator's relationship collection
        if source not in self.relationships[rel_type]:
            self.relationships[rel_type][source] = []
        if target not in self.relationships[rel_type][source]:
            self.relationships[rel_type][source].append(target)

        # Add to relationship graph for analysis
        self.relationship_graph.add_relationship(source, rel_type, target)

    def _calculate_coherence_metrics(self) -> None:
        """Calculate system coherence metrics."""
        self.coherence_metrics = self.relationship_graph.calculate_coherence_metrics()

    def _calculate_authority_flow(self) -> None:
        """Calculate authority flow analysis."""
        self.authority_flow = self.relationship_graph.get_authority_flow()

    def _calculate_file_metrics(self) -> None:
        """Calculate file metrics for all documents."""
        self.file_metrics = {}

        for doc_path in self.documents.keys():
            file_path = Path(doc_path)
            if file_path.exists():
                self.file_metrics[doc_path] = self.file_metrics_analyzer.analyze_file(file_path)

    def _calculate_importance_scores(self) -> None:
        """Calculate importance scores for all documents and implementation files."""
        self.importance_scores = {}

        for doc_path, doc_metadata in self.documents.items():
            # Get relationship count for connectivity
            relationships = self.relationship_graph.get_relationships_for_doc(doc_path)
            total_relationships = sum(len(targets) for targets in relationships.values())

            # Determine if this is a document or implementation file
            is_implementation = doc_path.startswith(('src/', 'scripts/'))

            # Get authority weight
            authority_weight = 1.0
            if doc_metadata.frontmatter:
                if is_implementation:
                    # For implementation files, use DOE layer hierarchy
                    doe_layer = doc_metadata.frontmatter.get('doe_layer')
                    if doe_layer == 'directive':
                        authority_weight = 0.8  # High authority
                    elif doe_layer == 'orchestration':
                        authority_weight = 0.7  # Medium-high authority
                    elif doe_layer == 'execution':
                        authority_weight = 0.6  # Medium authority
                    else:
                        authority_weight = 0.5  # Default for implementation files
                else:
                    # For documents, use DOE precedence or authority level
                    doe_precedence = doc_metadata.frontmatter.get('doe_precedence')
                    if doe_precedence is not None:
                        # Lower precedence = higher authority = higher weight
                        authority_weight = max(0.1, 1.0 - (doe_precedence * 0.1))
                    else:
                        # Fall back to authority level
                        authority_level = doc_metadata.authority_level
                        authority_weight = max(0.1, 1.0 - (authority_level * 0.1))

            # Get criticality factor
            criticality_factor = 1.0
            importance_factors = doc_metadata.frontmatter.get('importance_factors', {}) if doc_metadata.frontmatter else {}

            if is_implementation:
                # Special criticality for implementation files
                if doc_path == 'src/agentos.py':
                    criticality_factor = 2.0  # Core execution engine
                elif 'data_orchestrator' in doc_path:
                    criticality_factor = 1.8  # Central data hub
                elif 'agentos_data_models' in doc_path:
                    criticality_factor = 1.7  # Knowledge foundation
                elif '_analyzer' in doc_path or '_planner' in doc_path:
                    criticality_factor = 1.4  # Analysis components
                elif 'validate' in doc_path:
                    criticality_factor = 1.3  # Validation systems
                else:
                    criticality_factor = 1.2  # Other utilities
            else:
                # Document criticality from frontmatter
                if importance_factors:
                    criticality = importance_factors.get('criticality', 'normal')
                    if criticality == 'system_foundation':
                        criticality_factor = 1.5
                    elif criticality == 'layer_foundation':
                        criticality_factor = 1.3
                    elif criticality == 'directive_layer':
                        criticality_factor = 1.4
                    elif criticality == 'orchestration_layer':
                        criticality_factor = 1.3
                    elif criticality == 'execution_layer':
                        criticality_factor = 1.2
                    elif criticality == 'high':
                        criticality_factor = 1.2

                    # Apply manual authority weight if specified
                    manual_weight = importance_factors.get('authority_weight')
                    if manual_weight:
                        authority_weight = manual_weight

            # Connectivity factor (more relationships = slightly higher importance)
            connectivity_factor = min(1.3, 1.0 + (total_relationships * 0.05))

            # Calculate final importance score (0-100 scale)
            importance_score = (authority_weight * criticality_factor * connectivity_factor) * 100
            importance_score = min(100, max(0, importance_score))

            self.importance_scores[doc_path] = {
                'importance_score': round(importance_score, 2),
                'authority_weight': round(authority_weight, 2),
                'criticality_factor': round(criticality_factor, 2),
                'connectivity_factor': round(connectivity_factor, 2),
                'total_relationships': total_relationships,
                'file_type': 'implementation' if is_implementation else 'documentation',
                'doe_layer': doc_metadata.frontmatter.get('doe_layer') if doc_metadata.frontmatter else None,
                'factors': importance_factors,
                'ranking_factors': {
                    'authority_contribution': round(authority_weight * 40, 2),
                    'criticality_contribution': round(criticality_factor * 30, 2),
                    'connectivity_contribution': round(connectivity_factor * 30, 2)
                }
            }

    def _verify_data_integrity(self) -> Dict[str, Any]:
        """Verify the integrity of loaded data."""
        integrity = {
            'documents_loaded': len(self.documents),
            'relationships_loaded': sum(len(targets) for rel_data in self.relationships.values() for targets in rel_data.values()),
            'coherence_calculated': self.coherence_metrics is not None,
            'authority_flow_calculated': self.authority_flow is not None,
            'file_metrics_calculated': len(self.file_metrics) > 0,
            'orphaned_relationships': [],
            'invalid_paths': [],
            'doe_registry_compliance': self._verify_doe_registry_compliance()
        }

        # Check for relationships to non-existent documents
        all_doc_paths = set(self.documents.keys())
        for rel_type, rel_data in self.relationships.items():
            for source, targets in rel_data.items():
                if source not in all_doc_paths:
                    integrity['invalid_paths'].append(f"source: {source}")
                for target in targets:
                    if target not in all_doc_paths:
                        integrity['orphaned_relationships'].append(f"{source} -> {target} ({rel_type})")

        integrity['data_valid'] = (
            len(integrity['orphaned_relationships']) == 0 and
            len(integrity['invalid_paths']) == 0 and
            integrity['coherence_calculated'] and
            integrity['authority_flow_calculated'] and
            integrity['doe_registry_compliance']['registry_valid']
        )

        return integrity

    def _verify_doe_registry_compliance(self) -> Dict[str, Any]:
        """Verify DOE registry bidirectional linkages."""
        compliance = {
            'registry_valid': False,  # Start as invalid until comprehensive check
            'forward_linkages': 0,
            'backward_linkages': 0,
            'missing_directives': [],
            'orphaned_implementations': [],
            'coverage_analysis': {
                'docs_with_implementations': 0,
                'total_docs': len([d for d in self.documents.values() if d.doc_path.startswith('docs/')]),
                'governed_implementations': 0,
                'total_implementations': 0,
                'coverage_percentage': 0.0,
                'orphaned_implementations_count': 0,
                'ineffective_docs_count': 0
            }
        }

        # Check forward linkages: docs with implementations/implements fields
        for doc_path, doc_metadata in self.documents.items():
            if doc_metadata.frontmatter:
                # Support both field names for compatibility
                impl_field = None
                if 'implementations' in doc_metadata.frontmatter:
                    impl_field = 'implementations'
                elif 'implements' in doc_metadata.frontmatter:
                    impl_field = 'implements'

                if impl_field:
                    implementations = doc_metadata.frontmatter[impl_field]
                    compliance['forward_linkages'] += len(implementations)

                    # Check backward linkages: implementations should have @directive annotations
                    for impl_path in implementations:
                        try:
                            impl_full_path = Path(impl_path)
                            if impl_full_path.exists():
                                with open(impl_full_path, 'r', encoding='utf-8') as f:
                                    impl_content = f.read()
                                doc_relative = doc_path  # Use full path for now, could optimize to relative

                                # Look for @directive annotation (support multiple formats)
                                directive_found = False
                                for line in impl_content.split('\n'):
                                    line = line.strip()
                                    # Check for @directive at start of line or within docstrings/comments
                                    if ('@directive' in line and doc_path in line):
                                        directive_found = True
                                        compliance['backward_linkages'] += 1
                                        break

                                if not directive_found:
                                    compliance['missing_directives'].append({
                                        'implementation': impl_path,
                                        'expected_directive': doc_path,
                                        'reason': 'Missing @directive annotation in implementation file'
                                    })
                            else:
                                compliance['orphaned_implementations'].append({
                                    'doc': doc_path,
                                    'implementation': impl_path,
                                    'reason': 'Referenced implementation file does not exist'
                                })
                        except Exception as e:
                            compliance['orphaned_implementations'].append({
                                'doc': doc_path,
                                'implementation': impl_path,
                                'reason': f'Cannot read implementation file: {e}'
                            })

        # Analyze comprehensive coverage
        total_docs = len([d for d in self.documents.values() if d.doc_path.startswith('docs/')])
        docs_with_implementations = sum(1 for d in self.documents.values()
                                      if d.doc_path.startswith('docs/') and d.frontmatter and
                                      ('implementations' in d.frontmatter or 'implements' in d.frontmatter))

        # Find all Python implementation files
        all_impl_files = set()
        scripts_dir = Path(self.docs_dir.parent / "scripts")
        src_dir = Path(self.docs_dir.parent / "src")

        if scripts_dir.exists():
            all_impl_files.update([f"scripts/{f.name}" for f in scripts_dir.glob("*.py")])
        if src_dir.exists():
            all_impl_files.update([f"src/{f.name}" for f in src_dir.glob("*.py")])

        total_implementations = len(all_impl_files)

        # Count unique governed implementations (avoid double-counting)
        governed_implementations = set()
        for doc_path, doc_metadata in self.documents.items():
            if doc_metadata.frontmatter:
                impl_field = 'implementations' if 'implementations' in doc_metadata.frontmatter else ('implements' if 'implements' in doc_metadata.frontmatter else None)
                if impl_field:
                    for impl_path in doc_metadata.frontmatter[impl_field]:
                        governed_implementations.add(impl_path)

        governed_count = len(governed_implementations)

        # Calculate coverage metrics
        compliance['coverage_analysis'].update({
            'docs_with_implementations': docs_with_implementations,
            'total_docs': total_docs,
            'governed_implementations': governed_count,
            'total_implementations': total_implementations,
            'orphaned_implementations_count': max(0, total_implementations - governed_count),
            'ineffective_docs_count': max(0, total_docs - docs_with_implementations)
        })

        # Calculate overall coverage percentage
        if total_docs > 0 and total_implementations > 0:
            doc_coverage = min(1.0, docs_with_implementations / total_docs)
            impl_coverage = min(1.0, governed_count / total_implementations)
            compliance['coverage_analysis']['coverage_percentage'] = (doc_coverage + impl_coverage) / 2.0
        else:
            compliance['coverage_analysis']['coverage_percentage'] = 0.0

        # Registry is valid with proper linkage integrity and reasonable coverage
        linkage_integrity = (
            compliance['forward_linkages'] > 0 and
            len(compliance['missing_directives']) == 0 and
            len(compliance['orphaned_implementations']) == 0
        )

        # Require at least 50% coverage (some docs are purely informational)
        min_coverage = 0.5

        compliance['registry_valid'] = (
            linkage_integrity and
            compliance['coverage_analysis']['coverage_percentage'] >= min_coverage
        )

        return compliance

    def _load_implementation_file(self, file_path: Path, impl_path: str) -> Optional[DocumentMetadata]:
        """Load Python implementation file and extract DOE declarations."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract DOE declarations from comments/docstrings
            frontmatter = {}
            lines = content.split('\n')

            # Look for DOE declarations
            doe_layer = None
            doe_responsibility = None
            doe_governance = None
            doe_precedence = None
            directives = []

            for line in lines[:50]:  # Check first 50 lines
                line = line.strip()
                if line.startswith('DOE_LAYER = '):
                    doe_layer = line.split('=')[1].strip().strip('"\'')
                elif line.startswith('DOE_RESPONSIBILITY = '):
                    doe_responsibility = line.split('=')[1].strip().strip('"\'')
                elif line.startswith('DOE_GOVERNANCE = '):
                    doe_governance = line.split('=')[1].strip().strip('"\'')
                elif line.startswith('DOE_PRECEDENCE = '):
                    try:
                        doe_precedence = int(line.split('=')[1].strip())
                    except ValueError:
                        doe_precedence = None
                elif '@directive' in line and line.strip().startswith('#'):
                    # Look for @directive in comments
                    directive_match = line.find('@directive')
                    if directive_match != -1:
                        directive = line[directive_match + 11:].strip()
                        if directive.startswith('docs/'):
                            directives.append(directive)

            # Special handling for core files without DOE declarations
            if not doe_layer and impl_path == 'src/agentos.py':
                # Core implementation engine - highest criticality
                frontmatter['doe_layer'] = 'execution'  # Primary execution
                frontmatter['doe_responsibility'] = 'Core CLI implementation and system orchestration'
                frontmatter['doe_governance'] = 'docs/reference/agentos/doe-framework.md'
                frontmatter['doe_precedence'] = 2  # High precedence for core engine
                frontmatter['importance_factors'] = {
                    'authority_weight': 0.9,  # Very high authority
                    'criticality': 'core_engine',  # Special criticality
                    'connectivity_impact': 'system_orchestrator'
                }
                doe_layer = 'execution'

            # Build frontmatter
            if doe_layer or directives:  # Include files with directives even without DOE declarations
                frontmatter['doe_layer'] = doe_layer
                frontmatter['doe_responsibility'] = doe_responsibility or ""
                frontmatter['doe_governance'] = doe_governance or ""
                frontmatter['doe_precedence'] = doe_precedence
                frontmatter['governed_by'] = [doe_governance] if doe_governance else []
                frontmatter['implementations'] = []  # Implementation files don't implement themselves

                # Add importance factors based on DOE layer
                if doe_layer == 'directive':
                    frontmatter['importance_factors'] = {
                        'authority_weight': 0.8,
                        'criticality': 'directive_layer',
                        'connectivity_impact': 'defines_system_behavior'
                    }
                elif doe_layer == 'orchestration':
                    frontmatter['importance_factors'] = {
                        'authority_weight': 0.7,
                        'criticality': 'orchestration_layer',
                        'connectivity_impact': 'enables_intelligence'
                    }
                elif doe_layer == 'execution':
                    frontmatter['importance_factors'] = {
                        'authority_weight': 0.6,
                        'criticality': 'execution_layer',
                        'connectivity_impact': 'provides_operations'
                    }

                # Add @directive relationships as governs
                if directives:
                    frontmatter['governs'] = directives

                # Create DocumentMetadata for the implementation file
                return DocumentMetadata(impl_path, frontmatter)

        except Exception as e:
            # If we can't parse the file, return None
            return None

        return None

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

            import yaml
            return yaml.safe_load(frontmatter_text)
        except Exception:
            return None

    def get_document_context(self, doc_path: str) -> Optional[Dict[str, Any]]:
        """Get comprehensive context for a specific document."""
        if doc_path not in self.documents:
            return None

        doc = self.documents[doc_path]
        relationships = self.relationship_graph.get_relationships_for_doc(doc_path)

        return {
            'document': doc.to_dict(),
            'relationships': relationships,
            'authority_context': self.authority_hierarchy.validate_hierarchy(doc_path),
            'file_metrics': self.file_metrics.get(doc_path, {}),
            'coherence_impact': self._calculate_document_coherence_impact(doc_path)
        }

    def _calculate_document_coherence_impact(self, doc_path: str) -> Dict[str, Any]:
        """Calculate how this document impacts system coherence."""
        if not self.coherence_metrics:
            return {'error': 'coherence metrics not calculated'}

        # Count relationships this document has
        doc_relationships = self.relationship_graph.get_relationships_for_doc(doc_path)
        total_rels = sum(len(targets) for targets in doc_relationships.values())

        # Determine if document is connected
        connected = total_rels > 0

        return {
            'is_connected': connected,
            'relationship_count': total_rels,
            'coherence_contribution': 'connected' if connected else 'isolated',
            'authority_level': self.documents[doc_path].authority_level if doc_path in self.documents else None
        }

def main():
    """CLI interface for data orchestration testing."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Data Orchestrator - unified AgentOS data coordination"
    )

    parser.add_argument(
        "command",
        choices=["load", "verify", "stats", "importance", "insights"],
        help="Command to execute"
    )

    parser.add_argument(
        "--output", "-o",
        choices=["json", "text"],
        default="text",
        help="Output format (default: text)"
    )

    args = parser.parse_args()

    orchestrator = DataOrchestrator()

    if args.command == "load":
        success = orchestrator.load_all_data()
        if success:
            if args.output == "json":
                data = orchestrator.get_structured_data()
                print(json.dumps(data['metadata'], indent=2))
            else:
                print("✅ Data loaded successfully")
        else:
            print("❌ Data loading failed")
            sys.exit(1)

    elif args.command == "verify":
        orchestrator.load_all_data()
        integrity = orchestrator._verify_data_integrity()

        if args.output == "json":
            print(json.dumps(integrity, indent=2))
        else:
            status = "✅" if integrity['data_valid'] else "❌"
            print(f"{status} Data integrity: {integrity['data_valid']}")
            if integrity['orphaned_relationships']:
                print(f"⚠️  {len(integrity['orphaned_relationships'])} orphaned relationships")
            if integrity['invalid_paths']:
                print(f"⚠️  {len(integrity['invalid_paths'])} invalid paths")

    elif args.command == "stats":
        orchestrator.load_all_data()
        data = orchestrator.get_structured_data()

        if args.output == "json":
            stats = {
                'documents': data['metadata']['documents_count'],
                'relationships': data['metadata']['relationships_count'],
                'coherence': data['coherence_metrics'],
                'authority_flow': {
                    'valid_flows': len(data['authority_flow']['valid_flows']),
                    'invalid_flows': len(data['authority_flow']['invalid_flows'])
                }
            }
            print(json.dumps(stats, indent=2))
        else:
            meta = data['metadata']
            coh = data['coherence_metrics']
            auth = data['authority_flow']
            print("📊 AgentOS Data Statistics")
            print(f"Documents: {meta['documents_count']}")
            print(f"Relationships: {meta['relationships_count']}")
            print(f"Connection Coverage: {coh['connection_coverage']:.1%}")
            print(f"Isolated Documents: {coh['isolated_documents']}")
            print(f"Authority Valid Flows: {len(auth['valid_flows'])}")
            print(f"Authority Invalid Flows: {len(auth['invalid_flows'])}")

    elif args.command == "importance":
        orchestrator.load_all_data()
        rankings = orchestrator.get_importance_rankings(limit=20)

        if args.output == "json":
            print(json.dumps(rankings, indent=2))
        else:
            print("🏆 AgentOS Document Importance Rankings (Top 20)")
            print("-" * 80)
            for i, ranking in enumerate(rankings, 1):
                print("2d")
                print(f"  Authority: {ranking['authority_weight']:.2f} | Criticality: {ranking['criticality_factor']:.2f} | Connectivity: {ranking['connectivity_factor']:.2f}")
                print(f"  Relationships: {ranking['total_relationships']}")
                print()

    elif args.command == "insights":
        orchestrator.load_all_data()
        insights = orchestrator.get_importance_insights()

        if args.output == "json":
            print(json.dumps(insights, indent=2))
        else:
            overview = insights['system_overview']
            print("🔍 AgentOS Importance Insights")
            print("-" * 40)
            print(f"Total Documents: {overview['total_documents']}")
            print(f"Average Importance: {overview['average_importance']:.1f}/100")
            print(f"Score Range: {overview['lowest_score']:.1f} - {overview['highest_score']:.1f}")
            print()
            print("Distribution:")
            dist = overview['importance_distribution']
            print(f"  Very High (80+): {dist['very_high']}")
            print(f"  High (60-79): {dist['high']}")
            print(f"  Medium (40-59): {dist['medium']}")
            print(f"  Low (20-39): {dist['low']}")
            print(f"  Very Low (<20): {dist['very_low']}")
            print()
            print("Self-Reflection Insights:")
            for insight in insights['self_reflection_insights']:
                print(f"  • {insight}")
            print()
            if insights['gap_analysis_opportunities']:
                print("Gap Analysis Opportunities:")
                for gap in insights['gap_analysis_opportunities'][:5]:
                    print(f"  • {gap['doc_path']}: {gap['issue']}")

if __name__ == "__main__":
    main()