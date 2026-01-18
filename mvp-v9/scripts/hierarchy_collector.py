#!/usr/bin/env python3
"""
Hierarchy Evidence Collector - AgentOS v9

Collects evidence about authoritative hierarchy and precedence relationships.
Provides structured data for intelligent analysis of governance flow and precedence compliance.

DOE Declaration:
- DOE_LAYER: execution
- DOE_RESPONSIBILITY: Collect evidence about authoritative hierarchy and precedence
- DOE_GOVERNANCE: docs/reference/agentos/doe-framework.md
- DOE_PRECEDENCE: 4
"""

import sys
import json
from pathlib import Path
from typing import Dict, List, Any, Optional

# DOE Layer Declaration
DOE_LAYER = "execution"
DOE_RESPONSIBILITY = "Collect evidence about authoritative hierarchy and precedence"
DOE_GOVERNANCE = "docs/reference/agentos/doe-framework.md"
DOE_PRECEDENCE = 4

class HierarchyEvidenceCollector:
    """Collects evidence about authoritative hierarchy and precedence relationships."""

    def __init__(self):
        self.project_root = Path(__file__).parent.parent
        self.docs_dir = self.project_root / "docs"

    def get_hierarchy_evidence(self) -> Dict[str, Any]:
        """Collect comprehensive hierarchy evidence."""
        return {
            "timestamp": self._get_timestamp(),
            "precedence_declarations": self._collect_precedence_declarations(),
            "governance_relationships": self._collect_governance_relationships(),
            "authority_levels": self._collect_authority_levels(),
            "hierarchy_flow_evidence": self._collect_hierarchy_flow_evidence(),
            "doe_compliance": self._collect_doe_compliance_evidence()
        }

    def _get_timestamp(self) -> str:
        """Get current timestamp."""
        from datetime import datetime
        return datetime.now().isoformat()

    def _collect_precedence_declarations(self) -> Dict[str, Any]:
        """Collect all doe_precedence declarations."""
        precedence_data = {}

        # Collect from docs
        if self.docs_dir.exists():
            for md_file in self.docs_dir.rglob("*.md"):
                if md_file.name == 'index.md':
                    continue

                frontmatter = self._load_frontmatter(md_file)
                if frontmatter and 'doe_precedence' in frontmatter:
                    doc_path = f"docs/{md_file.relative_to(self.docs_dir)}"
                    precedence_data[doc_path] = {
                        "precedence_level": frontmatter['doe_precedence'],
                        "authority_level": frontmatter.get('authority_level'),
                        "doe_layer": frontmatter.get('doe_layer')
                    }

        # Collect from scripts
        scripts_dir = self.project_root / "scripts"
        if scripts_dir.exists():
            for py_file in scripts_dir.glob("*.py"):
                content = py_file.read_text()
                precedence_match = self._extract_constant_value(content, "DOE_PRECEDENCE")
                if precedence_match is not None:
                    script_path = f"scripts/{py_file.name}"
                    precedence_data[script_path] = {
                        "precedence_level": precedence_match,
                        "doe_layer": self._extract_constant_value(content, "DOE_LAYER"),
                        "governance": self._extract_constant_value(content, "DOE_GOVERNANCE")
                    }

        # Collect from src
        src_dir = self.project_root / "src"
        if src_dir.exists():
            for py_file in src_dir.glob("*.py"):
                content = py_file.read_text()
                precedence_match = self._extract_constant_value(content, "DOE_PRECEDENCE")
                if precedence_match is not None:
                    src_path = f"src/{py_file.name}"
                    precedence_data[src_path] = {
                        "precedence_level": precedence_match,
                        "doe_layer": self._extract_constant_value(content, "DOE_LAYER"),
                        "governance": self._extract_constant_value(content, "DOE_GOVERNANCE")
                    }

        return precedence_data

    def _collect_governance_relationships(self) -> Dict[str, Any]:
        """Collect all governance relationships (governs/governed_by)."""
        relationships = {
            "governs": {},
            "governed_by": {}
        }

        # Collect from docs
        if self.docs_dir.exists():
            for md_file in self.docs_dir.rglob("*.md"):
                if md_file.name == 'index.md':
                    continue

                frontmatter = self._load_frontmatter(md_file)
                if not frontmatter:
                    continue

                doc_path = f"docs/{md_file.relative_to(self.docs_dir)}"

                if 'governs' in frontmatter:
                    relationships["governs"][doc_path] = frontmatter['governs']

                if 'governed_by' in frontmatter:
                    relationships["governed_by"][doc_path] = frontmatter['governed_by']

        return relationships

    def _collect_authority_levels(self) -> Dict[str, Any]:
        """Collect authority level declarations."""
        authority_data = {}

        if self.docs_dir.exists():
            for md_file in self.docs_dir.rglob("*.md"):
                if md_file.name == 'index.md':
                    continue

                frontmatter = self._load_frontmatter(md_file)
                if frontmatter and 'authority_level' in frontmatter:
                    doc_path = f"docs/{md_file.relative_to(self.docs_dir)}"
                    authority_data[doc_path] = frontmatter['authority_level']

        return authority_data

    def _collect_hierarchy_flow_evidence(self) -> Dict[str, Any]:
        """Collect evidence about information flow in hierarchy."""
        flow_evidence = {
            "precedence_distribution": {},
            "authority_distribution": {},
            "layer_distribution": {}
        }

        precedence_data = self._collect_precedence_declarations()

        # Analyze precedence distribution
        precedence_counts = {}
        for item_data in precedence_data.values():
            level = item_data.get('precedence_level')
            if level is not None:
                precedence_counts[level] = precedence_counts.get(level, 0) + 1

        flow_evidence["precedence_distribution"] = precedence_counts

        # Analyze authority distribution
        authority_counts = {}
        for item_data in precedence_data.values():
            level = item_data.get('authority_level')
            if level is not None:
                authority_counts[str(level)] = authority_counts.get(str(level), 0) + 1

        flow_evidence["authority_distribution"] = authority_counts

        # Analyze layer distribution
        layer_counts = {}
        for item_data in precedence_data.values():
            layer = item_data.get('doe_layer')
            if layer:
                layer_counts[layer] = layer_counts.get(layer, 0) + 1

        flow_evidence["layer_distribution"] = layer_counts

        return flow_evidence

    def _collect_doe_compliance_evidence(self) -> Dict[str, Any]:
        """Collect evidence about DOE compliance."""
        compliance_evidence = {
            "layer_declarations": {},
            "governance_completeness": {},
            "precedence_completeness": {}
        }

        precedence_data = self._collect_precedence_declarations()

        # Count layer declarations
        layer_counts = {}
        for item_data in precedence_data.values():
            layer = item_data.get('doe_layer')
            if layer:
                layer_counts[layer] = layer_counts.get(layer, 0) + 1

        compliance_evidence["layer_declarations"] = layer_counts

        # Count governance completeness
        governance_count = 0
        total_items = 0
        for item_data in precedence_data.values():
            total_items += 1
            if item_data.get('governance'):
                governance_count += 1

        compliance_evidence["governance_completeness"] = {
            "declared_governance": governance_count,
            "total_items": total_items
        }

        # Count precedence completeness
        precedence_count = 0
        for item_data in precedence_data.values():
            if item_data.get('precedence_level') is not None:
                precedence_count += 1

        compliance_evidence["precedence_completeness"] = {
            "declared_precedence": precedence_count,
            "total_items": total_items
        }

        return compliance_evidence

    def _load_frontmatter(self, file_path: Path) -> Optional[Dict]:
        """Load YAML frontmatter from markdown file."""
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
        except:
            return None

    def _extract_constant_value(self, content: str, constant_name: str) -> Optional[Any]:
        """Extract constant value from Python code."""
        import re

        # Look for patterns like: CONSTANT_NAME = value
        # Handle strings, numbers, etc.
        pattern = rf'{constant_name}\s*=\s*([^#\n]+)'
        match = re.search(pattern, content)
        if match:
            value_str = match.group(1).strip()
            # Remove quotes if present
            if (value_str.startswith('"') and value_str.endswith('"')) or \
               (value_str.startswith("'") and value_str.endswith("'")):
                return value_str[1:-1]
            # Try to convert to int/float
            try:
                return int(value_str)
            except ValueError:
                try:
                    return float(value_str)
                except ValueError:
                    return value_str

        return None


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Collect evidence about authoritative hierarchy and precedence"
    )
    parser.add_argument(
        "evidence_type",
        choices=["hierarchy", "precedence", "governance", "authority", "compliance"],
        help="Type of hierarchy evidence to collect"
    )
    parser.add_argument(
        "--output", "-o",
        choices=["text", "json"],
        default="text",
        help="Output format"
    )

    args = parser.parse_args()

    collector = HierarchyEvidenceCollector()
    evidence = {}  # Initialize evidence

    if args.evidence_type == "hierarchy":
        evidence = collector.get_hierarchy_evidence()
    elif args.evidence_type == "precedence":
        evidence = collector._collect_precedence_declarations()
    elif args.evidence_type == "governance":
        evidence = collector._collect_governance_relationships()
    elif args.evidence_type == "authority":
        evidence = collector._collect_authority_levels()
    elif args.evidence_type == "compliance":
        evidence = collector._collect_doe_compliance_evidence()

    if args.output == "json":
        print(json.dumps(evidence, indent=2))
    else:
        print(f"🔍 Hierarchy Evidence: {args.evidence_type.upper()}")
        print("=" * 50)
        print(json.dumps(evidence, indent=2))


if __name__ == "__main__":
    main()