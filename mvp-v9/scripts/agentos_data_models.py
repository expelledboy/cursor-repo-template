#!/usr/bin/env python3
"""
AgentOS Data Models - Shared utilities for core AgentOS data structures.

Provides unified data models and utilities for:
- Document metadata and relationships
- Authority hierarchies
- File metrics and analysis
- System coherence calculations

DOE Registry - Bidirectional Linkages:
@directive docs/reference/agentos/architecture.md

# DOE Layer Declaration
DOE_LAYER = "orchestration"
DOE_RESPONSIBILITY = "Provide unified data models and relationship structures"
DOE_GOVERNANCE = "docs/reference/agentos/doe-framework.md"
DOE_PRECEDENCE = 3
"""

import os
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
import yaml

class DocumentMetadata:
    """Standardized document metadata structure."""

    AUTHORITY_LEVELS = {
        'framework': 0,  # Special level for DOE framework
        'reference': 1,
        'how-to': 2,
        'explanation': 3,
        'tutorials': 4,
        'work': 5,
        'archive': 6
    }

    AUTHORITY_NAMES = {v: k for k, v in AUTHORITY_LEVELS.items()}

    def __init__(self, doc_path: str, frontmatter: Optional[Dict] = None):
        self.doc_path = doc_path
        self.title = frontmatter.get('title', 'Untitled') if frontmatter else 'Untitled'
        self.status = frontmatter.get('status', 'unknown') if frontmatter else 'unknown'
        self.domain = frontmatter.get('domain', 'unknown') if frontmatter else 'unknown'
        self.created_date = frontmatter.get('created_date') if frontmatter else None
        self.authority_level = self._calculate_authority_level(doc_path, frontmatter)
        self.frontmatter = frontmatter or {}

        # File system metadata
        doc_file = Path(doc_path)
        self.file_size = os.path.getsize(doc_file) if doc_file.exists() else 0
        self.last_modified = datetime.fromtimestamp(os.path.getmtime(doc_file)).isoformat() if doc_file.exists() else None

    def _calculate_authority_level(self, doc_path: str, frontmatter: Optional[Dict] = None) -> int:
        """Calculate authority level from frontmatter or file path."""
        # Check frontmatter first for explicit authority_level
        if frontmatter and 'authority_level' in frontmatter:
            level_value = frontmatter['authority_level']
            # If it's a string, look it up in AUTHORITY_LEVELS
            if isinstance(level_value, str):
                return self.AUTHORITY_LEVELS.get(level_value, 7)
            # If it's already a number, use it
            elif isinstance(level_value, int):
                return level_value

        # Fall back to path-based calculation
        for level_name, level_num in self.AUTHORITY_LEVELS.items():
            if f'docs/{level_name}/' in doc_path:
                return level_num
        return 7  # Unknown

    def get_authority_name(self) -> str:
        """Get human-readable authority level name."""
        return self.AUTHORITY_NAMES.get(self.authority_level, 'Unknown')

    def can_govern(self, other_doc: 'DocumentMetadata') -> bool:
        """Check if this document can govern another document."""
        return self.authority_level < other_doc.authority_level

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation."""
        return {
            'doc_path': self.doc_path,
            'title': self.title,
            'status': self.status,
            'domain': self.domain,
            'authority_level': self.authority_level,
            'authority_name': self.get_authority_name(),
            'file_size': self.file_size,
            'last_modified': self.last_modified,
            'frontmatter': self.frontmatter
        }

class RelationshipGraph:
    """Manages document relationship graphs."""

    VALID_RELATIONSHIP_TYPES = {
        'depends_on', 'informs', 'evidence_for', 'implements',
        'governed_by', 'related', 'supersedes', 'superseded_by'
    }

    def __init__(self):
        self.relationships: Dict[str, Dict[str, List[str]]] = {}
        self.documents: Dict[str, DocumentMetadata] = {}

    def add_document(self, doc_path: str, frontmatter: Optional[Dict] = None) -> None:
        """Add a document to the graph."""
        self.documents[doc_path] = DocumentMetadata(doc_path, frontmatter)

    def add_relationship(self, source_doc: str, rel_type: str, target_doc: str) -> bool:
        """Add a relationship between documents."""
        if rel_type not in self.VALID_RELATIONSHIP_TYPES:
            return False

        if rel_type not in self.relationships:
            self.relationships[rel_type] = {}

        if source_doc not in self.relationships[rel_type]:
            self.relationships[rel_type][source_doc] = []

        if target_doc not in self.relationships[rel_type][source_doc]:
            self.relationships[rel_type][source_doc].append(target_doc)

        return True

    def get_relationships_for_doc(self, doc_path: str) -> Dict[str, List[str]]:
        """Get all relationships for a specific document."""
        outgoing = {}
        for rel_type, rel_data in self.relationships.items():
            if doc_path in rel_data:
                outgoing[rel_type] = rel_data[doc_path]

        # Also check for incoming relationships
        incoming = {}
        for rel_type, rel_data in self.relationships.items():
            incoming_rels = []
            for source_doc, targets in rel_data.items():
                if doc_path in targets:
                    incoming_rels.append(source_doc)
            if incoming_rels:
                incoming[f"incoming_{rel_type}"] = incoming_rels

        return {**outgoing, **incoming}

    def get_authority_flow(self) -> Dict[str, Any]:
        """Analyze how authority flows through relationships."""
        flow_analysis = {
            'valid_flows': [],
            'invalid_flows': [],
            'authority_levels': {},
            'governance_chains': []
        }

        # Analyze each relationship for authority compliance
        for rel_type, rel_data in self.relationships.items():
            for source_doc, targets in rel_data.items():
                source_meta = self.documents.get(source_doc)
                if not source_meta:
                    continue

                for target_doc in targets:
                    target_meta = self.documents.get(target_doc)
                    if not target_meta:
                        continue

                    # For governed_by relationships: target governs source, so target should have lower authority level
                    is_valid = True
                    if rel_type == 'governed_by':
                        is_valid = target_meta.authority_level < source_meta.authority_level

                    flow = {
                        'relationship_type': rel_type,
                        'source': source_doc,
                        'source_authority': source_meta.authority_level,
                        'target': target_doc,
                        'target_authority': target_meta.authority_level,
                        'valid': is_valid
                    }

                    if flow['valid']:
                        flow_analysis['valid_flows'].append(flow)
                    else:
                        flow_analysis['invalid_flows'].append(flow)

        return flow_analysis

    def calculate_coherence_metrics(self) -> Dict[str, Any]:
        """Calculate system coherence metrics."""
        total_docs = len(self.documents)
        connected_docs = set()

        # Find all connected documents
        for rel_data in self.relationships.values():
            for source_doc, targets in rel_data.items():
                connected_docs.add(source_doc)
                connected_docs.update(targets)

        isolated_docs = total_docs - len(connected_docs)

        # Calculate authority distribution
        authority_counts = {}
        for doc in self.documents.values():
            level = doc.authority_level
            authority_counts[level] = authority_counts.get(level, 0) + 1

        return {
            'total_documents': total_docs,
            'connected_documents': len(connected_docs),
            'isolated_documents': isolated_docs,
            'connection_coverage': len(connected_docs) / total_docs if total_docs > 0 else 0,
            'authority_distribution': authority_counts,
            'relationship_types_count': len(self.relationships),
            'total_relationships': sum(len(targets) for rel_data in self.relationships.values() for targets in rel_data.values())
        }

class AuthorityHierarchy:
    """Manages document authority hierarchies."""

    def __init__(self):
        self.levels = DocumentMetadata.AUTHORITY_LEVELS

    def validate_hierarchy(self, doc_path: str) -> Dict[str, Any]:
        """Validate that a document is in the correct authority location."""
        expected_level = None
        actual_level = None

        for level_name, level_num in self.levels.items():
            if f'docs/{level_name}/' in doc_path:
                expected_level = level_num
                actual_level = level_num
                break

        if expected_level is None:
            actual_level = 7  # Unknown

        return {
            'doc_path': doc_path,
            'expected_authority_level': expected_level,
            'actual_authority_level': actual_level,
            'compliant': expected_level == actual_level if expected_level is not None else False,
            'expected_path_pattern': f'docs/{list(self.levels.keys())[actual_level-1]}/' if actual_level and actual_level <= len(self.levels) else 'unknown'
        }

    def get_hierarchy_path(self, from_level: int, to_level: int) -> List[str]:
        """Get the valid hierarchy path between authority levels."""
        if from_level >= to_level:
            return []  # Cannot flow upward in authority

        path = []
        for level in range(from_level + 1, to_level + 1):
            level_name = DocumentMetadata.AUTHORITY_NAMES.get(level, 'unknown')
            path.append(f'docs/{level_name}/')

        return path

class FileMetrics:
    """Provides file analysis metrics."""

    def analyze_file(self, file_path: Path) -> Dict[str, Any]:
        """Analyze a file for various metrics."""
        metrics = {
            'file_path': str(file_path),
            'exists': file_path.exists(),
            'size_bytes': 0,
            'size_category': 'nonexistent',
            'line_count': 0,
            'word_count': 0,
            'has_frontmatter': False,
            'content_complexity': 'unknown'
        }

        if not file_path.exists():
            return metrics

        try:
            metrics['size_bytes'] = os.path.getsize(file_path)
            metrics['size_category'] = self._categorize_size(metrics['size_bytes'])

            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                metrics['line_count'] = len(content.split('\n'))
                metrics['word_count'] = len(content.split())

                # Check for frontmatter
                metrics['has_frontmatter'] = content.startswith('---')

                # Basic complexity assessment
                if metrics['word_count'] > 2000:
                    metrics['content_complexity'] = 'high'
                elif metrics['word_count'] > 500:
                    metrics['content_complexity'] = 'medium'
                else:
                    metrics['content_complexity'] = 'low'

        except Exception as e:
            metrics['error'] = str(e)

        return metrics

    def _categorize_size(self, size_bytes: int) -> str:
        """Categorize file size."""
        if size_bytes < 1000:
            return 'small'
        elif size_bytes < 5000:
            return 'medium'
        elif size_bytes < 10000:
            return 'large'
        else:
            return 'very_large'

    def analyze_directory(self, dir_path: Path) -> Dict[str, Any]:
        """Analyze all files in a directory."""
        if not dir_path.exists() or not dir_path.is_dir():
            return {'error': 'Directory does not exist or is not a directory'}

        file_analyses = {}
        total_metrics = {
            'total_files': 0,
            'total_size': 0,
            'size_categories': {},
            'complexity_distribution': {}
        }

        for file_path in dir_path.rglob('*.md'):
            if file_path.name == 'index.md':
                continue

            analysis = self.analyze_file(file_path)
            file_analyses[str(file_path)] = analysis

            total_metrics['total_files'] += 1
            total_metrics['total_size'] += analysis['size_bytes']

            # Update category counts
            category = analysis['size_category']
            total_metrics['size_categories'][category] = total_metrics['size_categories'].get(category, 0) + 1

            complexity = analysis['content_complexity']
            total_metrics['complexity_distribution'][complexity] = total_metrics['complexity_distribution'].get(complexity, 0) + 1

        return {
            'directory': str(dir_path),
            'summary': total_metrics,
            'file_analyses': file_analyses
        }