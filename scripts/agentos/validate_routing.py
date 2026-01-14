#!/usr/bin/env python3
# @directive docs/reference/agentos/validation-scripts.md

import os
import re
import sys
from glob import glob

RULE_GLOB = ".cursor/rules/*.mdc"
RULE_REF_RE = re.compile(r"\.cursor/rules/[^\s`)]*\.mdc")
DOC_REF_RE = re.compile(r"docs/[^\s`\"')]+")


def read_text(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as fh:
        return fh.read()


def main():
    if not os.path.isfile("docs/index.md"):
        print("Missing docs/index.md")
        return 1
    if not os.path.isdir(".cursor/rules"):
        print("Missing .cursor/rules directory")
        return 1

    rules_fs = sorted({p[2:] if p.startswith("./") else p for p in glob(RULE_GLOB)})
    if not rules_fs:
        print("No rule files found in .cursor/rules")
        return 1

    index_text = read_text("docs/index.md")
    rules_idx = sorted(set(RULE_REF_RE.findall(index_text)))

    missing_in_index = [r for r in rules_fs if r not in index_text]
    missing_files = [r for r in rules_idx if not os.path.isfile(r)]

    doc_errors = []
    for rule in rules_fs:
        rule_text = read_text(rule)
        doc_refs = sorted(set(DOC_REF_RE.findall(rule_text)))
        for ref in doc_refs:
            clean = re.sub(r"[^A-Za-z0-9_./*-]+$", "", ref)
            if not clean:
                continue
            if "<" in clean or ">" in clean:
                continue
            if "*" in clean:
                base = clean.split("*")[0]
                if base and not os.path.exists(base):
                    doc_errors.append(f"{rule} -> {clean} (missing base path)")
            else:
                if not os.path.exists(clean):
                    doc_errors.append(f"{rule} -> {clean} (missing path)")

    errors = False
    if missing_in_index:
        print("Rules not listed in docs/index.md:")
        for item in missing_in_index:
            print(f"  - {item}")
        errors = True
    if missing_files:
        print("Rules referenced in docs/index.md but missing on disk:")
        for item in missing_files:
            print(f"  - {item}")
        errors = True
    if doc_errors:
        print("Rule doc references missing:")
        for item in doc_errors:
            print(f"  - {item}")
        errors = True

    if errors:
        return 1

    print(f"Routing validation passed ({len(rules_fs)} rules)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
