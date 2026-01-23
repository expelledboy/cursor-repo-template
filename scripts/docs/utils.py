"""Shared helpers for docs tooling."""

from pathlib import Path


def format_size_kb(size_bytes):
    return f"{size_bytes / 1024:.1f} KB"


def extract_rels(rel_data):
    if isinstance(rel_data, dict):
        return list(rel_data.keys())
    if isinstance(rel_data, list):
        return rel_data
    return []


def normalize_filter_path(file_filter):
    if not file_filter:
        return None
    cleaned = file_filter.strip()
    if cleaned.startswith("./"):
        cleaned = cleaned[2:]
    if cleaned.startswith("docs/"):
        return cleaned
    buckets = {
        "reference",
        "how-to",
        "explanation",
        "tutorials",
        "work",
        "archive",
        "domains",
    }
    first_segment = cleaned.split("/", 1)[0]
    if first_segment in buckets:
        return f"docs/{cleaned}"
    return cleaned


def is_draft(status):
    if status is None:
        return False
    return str(status).strip().lower() == "draft"


def repo_path_exists(path):
    return Path(path).exists()
