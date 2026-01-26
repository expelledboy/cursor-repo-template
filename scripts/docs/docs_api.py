"""Docs API for loading and querying docs metadata."""

import os
from pathlib import Path
import yaml

from .utils import extract_rels, is_active


class DocsRepository:
    def __init__(self, docs_root="docs"):
        self.docs_root = Path(docs_root)
        self.docs = {}  # path -> {frontmatter, file_size, relationships}

    def load_docs(self, include_drafts=False):
        for md_file in self.docs_root.rglob("*.md"):
            frontmatter = self._parse_frontmatter(md_file)
            if not frontmatter:
                continue
            doc_status = frontmatter.get("doc_status")
            if not include_drafts and not is_active(doc_status):
                continue
            rel_path = str(md_file.relative_to(self.docs_root.parent))
            self.docs[rel_path] = {
                "frontmatter": frontmatter,
                "file_size": os.path.getsize(md_file),
                "relationships": self._process_relationships(frontmatter),
            }

    def _parse_frontmatter(self, md_file):
        try:
            content = md_file.read_text(encoding="utf-8")
            if not content.startswith("---"):
                return None
            parts = content.split("---", 2)
            return yaml.safe_load(parts[1]) if len(parts) >= 3 else None
        except Exception:
            return None

    def _process_relationships(self, frontmatter):
        return {
            "governed_by": extract_rels(frontmatter.get("governed_by", {})),
            "governs": extract_rels(frontmatter.get("governs", {})),
            "implements": extract_rels(frontmatter.get("implements", {})),
            "implemented_by": extract_rels(frontmatter.get("implemented_by", {})),
            "related": extract_rels(frontmatter.get("related", {})),
        }

    def governed_by_targets(self, doc_path):
        rels = self.docs[doc_path]["relationships"].get("governed_by", [])
        return [t for t in rels if t in self.docs]

    def get_docs(self):
        return self.docs
