#!/usr/bin/env python3
# @directive docs/reference/agentos/validation-scripts.md

import os
import sys


def read_text(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as fh:
        return fh.read()


REQUIRED_FILES = [
    ".cursor/commands/agentos-bootstrap.md",
    ".cursor/commands/agentos-init.md",
    ".cursor/commands/agentos-start.md",
    ".cursor/commands/agentos-plan.md",
    ".cursor/commands/agentos-design.md",
    ".cursor/commands/agentos-execute.md",
    ".cursor/commands/agentos-verify.md",
    ".cursor/commands/agentos-complete.md",
]

REQUIRED_SECTIONS = [
    "## Purpose",
    "## Lifecycle Entrypoint",
    "## Canonical entrypoints",
    "## Adapter boundary",
    "## Next command",
]


def validate_file(path):
    if not os.path.exists(path):
        return [f"Missing command file: {path}"]
    text = read_text(path)
    errors = []
    if not text.strip().startswith("# /agentos-"):
        errors.append(f"Command header must start with '# /agentos-': {path}")
    for section in REQUIRED_SECTIONS:
        if section not in text:
            errors.append(f"Missing section '{section}' in {path}")
    return errors


def main():
    errors = []
    for path in REQUIRED_FILES:
        errors.extend(validate_file(path))

    if errors:
        for err in errors:
            print(err)
        return 1

    print("Command validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
