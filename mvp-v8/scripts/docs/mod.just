# Documentation management module
# @directive docs/reference/docs/doc-authority.md
# @directive docs/explanation/decisions/2026-01-16-restructuring-tool-architecture.md

# List active problems (stdout)
list-problems:
  python3 index.py problems

list-problems-full:
  python3 index.py problems --format full

# List active discoveries (stdout)
list-discoveries:
  python3 index.py discoveries

list-discoveries-full:
  python3 index.py discoveries --format full

# List accepted decisions (stdout)
list-decisions:
  python3 index.py decisions

list-decisions-full:
  python3 index.py decisions --format full

# List all domains
list-domains:
  python3 index.py domains

# Validate frontmatter and find missing frontmatter
validate:
  python3 index.py validate

# Check system health and provide guidance
[script("bash")]
doctor:
  echo "🔎 Diagnosing AgentOS Documentation System..."
  echo ""
  # Check for stale drafts (simple find command)
  STALE=$(find ../docs/work -name "*.md" -mtime +30 2>/dev/null)
  if [ ! -z "$STALE" ]; then
    echo "Warning: Stale Work files found (>30 days):"
    echo "$STALE" | sed 's/^/  /'
  else
    echo "✅ No stale drafts found."
  fi
  echo ""
  echo "✅ Diagnosis complete."

# Lint documentation (find missing frontmatter)
[script("bash")]
lint:
  MISSING=$(find ../docs -name "*.md" -not -name "index.md" -exec sh -c 'if ! head -1 "$1" | grep -q "^---$"; then echo "$1"; fi' _ {} \; 2>/dev/null)
  if [ -z "$MISSING" ]; then
    echo "NONE - All files have YAML frontmatter"
  else
    echo "Files missing YAML frontmatter:"
    echo "$MISSING" | sed 's/^/  /'
  fi

# Show documentation statistics
[script("bash")]
stats:
  TOTAL=$(find ../docs -name "*.md" | wc -l)
  WITH_FRONTMATTER=$(find ../docs -name "*.md" -exec grep -l "^---$" {} \; | wc -l)
  DOMAINS=$(python3 index.py domains | grep -c "^- " || echo "0")

  printf "📊 Documentation Statistics\n"
  printf "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
  printf "Total .md files:     %3d\n" $TOTAL
  printf "With frontmatter:    %3d\n" $WITH_FRONTMATTER
  printf "Domains found:       %3d\n" $DOMAINS
  printf "Coverage:           %3d%%\n" $(( WITH_FRONTMATTER * 100 / TOTAL ))

# Show documentation registry (stdout)
registry:
  python3 index.py registry

# Validate registry linkages
validate-registry:
  python3 index.py validate-registry

# Restructuring workflow tools
inventory:
  OUT=../docs/local/docs-inventory-$(date +%Y%m%d).txt; python3 index.py inventory --output-file "$OUT" && echo "Inventory saved to docs/local/docs-inventory-$(date +%Y%m%d).txt"

create-batch BATCH_NAME FILES:
  python3 index.py create-batch {{BATCH_NAME}} "{{FILES}}"

state BATCH_NAME STATUS:
  python3 index.py state {{BATCH_NAME}} "{{STATUS}}"

validate-batch BATCH_NAME:
  python3 index.py validate-batch {{BATCH_NAME}}

cleanup-batch BATCH_NAME:
  python3 index.py cleanup-batch {{BATCH_NAME}}

cleanup-all:
  python3 index.py cleanup-all

# Run progress + batch iteration helpers
list-batches:
  python3 index.py list-batches

run-summary:
  python3 index.py run-summary

next-batch:
  python3 index.py next-batch

mark-batch-complete BATCH_NAME:
  python3 index.py mark-batch-complete {{BATCH_NAME}}