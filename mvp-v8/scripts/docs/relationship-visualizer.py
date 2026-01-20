#!/usr/bin/env python3
"""
Documentation Relationship Visualizer

Generates visual representations of documentation relationships using the
deterministic directional schema. Creates graph visualizations and
relationship analysis reports.
"""

import sys
from pathlib import Path
from collections import defaultdict, Counter
import yaml
import json

def load_frontmatter(file_path):
    """Load YAML frontmatter from a markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        if not content.startswith('---'):
            return None

        # Find the end of frontmatter
        end_pos = content.find('---', 3)
        if end_pos == -1:
            return None

        frontmatter_text = content[3:end_pos]
        return yaml.safe_load(frontmatter_text)
    except Exception as e:
        print(f"Error loading frontmatter from {file_path}: {e}", file=sys.stderr)
        return None

def collect_relationships():
    """Collect all relationships from documentation files."""
    relationships = defaultdict(lambda: defaultdict(list))
    documents = {}

    # Define relationship types
    relationship_types = [
        'informs', 'depends_on', 'implemented_by', 'implements',
        'evidence_for', 'supersedes', 'superseded_by', 'governed_by',
        'related'  # Include deprecated field for completeness
    ]

    for md_file in Path('docs').rglob('*.md'):
        if md_file.name == 'index.md':
            continue

        frontmatter = load_frontmatter(md_file)
        if not frontmatter:
            continue

        doc_path = f"docs/{md_file.relative_to('docs')}"
        doc_info = {
            'path': doc_path,
            'title': frontmatter.get('title', 'Untitled'),
            'status': frontmatter.get('status', 'unknown'),
            'domain': frontmatter.get('domain', 'unknown'),
            'authority_level': get_authority_level(doc_path)
        }
        documents[doc_path] = doc_info

        # Collect relationships
        for rel_type in relationship_types:
            if rel_type in frontmatter:
                targets = frontmatter[rel_type]
                if isinstance(targets, list):
                    for target in targets:
                        if isinstance(target, str):
                            # Normalize paths - if it's a docs path, make it relative to docs/
                            if target.startswith('docs/'):
                                relationships[rel_type][doc_path].append(target)
                            else:
                                # Non-docs paths (like scripts/) are stored as-is
                                relationships[rel_type][doc_path].append(target)

    return relationships, documents

def get_authority_level(doc_path):
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

def get_authority_name(level):
    """Get authority level name."""
    names = {
        1: 'Reference',
        2: 'How-to',
        3: 'Explanation',
        4: 'Tutorial',
        5: 'Work',
        6: 'Archive',
        7: 'Unknown'
    }
    return names.get(level, 'Unknown')

def generate_text_graph(relationships, documents, output_file=None):
    """Generate a text-based graph representation."""
    output_lines = []
    output_lines.append("=" * 80)
    output_lines.append("DOCUMENTATION RELATIONSHIP GRAPH")
    output_lines.append("=" * 80)
    output_lines.append("")

    # Group by relationship type
    relationship_types = [
        'governed_by', 'depends_on', 'implements', 'evidence_for',
        'informs', 'implemented_by', 'supersedes', 'superseded_by',
        'related'  # Include deprecated
    ]

    for rel_type in relationship_types:
        if rel_type not in relationships:
            continue

        output_lines.append(f"🔗 {rel_type.upper().replace('_', ' ')} RELATIONSHIPS")
        output_lines.append("-" * 50)

        rel_data = relationships[rel_type]
        if not rel_data:
            output_lines.append("  (No relationships of this type)")
            output_lines.append("")
            continue

        for source, targets in rel_data.items():
            source_info = documents.get(source, {})
            source_title = source_info.get('title', source)
            source_domain = source_info.get('domain', 'unknown')

            for target in targets:
                # Check if target exists (docs files vs other files)
                if target.startswith('docs/'):
                    exists = "✓" if target in documents else "✗"
                    target_info = documents.get(target, {})
                    target_title = target_info.get('title', target)
                    target_domain = target_info.get('domain', 'unknown')
                else:
                    # Non-docs paths (scripts, etc.)
                    exists = "✓" if Path(target).exists() else "✗"
                    target_title = target
                    target_domain = 'external'

                output_lines.append(f"  [{source_domain}] {source_title}")
                output_lines.append(f"    {rel_type} → {exists} [{target_domain}] {target_title}")
                if target not in documents:
                    output_lines.append("    ⚠️  TARGET DOCUMENT DOES NOT EXIST")

        output_lines.append("")

    # Statistics
    output_lines.append("=" * 80)
    output_lines.append("RELATIONSHIP STATISTICS")
    output_lines.append("=" * 80)
    output_lines.append("")

    total_relationships = sum(len(targets) for rel_data in relationships.values()
                           for targets in rel_data.values())

    output_lines.append(f"Total relationships: {total_relationships}")

    # Count by type
    type_counts = {}
    for rel_type, rel_data in relationships.items():
        count = sum(len(targets) for targets in rel_data.values())
        type_counts[rel_type] = count

    output_lines.append("\nRelationships by type:")
    for rel_type, count in sorted(type_counts.items(), key=lambda x: x[1], reverse=True):
        output_lines.append(f"  {rel_type}: {count}")

    # Domain analysis
    domain_relationships = defaultdict(lambda: defaultdict(int))
    for rel_type, rel_data in relationships.items():
        for source, targets in rel_data.items():
            source_domain = documents.get(source, {}).get('domain', 'unknown')
            for target in targets:
                target_domain = documents.get(target, {}).get('domain', 'unknown')
                domain_relationships[source_domain][target_domain] += 1

    output_lines.append("\nCross-domain relationships:")
    for source_domain, targets in domain_relationships.items():
        for target_domain, count in targets.items():
            if source_domain != target_domain:
                output_lines.append(f"  {source_domain} → {target_domain}: {count}")

    # Authority violations
    output_lines.append("\nAuthority violations (higher authority referencing lower):")
    violations_found = False

    for rel_type, rel_data in relationships.items():
        for source, targets in rel_data.items():
            source_auth = get_authority_level(source)
            for target in targets:
                target_auth = get_authority_level(target)
                if source_auth < target_auth and target in documents:  # Lower number = higher authority
                    output_lines.append(f"  ⚠️  {get_authority_name(source_auth)} '{source}' → {get_authority_name(target_auth)} '{target}'")
                    violations_found = True

    if not violations_found:
        output_lines.append("  ✓ No authority violations detected")

    # Bidirectional consistency check
    output_lines.append("\nBidirectional consistency:")
    consistency_issues = []

    # Check informs/depends_on pairs
    informs_sources = set()
    depends_targets = set()

    for source, targets in relationships.get('informs', {}).items():
        for target in targets:
            informs_sources.add((source, target))

    for source, targets in relationships.get('depends_on', {}).items():
        for target in targets:
            depends_targets.add((target, source))  # Reverse the relationship

    missing_reverse = informs_sources - depends_targets
    if missing_reverse:
        consistency_issues.extend([f"  ⚠️  Missing reverse: {source} informs {target} but {target} doesn't depend_on {source}" for source, target in missing_reverse])

    # Check implements/implemented_by pairs
    implements_sources = set()
    implemented_targets = set()

    for source, targets in relationships.get('implements', {}).items():
        for target in targets:
            implements_sources.add((source, target))

    for source, targets in relationships.get('implemented_by', {}).items():
        for target in targets:
            implemented_targets.add((target, source))  # Reverse the relationship

    missing_reverse = implements_sources - implemented_targets
    if missing_reverse:
        consistency_issues.extend([f"  ⚠️  Missing reverse: {source} implements {target} but {target} doesn't have implemented_by {source}" for source, target in missing_reverse])

    if consistency_issues:
        output_lines.extend(consistency_issues)
    else:
        output_lines.append("  ✓ All major bidirectional relationships are consistent")

    # Output
    output = "\n".join(output_lines)

    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"Relationship graph saved to {output_file}")
    else:
        print(output)

def generate_json_data(relationships, documents, output_file):
    """Generate JSON data for external visualization tools."""
    data = {
        'documents': documents,
        'relationships': dict(relationships)
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"JSON relationship data saved to {output_file}")

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Generate documentation relationship visualizations')
    parser.add_argument('--format', choices=['text', 'json'], default='text',
                       help='Output format (default: text)')
    parser.add_argument('--output', '-o', help='Output file path')
    parser.add_argument('--json-data', help='Also generate JSON data file')

    args = parser.parse_args()

    print("🔍 Collecting documentation relationships...")
    relationships, documents = collect_relationships()

    print(f"Found {len(documents)} documents with relationships")

    if args.format == 'text':
        generate_text_graph(relationships, documents, args.output)
    elif args.format == 'json':
        if not args.output:
            print("❌ Output file required for JSON format")
            sys.exit(1)
        generate_json_data(relationships, documents, args.output)

    if args.json_data:
        generate_json_data(relationships, documents, args.json_data)

if __name__ == '__main__':
    main()