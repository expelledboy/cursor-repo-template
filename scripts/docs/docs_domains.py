#!/usr/bin/env python3
"""Render a deterministic domain index from docs/domains."""

import sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[2]
DOMAINS_DIR = ROOT / "docs" / "domains"


def load_frontmatter(path):
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return None
    parts = content.split("---", 2)
    return yaml.safe_load(parts[1]) if len(parts) >= 3 else None


def main():
    if not DOMAINS_DIR.exists():
        print("No domain docs found")
        sys.exit(0)

    entries = []
    for path in sorted(DOMAINS_DIR.glob("*.md")):
        fm = load_frontmatter(path)
        if not fm:
            continue
        entries.append(
            (
                str(fm.get("domain_id", "")),
                str(fm.get("domain_scope", "")),
                str(fm.get("domain_status", "")),
                str(path.relative_to(ROOT)),
            )
        )

    print("domain_id | domain_scope | domain_status | path")
    for domain_id, scope, status, rel_path in entries:
        print(f"{domain_id} | {scope} | {status} | {rel_path}")


if __name__ == "__main__":
    main()
