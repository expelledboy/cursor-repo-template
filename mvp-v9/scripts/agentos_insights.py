#!/usr/bin/env python3
"""
AgentOS Insights - Unified Evidence Provider
Simple, text-based insights for docs-implementation alignment.

DOE Declaration:
- DOE_LAYER: execution
- DOE_RESPONSIBILITY: Provide structured evidence for docs-implementation alignment insights
- DOE_GOVERNANCE: docs/reference/agentos/doe-framework.md
- DOE_PRECEDENCE: 4
"""

# @directive docs/reference/agentos/behavior-spec.md
# @directive docs/reference/agentos/doe-framework.md

import sys
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional

# DOE Layer Declaration
DOE_LAYER = "execution"
DOE_RESPONSIBILITY = "Provide structured evidence for docs-implementation alignment insights"
DOE_GOVERNANCE = "docs/reference/agentos/doe-framework.md"
DOE_PRECEDENCE = 4

class AgentOSInsights:
    """Unified evidence provider for docs-implementation alignment insights."""

    def __init__(self):
        self.project_root = Path(__file__).parent.parent
        self.docs_dir = self.project_root / "docs"
        self.scripts_dir = self.project_root / "scripts"
        self.src_dir = self.project_root / "src"

    def get_system_evidence(self) -> Dict[str, Any]:
        """Collect basic system structure evidence."""
        return {
            "timestamp": datetime.now().isoformat(),
            "directories": {
                "docs": self.docs_dir.exists(),
                "scripts": self.scripts_dir.exists(),
                "src": self.src_dir.exists()
            },
            "file_counts": {
                "docs": len(list(self.docs_dir.rglob("*.md"))) if self.docs_dir.exists() else 0,
                "scripts": len(list(self.scripts_dir.glob("*.py"))) if self.scripts_dir.exists() else 0,
                "src": len(list(self.src_dir.glob("*.py"))) if self.src_dir.exists() else 0
            },
            "total_files": len(list(self.project_root.rglob("*")))
        }

    def get_alignment_evidence(self) -> Dict[str, Any]:
        """Collect docs-implementation alignment evidence."""
        evidence = {
            "timestamp": datetime.now().isoformat(),
            "docs_files": [],
            "impl_files": [],
            "relationships": []
        }

        # Collect docs with implementations field
        if self.docs_dir.exists():
            for md_file in self.docs_dir.rglob("*.md"):
                if md_file.name == 'index.md':
                    continue

                frontmatter = self._load_frontmatter(md_file)
                if frontmatter and ('implementations' in frontmatter or 'implements' in frontmatter):
                    doc_info = {
                        "path": f"docs/{md_file.relative_to(self.docs_dir)}",
                        "has_implementations": True,
                        "implementation_refs": frontmatter.get('implementations', frontmatter.get('implements', []))
                    }
                    evidence["docs_files"].append(doc_info)

        # Collect implementation files
        for dir_path, dir_name in [(self.scripts_dir, "scripts"), (self.src_dir, "src")]:
            if dir_path.exists():
                for py_file in dir_path.glob("*.py"):
                    impl_info = {
                        "path": f"{dir_name}/{py_file.name}",
                        "has_directive": self._check_for_directive(py_file)
                    }
                    evidence["impl_files"].append(impl_info)

        # Simple relationship evidence
        evidence["relationship_summary"] = {
            "docs_with_implementations": len([d for d in evidence["docs_files"] if d["has_implementations"]]),
            "impl_with_directives": len([i for i in evidence["impl_files"] if i["has_directive"]]),
            "total_docs": len(list(self.docs_dir.rglob("*.md"))) if self.docs_dir.exists() else 0,
            "total_impl": len(evidence["impl_files"])
        }

        return evidence

    def get_gap_evidence(self) -> Dict[str, Any]:
        """Collect evidence of potential gaps in alignment."""
        alignment = self.get_alignment_evidence()

        gaps = {
            "timestamp": datetime.now().isoformat(),
            "potential_issues": []
        }

        # Check for docs without implementations
        docs_without_impl = []
        if self.docs_dir.exists():
            for md_file in self.docs_dir.rglob("*.md"):
                if md_file.name == 'index.md':
                    continue
                doc_path = f"docs/{md_file.relative_to(self.docs_dir)}"
                if not any(d["path"] == doc_path for d in alignment["docs_files"]):
                    docs_without_impl.append(doc_path)

        if docs_without_impl:
            gaps["potential_issues"].append({
                "type": "docs_without_implementations",
                "description": f"{len(docs_without_impl)} docs files lack implementation references",
                "examples": docs_without_impl[:3],
                "total": len(docs_without_impl)
            })

        # Check for impls without directives
        impls_without_directives = [i["path"] for i in alignment["impl_files"] if not i["has_directive"]]
        if impls_without_directives:
            gaps["potential_issues"].append({
                "type": "impls_without_directives",
                "description": f"{len(impls_without_directives)} implementation files lack @directive annotations",
                "examples": impls_without_directives[:3],
                "total": len(impls_without_directives)
            })

        return gaps

    def get_validation_evidence(self) -> Dict[str, Any]:
        """Collect evidence for system validation."""
        return {
            "timestamp": datetime.now().isoformat(),
            "doe_compliance": {
                "layer": DOE_LAYER,
                "responsibility": DOE_RESPONSIBILITY,
                "governance": DOE_GOVERNANCE,
                "precedence": DOE_PRECEDENCE
            },
            "system_integrity": {
                "python_syntax_check": self._check_python_syntax(),
                "required_directories": self._check_required_directories(),
                "core_files_present": self._check_core_files()
            }
        }

    def _load_frontmatter(self, file_path: Path) -> Optional[Dict]:
        """Load YAML frontmatter from markdown file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            if not content.startswith('---'):
                return None

            end_pos = content.find('---', 3)
            if end_pos == -1:
                return None

            frontmatter_text = content[3:end_pos]
            import yaml
            return yaml.safe_load(frontmatter_text)
        except:
            return None

    def _check_for_directive(self, file_path: Path) -> bool:
        """Check if Python file contains @directive annotation."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Check first 100 lines for @directive
            lines = content.split('\n')[:100]
            return any('@directive' in line for line in lines)
        except:
            return False

    def _check_python_syntax(self) -> Dict[str, Any]:
        """Check Python syntax in scripts and src directories."""
        issues = []
        total_files = 0

        for dir_path in [self.scripts_dir, self.src_dir]:
            if dir_path.exists():
                for py_file in dir_path.glob("*.py"):
                    total_files += 1
                    try:
                        compile(open(py_file).read(), str(py_file), 'exec')
                    except SyntaxError as e:
                        issues.append({
                            "file": str(py_file.relative_to(self.project_root)),
                            "error": str(e)
                        })

        return {
            "total_files_checked": total_files,
            "syntax_errors": len(issues),
            "issues": issues[:5]  # Limit examples
        }

    def _check_required_directories(self) -> Dict[str, bool]:
        """Check presence of required directories."""
        return {
            "docs": self.docs_dir.exists(),
            "scripts": self.scripts_dir.exists(),
            "src": self.src_dir.exists()
        }

    def _check_core_files(self) -> Dict[str, Any]:
        """Check presence of core AgentOS files."""
        core_files = [
            "src/agentos.py",
            "scripts/validate.py",
            "docs/README.md"
        ]

        present = []
        missing = []

        for file_path in core_files:
            full_path = self.project_root / file_path
            if full_path.exists():
                present.append(file_path)
            else:
                missing.append(file_path)

        return {
            "present": present,
            "missing": missing,
            "core_files_checked": len(core_files)
        }

    def render_text_insights(self, evidence_type: str, data: Dict[str, Any]) -> str:
        """Render evidence as simple, structured text for human + AI consumption."""
        lines = []

        if evidence_type == "system":
            lines.extend([
                "📊 AgentOS System Evidence",
                "=" * 30,
                f"Timestamp: {data['timestamp']}",
                "",
                "Directory Structure:",
                f"  docs: {'✅' if data['directories']['docs'] else '❌'}",
                f"  scripts: {'✅' if data['directories']['scripts'] else '❌'}",
                f"  src: {'✅' if data['directories']['src'] else '❌'}",
                "",
                "File Counts:",
                f"  Documentation: {data['file_counts']['docs']} files",
                f"  Scripts: {data['file_counts']['scripts']} files",
                f"  Source: {data['file_counts']['src']} files",
                f"  Total: {data['total_files']} files"
            ])

        elif evidence_type == "alignment":
            summary = data["relationship_summary"]
            lines.extend([
                "🔗 Docs-Implementation Alignment Evidence",
                "=" * 40,
                f"Timestamp: {data['timestamp']}",
                "",
                "Summary:",
                f"  Total docs: {summary['total_docs']}",
                f"  Docs with implementations: {summary['docs_with_implementations']}",
                f"  Total implementations: {summary['total_impl']}",
                f"  Impls with directives: {summary['impl_with_directives']}",
                "",
                "Evidence for analysis:",
                f"  - {len(data['docs_files'])} docs reference implementations",
                f"  - {len(data['impl_files'])} implementation files found",
                "  - Ready for bidirectional alignment analysis"
            ])

        elif evidence_type == "gaps":
            lines.extend([
                "🎯 Potential Alignment Gaps",
                "=" * 30,
                f"Timestamp: {data['timestamp']}",
                "",
                f"Issues found: {len(data['potential_issues'])}"
            ])

            for issue in data["potential_issues"]:
                lines.extend([
                    "",
                    f"⚠️  {issue['type'].replace('_', ' ').title()}:",
                    f"   {issue['description']}",
                    f"   Examples: {', '.join(issue['examples'])}"
                ])

            if not data["potential_issues"]:
                lines.append("✅ No obvious alignment gaps detected")

        elif evidence_type == "validation":
            integrity = data["system_integrity"]
            lines.extend([
                "✅ System Validation Evidence",
                "=" * 30,
                f"Timestamp: {data['timestamp']}",
                "",
                "DOE Compliance:",
                f"  Layer: {data['doe_compliance']['layer']}",
                f"  Responsibility: {data['doe_compliance']['responsibility'][:50]}...",
                "",
                "System Integrity:",
                f"  Python syntax: {integrity['python_syntax_check']['syntax_errors']} errors in {integrity['python_syntax_check']['total_files_checked']} files",
                f"  Required directories: {sum(integrity['required_directories'].values())}/3 present",
                f"  Core files: {len(integrity['core_files_present']['present'])}/{integrity['core_files_present']['core_files_checked']} present"
            ])

            if integrity['python_syntax_check']['syntax_errors'] > 0:
                lines.extend([
                    "",
                    "Syntax issues:",
                    *[f"  • {issue['file']}: {issue['error']}" for issue in integrity['python_syntax_check']['issues']]
                ])

        return "\n".join(lines)


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="AgentOS unified evidence provider for docs-implementation insights"
    )
    parser.add_argument(
        "insight_type",
        choices=["system", "alignment", "gaps", "validation"],
        help="Type of evidence to collect"
    )
    parser.add_argument(
        "--output", "-o",
        choices=["text", "json"],
        default="text",
        help="Output format (default: text)"
    )

    args = parser.parse_args()

    insights = AgentOSInsights()
    data = {}  # Initialize data

    # Collect evidence based on type
    if args.insight_type == "system":
        data = insights.get_system_evidence()
    elif args.insight_type == "alignment":
        data = insights.get_alignment_evidence()
    elif args.insight_type == "gaps":
        data = insights.get_gap_evidence()
    elif args.insight_type == "validation":
        data = insights.get_validation_evidence()

    # Output in requested format
    if args.output == "json":
        print(json.dumps(data, indent=2))
    else:
        print(insights.render_text_insights(args.insight_type, data))


if __name__ == "__main__":
    main()