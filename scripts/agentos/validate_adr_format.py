#!/usr/bin/env python3
# @directive docs/reference/agentos/validation-scripts.md

import os
import re
import sys

from validation_utils import list_markdown_files, read_lines

DECISIONS_DIR = "docs/explanation/agentos/decisions"
FILENAME_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-[a-z0-9-]+\.md$")
STATUS_ALLOWED = {"Proposed", "Accepted", "Superseded"}
REQUIRED_FIELDS = ["Status", "Date", "Scope", "Problem IDs"]
REQUIRED_SECTIONS = [
    "Context",
    "Decision",
    "Alternatives",
    "Consequences",
    "Why this worked",
    "Artifacts",
]


def extract_field(lines, field):
    pattern = re.compile(rf"^\*\*{re.escape(field)}\*\*:\s*(.+)$")
    for line in lines:
        match = pattern.match(line.strip())
        if match:
            return match.group(1).strip()
    return ""


def section_content(lines, heading):
    content = []
    in_section = False
    header = f"## {heading}"
    for line in lines:
        if line.strip() == header:
            in_section = True
            continue
        if in_section and line.startswith("## "):
            break
        if in_section:
            content.append(line)
    return content


def has_meaningful_content(lines):
    return any(line.strip() for line in lines)


def artifacts_have_items(lines):
    for line in lines:
        if line.strip().startswith("- "):
            return True
    return False


def main():
    if not os.path.isdir(DECISIONS_DIR):
        print("Missing decisions directory")
        return 1

    decision_files = list_markdown_files(DECISIONS_DIR)
    if not decision_files:
        print("No ADR files found")
        return 1

    errors = False
    for path in decision_files:
        base = os.path.basename(path)
        if not FILENAME_RE.match(base):
            print(f"ADR filename invalid: {path}")
            errors = True

        lines = read_lines(path)
        for field in REQUIRED_FIELDS:
            value = extract_field(lines, field)
            if not value:
                print(f"ADR missing {field}: {path}")
                errors = True
                continue
            if field == "Status" and value not in STATUS_ALLOWED:
                print(f"ADR status invalid ({value}): {path}")
                errors = True
            if field == "Date" and not re.match(r"^\d{4}-\d{2}-\d{2}$", value):
                print(f"ADR date invalid ({value}): {path}")
                errors = True
            if field == "Problem IDs" and "PRB-" not in value:
                print(f"ADR Problem IDs missing PRB- entry: {path}")
                errors = True

        for section in REQUIRED_SECTIONS:
            content = section_content(lines, section)
            if not has_meaningful_content(content):
                print(f"ADR section empty or missing ({section}): {path}")
                errors = True
            if section == "Artifacts" and not artifacts_have_items(content):
                print(f"ADR artifacts list missing: {path}")
                errors = True

    if errors:
        return 1

    print(f"ADR format validation passed ({len(decision_files)} ADRs)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
