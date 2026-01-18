#!/usr/bin/env python3
"""
Docs-Implementation Alignment Renderer - AgentOS v9

Renders comprehensive docs-implementation alignment relationships with rich context and metrics.
Shows bidirectional linkages, compliance status, and provides evidence for development processes.

DOE Declaration:
- DOE_LAYER: execution
- DOE_RESPONSIBILITY: Render docs-implementation alignment relationships with evidence
- DOE_GOVERNANCE: docs/reference/agentos/doe-framework.md
- DOE_PRECEDENCE: 4
"""

import sys
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime

# DOE Layer Declaration
DOE_LAYER = "execution"
DOE_RESPONSIBILITY = "Render docs-implementation alignment relationships with evidence"
DOE_GOVERNANCE = "docs/reference/agentos/doe-framework.md"
DOE_PRECEDENCE = 4

class AlignmentRenderer:
    """Renders comprehensive docs-implementation alignment relationships."""

    def __init__(self):
        self.data_orchestrator = None
        self.alignment_data = {}

    def initialize_data(self) -> bool:
        """Initialize data orchestrator and load all alignment data."""
        try:
            # Import data orchestrator
            sys.path.insert(0, str(Path(__file__).parent))
            from data_orchestrator import DataOrchestrator

            self.data_orchestrator = DataOrchestrator()
            success = self.data_orchestrator.load_all_data()

            if success:
                self._collect_alignment_data()
                return True
            return False

        except Exception as e:
            print(f"Error initializing data: {e}", file=sys.stderr)
            return False

    def _collect_alignment_data(self):
        """Collect comprehensive alignment data from orchestrator."""
        if not self.data_orchestrator:
            return

        # Get compliance data
        compliance = self.data_orchestrator._verify_doe_registry_compliance()

        # Get importance data
        importance_data = self.data_orchestrator.get_importance_insights()

        # Build bidirectional alignment map
        alignment_map = self._build_alignment_map()

        self.alignment_data = {
            "collection_timestamp": datetime.now().isoformat(),
            "compliance_metrics": compliance,
            "importance_overview": importance_data.get("system_overview", {}),
            "alignment_map": alignment_map,
            "doe_layer": DOE_LAYER,
            "evidence_quality": "comprehensive_alignment_analysis"
        }

    def _build_alignment_map(self) -> Dict[str, Any]:
        """Build comprehensive bidirectional alignment map."""
        alignment_map = {
            "docs_to_impl": {},  # Forward linkages
            "impl_to_docs": {},  # Backward linkages
            "bidirectional_alignments": [],  # Perfect alignments
            "orphaned_docs": [],  # Docs without implementations
            "orphaned_impls": []   # Impls without directives
        }

        if not self.data_orchestrator:
            return alignment_map

        # Process forward linkages (docs → impl) - only for actual docs
        for doc_path, doc_metadata in self.data_orchestrator.documents.items():
            # Skip implementation files (they shouldn't have implementation references)
            if doc_path.startswith(('src/', 'scripts/')):
                continue

            doc_alignments = {
                "doc_path": doc_path,
                "importance_score": self._get_importance_score(doc_path),
                "implementations": [],
                "compliance_status": "unknown"
            }

            # Check for implementation fields
            if 'implementations' in doc_metadata.frontmatter:
                implementations = doc_metadata.frontmatter['implementations']
                if isinstance(implementations, list):
                    doc_alignments["implementations"] = implementations
                elif isinstance(implementations, str):
                    doc_alignments["implementations"] = [implementations]

            if 'implements' in doc_metadata.frontmatter:
                implements = doc_metadata.frontmatter['implements']
                if isinstance(implements, list):
                    doc_alignments["implementations"].extend(implements)
                elif isinstance(implements, str):
                    doc_alignments["implementations"].append(implements)

            # Remove duplicates
            doc_alignments["implementations"] = list(set(doc_alignments["implementations"]))

            if doc_alignments["implementations"]:
                alignment_map["docs_to_impl"][doc_path] = doc_alignments

                # Check if doc has implementations - if it has any, it's not orphaned
                has_any_impls = len(doc_alignments["implementations"]) > 0
                if not has_any_impls:
                    alignment_map["orphaned_docs"].append({
                        "doc_path": doc_path,
                        "importance_score": float(doc_alignments["importance_score"]),
                        "reason": "No implementation references found"
                    })
            else:
                # No implementations field at all
                alignment_map["orphaned_docs"].append({
                    "doc_path": doc_path,
                    "importance_score": float(doc_alignments["importance_score"]),
                    "reason": "No implementation references found"
                })

        # Process backward linkages (impl → docs)
        all_impl_files = self._get_all_implementation_files()
        for impl_path in all_impl_files:
            impl_alignment = {
                "impl_path": impl_path,
                "importance_score": self._get_importance_score(impl_path),
                "directive_annotations": [],
                "compliance_status": "unknown"
            }

            # Check for @directive annotations by reading the file directly
            directive_annotations = self._extract_directive_annotations(impl_path)
            impl_alignment["directive_annotations"] = directive_annotations

            if impl_alignment["directive_annotations"]:
                alignment_map["impl_to_docs"][impl_path] = impl_alignment
            else:
                alignment_map["orphaned_impls"].append({
                    "impl_path": impl_path,
                    "reason": "Missing @directive annotations"
                })

        # Find bidirectional alignments
        for doc_path, doc_data in alignment_map["docs_to_impl"].items():
            for impl_path in doc_data["implementations"]:
                if (impl_path in alignment_map["impl_to_docs"] and
                    doc_path in alignment_map["impl_to_docs"][impl_path]["directive_annotations"]):
                    alignment_map["bidirectional_alignments"].append({
                        "doc_path": doc_path,
                        "impl_path": impl_path,
                        "doc_importance": float(doc_data["importance_score"]),
                        "impl_importance": float(alignment_map["impl_to_docs"][impl_path]["importance_score"]),
                        "status": "perfect_alignment"
                    })

        return alignment_map

    def _get_importance_score(self, file_path: str) -> float:
        """Get importance score for a file."""
        if not self.data_orchestrator:
            return 0.0

        # Try to get from importance scores directly
        try:
            if hasattr(self.data_orchestrator, 'importance_scores') and self.data_orchestrator.importance_scores:
                score_data = self.data_orchestrator.importance_scores.get(file_path)
                if score_data and isinstance(score_data, dict):
                    return score_data.get('importance_score', 0.0)

            # Fallback to insights
            importance_data = self.data_orchestrator.get_importance_insights()
            rankings = importance_data.get("top_important_documents", [])

            for item in rankings:
                if item.get("doc_path") == file_path:
                    return item.get("importance_score", 0.0)
        except Exception:
            pass

        return 0.0

    def _implementation_exists(self, impl_path: str) -> bool:
        """Check if implementation file exists."""
        if not self.data_orchestrator:
            return False

        return impl_path in self.data_orchestrator.documents

    def _get_all_implementation_files(self) -> List[str]:
        """Get all implementation files in the system."""
        if not self.data_orchestrator:
            return []

        impl_files = []
        for doc_path in self.data_orchestrator.documents.keys():
            if doc_path.startswith(('src/', 'scripts/')):
                impl_files.append(doc_path)

        return impl_files

    def _extract_directive_annotations(self, impl_path: str) -> List[str]:
        """Extract @directive annotations from implementation file."""
        directives = []

        try:
            file_path = Path(__file__).parent.parent / impl_path
            if file_path.exists():
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                lines = content.split('\n')
                for line in lines[:100]:  # Check first 100 lines for directives
                    line = line.strip()
                    if '@directive' in line and 'docs/' in line:
                        # Extract path after docs/
                        if 'docs/' in line:
                            docs_part = line.split('docs/')[1]
                            # Extract path until whitespace, quote, or comment
                            path = docs_part.split()[0].strip('\'"')
                            if path.endswith('.md'):
                                full_path = f"docs/{path}"
                                directives.append(full_path)

        except Exception:
            pass  # File reading errors don't break alignment analysis

        return directives

    def render_alignment_map(self) -> str:
        """Render comprehensive alignment map with rich context."""
        if not self.alignment_data:
            return "❌ No alignment data available - run initialize_data() first"

        output_lines = [
            "📊 AgentOS v9 Docs-Implementation Alignment Map",
            "=" * 60,
            f"Generated: {self.alignment_data['collection_timestamp']}",
            f"DOE Layer: {self.alignment_data['doe_layer']}",
            ""
        ]

        # Overall metrics
        compliance = self.alignment_data.get("compliance_metrics", {})
        coverage = compliance.get("coverage_analysis", {})

        output_lines.extend([
            "🎯 Overall Alignment Metrics:",
            f"• Coverage: {coverage.get('coverage_percentage', 0):.1%}",
            f"• Forward Linkages: {compliance.get('forward_linkages', 0)} (docs → impl)",
            f"• Backward Linkages: {compliance.get('backward_linkages', 0)} (impl → docs)",
            f"• Bidirectional Alignments: {len(self.alignment_data['alignment_map'].get('bidirectional_alignments', []))}",
            f"• Orphaned Docs: {len(self.alignment_data['alignment_map'].get('orphaned_docs', []))}",
            f"• Orphaned Impls: {len(self.alignment_data['alignment_map'].get('orphaned_impls', []))}",
            ""
        ])

        # Importance context
        importance = self.alignment_data.get("importance_overview", {})
        if importance:
            output_lines.extend([
                "⭐ Importance Context:",
                f"• Total Files Analyzed: {importance.get('total_documents', 0)}",
                f"• Average Importance: {importance.get('average_importance', 0):.1f}/100",
                ""
            ])

        # Bidirectional alignments (perfect)
        bidirectional = self.alignment_data["alignment_map"].get("bidirectional_alignments", [])
        if bidirectional:
            output_lines.extend([
                "✅ Perfect Bidirectional Alignments:",
                "-" * 40
            ])

            # Sort by combined importance
            sorted_alignments = sorted(
                bidirectional,
                key=lambda x: x["doc_importance"] + x["impl_importance"],
                reverse=True
            )

            for alignment in sorted_alignments:
                output_lines.extend([
                    f"📄 {alignment['doc_path']}",
                    f"   ↔️  🔗 {alignment['impl_path']}",
                    f"   📊 Scores: Doc({alignment['doc_importance']:.1f}) | Impl({alignment['impl_importance']:.1f})",
                    ""
                ])

        # Forward linkages only
        forward_only = []
        alignment_map = self.alignment_data["alignment_map"]

        for doc_path, doc_data in alignment_map.get("docs_to_impl", {}).items():
            has_bidirectional = any(
                align["doc_path"] == doc_path for align in bidirectional
            )
            if not has_bidirectional and doc_data["implementations"]:
                forward_only.append((doc_path, doc_data))

        if forward_only:
            output_lines.extend([
                "⚠️  Forward Linkages Only (Missing @directive):",
                "-" * 50
            ])

            for doc_path, doc_data in forward_only:
                output_lines.extend([
                    f"📄 {doc_path} (importance: {doc_data['importance_score']:.1f})",
                    f"   → 🔗 {', '.join(doc_data['implementations'])}",
                    "   ❌ Missing @directive annotations in implementations",
                    ""
                ])

        # Orphaned docs
        orphaned_docs = alignment_map.get("orphaned_docs", [])
        if orphaned_docs:
            output_lines.extend([
                "🚨 Orphaned Documentation (No Implementation Links):",
                "-" * 55
            ])

            for orphaned in orphaned_docs:
                output_lines.extend([
                    f"📄 {orphaned['doc_path']} (importance: {self._get_importance_score(orphaned['doc_path']):.1f})",
                    f"   ❌ {orphaned['reason']}",
                ])
                if 'referenced_impls' in orphaned:
                    output_lines.append(f"   📝 References: {', '.join(orphaned['referenced_impls'])}")
                output_lines.append("")

        # Orphaned implementations
        orphaned_impls = alignment_map.get("orphaned_impls", [])
        if orphaned_impls:
            output_lines.extend([
                "🚨 Orphaned Implementations (No @directive Links):",
                "-" * 55
            ])

            for orphaned in orphaned_impls:
                output_lines.extend([
                    f"🐍 {orphaned['impl_path']} (importance: {self._get_importance_score(orphaned['impl_path']):.1f})",
                    f"   ❌ {orphaned['reason']}",
                    ""
                ])

        # Evidence for process improvement
        output_lines.extend([
            "🔍 Evidence for Development Process:",
            "-" * 40,
            "• Perfect alignments indicate strong docs-impl coupling",
            "• Forward-only links suggest missing @directive annotations",
            "• Orphaned docs indicate unimplemented specifications",
            "• Orphaned impls indicate undocumented functionality",
            "• Use importance scores to prioritize alignment improvements",
            "",
            f"📈 Next Steps: Focus on {len(orphaned_docs) + len(orphaned_impls)} orphaned files for better alignment"
        ])

        return "\n".join(output_lines)

    def render_metrics_only(self) -> str:
        """Render alignment metrics only."""
        if not self.alignment_data:
            return "❌ No alignment data available"

        compliance = self.alignment_data.get("compliance_metrics", {})
        coverage = compliance.get("coverage_analysis", {})

        return "\n".join([
            "📊 Alignment Metrics:",
            f"Coverage: {coverage.get('coverage_percentage', 0):.1%}",
            f"Forward: {compliance.get('forward_linkages', 0)} | Backward: {compliance.get('backward_linkages', 0)}",
            f"Bidirectional: {len(self.alignment_data['alignment_map'].get('bidirectional_alignments', []))}",
            f"Orphaned: {len(self.alignment_data['alignment_map'].get('orphaned_docs', []))} docs, {len(self.alignment_data['alignment_map'].get('orphaned_impls', []))} impls"
        ])

    def export_json(self) -> str:
        """Export complete alignment data as JSON."""
        return json.dumps(self.alignment_data, indent=2)


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Render docs-implementation alignment relationships"
    )
    parser.add_argument(
        "command",
        choices=["render", "metrics", "export", "check"],
        help="Command to execute"
    )
    parser.add_argument(
        "file",
        nargs="?",
        help="Specific file to check alignment for (used with check command)"
    )
    parser.add_argument(
        "--output", "-o",
        choices=["text", "json"],
        default="text",
        help="Output format"
    )

    args = parser.parse_args()

    renderer = AlignmentRenderer()

    if not renderer.initialize_data():
        print("❌ Failed to initialize alignment data", file=sys.stderr)
        sys.exit(1)

    if args.command == "render":
        if args.output == "json":
            print(renderer.export_json())
        else:
            print(renderer.render_alignment_map())

    elif args.command == "metrics":
        print(renderer.render_metrics_only())

    elif args.command == "export":
        print(renderer.export_json())

    elif args.command == "check":
        if not args.file:
            print("❌ File path required for check command", file=sys.stderr)
            sys.exit(1)

        # Check specific file alignment
        alignment_map = renderer.alignment_data["alignment_map"]

        # Check if it's a doc
        if args.file in alignment_map["docs_to_impl"]:
            doc_data = alignment_map["docs_to_impl"][args.file]
            print(f"📄 {args.file}")
            print(f"Importance: {doc_data['importance_score']:.1f}")
            print(f"Implementations: {', '.join(doc_data['implementations'])}")

            # Check bidirectional
            bidirectional = [
                align for align in alignment_map["bidirectional_alignments"]
                if align["doc_path"] == args.file
            ]
            if bidirectional:
                print(f"Bidirectional alignments: {len(bidirectional)}")
            else:
                print("⚠️  No bidirectional alignments found")

        # Check if it's an implementation
        elif args.file in alignment_map["impl_to_docs"]:
            impl_data = alignment_map["impl_to_docs"][args.file]
            print(f"🐍 {args.file}")
            print(f"Importance: {impl_data['importance_score']:.1f}")
            print(f"Directive annotations: {', '.join(impl_data['directive_annotations'])}")

            # Check bidirectional
            bidirectional = [
                align for align in alignment_map["bidirectional_alignments"]
                if align["impl_path"] == args.file
            ]
            if bidirectional:
                print(f"Bidirectional alignments: {len(bidirectional)}")
            else:
                print("⚠️  No bidirectional alignments found")

        else:
            print(f"❌ {args.file} not found in alignment data")


if __name__ == "__main__":
    main()