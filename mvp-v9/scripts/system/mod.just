# AgentOS System API - Health, Validation & Documentation
# @directive docs/reference/agentos/doe-framework.md

# Pure bash system health check (efficient, no Python overhead)
health:
  #!/usr/bin/env bash
  echo "🏥 AgentOS System Health Check"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

  # Check core directories (relative to current working directory)
  echo "📁 Directory Structure:"
  if [ -d "docs" ]; then
    DOC_COUNT=$(find docs -name "*.md" 2>/dev/null | wc -l)
    echo "  ✅ docs: ${DOC_COUNT} markdown files"
  else
    echo "  ❌ docs: directory missing"
  fi

  if [ -d "scripts" ]; then
    SCRIPT_COUNT=$(find scripts -name "*.py" 2>/dev/null | wc -l)
    echo "  ✅ scripts: ${SCRIPT_COUNT} Python files"
  else
    echo "  ❌ scripts: directory missing"
  fi

  if [ -d "src" ]; then
    SRC_COUNT=$(find src -name "*.py" 2>/dev/null | wc -l)
    echo "  ✅ src: ${SRC_COUNT} Python files"
  else
    echo "  ❌ src: directory missing"
  fi

  echo ""

  # Check core files
  echo "📄 Core Files:"
  if [ -f "src/agentos.py" ]; then
    echo "  ✅ src/agentos.py: present"
  else
    echo "  ❌ src/agentos.py: missing"
  fi

  if [ -f "README.md" ]; then
    echo "  ✅ README.md: present"
  else
    echo "  ❌ README.md: missing"
  fi

  echo ""

  # Basic syntax check (pure bash)
  echo "🐍 Python Syntax Check:"
  PYTHON_FILES=$(find . -name "*.py" -type f 2>/dev/null)
  TOTAL_PY=$(echo "$PYTHON_FILES" | wc -l)
  SYNTAX_ERRORS=0

  for py_file in $PYTHON_FILES; do
    if [ -f "$py_file" ]; then
      if ! python3 -m py_compile "$py_file" 2>/dev/null; then
        SYNTAX_ERRORS=$((SYNTAX_ERRORS + 1))
      fi
    fi
  done

  if [ $SYNTAX_ERRORS -eq 0 ]; then
    echo "  ✅ ${TOTAL_PY} Python files: no syntax errors"
  else
    echo "  ⚠️  ${TOTAL_PY} Python files: ${SYNTAX_ERRORS} syntax errors found"
  fi

  echo ""
  echo "🎯 Health check complete!"

# Python-wrapped system validation
validate:
  @echo "🔍 Running complete system validation..."
  python3 scripts/validate.py

# API documentation (pure bash - no Python dependency)
api:
  #!/usr/bin/env bash
  echo "📚 AgentOS Complete API Reference"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo ""
  echo "🎯 QUICK WORKFLOWS:"
  echo "  just assess          # Start self-determination assessment"
  echo "  just self-determine  # Complete self-determination workflow"
  echo "  just health          # Basic system health check"
  echo ""
  echo "🔍 EVIDENCE API (just evidence):"
  echo "  just evidence system        # System structure evidence"
  echo "  just evidence alignment     # Docs-implementation alignment"
  echo "  just evidence gaps          # Gap detection evidence"
  echo "  just evidence hierarchy     # Authority hierarchy evidence"
  echo "  just evidence all           # Complete evidence suite"
  echo "  just evidence analyze-*     # Analysis guidance for each type"
  echo ""
  echo "🎯 TASK API (just tasks):"
  echo "  just tasks assess           # Start assessment workflow"
  echo "  just tasks learn            # Start learning workflow"
  echo "  just tasks improve          # Start improvement workflow"
  echo "  just tasks reflect          # Start reflection workflow"
  echo "  just tasks list             # Show active tasks"
  echo "  just tasks create NAME OBJ  # Create custom task"
  echo "  just tasks add-sub-objective # Advanced task management"
  echo "  just tasks record-*         # Progress diary entries"
  echo ""
  echo "🔧 SYSTEM API (just system):"
  echo "  just system validate        # Complete system validation"
  echo "  just system health          # Basic health check (pure bash)"
  echo "  just system api             # Show this API reference"
  echo ""
  echo "🔗 INTEGRATION PATTERNS:"
  echo "  Assessment → Learning → Improvement:"
  echo "    just assess && just tasks learn && just tasks improve"
  echo ""
  echo "  Evidence + Tasks:"
  echo "    just evidence all && just tasks assess"
  echo ""
  echo "  Health + Validation:"
  echo "    just health && just system validate"
  echo ""
  echo "📖 HELP SYSTEM:"
  echo "  just --list                 # Show all available commands"
  echo "  just [module] --help        # Module-specific help"
  echo "  just [module] help          # Detailed module documentation"

# System statistics (pure bash)
stats:
  #!/usr/bin/env bash
  echo "📊 AgentOS System Statistics"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

  # File counts
  TOTAL_MD=$(find docs -name "*.md" 2>/dev/null | wc -l)
  TOTAL_PY=$(find . -name "*.py" -type f 2>/dev/null | wc -l)
  TOTAL_FILES=$(find . -type f 2>/dev/null | wc -l)

  printf "Total files:     %6d\n" $TOTAL_FILES
  printf "Markdown docs:   %6d\n" $TOTAL_MD
  printf "Python scripts:  %6d\n" $TOTAL_PY

  # Directory sizes
  echo ""
  echo "📁 Directory Sizes:"
  if [ -d "docs" ]; then
    DOCS_SIZE=$(du -sh docs 2>/dev/null | cut -f1)
    echo "  docs:    $DOCS_SIZE"
  fi
  if [ -d "scripts" ]; then
    SCRIPTS_SIZE=$(du -sh scripts 2>/dev/null | cut -f1)
    echo "  scripts: $SCRIPTS_SIZE"
  fi
  if [ -d "src" ]; then
    SRC_SIZE=$(du -sh src 2>/dev/null | cut -f1)
    echo "  src:     $SRC_SIZE"
  fi

  # Git status (if applicable)
  if git rev-parse --git-dir > /dev/null 2>&1; then
    echo ""
    echo "🔄 Git Status:"
    CHANGES=$(git status --porcelain | wc -l)
    BRANCH=$(git branch --show-current)
    printf "  Branch:  %s\n" $BRANCH
    printf "  Changes: %d files\n" $CHANGES
  fi

# Help documentation
help:
  @echo "📖 AgentOS System API"
  @echo "━━━━━━━━━━━━━━━━━━━━━━"
  @echo ""
  @echo "🏥 HEALTH & VALIDATION:"
  @echo "  just system health          # Basic health check (pure bash)"
  @echo "  just system validate        # Complete system validation"
  @echo "  just system stats           # System statistics"
  @echo ""
  @echo "📚 DOCUMENTATION:"
  @echo "  just system api             # Complete API reference"
  @echo "  just system help            # This help documentation"
  @echo ""
  @echo "🔧 IMPLEMENTATION NOTES:"
  @echo "  health, stats, api: Pure bash (efficient, no dependencies)"
  @echo "  validate: Python-wrapped (complex validation logic)"
  @echo ""
  @echo "🔗 INTEGRATION:"
  @echo "  Use with: just evidence all (comprehensive system assessment)"