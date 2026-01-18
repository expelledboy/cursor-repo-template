#!/usr/bin/env python3
"""
Frontmatter Intelligence - AgentOS v9

Provides intelligent analysis of frontmatter relationships for context loading.

DOE Registry - Bidirectional Linkages:
@directive docs/reference/agentos/architecture.md

# DOE Layer Declaration
DOE_LAYER = "orchestration"
DOE_RESPONSIBILITY = "Provide intelligent frontmatter relationship analysis"
DOE_GOVERNANCE = "docs/reference/agentos/doe-framework.md"
DOE_PRECEDENCE = 3
"""

import yaml
from pathlib import Path
from collections import defaultdict, Counter
from typing import Dict, List, Set, Tuple, Optional, Any

class FrontmatterIntelligence:
    """Provides intelligent analysis of frontmatter relationships for context loading."""

    def __init__(self):
        self.docs_dir = Path("docs")
        self.relationships_cache = {}
        self._load_relationships()

    def _load_relationships(self):
        """Load and cache all frontmatter relationships."""
        self.relationships_cache = self._analyze_relationships()

    def _analyze_relationships(self) -> Dict[str, Dict]:
        """Analyze all frontmatter relationships in documentation."""
        relationships = defaultdict(lambda: defaultdict(list))
        document_metadata = {}

        # Relationship types to analyze
        relationship_types = [
            'depends_on', 'informs', 'evidence_for', 'implements',
            'governed_by', 'related', 'references', 'supersedes'
        ]

        for md_file in self.docs_dir.rglob('*.md'):
            if md_file.name == 'index.md':
                continue

            frontmatter = self._load_frontmatter(md_file)
            if not frontmatter:
                continue

            doc_path = f"docs/{md_file.relative_to(self.docs_dir)}"
            doc_info = {
                'path': doc_path,
                'title': frontmatter.get('title', 'Untitled'),
                'status': frontmatter.get('status', 'unknown'),
                'domain': frontmatter.get('domain', 'unknown'),
                'authority_level': self._get_authority_level(doc_path)
            }
            document_metadata[doc_path] = doc_info

            # Collect relationships
            for rel_type in relationship_types:
                if rel_type in frontmatter:
                    targets = frontmatter[rel_type]
                    if isinstance(targets, list):
                        for target in targets:
                            if isinstance(target, str) and target.startswith('docs/'):
                                relationships[rel_type][doc_path].append(target)
                    elif isinstance(targets, str) and targets.startswith('docs/'):
                        relationships[rel_type][doc_path].append(targets)

        return {
            'relationships': dict(relationships),
            'documents': document_metadata
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

    def get_relevant_context(self, current_doc: str, task_intent: str = "execution") -> Dict[str, Any]:
        """
        Get intelligently selected context documents based on relationships and task intent.

        Args:
            current_doc: Current document path
            task_intent: Task intent (execution, learning, architecture, meta-maintenance)

        Returns:
            Dict with recommended documents and reasoning
        """
        recommendations = {
            'primary_documents': [],
            'secondary_documents': [],
            'reasoning': [],
            'coverage': {}
        }

        relationships = self.relationships_cache.get('relationships', {})
        documents = self.relationships_cache.get('documents', {})

        # Context compass rules based on task intent
        context_rules = {
            'execution': ['reference', 'how-to'],
            'learning': ['tutorials', 'explanation'],
            'architecture': ['explanation', 'reference'],
            'meta-maintenance': ['reference', 'how-to', 'explanation']
        }

        allowed_levels = context_rules.get(task_intent, ['reference'])

        # Find directly related documents
        direct_relations = self._find_direct_relations(current_doc, relationships)

        # Filter by authority and intent
        for rel_type, related_docs in direct_relations.items():
            for doc_path in related_docs:
                doc_info = documents.get(doc_path, {})
                authority_level = doc_info.get('authority_level', 7)

                # Check if document is in allowed authority levels
                if any(f'docs/{level}/' in doc_path for level in allowed_levels):
                    if authority_level <= 2:  # Reference or how-to (high priority)
                        if doc_path not in recommendations['primary_documents']:
                            recommendations['primary_documents'].append(doc_path)
                            recommendations['reasoning'].append(
                                f"Direct {rel_type} relationship: {doc_path} (authority level {authority_level})"
                            )
                    elif authority_level <= 4:  # Include explanation/tutorials if relevant
                        if doc_path not in recommendations['secondary_documents']:
                            recommendations['secondary_documents'].append(doc_path)
                            recommendations['reasoning'].append(
                                f"Related {rel_type} document: {doc_path} (authority level {authority_level})"
                            )

        # Analyze relationship patterns
        recommendations['coverage'] = self._analyze_relationship_coverage(
            current_doc, recommendations['primary_documents'] + recommendations['secondary_documents']
        )

        return recommendations

    def _find_direct_relations(self, doc_path: str, relationships: Dict) -> Dict[str, List[str]]:
        """Find documents directly related to the given document."""
        direct_relations = defaultdict(list)

        # Check outgoing relationships (this doc relates to others)
        for rel_type, rel_data in relationships.items():
            if doc_path in rel_data:
                direct_relations[rel_type].extend(rel_data[doc_path])

        # Check incoming relationships (others relate to this doc)
        for rel_type, rel_data in relationships.items():
            for source_doc, targets in rel_data.items():
                if doc_path in targets:
                    direct_relations[f"incoming_{rel_type}"].append(source_doc)

        return dict(direct_relations)

    def _analyze_relationship_coverage(self, current_doc: str, recommended_docs: List[str]) -> Dict[str, Any]:
        """Analyze how well the recommendations cover relationship needs."""
        relationships = self.relationships_cache.get('relationships', {})

        # Count relationship types covered
        covered_types = set()
        total_relationships = 0

        for doc in [current_doc] + recommended_docs:
            for rel_type, rel_data in relationships.items():
                if doc in rel_data:
                    covered_types.add(rel_type)
                    total_relationships += len(rel_data[doc])

        return {
            'relationship_types_covered': len(covered_types),
            'total_relationships_analyzed': total_relationships,
            'coverage_score': len(recommended_docs) / max(1, len(covered_types))  # docs per relationship type
        }

    def detect_relationship_gaps(self) -> Dict[str, List[str]]:
        """Detect documents that lack proper relationship connections."""
        gaps = {
            'isolated_documents': [],
            'under_connected_domains': [],
            'missing_relationships': [],
            'authority_violations': [],
            'implementation_alignment_gaps': []
        }

        relationships = self.relationships_cache.get('relationships', {})
        documents = self.relationships_cache.get('documents', {})

        # Find documents with no relationships
        all_docs = set(documents.keys())
        docs_with_relations = set()

        for rel_data in relationships.values():
            for source_doc, targets in rel_data.items():
                docs_with_relations.add(source_doc)
                docs_with_relations.update(targets)

        isolated = all_docs - docs_with_relations
        gaps['isolated_documents'] = sorted(list(isolated))

        # Find domains with low connectivity
        domain_connections = defaultdict(int)
        for rel_data in relationships.values():
            for source_doc, targets in rel_data.items():
                domain = documents.get(source_doc, {}).get('domain', 'unknown')
                domain_connections[domain] += len(targets)

        avg_connections = sum(domain_connections.values()) / max(1, len(domain_connections))
        under_connected = [
            domain for domain, connections in domain_connections.items()
            if connections < avg_connections * 0.5
        ]
        gaps['under_connected_domains'] = under_connected

        # Check for implementation alignment gaps
        alignment_gaps = self._check_implementation_alignment_all()
        gaps['implementation_alignment_gaps'] = alignment_gaps

        # Check for authority hierarchy violations
        authority_violations = self._check_authority_violations()
        gaps['authority_violations'] = authority_violations

        return gaps

    def get_agent_self_awareness(self, current_doc: str) -> Dict[str, Any]:
        """Provide agent with relationship-based self-awareness."""
        awareness = {
            'document_precedence': self._get_document_precedence(current_doc),
            'implementation_alignment': self._check_implementation_alignment(current_doc),
            'relationship_context': self._get_relationship_context(current_doc),
            'authority_validation': self._validate_authority_compliance(current_doc)
        }

        return awareness

    def _check_implementation_alignment_all(self) -> List[str]:
        """Check implementation alignment for all documents."""
        gaps = []
        documents = self.relationships_cache.get('documents', {})

        for doc_path, doc_info in documents.items():
            alignment = self._check_implementation_alignment(doc_path)
            if not alignment.get('has_implementations', True) or not alignment.get('implementations_exist', True):
                gaps.append(f"{doc_path}: Missing or invalid implementations")

        return gaps

    def _check_authority_violations(self) -> List[str]:
        """Check for authority hierarchy violations in relationships."""
        violations = []
        relationships = self.relationships_cache.get('relationships', {})
        documents = self.relationships_cache.get('documents', {})

        for rel_type, rel_data in relationships.items():
            for source_doc, targets in rel_data.items():
                source_auth = documents.get(source_doc, {}).get('authority_level', 7)
                for target_doc in targets:
                    if isinstance(target_doc, str) and target_doc.startswith('docs/'):
                        target_auth = documents.get(target_doc, {}).get('authority_level', 7)

                        # Check for problematic relationships
                        if rel_type == 'governed_by' and source_auth > target_auth:
                            violations.append(f"Authority violation: {source_doc} (level {source_auth}) governed_by {target_doc} (level {target_auth})")

        return violations

    def _get_document_precedence(self, current_doc: str) -> Dict[str, Any]:
        """Get precedence information for the current document."""
        documents = self.relationships_cache.get('documents', {})
        current_auth = documents.get(current_doc, {}).get('authority_level', 7)

        precedence = {
            'current_authority_level': current_auth,
            'higher_authority_docs': [],
            'same_authority_docs': [],
            'lower_authority_docs': []
        }

        for doc_path, doc_info in documents.items():
            auth_level = doc_info.get('authority_level', 7)
            if auth_level < current_auth:
                precedence['higher_authority_docs'].append(doc_path)
            elif auth_level == current_auth:
                precedence['same_authority_docs'].append(doc_path)
            else:
                precedence['lower_authority_docs'].append(doc_path)

        return precedence

    def _check_implementation_alignment(self, doc_path: str) -> Dict[str, Any]:
        """Check if documented implementations actually exist."""
        frontmatter = self._load_frontmatter(Path(doc_path))

        if not frontmatter:
            return {'has_implementations': False, 'implementations_exist': False, 'error': 'No frontmatter'}

        implementations = frontmatter.get('implementations', [])
        has_implementations = len(implementations) > 0

        implementations_exist = True
        if has_implementations:
            for impl_path in implementations:
                if isinstance(impl_path, str):
                    # Check if file exists (relative to project root)
                    full_path = Path(impl_path)
                    if not full_path.exists() and not (Path('../') / impl_path).exists():
                        implementations_exist = False
                        break

        return {
            'has_implementations': has_implementations,
            'implementations_exist': implementations_exist,
            'implementation_count': len(implementations) if has_implementations else 0
        }

    def _get_relationship_context(self, current_doc: str) -> Dict[str, Any]:
        """Get comprehensive relationship context for a document."""
        relationships = self.relationships_cache.get('relationships', {})

        context = {
            'outgoing_relationships': {},
            'incoming_relationships': {},
            'relationship_summary': {}
        }

        # Outgoing relationships
        for rel_type, rel_data in relationships.items():
            if current_doc in rel_data:
                context['outgoing_relationships'][rel_type] = rel_data[current_doc]

        # Incoming relationships (simplified - would need full bidirectional analysis)
        context['incoming_relationships'] = {}  # Placeholder for full implementation

        # Summary
        total_outgoing = sum(len(targets) for targets in context['outgoing_relationships'].values())
        context['relationship_summary'] = {
            'total_outgoing_relationships': total_outgoing,
            'relationship_types_used': list(context['outgoing_relationships'].keys()),
            'most_connected_type': max(context['outgoing_relationships'].keys(),
                                     key=lambda k: len(context['outgoing_relationships'][k])) if context['outgoing_relationships'] else None
        }

        return context

    def _validate_authority_compliance(self, current_doc: str) -> Dict[str, Any]:
        """Validate that the document complies with authority hierarchy."""
        documents = self.relationships_cache.get('documents', {})
        current_auth = documents.get(current_doc, {}).get('authority_level', 7)

        compliance = {
            'authority_level': current_auth,
            'complies_with_hierarchy': True,
            'hierarchy_violations': [],
            'authority_guidance': self._get_authority_guidance(current_auth)
        }

        # Check file location matches authority level
        path_indicators = {
            1: 'docs/reference/',
            2: 'docs/how-to/',
            3: 'docs/explanation/',
            4: 'docs/tutorials/',
            5: 'docs/work/',
            6: 'docs/archive/'
        }

        expected_path = path_indicators.get(current_auth)
        if expected_path and expected_path not in current_doc:
            compliance['complies_with_hierarchy'] = False
            compliance['hierarchy_violations'].append(f"Document at authority level {current_auth} should be in {expected_path}")

        return compliance

    def _get_authority_guidance(self, authority_level: int) -> str:
        """Get guidance for working with documents at this authority level."""
        guidance = {
            1: "Reference docs define immutable contracts. Changes require ADR process.",
            2: "How-to docs provide procedures for reference docs. Keep aligned with specs.",
            3: "Explanation docs provide context. Update as understanding evolves.",
            4: "Tutorials support learning. Update based on user feedback.",
            5: "Work docs capture current tasks. Clean up after completion.",
            6: "Archive docs preserve history. Reference but don't modify."
        }

        return guidance.get(authority_level, "Unknown authority level - follow general documentation practices.")

# CLI Interface
def main():
    import argparse

    parser = argparse.ArgumentParser(description='Frontmatter Relationship Intelligence')
    subparsers = parser.add_subparsers(dest='command')

    # Analyze context for document
    context_parser = subparsers.add_parser('context', help='Get relevant context for a document')
    context_parser.add_argument('document', help='Document path to analyze')
    context_parser.add_argument('--intent', default='execution', choices=['execution', 'learning', 'architecture', 'meta-maintenance'], help='Task intent')

    # Detect relationship gaps
    subparsers.add_parser('gaps', help='Detect relationship gaps in documentation')

    # Get agent self-awareness
    awareness_parser = subparsers.add_parser('awareness', help='Get agent self-awareness for a document')
    awareness_parser.add_argument('document', help='Document path to analyze for self-awareness')

    # Refresh relationship cache
    subparsers.add_parser('refresh', help='Refresh relationship analysis cache')

    args = parser.parse_args()

    intelligence = FrontmatterIntelligence()

    if args.command == 'context':
        result = intelligence.get_relevant_context(args.document, args.intent)
        print("Relevant Context Analysis:")
        print(f"Task Intent: {args.intent}")
        print(f"Primary Documents ({len(result['primary_documents'])}):")
        for doc in result['primary_documents']:
            print(f"  - {doc}")
        print(f"Secondary Documents ({len(result['secondary_documents'])}):")
        for doc in result['secondary_documents']:
            print(f"  - {doc}")
        print("Reasoning:")
        for reason in result['reasoning']:
            print(f"  - {reason}")
        print(f"Coverage: {result['coverage']['relationship_types_covered']} types, {result['coverage']['total_relationships_analyzed']} relationships analyzed")

    elif args.command == 'gaps':
        gaps = intelligence.detect_relationship_gaps()
        print("Relationship Gap Analysis:")
        print(f"Isolated Documents ({len(gaps['isolated_documents'])}):")
        for doc in gaps['isolated_documents']:
            print(f"  - {doc}")
        print(f"Under-connected Domains ({len(gaps['under_connected_domains'])}):")
        for domain in gaps['under_connected_domains']:
            print(f"  - {domain}")
        print(f"Implementation Alignment Gaps ({len(gaps['implementation_alignment_gaps'])}):")
        for gap in gaps['implementation_alignment_gaps']:
            print(f"  - {gap}")
        print(f"Authority Violations ({len(gaps['authority_violations'])}):")
        for violation in gaps['authority_violations']:
            print(f"  - {violation}")

    elif args.command == 'awareness':
        awareness = intelligence.get_agent_self_awareness(args.document)
        print("Agent Self-Awareness Analysis:")
        print(f"Document: {args.document}")
        print(f"Authority Level: {awareness['document_precedence']['current_authority_level']}")
        print(f"Higher Authority Docs: {len(awareness['document_precedence']['higher_authority_docs'])}")
        print(f"Implementation Aligned: {awareness['implementation_alignment']['implementations_exist']}")
        print(f"Authority Compliant: {awareness['authority_validation']['complies_with_hierarchy']}")
        print(f"Authority Guidance: {awareness['authority_validation']['authority_guidance']}")
        if not awareness['authority_validation']['complies_with_hierarchy']:
            print("Violations:")
            for violation in awareness['authority_validation']['hierarchy_violations']:
                print(f"  - {violation}")

    elif args.command == 'refresh':
        intelligence._load_relationships()
        print("Relationship cache refreshed")

if __name__ == '__main__':
    main()