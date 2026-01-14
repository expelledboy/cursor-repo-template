#!/usr/bin/env python3
# @directive docs/reference/agentos/validation-scripts.md

import os
import re
import sys

from validation_utils import list_markdown_files, read_lines

IMPROVEMENT_DIR = "docs/work/agentos/improvement"
FIELD_NAMES = ["Evidence", "Affected artifacts"]


def extract_field(lines, field):
    pattern = re.compile(rf"^\*\*{re.escape(field)}\*\*:\s*(.+)$")
    for line in lines:
        match = pattern.match(line.strip())
        if match:
            return match.group(1).strip()
    return ""


def has_content(value):
    return bool(re.search(r"[A-Za-z0-9]", value or ""))


def main():
    if not os.path.isdir(IMPROVEMENT_DIR):
        print("Missing improvement notes directory")
        return 1

    notes = list_markdown_files(IMPROVEMENT_DIR)
    if not notes:
        print("No improvement notes found")
        return 0

    errors = False
    for path in notes:
        lines = read_lines(path)
        for field in FIELD_NAMES:
            value = extract_field(lines, field)
            if not has_content(value):
                print(f"Improvement note missing {field}: {path}")
                errors = True

    if errors:
        return 1

    print(f"Improvement notes validation passed ({len(notes)} notes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
