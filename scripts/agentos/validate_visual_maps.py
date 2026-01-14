#!/usr/bin/env python3
# @directive docs/reference/agentos/validation-scripts.md

import re
import sys
from pathlib import Path
from typing import List


TARGETS = [
    ("docs/reference/agentos/behavior-spec.md", "docs/reference/agentos/behavior-spec.md#4-task-lifecycle"),
    ("docs/reference/agentos/routing.md", "docs/reference/agentos/routing.md#1-definition"),
    ("docs/reference/agentos/self-improvement.md", "docs/reference/agentos/self-improvement.md#2-definitions"),
    ("docs/reference/agentos/verification-contract.md", "docs/reference/agentos/verification-contract.md#1-gate-requirement"),
]


MERMAID_RE = re.compile(r"```mermaid\s+(.*?)```", re.DOTALL | re.IGNORECASE)
AUTHORITY_RE = re.compile(r"> \*\*Note:\*\* This diagram is supplementary\.", re.IGNORECASE)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def find_blocks(text: str) -> List[re.Match]:
    return list(MERMAID_RE.finditer(text))


def next_lines(text: str, start_idx: int, max_lines: int = 6) -> List[str]:
    tail = text[start_idx:]
    lines = tail.splitlines()
    return lines[:max_lines]


def validate_file(path: Path, section_ref: str) -> List[str]:
    errors: List[str] = []
    text = read_text(path)
    blocks = find_blocks(text)
    if not blocks:
        errors.append(f"{path}: missing mermaid diagram")
        return errors

    for block in blocks:
        body = block.group(1)
        if "graph TD" not in body:
            errors.append(f"{path}: mermaid block missing 'graph TD'")

        following = next_lines(text, block.end())
        note_line = next((ln for ln in following if AUTHORITY_RE.search(ln)), None)
        if not note_line:
            errors.append(f"{path}: authority statement missing after diagram")
        else:
            if section_ref not in "\n".join(following):
                errors.append(f"{path}: section reference missing or incorrect (expected '{section_ref}')")
    return errors


def main() -> int:
    all_errors: List[str] = []
    for target, section_ref in TARGETS:
        path = Path(target)
        if not path.is_file():
            all_errors.append(f"{target}: file not found")
            continue
        all_errors.extend(validate_file(path, section_ref))

    if all_errors:
        print("Visual maps validation failed:")
        for err in all_errors:
            print(f" - {err}")
        return 1

    print(f"Visual maps validation passed ({len(TARGETS)} files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
