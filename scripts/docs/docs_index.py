#!/usr/bin/env python3
"""Render a governed_by graph as a branching tree."""

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from scripts.docs.docs_api import DocsRepository
from scripts.docs.utils import format_size_kb, normalize_filter_path


def render_implemented_by(repo, node, prefix, is_last):
    implemented_by = repo.get_docs()[node]["relationships"].get("implemented_by", [])
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


def render_child(repo, node, prefix, is_last, stack, child_map):
    branch = "└──" if is_last else "├──"
    line_prefix = f"{prefix}{branch} "
    size = format_size_kb(repo.get_docs()[node]["file_size"])

    if node in stack:
        return [f"{line_prefix}{node} ({size}) [cycle]"]

    lines = [f"{line_prefix}{node} ({size})"]
    stack.add(node)

    children = sorted(child_map.get(node, []))
    has_impl = bool(repo.get_docs()[node]["relationships"].get("implemented_by"))
    entries = []
    if has_impl:
        entries.append(("implemented_by", None))
    for child in children:
        entries.append(("child", child))

    child_prefix = f"{prefix}{'    ' if is_last else '│   '}"
    for idx, (kind, child) in enumerate(entries):
        child_is_last = idx == len(entries) - 1
        if kind == "implemented_by":
            lines.extend(render_implemented_by(repo, node, child_prefix, child_is_last))
            continue
        lines.extend(render_child(repo, child, child_prefix, child_is_last, stack, child_map))

    stack.remove(node)
    return lines


def render_tree(repo, root, child_map):
    size = format_size_kb(repo.get_docs()[root]["file_size"])
    lines = [f"{root} ({size})"]
    stack = {root}

    children = sorted(child_map.get(root, []))
    has_impl = bool(repo.get_docs()[root]["relationships"].get("implemented_by"))
    entries = []
    if has_impl:
        entries.append(("implemented_by", None))
    for child in children:
        entries.append(("child", child))

    for idx, (kind, child) in enumerate(entries):
        is_last = idx == len(entries) - 1
        if kind == "implemented_by":
            lines.extend(render_implemented_by(repo, root, "", is_last))
            continue
        lines.extend(render_child(repo, child, "", is_last, stack, child_map))

    return lines


def main():
    parser = argparse.ArgumentParser(description="Render governed_by graph from entrypoint")
    parser.add_argument("--from", dest="entry", help="Entrypoint doc path")
    args = parser.parse_args()

    repo = DocsRepository()
    repo.load_docs(include_drafts=False)

    if args.entry:
        entry = normalize_filter_path(args.entry)
        if entry not in repo.get_docs():
            print(f"Entry not found in docs: {entry}")
            sys.exit(1)
        child_map = {}
        for doc_path in repo.get_docs().keys():
            child_map[doc_path] = repo.governed_by_targets(doc_path)
        print("\n".join(render_tree(repo, entry, child_map)))
        return

    reverse_map = {path: [] for path in repo.get_docs().keys()}
    for path in repo.get_docs().keys():
        for parent in repo.governed_by_targets(path):
            reverse_map[parent].append(path)

    roots = [path for path in repo.get_docs().keys() if not repo.governed_by_targets(path)]
    for idx, root in enumerate(sorted(roots)):
        if idx:
            print("")
        print("\n".join(render_tree(repo, root, reverse_map)))


if __name__ == "__main__":
    main()
