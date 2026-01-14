#!/usr/bin/env python3
# @directive docs/reference/agentos/validation-scripts.md

import os
import re


def read_text(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as fh:
        return fh.read()


def read_lines(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as fh:
        return fh.readlines()


def normalize_path(raw):
    if raw is None:
        return ""
    cleaned = raw.strip().strip("\"'")
    cleaned = re.sub(r"[^A-Za-z0-9_./-]+$", "", cleaned)
    if cleaned.startswith("./"):
        cleaned = cleaned[2:]
    return cleaned


def extract_backtick_paths(text):
    if not text:
        return []
    return [normalize_path(match) for match in re.findall(r"`([^`]+)`", text)]


def extract_section_lines(lines, header):
    in_section = False
    section = []
    for line in lines:
        if line.strip() == header:
            in_section = True
            continue
        if in_section and line.startswith("## "):
            break
        if in_section:
            section.append(line)
    return section


def parse_markdown_table(lines, header_label):
    headers = None
    rows = []
    for idx, line in enumerate(lines):
        if not line.strip().startswith("|"):
            continue
        if header_label not in line:
            continue
        candidate = [h.strip() for h in line.strip().strip("|").split("|")]
        if idx + 1 >= len(lines):
            continue
        separator = lines[idx + 1]
        if "---" not in separator:
            continue
        headers = candidate
        for row in lines[idx + 2 :]:
            if not row.strip().startswith("|"):
                break
            cells = [c.strip() for c in row.strip().strip("|").split("|")]
            if len(cells) != len(headers):
                continue
            rows.append(dict(zip(headers, cells)))
        break
    return headers, rows


def list_markdown_files(dir_path):
    if not os.path.isdir(dir_path):
        return []
    items = []
    for name in os.listdir(dir_path):
        if not name.endswith(".md"):
            continue
        path = os.path.join(dir_path, name)
        if os.path.isfile(path):
            items.append(path)
    return sorted(items)
