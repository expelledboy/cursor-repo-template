#!/usr/bin/env python3
# @directive docs/reference/agentos/validation-scripts.md

import re
import sys
from pathlib import Path
from typing import List

FILES = {
    "behavior": Path("docs/reference/agentos/behavior-spec.md"),
    "det_ref": Path("docs/reference/agentos/complexity-determination.md"),
    "wf_ref": Path("docs/reference/agentos/workflow-variations.md"),
    "howto": Path("docs/how-to/agentos/determine-complexity.md"),
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def check_exists() -> List[str]:
    errors = []
    for key, path in FILES.items():
        if not path.is_file():
            errors.append(f"{path}: file not found")
    return errors


def check_behavior(txt: str) -> List[str]:
    errs = []
    if "All 8 steps must be completed" not in txt or "workflow variations" not in txt:
        errs.append("behavior-spec.md: missing lifecycle/variation cues in Section 4")
    if "Complexity level (1-4)" not in txt or "Workflow variation" not in txt:
        errs.append("behavior-spec.md: missing complexity/workflow fields in Section 11")
    if "Design-decision checkpoint status varies by complexity level" not in txt:
        errs.append("behavior-spec.md: missing checkpoint-by-level rule in Section 11")
    return errs


def check_det_ref(txt: str) -> List[str]:
    errs = []
    for token in ("Level 1", "Level 2", "Level 3", "Level 4"):
        if token not in txt:
            errs.append(f"complexity-determination.md: missing {token}")
    for crit in ("Scope", "Design decisions", "Risk", "Effort", "Dependencies"):
        if crit not in txt:
            errs.append(f"complexity-determination.md: missing criterion {crit}")
    if "Decision tree" not in txt:
        errs.append("complexity-determination.md: missing decision tree")
    if "Escalation" not in txt:
        errs.append("complexity-determination.md: missing escalation rules")
    return errs


def check_wf_ref(txt: str) -> List[str]:
    errs = []
    steps = ["Intake", "Classify", "Route", "Plan", "Execute", "Verify", "Report", "Anneal"]
    for step in steps:
        if step not in txt:
            errs.append(f"workflow-variations.md: missing step {step} in lifecycle table")
    if "Tier loading mapping" not in txt:
        errs.append("workflow-variations.md: missing Tier mapping")
    if "Design-decision checkpoint requirements" not in txt:
        errs.append("workflow-variations.md: missing checkpoint requirements")
    return errs


def check_howto(txt: str) -> List[str]:
    errs = []
    if "When to determine" not in txt or "Escalation" not in txt:
        errs.append("determine-complexity.md: missing steps or escalation guidance")
    if "Selected Level" not in txt:
        errs.append("determine-complexity.md: missing example")
    return errs


def main() -> int:
    errors = []
    errors.extend(check_exists())
    if errors:
        for e in errors:
            print(e)
        return 1

    errors.extend(check_behavior(read_text(FILES["behavior"])))
    errors.extend(check_det_ref(read_text(FILES["det_ref"])))
    errors.extend(check_wf_ref(read_text(FILES["wf_ref"])))
    errors.extend(check_howto(read_text(FILES["howto"])))

    if errors:
        print("Complexity workflow validation failed:")
        for e in errors:
            print(f" - {e}")
        return 1

    print("Complexity workflow validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
