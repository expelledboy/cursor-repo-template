#!/usr/bin/env python3
# @directive docs/reference/agentos/validation-scripts.md

import os
import sys

from validation_utils import (
    extract_backtick_paths,
    extract_section_lines,
    normalize_path,
    read_lines,
)

COMPONENTS_PATH = "docs/reference/agentos/components.md"
INDEX_PATH = "docs/index.md"
RULE_PATH = ".cursor/rules/20-agentos.topic.mdc"
CORE_RULE_PATH = ".cursor/rules/agentos/core.mdc"
CORE_PREFIX = "docs/reference/agentos/"
MINIMAL_CORE_REQUIRED = {
    "docs/reference/agentos/behavior-spec.md",
    "docs/reference/agentos/routing.md",
    "docs/reference/agentos/context-compass.md",
    "docs/reference/agentos/safety-policy.md",
    "docs/reference/agentos/directive-tiers.md",
    "docs/reference/agentos/cursor-mechanics.md",
}


def collect_paths(lines):
    paths = []
    for line in lines:
        if "`" in line:
            paths.extend(extract_backtick_paths(line))
            continue
        stripped = line.strip()
        if stripped.startswith("- "):
            token = normalize_path(stripped[2:].strip())
            if token:
                paths.append(token)
    return [p for p in paths if p.startswith(CORE_PREFIX)]


def core_from_components():
    lines = read_lines(COMPONENTS_PATH)
    section = extract_section_lines(lines, "## 1. Core contracts")
    return collect_paths(section)


def core_from_index():
    lines = read_lines(INDEX_PATH)
    section = extract_section_lines(lines, "## AgentOS Framework")
    return collect_paths(section)


def core_from_rule():
    lines = read_lines(RULE_PATH)
    in_section = False
    section = []
    for line in lines:
        if "Load the AgentOS core docs" in line:
            in_section = True
            continue
        if in_section and "Adapter notes" in line:
            break
        if in_section:
            section.append(line)
    return collect_paths(section)


def rule_uses_core_mdc():
    lines = read_lines(RULE_PATH)
    for line in lines:
        if CORE_RULE_PATH in line:
            return True
    return False


def core_from_core_mdc():
    if not os.path.exists(CORE_RULE_PATH):
        return []
    lines = read_lines(CORE_RULE_PATH)
    return collect_paths(lines)


def main():
    missing_files = [p for p in (COMPONENTS_PATH, INDEX_PATH, RULE_PATH) if not os.path.exists(p)]
    if missing_files:
        print("Missing required files:")
        for path in missing_files:
            print(f"  - {path}")
        return 1

    components = core_from_components()
    index = core_from_index()
    rule = core_from_rule()
    rule_indirect = rule_uses_core_mdc()
    core_mdc = core_from_core_mdc()

    components_set = set(components)
    index_set = set(index)
    rule_set = set(rule)

    errors = False

    if not components_set:
        print("Core list missing in components.md")
        errors = True

    missing_in_index = sorted(components_set - index_set)
    extra_in_index = sorted(index_set - components_set)
    missing_in_rule = sorted(components_set - rule_set)
    extra_in_rule = sorted(rule_set - components_set)

    missing_paths = [p for p in sorted(components_set) if not os.path.exists(p)]

    if missing_in_index:
        print("Core docs missing in docs/index.md:")
        for item in missing_in_index:
            print(f"  - {item}")
        errors = True
    if extra_in_index:
        print("Extra core docs in docs/index.md:")
        for item in extra_in_index:
            print(f"  - {item}")
        errors = True
    if rule_indirect:
        core_mdc_set = set(core_mdc)
        missing_minimal = sorted(MINIMAL_CORE_REQUIRED - core_mdc_set)
        extra_core_mdc = sorted(core_mdc_set - components_set)
        if not core_mdc_set:
            print("Core rule .cursor/rules/agentos/core.mdc is empty or missing core paths")
            errors = True
        if missing_minimal:
            print("Minimal core docs missing in .cursor/rules/agentos/core.mdc:")
            for item in missing_minimal:
                print(f"  - {item}")
            errors = True
        if extra_core_mdc:
            print("Core rule includes docs not in components list:")
            for item in extra_core_mdc:
                print(f"  - {item}")
            errors = True
    else:
        if missing_in_rule:
            print("Core docs missing in .cursor/rules/20-agentos.topic.mdc:")
            for item in missing_in_rule:
                print(f"  - {item}")
            errors = True
        if extra_in_rule:
            print("Extra core docs in .cursor/rules/20-agentos.topic.mdc:")
            for item in extra_in_rule:
                print(f"  - {item}")
            errors = True
    if missing_paths:
        print("Core docs listed but missing on disk:")
        for item in missing_paths:
            print(f"  - {item}")
        errors = True

    if errors:
        return 1

    print(f"Core list sync passed ({len(components_set)} docs)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
