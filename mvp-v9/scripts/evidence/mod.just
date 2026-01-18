# AgentOS Evidence API - Collection & Analysis
# @directive docs/reference/agentos/behavior-spec.md

# System evidence collection
system:
  @echo "🔍 Collecting system evidence..."
  python3 ../../scripts/agentos_insights.py system

system-json:
  python3 ../../scripts/agentos_insights.py system --output json

# Alignment evidence collection
alignment:
  @echo "🔗 Collecting docs-implementation alignment evidence..."
  python3 ../../scripts/agentos_insights.py alignment

alignment-json:
  python3 ../../scripts/agentos_insights.py alignment --output json

# Gap evidence collection
gaps:
  @echo "🎯 Collecting gap detection evidence..."
  python3 ../../scripts/agentos_insights.py gaps

gaps-json:
  python3 ../../scripts/agentos_insights.py gaps --output json

# Hierarchy evidence collection
hierarchy:
  @echo "📊 Collecting authority hierarchy evidence..."
  python3 ../../scripts/hierarchy_collector.py hierarchy

hierarchy-json:
  python3 ../../scripts/hierarchy_collector.py hierarchy --output json

# Complete evidence suite
all: system alignment gaps hierarchy
  @echo ""
  @echo "✅ Complete evidence collection finished"
  @echo "📊 Collected: system, alignment, gaps, hierarchy evidence"

# Evidence analysis workflow
analyze-system: system
  @echo ""
  @echo "💡 Analysis suggestions:"
  @echo "  - Check docs count vs implementation files"
  @echo "  - Verify directory structure completeness"
  @echo "  - Compare with previous system snapshots"

analyze-alignment: alignment
  @echo ""
  @echo "💡 Analysis suggestions:"
  @echo "  - Review bidirectional linkage completeness"
  @echo "  - Identify orphaned implementations/docs"
  @echo "  - Check governance relationship validity"

analyze-gaps: gaps
  @echo ""
  @echo "💡 Analysis suggestions:"
  @echo "  - Prioritize missing @directive annotations"
  @echo "  - Address orphaned documentation"
  @echo "  - Plan implementation for gap-filling"

analyze-hierarchy: hierarchy
  @echo ""
  @echo "💡 Analysis suggestions:"
  @echo "  - Verify DOE layer assignments"
  @echo "  - Check precedence level consistency"
  @echo "  - Validate governance relationships"

# Help documentation
help:
  @echo "📖 AgentOS Evidence API"
  @echo "━━━━━━━━━━━━━━━━━━━━━━━━"
  @echo ""
  @echo "🔍 EVIDENCE COLLECTION:"
  @echo "  just evidence system        # System structure evidence"
  @echo "  just evidence alignment     # Docs-implementation alignment"
  @echo "  just evidence gaps          # Gap detection evidence"
  @echo "  just evidence hierarchy     # Authority hierarchy evidence"
  @echo "  just evidence all           # Complete evidence suite"
  @echo ""
  @echo "📊 ANALYSIS WORKFLOWS:"
  @echo "  just evidence analyze-system    # System evidence analysis guide"
  @echo "  just evidence analyze-alignment # Alignment analysis guide"
  @echo "  just evidence analyze-gaps      # Gap analysis guide"
  @echo "  just evidence analyze-hierarchy # Hierarchy analysis guide"
  @echo ""
  @echo "📤 OUTPUT FORMATS:"
  @echo "  Add '-json' suffix for JSON output (system-json, alignment-json, etc.)"
  @echo ""
  @echo "🔗 INTEGRATION:"
  @echo "  Evidence feeds into task workflows and Cursor commands"
  @echo "  Use with: just tasks assess (for self-determination workflows)"