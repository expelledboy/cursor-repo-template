#!/usr/bin/env python3
"""Validate docs frontmatter, relationships, and file links.

@implements docs/system/governance.md
@implements docs/system/intent-model.md
@implements docs/system/intent-task-matrix.md
@implements docs/system/task-model.md
@implements docs/system/model/problem-doc.md
@implements docs/system/model/decision-doc.md
@implements docs/system/model/procedure-doc.md
@implements docs/system/model/domain-doc.md
@implements docs/system/procedure/validating-doc-contracts.md
"""

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from scripts.docs.docs_api import DocsRepository
from scripts.docs.utils import normalize_filter_path, repo_path_exists
from scripts.docs.contract_specs import (
    ALLOWED_DOC_STATUS,
    ALLOWED_DOMAIN_STATUS,
    ALLOWED_INTENTS,
    DECISION_STATUS_VALUES,
    TASK_VALUES,
    INTENT_TASK_MATRIX,
)


def validate_required_frontmatter(repo):
    errors = []
    for path, data in repo.get_docs().items():
        fm = data["frontmatter"]
        if "doc_status" not in fm or not str(fm.get("doc_status")).strip():
            errors.append(f"{path}: missing frontmatter field 'doc_status'")
        if "purpose" not in fm or not str(fm.get("purpose")).strip():
            errors.append(f"{path}: missing frontmatter field 'purpose'")
        if "intent" not in fm or not str(fm.get("intent")).strip():
            errors.append(f"{path}: missing frontmatter field 'intent'")
    return errors


def validate_doc_status(repo):
    errors = []
    for path, data in repo.get_docs().items():
        value = str(data["frontmatter"].get("doc_status", "")).strip().lower()
        if value and value not in ALLOWED_DOC_STATUS:
            errors.append(f"{path}: invalid doc_status '{value}'")
    return errors


def validate_intent(repo):
    errors = []
    for path, data in repo.get_docs().items():
        value = str(data["frontmatter"].get("intent", "")).strip().lower()
        if value and value not in ALLOWED_INTENTS:
            errors.append(f"{path}: invalid intent '{value}'")
    return errors


def validate_decision_frontmatter(repo):
    errors = []
    for path, data in repo.get_docs().items():
        fm = data["frontmatter"]
        if str(fm.get("intent", "")).strip().lower() != "decision":
            continue
        status = str(fm.get("decision_status", "")).strip().lower()
        if not status:
            errors.append(f"{path}: missing frontmatter field 'decision_status'")
        elif status not in DECISION_STATUS_VALUES:
            errors.append(f"{path}: invalid decision_status '{status}'")
        decision_date = str(fm.get("decision_date", "")).strip()
        if not decision_date:
            errors.append(f"{path}: missing frontmatter field 'decision_date'")
        else:
            parts = decision_date.split("-")
            if len(parts) != 3 or any(len(p) != l for p, l in zip(parts, (4, 2, 2))):
                errors.append(f"{path}: decision_date must be YYYY-MM-DD")
    return errors


def validate_task_values(repo):
    errors = []
    for path, data in repo.get_docs().items():
        if path != "docs/system/task-model.md":
            continue
        content = Path(ROOT / path).read_text(encoding="utf-8")
        for task in TASK_VALUES:
            if f"`{task}`" not in content:
                errors.append(f"{path}: missing task '{task}' in body")
    return errors


def validate_intent_task_matrix(repo):
    errors = []
    path = "docs/system/intent-task-matrix.md"
    if path not in repo.get_docs():
        return errors
    content = Path(ROOT / path).read_text(encoding="utf-8")
    for task, intents in INTENT_TASK_MATRIX.items():
        for intent in intents:
            if f"`{task}`" in content and f"`{intent}`" not in content:
                errors.append(f"{path}: missing intent '{intent}' for task '{task}'")
    return errors


def validate_domain_docs(repo):
    errors = []
    for path, data in repo.get_docs().items():
        if not path.startswith("docs/domains/"):
            continue
        fm = data["frontmatter"]
        intent = str(fm.get("intent", "")).strip().lower()
        if intent != "facts":
            errors.append(f"{path}: domain docs must use intent 'facts'")
        domain_id = str(fm.get("domain_id", "")).strip()
        if not domain_id:
            errors.append(f"{path}: missing frontmatter field 'domain_id'")
        domain_scope = str(fm.get("domain_scope", "")).strip()
        if not domain_scope:
            errors.append(f"{path}: missing frontmatter field 'domain_scope'")
        domain_status = str(fm.get("domain_status", "")).strip().lower()
        if not domain_status:
            errors.append(f"{path}: missing frontmatter field 'domain_status'")
        elif domain_status not in ALLOWED_DOMAIN_STATUS:
            errors.append(f"{path}: invalid domain_status '{domain_status}'")
        governed_by = data["relationships"].get("governed_by", [])
        if "docs/system/model/domain-doc.md" not in governed_by:
            errors.append(f"{path}: missing governed_by docs/system/model/domain-doc.md")
    return errors


def validate_doc_code_links(repo):
    errors = []
    for path, data in repo.get_docs().items():
        implemented_by = data["relationships"].get("implemented_by", [])
        if not implemented_by:
            continue
        for target in implemented_by:
            if not repo_path_exists(target):
                continue
            if target.startswith("docs/") or target.endswith(".md") or target.endswith(".mdc"):
                continue
            target_path = ROOT / target
            if not target_path.is_file():
                continue
            content = target_path.read_text(encoding="utf-8", errors="replace")
            marker = f"@implements {path}"
            if marker not in content:
                errors.append(f"{path}: implemented_by {target} missing '{marker}'")
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
    errors.extend(validate_doc_status(repo))
    errors.extend(validate_intent(repo))
    errors.extend(validate_decision_frontmatter(repo))
    errors.extend(validate_task_values(repo))
    errors.extend(validate_intent_task_matrix(repo))
    errors.extend(validate_domain_docs(repo))
    errors.extend(validate_doc_code_links(repo))
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
