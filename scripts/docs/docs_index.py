#!/usr/bin/env python3
"""Generate a precedence tree for docs based on governed_by relationships."""

import argparse
from datetime import datetime
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from scripts.docs.docs_api import DocsRepository
from scripts.docs.utils import format_size_kb, normalize_filter_path


def select_parent(repo, parents):
    if not parents:
        return None
    if len(parents) == 1:
        return parents[0]
    non_root = [p for p in parents if repo.governed_by_targets(p)]
    if non_root:
        return sorted(non_root)[0]
    return sorted(parents)[0]


def build_parent_map(repo):
    parent_map = {}
    for doc_path in repo.get_docs().keys():
        parents = repo.governed_by_targets(doc_path)
        parent_map[doc_path] = select_parent(repo, parents)
    return parent_map


def build_children_map(parent_map):
    children = {doc_path: [] for doc_path in parent_map.keys()}
    for doc_path, parent in parent_map.items():
        if parent:
            children[parent].append(doc_path)
    for parent in children:
        children[parent] = sorted(children[parent])
    return children


def find_roots(parent_map):
    roots = [doc for doc, parent in parent_map.items() if parent is None]
    return sorted(roots)


def render_implemented_by(repo, doc_path, prefix, is_last):
    implemented_by = repo.get_docs()[doc_path]["relationships"].get("implemented_by", [])
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


def render_tree(repo, root, children_map, prefix="", seen=None):
    if seen is None:
        seen = set()
    lines = []
    size = format_size_kb(repo.get_docs()[root]["file_size"])
    lines.append(f"{prefix}{root} ({size})")

    if root in seen:
        lines.append(f"{prefix}└── [cycle]")
        return lines
    seen.add(root)

    children = children_map.get(root, [])
    has_impl = bool(repo.get_docs()[root]["relationships"].get("implemented_by"))
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
            lines.extend(render_implemented_by(repo, root, child_prefix, True))
            continue

        size_child = format_size_kb(repo.get_docs()[child]["file_size"])
        lines.append(f"{prefix}{branch} {child} ({size_child})")
        subtree_prefix = f"{prefix}{'    ' if is_last else '│   '}"
        lines.extend(render_tree(repo, child, children_map, subtree_prefix, seen.copy())[1:])

    return lines


def render_tree_with_branch(repo, root, children_map, prefix, branch):
    lines = render_tree(repo, root, children_map, prefix + ("    " if branch == "└──" else "│   "))
    if not lines:
        return []
    root_line = lines[0].lstrip()
    lines[0] = f"{prefix}{branch} {root_line}"
    return lines


def generate_index(repo, file_filter=None):
    output = [""]

    parent_map = build_parent_map(repo)
    children_map = build_children_map(parent_map)
    roots = find_roots(parent_map)

    if file_filter:
        roots = [file_filter] if file_filter in repo.get_docs() else []

    reachable = set()
    if len(roots) == 1:
        root = roots[0]
        lines = render_tree(repo, root, children_map)
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
            output.extend(render_tree_with_branch(repo, root, children_map, "", branch))
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

    if not file_filter:
        unlinked = sorted([p for p in repo.get_docs().keys() if p not in reachable])
        if unlinked:
            output.append("Unlinked")
            for doc_path in unlinked:
                size = format_size_kb(repo.get_docs()[doc_path]["file_size"])
                output.append(f"- {doc_path} ({size})")
            output.append("")

    output.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(description="Generate documentation index")
    parser.add_argument("--filter", help="Filter to show contexts for specific file")
    args = parser.parse_args()

    repo = DocsRepository()
    repo.load_docs(include_drafts=False)

    normalized = normalize_filter_path(args.filter)
    print(generate_index(repo, normalized))


if __name__ == "__main__":
    main()
