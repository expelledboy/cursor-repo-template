#!/usr/bin/env python3
"""Validate docs frontmatter, relationships, and file links."""

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from scripts.docs.docs_api import DocsRepository
from scripts.docs.utils import normalize_filter_path, repo_path_exists


def validate_required_frontmatter(repo):
    errors = []
    for path, data in repo.get_docs().items():
        fm = data["frontmatter"]
        if "status" not in fm or not str(fm.get("status")).strip():
            errors.append(f"{path}: missing frontmatter field 'status'")
        if "purpose" not in fm or not str(fm.get("purpose")).strip():
            errors.append(f"{path}: missing frontmatter field 'purpose'")
    return errors


def validate_paths_exist(repo):
    errors = []
    for path, data in repo.get_docs().items():
        rels = data["relationships"]
        for rel_type, targets in rels.items():
            for target in targets:
                if not repo_path_exists(target):
                    errors.append(f"{path}: {rel_type} target does not exist: {target}")
    return errors


def validate_bidirectional(repo):
    errors = []
    docs = repo.get_docs()

    def has_link(src, rel_type, target):
        return target in docs[src]["relationships"].get(rel_type, [])

    for path, data in docs.items():
        rels = data["relationships"]
        for target in rels.get("governs", []):
            if target in docs and not has_link(target, "governed_by", path):
                errors.append(f"{path}: governs {target} but reverse governed_by missing")
        for target in rels.get("governed_by", []):
            if target in docs and not has_link(target, "governs", path):
                errors.append(f"{path}: governed_by {target} but reverse governs missing")
        for target in rels.get("implements", []):
            if target in docs and not has_link(target, "implemented_by", path):
                errors.append(f"{path}: implements {target} but reverse implemented_by missing")
        for target in rels.get("implemented_by", []):
            if target in docs and not has_link(target, "implements", path):
                errors.append(f"{path}: implemented_by {target} but reverse implements missing")
        for target in rels.get("related", []):
            if target in docs and not has_link(target, "related", path):
                errors.append(f"{path}: related {target} but reverse related missing")

    return errors


def main():
    parser = argparse.ArgumentParser(description="Validate documentation frontmatter and links")
    parser.add_argument("--filter", help="Validate a specific doc")
    args = parser.parse_args()

    repo = DocsRepository()
    repo.load_docs(include_drafts=True)

    normalized = normalize_filter_path(args.filter)
    if normalized and normalized in repo.get_docs():
        repo.docs = {normalized: repo.get_docs()[normalized]}

    errors = []
    errors.extend(validate_required_frontmatter(repo))
    errors.extend(validate_paths_exist(repo))
    errors.extend(validate_bidirectional(repo))

    if errors:
        print("Validation failed")
        for err in errors:
            print(f"- {err}")
        raise SystemExit(1)

    print("Validation passed")


if __name__ == "__main__":
    main()
