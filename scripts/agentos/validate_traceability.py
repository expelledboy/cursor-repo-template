#!/usr/bin/env python3
# @directive docs/reference/agentos/validation-scripts.md

import os
import sys

from validation_utils import (
    extract_backtick_paths,
    list_markdown_files,
    parse_markdown_table,
    read_lines,
)

PROBLEM_REGISTRY_PATH = "docs/reference/agentos/problem-registry.md"
TRACEABILITY_PATH = "docs/reference/agentos/traceability.md"
DECISIONS_DIR = "docs/explanation/agentos/decisions"


def load_problem_ids():
    lines = read_lines(PROBLEM_REGISTRY_PATH)
    headers, rows = parse_markdown_table(lines, "ID")
    if not headers or "ID" not in headers or "Status" not in headers:
        return None, None
    all_ids = set()
    validated = set()
    for row in rows:
        pid = row.get("ID", "").strip()
        if not pid.startswith("PRB-"):
            continue
        all_ids.add(pid)
        status = row.get("Status", "").strip().lower()
        if status == "validated":
            validated.add(pid)
    return all_ids, validated


def load_traceability():
    lines = read_lines(TRACEABILITY_PATH)
    headers, rows = parse_markdown_table(lines, "Problem ID")
    if not headers or "Problem ID" not in headers:
        return None, None, None, None
    trace_ids = set()
    decision_paths = set()
    artifact_paths = set()
    blank_problem_rows = 0
    for row in rows:
        pid = row.get("Problem ID", "").strip()
        if pid:
            trace_ids.add(pid)
        else:
            blank_problem_rows += 1
        decisions = extract_backtick_paths(row.get("Decision Record", ""))
        artifacts = extract_backtick_paths(row.get("Artifacts", ""))
        for item in decisions:
            if item:
                decision_paths.add(item)
        for item in artifacts:
            if item:
                artifact_paths.add(item)
    return trace_ids, decision_paths, artifact_paths, blank_problem_rows


def main():
    required = [PROBLEM_REGISTRY_PATH, TRACEABILITY_PATH, DECISIONS_DIR]
    missing = [path for path in required if not os.path.exists(path)]
    if missing:
        print("Missing required files or directories:")
        for path in missing:
            print(f"  - {path}")
        return 1

    all_ids, validated_ids = load_problem_ids()
    if all_ids is None:
        print("Unable to parse problem registry table")
        return 1

    trace_ids, decision_paths, artifact_paths, blank_problem_rows = load_traceability()
    if trace_ids is None:
        print("Unable to parse traceability table")
        return 1

    decision_files = {
        os.path.relpath(path, ".")
        for path in list_markdown_files(DECISIONS_DIR)
    }

    missing_validated = sorted(validated_ids - trace_ids)
    unknown_trace = sorted(trace_ids - all_ids)
    missing_decisions = sorted(decision_files - decision_paths)
    missing_files = sorted(path for path in decision_paths if not os.path.exists(path))
    missing_artifacts = sorted(path for path in artifact_paths if not os.path.exists(path))

    errors = False
    if missing_validated:
        print("Validated problems missing from traceability:")
        for item in missing_validated:
            print(f"  - {item}")
        errors = True
    if unknown_trace:
        print("Traceability references unknown problem IDs:")
        for item in unknown_trace:
            print(f"  - {item}")
        errors = True
    if missing_decisions:
        print("ADRs missing from traceability:")
        for item in missing_decisions:
            print(f"  - {item}")
        errors = True
    if missing_files:
        print("Decision records referenced but missing on disk:")
        for item in missing_files:
            print(f"  - {item}")
        errors = True
    if missing_artifacts:
        print("Artifacts referenced but missing on disk:")
        for item in missing_artifacts:
            print(f"  - {item}")
        errors = True

    if blank_problem_rows:
        print(f"Warning: {blank_problem_rows} traceability row(s) missing Problem ID.")
    if errors:
        return 1

    print(f"Traceability validation passed ({len(decision_files)} ADRs)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
