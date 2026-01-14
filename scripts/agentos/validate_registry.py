#!/usr/bin/env python3
# @directive docs/reference/agentos/validation-scripts.md

import os
import re
import sys
from glob import glob

SCOPE_HEADER = "## Registry Scope"


def read_registry_scope(path):
    scope = []
    in_scope = False
    with open(path, "r", encoding="utf-8", errors="ignore") as fh:
        for line in fh:
            line = line.rstrip("\n")
            if line.startswith(SCOPE_HEADER):
                in_scope = True
                continue
            if in_scope and line.startswith("## "):
                break
            if in_scope and line.startswith("- "):
                token = line[2:].strip()
                match = re.search(r"`([^`]+)`", token)
                if match:
                    scope.append(match.group(1))
                else:
                    scope.append(token)
    return [s for s in scope if s]


def clean_path(raw):
    raw = raw.strip().strip("\"'")
    raw = re.sub(r"[^A-Za-z0-9_./-]+$", "", raw)
    raw = raw.lstrip("./")
    return raw


def read_text(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as fh:
        return fh.read()


def main():
    if not os.path.isfile("AGENTS.md"):
        print("Missing AGENTS.md")
        return 1

    scope = read_registry_scope("AGENTS.md")
    if not scope:
        print("Registry Scope is missing or empty in AGENTS.md")
        return 1

    files = []
    missing_patterns = []
    for pattern in scope:
        pattern = pattern.lstrip("./")
        matches = glob(pattern, recursive=True)
        if not matches:
            missing_patterns.append(pattern)
            continue
        files.extend(matches)

    if not files:
        print("No files matched registry scope patterns")
        return 1

    files = sorted({f[2:] if f.startswith("./") else f for f in files})
    missing_annotations = []
    directive_pairs = []
    implementation_pairs = []

    for file_path in files:
        if "__pycache__" in file_path or file_path.endswith(".pyc"):
            continue
        try:
            text = read_text(file_path)
        except OSError:
            continue
        has_annotation = False
        for match in re.finditer(r"@directive\s+(\S+)", text):
            has_annotation = True
            directive_pairs.append((file_path, clean_path(match.group(1))))
        for match in re.finditer(r"@implementation\s+(\S+)", text):
            has_annotation = True
            implementation_pairs.append((file_path, clean_path(match.group(1))))
        if not has_annotation:
            missing_annotations.append(file_path)

    broken_links = []
    mismatches = []

    for code_path, doc_path in directive_pairs:
        if not doc_path:
            continue
        if not os.path.exists(doc_path):
            broken_links.append(f"{code_path} -> {doc_path} (missing doc)")
            continue
        doc_text = read_text(doc_path)
        if not re.search(r"@implementation\s+" + re.escape(code_path), doc_text):
            mismatches.append(f"{code_path} -> {doc_path} (missing @implementation)")

    for doc_path, code_path in implementation_pairs:
        if not code_path:
            continue
        if not os.path.exists(code_path):
            broken_links.append(f"{doc_path} -> {code_path} (missing code)")
            continue
        code_text = read_text(code_path)
        if not re.search(r"@directive\s+" + re.escape(doc_path), code_text):
            mismatches.append(f"{doc_path} -> {code_path} (missing @directive)")

    errors = False
    if missing_patterns:
        print("Registry scope patterns with no matches:")
        for pattern in missing_patterns:
            print(f"  - {pattern}")
        errors = True
    if missing_annotations:
        print("Files missing registry annotations:")
        for item in missing_annotations:
            print(f"  - {item}")
        errors = True
    if broken_links:
        print("Broken registry links:")
        for item in broken_links:
            print(f"  - {item}")
        errors = True
    if mismatches:
        print("Bidirectional mismatches:")
        for item in mismatches:
            print(f"  - {item}")
        errors = True

    if errors:
        return 1

    print(f"Registry validation passed ({len(files)} files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
