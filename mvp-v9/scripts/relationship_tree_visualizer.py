#!/usr/bin/env python3
"""
Authentic Relationship Tree Visualization for AgentOS v9

Provides genuine self-reflection through context-sensitive tree diagrams
showing file relationships, precedence hierarchies, and system coherence.

DOE Registry - Bidirectional Linkages:
@directive docs/reference/agentos/relationship-orchestration.md

# DOE Layer Declaration
DOE_LAYER = "execution"
DOE_RESPONSIBILITY = "Visualize relationship trees and system coherence"
DOE_GOVERNANCE = "docs/reference/agentos/doe-framework.md"
DOE_PRECEDENCE = 4
"""

import sys
import yaml
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from collections import defaultdict, deque

# Import shared data models
sys.path.append(str(Path(__file__).parent))
try:
    from agentos_data_models import DocumentMetadata, RelationshipGraph, AuthorityHierarchy, FileMetrics
except ImportError:
    print("Warning: Could not import shared data models")
    DocumentMetadata = None
    RelationshipGraph = None
    AuthorityHierarchy = None
    FileMetrics = None

class RelationshipTreeVisualizer:
    """Creates authentic relationship tree visualizations for self-reflection."""

    def __init__(self):
        self.relationship_graph = RelationshipGraph()
        self.authority_hierarchy = AuthorityHierarchy()
        self.file_metrics = FileMetrics()
        self.docs_dir = Path("docs")

    def load_system_data(self) -> None:
        """Load all system relationship and document data."""
        self._load_documents()
        self._load_relationships()

    def _load_documents(self) -> None:
        """Load all documents into the relationship graph."""
        for md_file in self.docs_dir.rglob('*.md'):
            if md_file.name == 'index.md':
                continue

            # Load frontmatter
            frontmatter = self._load_frontmatter(md_file)
            doc_path = f"docs/{md_file.relative_to(self.docs_dir)}"

            # Add to relationship graph
            self.relationship_graph.add_document(doc_path, frontmatter)

    def _load_relationships(self) -> None:
        """Load all document relationships."""
        relationship_types = ['depends_on', 'informs', 'evidence_for', 'implements', 'governed_by', 'related']

        for md_file in self.docs_dir.rglob('*.md'):
            if md_file.name == 'index.md':
                continue

            frontmatter = self._load_frontmatter(md_file)
            if not frontmatter:
                continue

            doc_path = f"docs/{md_file.relative_to(self.docs_dir)}"

            for rel_type in relationship_types:
                if rel_type in frontmatter:
                    targets = frontmatter[rel_type]
                    if isinstance(targets, list):
                        for target in targets:
                            if isinstance(target, str) and target.startswith('docs/'):
                                self.relationship_graph.add_relationship(doc_path, rel_type, target)
                    elif isinstance(targets, str) and targets.startswith('docs/'):
                        self.relationship_graph.add_relationship(doc_path, rel_type, target)

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

    def generate_authentic_tree(self, context: str = "overview") -> str:
        """Generate authentic, context-sensitive relationship tree."""
        if context == "architecture":
            return self._generate_architecture_tree()
        elif context == "implementation":
            return self._generate_implementation_tree()
        elif context == "maintenance":
            return self._generate_maintenance_tree()
        else:
            return self._generate_overview_tree()

    def _generate_overview_tree(self) -> str:
        """Generate overview relationship tree."""
        lines = ["System Relationship Overview Tree", "=" * 40, ""]

        # Build tree structure
        tree_structure = self._build_tree_structure()

        # Add summary metrics
        coherence = self.relationship_graph.calculate_coherence_metrics()
        lines.extend([
            f"Total Documents: {coherence['total_documents']}",
            f"Connected Documents: {coherence['connected_documents']} ({coherence['connection_coverage']:.1%})",
            f"Isolated Documents: {coherence['isolated_documents']}",
            f"Relationship Types: {coherence['relationship_types_count']}",
            f"Total Relationships: {coherence['total_relationships']}",
            ""
        ])

        # Add tree visualization
        lines.extend(self._format_tree_visualization(tree_structure))

        return "\n".join(lines)

    def _generate_architecture_tree(self) -> str:
        """Generate architecture-focused relationship tree."""
        lines = ["System Architecture Relationship Tree", "=" * 45, ""]

        # Focus on authority flow and structural relationships
        authority_flow = self.relationship_graph.get_authority_flow()

        lines.extend([
            f"Authority Compliance: {len(authority_flow['valid_flows'])} valid, {len(authority_flow['invalid_flows'])} invalid",
            ""
        ])

        # Show hierarchical structure
        tree_structure = self._build_authority_tree()
        lines.extend(self._format_tree_visualization(tree_structure))

        # Add gap analysis
        lines.extend(["", "Architecture Gaps:"])
        gaps = self._identify_architecture_gaps()
        for gap in gaps:
            lines.append(f"  ⚠️  {gap}")

        return "\n".join(lines)

    def _generate_implementation_tree(self) -> str:
        """Generate implementation-focused relationship tree."""
        lines = ["Implementation Coverage Tree", "=" * 30, ""]

        # Analyze docs-to-implementation coverage
        implementation_status = self._analyze_implementation_coverage()

        lines.extend([
            f"Fully Implemented: {len(implementation_status['fully_implemented'])}/{implementation_status['total_docs']}",
            f"Documentation Only: {len(implementation_status['documentation_only'])}/{implementation_status['total_docs']}",
            ""
        ])

        # Show implementation tree
        tree_structure = self._build_implementation_tree()
        lines.extend(self._format_tree_visualization(tree_structure))

        return "\n".join(lines)

    def _generate_maintenance_tree(self) -> str:
        """Generate maintenance-focused relationship tree."""
        lines = ["Maintenance Burden Tree", "=" * 25, ""]

        # Analyze maintenance burden
        maintenance_analysis = self._analyze_maintenance_burden()

        lines.extend([
            f"High Maintenance Documents: {len(maintenance_analysis['high_burden'])}",
            f"Moderate Maintenance: {len(maintenance_analysis['moderate_burden'])}",
            f"Low Maintenance: {len(maintenance_analysis['low_burden'])}",
            ""
        ])

        # Show maintenance tree
        tree_structure = self._build_maintenance_tree()
        lines.extend(self._format_tree_visualization(tree_structure))

        return "\n".join(lines)

    def _build_tree_structure(self) -> Dict[str, Any]:
        """Build basic tree structure from relationships."""
        tree = {"roots": [], "nodes": {}}

        # Find root nodes (documents with no incoming relationships)
        all_docs = set(self.relationship_graph.documents.keys())
        docs_with_incoming = set()

        for rel_data in self.relationship_graph.relationships.values():
            for targets in rel_data.values():
                docs_with_incoming.update(targets)

        root_docs = all_docs - docs_with_incoming
        tree["roots"] = sorted(list(root_docs))

        # Build node relationships
        for doc_path in self.relationship_graph.documents.keys():
            outgoing = self.relationship_graph.get_relationships_for_doc(doc_path)
            children = []
            for rel_type, targets in outgoing.items():
                if not rel_type.startswith('incoming_'):
                    for target in targets:
                        children.append({
                            'target': target,
                            'relationship': rel_type
                        })

            tree["nodes"][doc_path] = {
                'children': children,
                'authority_level': self.relationship_graph.documents[doc_path].authority_level
            }

        return tree

    def _build_authority_tree(self) -> Dict[str, Any]:
        """Build tree structure organized by authority levels."""
        tree = {"roots": [], "nodes": {}}

        # Group by authority level
        by_authority = defaultdict(list)
        for doc_path, doc_meta in self.relationship_graph.documents.items():
            by_authority[doc_meta.authority_level].append(doc_path)

        # Reference docs (level 1) are roots
        tree["roots"] = sorted(by_authority.get(1, []))

        # Build authority-aware relationships
        for doc_path in self.relationship_graph.documents.keys():
            doc_auth = self.relationship_graph.documents[doc_path].authority_level

            # Only show relationships that flow down in authority
            children = []
            outgoing = self.relationship_graph.get_relationships_for_doc(doc_path)

            for rel_type, targets in outgoing.items():
                if not rel_type.startswith('incoming_'):
                    for target_doc in targets:
                        if target_doc in self.relationship_graph.documents:
                            target_auth = self.relationship_graph.documents[target_doc].authority_level
                            if target_auth >= doc_auth:  # Same or higher authority (valid flow)
                                children.append({
                                    'target': target_doc,
                                    'relationship': rel_type,
                                    'authority_flow': f"{doc_auth}→{target_auth}"
                                })

            tree["nodes"][doc_path] = {
                'children': children,
                'authority_level': doc_auth,
                'authority_name': self.relationship_graph.documents[doc_path].get_authority_name()
            }

        return tree

    def _build_implementation_tree(self) -> Dict[str, Any]:
        """Build tree showing implementation coverage."""
        tree = {"roots": [], "nodes": {}}

        # Categorize documents by implementation status
        fully_implemented = []
        documentation_only = []

        for doc_path, doc_meta in self.relationship_graph.documents.items():
            implementations = doc_meta.frontmatter.get('implementations', [])
            if implementations:
                fully_implemented.append(doc_path)
            else:
                documentation_only.append(doc_path)

        # Implementation status as roots
        tree["roots"] = ["Fully Implemented", "Documentation Only"]

        # Add implementation nodes
        tree["nodes"]["Fully Implemented"] = {
            'children': [{'target': doc, 'relationship': 'implemented'} for doc in fully_implemented],
            'authority_level': 0
        }

        tree["nodes"]["Documentation Only"] = {
            'children': [{'target': doc, 'relationship': 'documented_only'} for doc in documentation_only],
            'authority_level': 0
        }

        # Add document nodes
        for doc_path in self.relationship_graph.documents.keys():
            tree["nodes"][doc_path] = {
                'children': [],  # No children in this view
                'authority_level': self.relationship_graph.documents[doc_path].authority_level
            }

        return tree

    def _build_maintenance_tree(self) -> Dict[str, Any]:
        """Build tree showing maintenance burden."""
        tree = {"roots": [], "nodes": {}}

        # Analyze maintenance burden for each document
        high_burden = []
        moderate_burden = []
        low_burden = []

        for doc_path, doc_meta in self.relationship_graph.documents.items():
            # Calculate maintenance burden
            relationship_count = len(self.relationship_graph.get_relationships_for_doc(doc_path))
            file_size = doc_meta.file_size

            if relationship_count >= 5 or file_size >= 10000:
                high_burden.append(doc_path)
            elif relationship_count >= 2 or file_size >= 5000:
                moderate_burden.append(doc_path)
            else:
                low_burden.append(doc_path)

        # Maintenance categories as roots
        tree["roots"] = ["High Maintenance", "Moderate Maintenance", "Low Maintenance"]

        # Add maintenance nodes
        tree["nodes"]["High Maintenance"] = {
            'children': [{'target': doc, 'relationship': 'high_burden'} for doc in high_burden],
            'authority_level': 0
        }

        tree["nodes"]["Moderate Maintenance"] = {
            'children': [{'target': doc, 'relationship': 'moderate_burden'} for doc in moderate_burden],
            'authority_level': 0
        }

        tree["nodes"]["Low Maintenance"] = {
            'children': [{'target': doc, 'relationship': 'low_burden'} for doc in low_burden],
            'authority_level': 0
        }

        # Add document nodes with maintenance details
        for doc_path in self.relationship_graph.documents.keys():
            relationship_count = len(self.relationship_graph.get_relationships_for_doc(doc_path))
            doc_meta = self.relationship_graph.documents[doc_path]

            tree["nodes"][doc_path] = {
                'children': [],
                'authority_level': doc_meta.authority_level,
                'maintenance_details': {
                    'relationship_count': relationship_count,
                    'file_size': doc_meta.file_size,
                    'file_size_category': self.file_metrics._categorize_size(doc_meta.file_size)
                }
            }

        return tree

    def _format_tree_visualization(self, tree_structure: Dict[str, Any]) -> List[str]:
        """Format tree structure into readable visualization."""
        lines = []

        def add_node(prefix: str, node_name: str, node_data: Dict, is_last: bool = False):
            """Recursively add tree nodes."""
            connector = "└── " if is_last else "├── "
            lines.append(f"{prefix}{connector}{node_name}")

            if node_name in tree_structure.get("nodes", {}):
                node_info = tree_structure["nodes"][node_name]

                # Add authority info if available
                if 'authority_level' in node_info and node_info['authority_level'] > 0:
                    auth_name = node_info.get('authority_name', f"Level {node_info['authority_level']}")
                    lines.append(f"{prefix}{'    ' if is_last else '│   '}Authority: {auth_name}")

                # Add maintenance details if available
                if 'maintenance_details' in node_info:
                    details = node_info['maintenance_details']
                    lines.append(f"{prefix}{'    ' if is_last else '│   '}Relationships: {details['relationship_count']}, Size: {details['file_size_category']}")

                # Add children
                children = node_info.get('children', [])
                for i, child in enumerate(children):
                    child_prefix = prefix + ("    " if is_last else "│   ")
                    is_last_child = (i == len(children) - 1)
                    child_connector = "└── " if is_last_child else "├── "

                    relationship = child.get('relationship', 'relates_to')
                    authority_flow = child.get('authority_flow', '')

                    child_display = f"{child['target']}"
                    if authority_flow:
                        child_display += f" ({authority_flow})"
                    if relationship != 'relates_to':
                        child_display += f" [{relationship}]"

                    lines.append(f"{child_prefix}{child_connector}{child_display}")

        # Add root nodes
        for i, root in enumerate(tree_structure.get("roots", [])):
            is_last = (i == len(tree_structure["roots"]) - 1)
            add_node("", root, tree_structure["nodes"].get(root, {}), is_last)

        return lines

    def _identify_architecture_gaps(self) -> List[str]:
        """Identify architecture-specific gaps."""
        gaps = []

        # Check for isolated reference docs
        for doc_path, doc_meta in self.relationship_graph.documents.items():
            if doc_meta.authority_level == 1:  # Reference docs
                relationships = self.relationship_graph.get_relationships_for_doc(doc_path)
                outgoing_count = sum(len(targets) for rel_type, targets in relationships.items()
                                    if not rel_type.startswith('incoming_'))

                if outgoing_count == 0:
                    gaps.append(f"Reference doc {doc_path} has no outgoing relationships - cannot guide system")

        # Check for authority violations
        authority_flow = self.relationship_graph.get_authority_flow()
        for violation in authority_flow['invalid_flows']:
            gaps.append(f"Authority violation: {violation['source']} (L{violation['source_authority']}) "
                       f"{violation['relationship_type']} {violation['target']} (L{violation['target_authority']})")

        return gaps

    def _analyze_implementation_coverage(self) -> Dict[str, Any]:
        """Analyze which documents have implementation coverage."""
        fully_implemented = []
        documentation_only = []

        for doc_path, doc_meta in self.relationship_graph.documents.items():
            implementations = doc_meta.frontmatter.get('implementations', [])
            if implementations:
                fully_implemented.append(doc_path)
            else:
                documentation_only.append(doc_path)

        return {
            'total_docs': len(self.relationship_graph.documents),
            'fully_implemented': fully_implemented,
            'documentation_only': documentation_only
        }

    def _analyze_maintenance_burden(self) -> Dict[str, Any]:
        """Analyze maintenance burden for documents."""
        high_burden = []
        moderate_burden = []
        low_burden = []

        for doc_path, doc_meta in self.relationship_graph.documents.items():
            relationship_count = len(self.relationship_graph.get_relationships_for_doc(doc_path))
            file_size = doc_meta.file_size

            if relationship_count >= 5 or file_size >= 10000:
                high_burden.append(doc_path)
            elif relationship_count >= 2 or file_size >= 5000:
                moderate_burden.append(doc_path)
            else:
                low_burden.append(doc_path)

        return {
            'high_burden': high_burden,
            'moderate_burden': moderate_burden,
            'low_burden': low_burden
        }

# CLI Interface
def main():
    import argparse

    parser = argparse.ArgumentParser(description='Authentic Relationship Tree Visualization')
    subparsers = parser.add_subparsers(dest='command')

    # Generate tree
    tree_parser = subparsers.add_parser('generate', help='Generate relationship tree')
    tree_parser.add_argument('--context', default='overview',
                           choices=['overview', 'architecture', 'implementation', 'maintenance'],
                           help='Tree context (default: overview)')

    # Analyze coherence
    subparsers.add_parser('coherence', help='Analyze system coherence')

    # Show authority flow
    subparsers.add_parser('authority', help='Show authority flow analysis')

    args = parser.parse_args()

    visualizer = RelationshipTreeVisualizer()
    visualizer.load_system_data()

    if args.command == 'generate':
        tree = visualizer.generate_authentic_tree(args.context)
        print(tree)

    elif args.command == 'coherence':
        coherence = visualizer.relationship_graph.calculate_coherence_metrics()
        print("System Coherence Analysis:")
        print(f"  Total Documents: {coherence['total_documents']}")
        print(f"  Connection Coverage: {coherence['connection_coverage']:.1%}")
        print(f"  Isolated Documents: {coherence['isolated_documents']}")
        print(f"  Relationship Types: {coherence['relationship_types_count']}")
        print(f"  Authority Distribution: {coherence['authority_distribution']}")

    elif args.command == 'authority':
        flow = visualizer.relationship_graph.get_authority_flow()
        print("Authority Flow Analysis:")
        print(f"  Valid Flows: {len(flow['valid_flows'])}")
        print(f"  Invalid Flows: {len(flow['invalid_flows'])}")

        if flow['invalid_flows']:
            print("\nAuthority Violations:")
            for violation in flow['invalid_flows'][:5]:  # Show first 5
                print(f"  ❌ {violation['source']} (L{violation['source_authority']}) "
                      f"{violation['relationship_type']} "
                      f"{violation['target']} (L{violation['target_authority']})")

if __name__ == '__main__':
    main()