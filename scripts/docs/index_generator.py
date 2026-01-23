#!/usr/bin/env python3
"""
Documentation Index Generator

Generates a precedence tree based on governed_by relationships.
"""

import yaml
import os
from pathlib import Path
from datetime import datetime
import argparse


class DocIndexGenerator:
    def __init__(self, docs_root="docs"):
        self.docs_root = Path(docs_root)
        self.docs = {}  # path -> {frontmatter, file_size, relationships}

    def load_docs(self):
        """Load all documents with frontmatter."""
        for md_file in self.docs_root.rglob("*.md"):
            frontmatter = self._parse_frontmatter(md_file)
            if not frontmatter:
                continue
            rel_path = str(md_file.relative_to(self.docs_root.parent))
            self.docs[rel_path] = {
                "frontmatter": frontmatter,
                "file_size": os.path.getsize(md_file),
                "relationships": self._process_relationships(frontmatter),
            }

    def _parse_frontmatter(self, md_file):
        """Parse YAML frontmatter from markdown file."""
        try:
            content = md_file.read_text(encoding="utf-8")
            if not content.startswith("---"):
                return None
            parts = content.split("---", 2)
            return yaml.safe_load(parts[1]) if len(parts) >= 3 else None
        except Exception:
            return None

    def _process_relationships(self, frontmatter):
        """Extract and standardize relationship types."""
        return {
            "governed_by": self._extract_rels(frontmatter.get("governed_by", {})),
            "governs": self._extract_rels(frontmatter.get("governs", {})),
            "implements": self._extract_rels(frontmatter.get("implements", {})),
            "implemented_by": self._extract_rels(frontmatter.get("implemented_by", {})),
            "related": self._extract_rels(frontmatter.get("related", {})),
        }

    def _extract_rels(self, rel_data):
        if isinstance(rel_data, dict):
            return list(rel_data.keys())
        if isinstance(rel_data, list):
            return rel_data
        return []

    def _format_size_kb(self, size_bytes):
        return f"{size_bytes / 1024:.1f} KB"

    def _normalize_filter_path(self, file_filter):
        if not file_filter:
            return None
        cleaned = file_filter.strip()
        if cleaned.startswith("./"):
            cleaned = cleaned[2:]
        if cleaned.startswith("docs/"):
            return cleaned
        buckets = {
            "reference",
            "how-to",
            "explanation",
            "tutorials",
            "work",
            "archive",
            "domains",
        }
        first_segment = cleaned.split("/", 1)[0]
        if first_segment in buckets:
            return f"docs/{cleaned}"
        return cleaned

    def _governed_by_targets(self, doc_path):
        rels = self.docs[doc_path]["relationships"].get("governed_by", [])
        return [t for t in rels if t in self.docs]

    def _select_parent(self, parents):
        if not parents:
            return None
        if len(parents) == 1:
            return parents[0]
        # Prefer parents that are themselves governed (non-root)
        non_root = [p for p in parents if self._governed_by_targets(p)]
        if non_root:
            return sorted(non_root)[0]
        return sorted(parents)[0]

    def _build_parent_map(self):
        parent_map = {}
        for doc_path in self.docs.keys():
            parents = self._governed_by_targets(doc_path)
            parent_map[doc_path] = self._select_parent(parents)
        return parent_map

    def _build_children_map(self, parent_map):
        children = {doc_path: [] for doc_path in self.docs.keys()}
        for doc_path, parent in parent_map.items():
            if parent:
                children[parent].append(doc_path)
        for parent in children:
            children[parent] = sorted(children[parent])
        return children

    def _find_roots(self, parent_map):
        roots = [doc for doc, parent in parent_map.items() if parent is None]
        return sorted(roots)

    def _render_implemented_by(self, doc_path, prefix, is_last):
        implemented_by = self.docs[doc_path]["relationships"].get("implemented_by", [])
        if not implemented_by:
            return []
        lines = []
        branch = "└──" if is_last else "├──"
        lines.append(f"{prefix}{branch} implemented_by")
        child_prefix = f"{prefix}{'    ' if is_last else '│   '}"
        for idx, target in enumerate(implemented_by):
            is_last_target = idx == len(implemented_by) - 1
            target_branch = "└──" if is_last_target else "├──"
            lines.append(f"{child_prefix}{target_branch} {target}")
        return lines

    def _render_tree(self, root, children_map, prefix="", seen=None):
        if seen is None:
            seen = set()
        lines = []
        size = self._format_size_kb(self.docs[root]["file_size"])
        lines.append(f"{prefix}{root} ({size})")

        if root in seen:
            lines.append(f"{prefix}└── [cycle]")
            return lines
        seen.add(root)

        children = children_map.get(root, [])
        has_impl = bool(self.docs[root]["relationships"].get("implemented_by"))
        entries = []
        if has_impl:
            entries.append(("implemented_by", None))
        for child in children:
            entries.append(("child", child))

        for idx, (kind, child) in enumerate(entries):
            is_last = idx == len(entries) - 1
            branch = "└──" if is_last else "├──"
            child_prefix = f"{prefix}{'    ' if is_last else '│   '}"

            if kind == "implemented_by":
                lines.extend(self._render_implemented_by(root, child_prefix, True))
                continue

            size_child = self._format_size_kb(self.docs[child]["file_size"])
            lines.append(f"{prefix}{branch} {child} ({size_child})")
            subtree_prefix = f"{prefix}{'    ' if is_last else '│   '}"
            lines.extend(self._render_tree(child, children_map, subtree_prefix, seen.copy())[1:])

        return lines

    def _render_tree_with_branch(self, root, children_map, prefix, branch):
        """Render a subtree with an explicit branch prefix for the root line."""
        lines = self._render_tree(root, children_map, prefix + ("    " if branch == "└──" else "│   "))
        if not lines:
            return []
        root_line = lines[0].lstrip()
        lines[0] = f"{prefix}{branch} {root_line}"
        return lines

    def generate_index(self, domain_filter=None, file_filter=None):
        output = []
        normalized_filter = self._normalize_filter_path(file_filter)
        output.append("")

        parent_map = self._build_parent_map()
        children_map = self._build_children_map(parent_map)
        roots = self._find_roots(parent_map)

        if normalized_filter:
            roots = [normalized_filter] if normalized_filter in self.docs else []

        reachable = set()
        if len(roots) == 1:
            root = roots[0]
            lines = self._render_tree(root, children_map)
            output.extend(lines)
            output.append("")
            stack = [root]
            while stack:
                node = stack.pop()
                if node in reachable:
                    continue
                reachable.add(node)
                for child in children_map.get(node, []):
                    stack.append(child)
        elif len(roots) > 1:
            output.append("ROOT")
            for idx, root in enumerate(roots):
                is_last = idx == len(roots) - 1
                branch = "└──" if is_last else "├──"
                output.extend(self._render_tree_with_branch(root, children_map, "", branch))
            output.append("")
            for root in roots:
                stack = [root]
                while stack:
                    node = stack.pop()
                    if node in reachable:
                        continue
                    reachable.add(node)
                    for child in children_map.get(node, []):
                        stack.append(child)

        if not normalized_filter:
            unlinked = sorted([p for p in self.docs.keys() if p not in reachable])
            if unlinked:
                output.append("Unlinked")
                for doc_path in unlinked:
                    size = self._format_size_kb(self.docs[doc_path]["file_size"])
                    output.append(f"- {doc_path} ({size})")
                output.append("")

        output.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(description="Generate documentation index")
    parser.add_argument("--domain", help="Filter by domain")
    parser.add_argument("--filter", help="Filter to show contexts for specific file")
    parser.add_argument("--validate", action="store_true", help="Validate relationships and exit")

    args = parser.parse_args()

    generator = DocIndexGenerator()
    generator.load_docs()

    if args.validate:
        total_docs = len(generator.docs)
        total_relationships = sum(
            len(doc_data["relationships"]["governed_by"])
            + len(doc_data["relationships"]["governs"])
            + len(doc_data["relationships"]["implements"])
            + len(doc_data["relationships"]["implemented_by"])
            + len(doc_data["relationships"]["related"])
            for doc_data in generator.docs.values()
        )
        print("Frontmatter validation passed")
        print(f"Loaded {total_docs} documents")
        print(f"Found {total_relationships} relationships")
        return

    print(generator.generate_index(args.domain, args.filter))


if __name__ == "__main__":
    main()
