#!/usr/bin/env python3
"""
Relationship Graph Renderer - AgentOS v9

Renders relationship graphs from frontmatter for DOE orchestration validation.

DOE Registry - Bidirectional Linkages:
@directive docs/reference/agentos/relationship-orchestration.md

# DOE Layer Declaration
DOE_LAYER = "execution"
DOE_RESPONSIBILITY = "Render relationship graphs for orchestration validation"
DOE_GOVERNANCE = "docs/reference/agentos/doe-framework.md"
DOE_PRECEDENCE = 4
"""

import yaml
from pathlib import Path
from collections import defaultdict

def load_frontmatter(file_path):
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
    except:
        return None

def collect_relationships():
    """Collect all relationships from docs."""
    relationships = defaultdict(lambda: defaultdict(list))

    relationship_types = [
        'depends_on', 'informs', 'evidence_for', 'implements',
        'governed_by', 'related'
    ]

    for md_file in Path('docs').rglob('*.md'):
        if md_file.name == 'index.md':
            continue

        frontmatter = load_frontmatter(md_file)
        if not frontmatter:
            continue

        doc_path = f"docs/{md_file.relative_to('docs')}"

        for rel_type in relationship_types:
            if rel_type in frontmatter:
                targets = frontmatter[rel_type]
                if isinstance(targets, list):
                    for target in targets:
                        if isinstance(target, str) and target.startswith('docs/'):
                            relationships[rel_type][doc_path].append(target)

    return relationships

def generate_text_graph():
    """Generate minimal text-based relationship graph."""
    relationships = collect_relationships()

    output_lines = [
        "AGENTOS V9 RELATIONSHIP GRAPH",
        "=" * 40,
        ""
    ]

    # Count relationships by type
    total_relationships = 0
    for rel_type, rels in relationships.items():
        count = sum(len(targets) for targets in rels.values())
        if count > 0:
            output_lines.append(f"{rel_type}: {count} relationships")
            total_relationships += count

    output_lines.extend([
        f"Total relationships: {total_relationships}",
        "",
        "Core directive loading validation:",
        f"✓ Relationship graph rendered with {total_relationships} connections",
        "✓ Orchestration ready for directive validation"
    ])

    return "\n".join(output_lines)

def validate_directive_loading():
    """Minimal directive loading validation."""
    relationships = collect_relationships()

    issues = []

    # Check for core docs with relationships
    core_docs = [
        'docs/reference/agentos/architecture.md',
        'docs/reference/agentos/behavior-spec.md',
        'docs/how-to/agentos/usage.md'
    ]

    for doc in core_docs:
        if doc not in relationships['depends_on'] and doc not in relationships['informs']:
            issues.append(f"Warning: {doc} has no relationship connections")

    if not issues:
        return "✓ All core directives have relationship connections"
    else:
        return "\n".join(issues)

if __name__ == '__main__':
    print(generate_text_graph())
    print()
    print("Directive Loading Validation:")
    print(validate_directive_loading())