#!/usr/bin/env python3
# @directive docs/reference/agentos/validation-scripts.md

import re
import sys
from pathlib import Path
from typing import List

TEMPLATES = Path("docs/reference/agentos/design-decision-templates.md")
HOWTO = Path("docs/how-to/agentos/design-decision-checkpoint.md")
STRUCTURED_EXPLORATION = Path("docs/reference/agentos/structured-exploration.md")
STRUCTURED_HOWTO = Path("docs/how-to/agentos/design-decision-structured-exploration.md")

REQUIRED_SECTIONS = [
    "Template selection",
    "Minimum required fields",
    "Template blocks",
    "Tradeoff table standard",
    "Usage",
]

LEVELS = ["Level 1", "Level 2", "Level 3", "Level 4"]
HOWTO_CHECKS = ["Checklist", "template level", "Tradeoff table"]
PHASES = ["Phase 1", "Phase 2", "Phase 3", "Phase 4", "Phase 5"]
PHASE_NAMES = [
    "Component Breakdown",
    "Option Exploration",
    "Trade-off Analysis",
    "Decision Documentation",
    "Decision Verification",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_sections(txt: str) -> List[str]:
    errors: List[str] = []
    for sec in REQUIRED_SECTIONS:
        if sec not in txt:
            errors.append(f"{TEMPLATES}: missing section '{sec}'")
    for lvl in LEVELS:
        if lvl not in txt:
            errors.append(f"{TEMPLATES}: missing template block for {lvl}")
    if "Tradeoff table" not in txt:
        errors.append(f"{TEMPLATES}: missing tradeoff table standard")
    return errors


def check_phase_integration(txt: str) -> List[str]:
    """Check that templates include phase markers."""
    errors: List[str] = []
    # Check that templates reference structured exploration
    if "structured-exploration.md" not in txt:
        errors.append(f"{TEMPLATES}: missing reference to structured-exploration.md")
    # Check that Level 3-4 templates include all 5 phases
    for phase in PHASES:
        if phase not in txt:
            errors.append(f"{TEMPLATES}: missing {phase} marker in templates")
    # Check for phase names
    for phase_name in PHASE_NAMES:
        if phase_name not in txt:
            errors.append(f"{TEMPLATES}: missing phase name '{phase_name}' in templates")
    return errors


def check_structured_exploration_ref(txt: str) -> List[str]:
    """Check structured exploration reference file."""
    errors: List[str] = []
    required_sections = [
        "Phase 1: Component Breakdown",
        "Phase 2: Option Exploration",
        "Phase 3: Trade-off Analysis",
        "Phase 4: Decision Documentation",
        "Phase 5: Decision Verification",
        "Complexity-Based Rigor",
    ]
    for sec in required_sections:
        if sec not in txt:
            errors.append(f"{STRUCTURED_EXPLORATION}: missing section '{sec}'")
    return errors


def check_structured_howto(txt: str) -> List[str]:
    """Check structured exploration how-to guide."""
    errors: List[str] = []
    required_sections = [
        "Phase 1",
        "Phase 2",
        "Phase 3",
        "Phase 4",
        "Phase 5",
        "Integration with templates",
        "Phase completion checklist",
    ]
    for sec in required_sections:
        if sec not in txt:
            errors.append(f"{STRUCTURED_HOWTO}: missing section '{sec}'")
    return errors


def check_table_standards(txt: str) -> List[str]:
    """Check that table formatting standards are documented."""
    errors: List[str] = []

    # Check for table standard sections
    required_table_sections = [
        "Format requirements",
        "Column structure",
        "Row structure",
        "Text guidelines",
        "Weight usage",
        "Examples by complexity level",
    ]

    for sec in required_table_sections:
        if sec not in txt:
            errors.append(f"{TEMPLATES}: missing table standard section '{sec}'")

    # Check for markdown table syntax guidance
    if "markdown table" not in txt.lower() and "table syntax" not in txt.lower():
        errors.append(f"{TEMPLATES}: missing markdown table syntax guidance")

    # Check for examples
    if "Level 1" not in txt or "Level 2" not in txt:
        errors.append(f"{TEMPLATES}: missing table examples for complexity levels")

    return errors


def check_table_examples_in_structured_exploration(txt: str) -> List[str]:
    """Check that structured exploration has table examples."""
    errors: List[str] = []

    # Check for Phase 3 table examples
    if "Phase 3: Trade-off Analysis" in txt:
        # Check for table examples by level
        if "Level 1" not in txt or "Level 2" not in txt:
            errors.append(f"{STRUCTURED_EXPLORATION}: missing table examples in Phase 3")

        # Check for criteria selection guidance
        if "Criteria Selection" not in txt and "criteria selection" not in txt.lower():
            errors.append(f"{STRUCTURED_EXPLORATION}: missing criteria selection guidance in Phase 3")

        # Check for common criteria patterns
        if "Common criteria" not in txt and "common criteria" not in txt.lower():
            errors.append(f"{STRUCTURED_EXPLORATION}: missing common criteria patterns in Phase 3")

    return errors


def validate_table_format(table_text: str) -> List[str]:
    """Validate a markdown table format."""
    errors: List[str] = []
    lines = [line.strip() for line in table_text.split("\n") if line.strip()]

    if not lines:
        errors.append("Empty table")
        return errors

    # Check for header row
    if not lines[0].startswith("|"):
        errors.append("Table missing header row")
        return errors

    # Check for separator row
    if len(lines) < 2 or "---" not in lines[1]:
        errors.append("Table missing separator row")
        return errors

    # Check header structure
    header_parts = [p.strip() for p in lines[0].split("|") if p.strip()]
    if len(header_parts) < 2:
        errors.append("Table must have at least Option column + 1 criteria column")
        return errors

    # Check for Option column
    if "Option" not in lines[0] and "option" not in lines[0].lower():
        errors.append("Table missing Option column")

    # Check data rows
    if len(lines) < 3:
        errors.append("Table missing data rows")
        return errors

    # Check row consistency
    header_cols = len([p for p in lines[0].split("|") if p.strip()])
    for i, line in enumerate(lines[2:], start=2):
        if line.startswith("|"):
            row_cols = len([p for p in line.split("|") if p.strip()])
            if row_cols != header_cols:
                errors.append(f"Row {i} has {row_cols} columns, expected {header_cols}")

    return errors


def main() -> int:
    errors: List[str] = []

    # Check templates
    if not TEMPLATES.is_file():
        errors.append("design-decision-templates.md: file not found")
    else:
        tmpl_txt = read_text(TEMPLATES)
        errors.extend(check_sections(tmpl_txt))
        errors.extend(check_phase_integration(tmpl_txt))

    # Check how-to guide
    if not HOWTO.is_file():
        errors.append("design-decision-checkpoint.md: file not found")
    else:
        howto_txt = read_text(HOWTO)
        for token in HOWTO_CHECKS:
            if token not in howto_txt:
                errors.append(f"design-decision-checkpoint.md: missing '{token}' guidance")

    # Check structured exploration reference
    if not STRUCTURED_EXPLORATION.is_file():
        errors.append("structured-exploration.md: file not found")
    else:
        se_txt = read_text(STRUCTURED_EXPLORATION)
        errors.extend(check_structured_exploration_ref(se_txt))

    # Check structured exploration how-to
    if not STRUCTURED_HOWTO.is_file():
        errors.append("design-decision-structured-exploration.md: file not found")
    else:
        se_howto_txt = read_text(STRUCTURED_HOWTO)
        errors.extend(check_structured_howto(se_howto_txt))

    # Check table standards in templates
    if TEMPLATES.is_file():
        tmpl_txt = read_text(TEMPLATES)
        errors.extend(check_table_standards(tmpl_txt))

    # Check table examples in structured exploration
    if STRUCTURED_EXPLORATION.is_file():
        se_txt = read_text(STRUCTURED_EXPLORATION)
        errors.extend(check_table_examples_in_structured_exploration(se_txt))

    if errors:
        print("Design decision validation failed:")
        for e in errors:
            print(f" - {e}")
        return 1

    print("Design decision validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
