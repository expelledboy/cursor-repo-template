#!/usr/bin/env python3
"""Render a deterministic skills index from agent/skills.

@implements docs/system/model/docs-skills-output.md
"""

import sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[2]
SKILLS_DIR = ROOT / "agent" / "skills"
SKILL_FILENAME = "SKILL.md"


def load_frontmatter(path):
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return None
    parts = content.split("---", 2)
    return yaml.safe_load(parts[1]) if len(parts) >= 3 else None


def main():
    if not SKILLS_DIR.exists():
        print("No skills found")
        sys.exit(0)

    entries = []
    for path in sorted(SKILLS_DIR.rglob(SKILL_FILENAME)):
        fm = load_frontmatter(path)
        if not fm:
            continue
        name = str(fm.get("name", "")).strip()
        description = str(fm.get("description", "")).strip()
        rel_path = str(path.relative_to(ROOT))
        entries.append((name, description, rel_path))

    print("name | description | path")
    for name, description, rel_path in sorted(entries, key=lambda e: (e[0], e[2])):
        print(f"{name} | {description} | {rel_path}")


if __name__ == "__main__":
    main()
