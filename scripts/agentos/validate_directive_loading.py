#!/usr/bin/env python3
# @directive docs/reference/agentos/validation-scripts.md

import os
import re
import sys
from pathlib import Path
from typing import List, Dict, Set

DIRECTIVE_TIERS = Path("docs/reference/agentos/directive-tiers.md")
CONTEXT_COMPASS = Path("docs/reference/agentos/context-compass.md")
BEHAVIOR_SPEC = Path("docs/reference/agentos/behavior-spec.md")

TIER_PATTERN = re.compile(r"Tier\s+(\d+)", re.IGNORECASE)
TIER_SECTION_PATTERN = re.compile(r"##\s+5\.\s+Hierarchical", re.IGNORECASE)
MINIMAL_MODE_PATTERN = re.compile(r"minimal\s+mode", re.IGNORECASE)
DEFERRED_PATTERN = re.compile(r"deferred", re.IGNORECASE)
TRIGGER_PATTERN = re.compile(r"trigger", re.IGNORECASE)


def read_text(path: Path) -> str:
    """Read file text."""
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")


def check_directive_tiers_table(txt: str) -> List[str]:
    """Check directive tiers table structure."""
    errors: List[str] = []

    # Check for table structure
    if "| Directive | Tier |" not in txt:
        errors.append(f"{DIRECTIVE_TIERS}: missing directive tiers table")
        return errors

    # Check for tier assignments
    tier_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    lines = txt.split("\n")
    in_table = False

    for line in lines:
        if "| Directive | Tier |" in line:
            in_table = True
            continue
        if in_table and line.strip().startswith("|") and "---" not in line:
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 3:
                tier_match = re.search(r"\d+", parts[2])
                if tier_match:
                    tier = int(tier_match.group())
                    if tier in tier_counts:
                        tier_counts[tier] += 1
        if in_table and line.strip() and not line.strip().startswith("|"):
            break

    # Check that tiers are present
    for tier, count in tier_counts.items():
        if count == 0:
            errors.append(f"{DIRECTIVE_TIERS}: no directives assigned to Tier {tier}")

    return errors


def check_context_compass_sections(txt: str) -> List[str]:
    """Check context compass has required sections for selective loading."""
    errors: List[str] = []

    required_sections = [
        "5.1. Loading sequence",
        "5.2. Tier loading triggers",
        "5.3. Deferral criteria",
        "5.4. Minimal mode",
        "5.5. Context window monitoring",
    ]

    for section in required_sections:
        if section not in txt:
            errors.append(f"{CONTEXT_COMPASS}: missing section '{section}'")

    # Check for loading sequence
    if "Tier 1" not in txt or "Tier 2" not in txt:
        errors.append(f"{CONTEXT_COMPASS}: missing loading sequence details")

    # Check for minimal mode definition
    if "Minimal mode" in txt:
        if ">80%" not in txt and "80% full" not in txt:
            errors.append(f"{CONTEXT_COMPASS}: minimal mode definition missing context threshold")

    return errors


def check_behavior_spec_header(txt: str) -> List[str]:
    """Check behavior spec has directive loading plan format."""
    errors: List[str] = []

    # Check for directive loading plan in Section 10
    if "Directive loading plan" not in txt:
        errors.append(f"{BEHAVIOR_SPEC}: missing directive loading plan in Section 10")

    # Check for context usage and minimal mode fields
    if "Context usage" not in txt:
        errors.append(f"{BEHAVIOR_SPEC}: missing context usage field in directive loading plan")

    if "Minimal mode" not in txt:
        errors.append(f"{BEHAVIOR_SPEC}: missing minimal mode field in directive loading plan")

    # Check for tier format
    if "Tier 1 (Core)" not in txt or "Tier 2 (Task-type)" not in txt:
        errors.append(f"{BEHAVIOR_SPEC}: missing tier format in directive loading plan")

    return errors


def check_tier_sequence(txt: str) -> List[str]:
    """Check that tier sequence is documented correctly."""
    errors: List[str] = []

    # Check for explicit sequence (Tier 1 → Tier 2 → Tier 3 → Tier 4/5)
    sequence_indicators = [
        "Tier 1",
        "Tier 2",
        "Tier 3",
        "Tier 4",
        "Tier 5",
    ]

    found_tiers = []
    for tier in sequence_indicators:
        if tier in txt:
            found_tiers.append(tier)

    if len(found_tiers) < 3:
        errors.append(f"{CONTEXT_COMPASS}: incomplete tier sequence documentation")

    return errors


def check_deferral_requirements(txt: str) -> List[str]:
    """Check that deferral requirements are documented."""
    errors: List[str] = []

    # Check for deferral criteria
    if "Deferral criteria" not in txt and "5.3" not in txt:
        errors.append(f"{CONTEXT_COMPASS}: missing deferral criteria section")

    # Check for explicit triggers requirement
    if "explicit" in txt.lower() and "trigger" in txt.lower():
        if "auditable" not in txt.lower() and "audit" not in txt.lower():
            # This is a warning, not an error
            pass

    return errors


def main() -> int:
    """Main validation function."""
    errors: List[str] = []

    # Check directive tiers table
    if not DIRECTIVE_TIERS.is_file():
        errors.append(f"{DIRECTIVE_TIERS}: file not found")
    else:
        tiers_txt = read_text(DIRECTIVE_TIERS)
        errors.extend(check_directive_tiers_table(tiers_txt))

    # Check context compass sections
    if not CONTEXT_COMPASS.is_file():
        errors.append(f"{CONTEXT_COMPASS}: file not found")
    else:
        compass_txt = read_text(CONTEXT_COMPASS)
        errors.extend(check_context_compass_sections(compass_txt))
        errors.extend(check_tier_sequence(compass_txt))
        errors.extend(check_deferral_requirements(compass_txt))

    # Check behavior spec header format
    if not BEHAVIOR_SPEC.is_file():
        errors.append(f"{BEHAVIOR_SPEC}: file not found")
    else:
        spec_txt = read_text(BEHAVIOR_SPEC)
        errors.extend(check_behavior_spec_header(spec_txt))

    if errors:
        print("Directive loading validation failed:")
        for e in errors:
            print(f" - {e}")
        return 1

    print("Directive loading validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
