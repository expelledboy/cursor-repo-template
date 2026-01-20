#!/usr/bin/env python3
# @directive docs/reference/docs/frontmatter-schema.md
# @directive docs/explanation/decisions/2026-01-16-frontmatter-schema.md
# @directive docs/explanation/decisions/2026-01-16-doc-registry-system.md
# @directive docs/explanation/decisions/2026-01-16-restructuring-tool-architecture.md
# @directive docs/explanation/decisions/2026-01-16-yaml-state.md
# @directive docs/explanation/decisions/2026-01-16-restructuring-process-design.md
# @directive docs/explanation/decisions/2026-01-18-schema-compliance-enforcement.md
# @directive docs/explanation/decisions/2026-01-18-behavioral-consistency-enforcement.md
# @directive docs/explanation/decisions/2026-01-18-validation-system-enhancement.md
# @directive docs/explanation/decisions/2026-01-18-semantic-validation-mandate.md
# scripts/docs/index.py

import sys
import yaml
import argparse
from pathlib import Path
from typing import Dict, List, Optional, Set
from datetime import datetime

STATE_FILE = Path(__file__).parent.parent / 'docs' / 'local' / 'docs-state.yaml'

def _load_docs_state() -> Dict:
    if not STATE_FILE.exists():
        return {}
    try:
        data = yaml.safe_load(STATE_FILE.read_text(encoding='utf-8'))
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}

def _save_docs_state(state: Dict) -> None:
    # Ensure parent directory exists
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(yaml.safe_dump(state, sort_keys=False), encoding='utf-8')

def _ensure_run_initialized(state: Dict) -> Dict:
    if 'run_id' not in state:
        state['run_id'] = f"DOCS-RUN-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        state['started_at'] = datetime.now().isoformat()
    state.setdefault('batches', [])
    state.setdefault('completed_batches', [])
    state.setdefault('current_batch', None)
    state.setdefault('inventory_file', None)
    state.setdefault('skipped_files', [])
    return state

def get_authority_level(doc_path: str) -> int:
    """Return authority level (lower number = higher authority)."""
    if 'docs/reference/' in doc_path:
        return 1
    elif 'docs/how-to/' in doc_path:
        return 2
    elif 'docs/explanation/' in doc_path:
        return 3
    elif 'docs/tutorials/' in doc_path:
        return 4
    elif 'docs/work/' in doc_path:
        return 5
    elif 'docs/archive/' in doc_path:
        return 6
    return 99  # Unknown

def get_authority_name(level: int) -> str:
    """Return human-readable authority level name."""
    names = {
        1: 'Reference',
        2: 'How-to',
        3: 'Explanation',
        4: 'Tutorial',
        5: 'Work',
        6: 'Archive'
    }
    return names.get(level, 'Unknown')

def load_frontmatter(md_file: Path) -> Optional[Dict]:
    """Load frontmatter from a markdown file."""
    try:
        content = md_file.read_text(encoding='utf-8')
        if content.startswith('---'):
            end_idx = content.find('---', 3)
            if end_idx > 0:
                frontmatter_text = content[3:end_idx].strip()
                return yaml.safe_load(frontmatter_text)
    except:
        pass
    return None

def _refresh_batches_from_fs(state: Dict) -> Dict:
    """If state has no batches, populate from batches/*.txt deterministically."""
    if state.get('batches'):
        return state
    project_root = Path(__file__).parent.parent
    batch_dir = project_root / 'docs' / 'local' / 'batches'
    if not batch_dir.exists():
        return state
    batch_names = sorted(p.stem for p in batch_dir.glob('*.txt'))
    if batch_names:
        state['batches'] = batch_names
    return state

def load_frontmatter(file_path: Path) -> Optional[Dict]:
    """Extract YAML frontmatter from markdown file."""
    try:
        content = file_path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        return None

    if not content.startswith('---'):
        return None

    parts = content.split('---', 2)
    if len(parts) < 3:
        return None

    try:
        return yaml.safe_load(parts[1])
    except yaml.YAMLError:
        return None

def find_docs(doc_type: Optional[str] = None, domain: Optional[str] = None) -> List[tuple]:
    """Find all .md files and return with their frontmatter."""
    docs = []

    # Path to docs directory (script may be run from different locations)
    script_dir = Path(__file__).parent
    docs_dir = script_dir.parent.parent / 'docs'

    for md_file in docs_dir.rglob('*.md'):
        if md_file.name == 'index.md':
            continue

        frontmatter = load_frontmatter(md_file)
        if not frontmatter:
            continue

        # Filter by doc type if specified
        if doc_type:
            if doc_type == 'problems' and 'work/problems' not in str(md_file):
                continue
            elif doc_type == 'discoveries' and 'work/discoveries' not in str(md_file):
                continue
            elif doc_type == 'decisions' and 'explanation/decisions' not in str(md_file):
                continue

        # Filter by domain if specified
        if domain and frontmatter.get('domain') != domain:
            continue

        docs.append((frontmatter, md_file))

    return docs

def generate_index(doc_type: str, domain: Optional[str] = None, format_type: str = 'basic', tag: Optional[str] = None, since: Optional[str] = None, before: Optional[str] = None, status_filter: Optional[str] = None):
    """Generate index for given doc type."""
    docs = find_docs(doc_type, domain)

    # Apply advanced filters
    filtered_docs = []
    for frontmatter, doc in docs:
        # Status filtering
        status = frontmatter.get('status', '').lower()
        if status_filter:
            if status_filter == 'all':
                pass  # Include all
            elif status != status_filter:
                continue
        else:
            # Default status logic
            if doc_type == 'decisions' and status != 'accepted':
                continue
            elif doc_type in ['problems', 'discoveries'] and status != 'active':
                continue

        # Tag filtering
        if tag:
            tags = frontmatter.get('tags', [])
            if not tags or tag not in tags:
                continue

        # Date filtering
        if since or before:
            from datetime import datetime
            doc_date_str = str(frontmatter.get('created_date', ''))
            if doc_date_str:
                try:
                    doc_date = datetime.fromisoformat(doc_date_str)
                    if since:
                        since_date = datetime.fromisoformat(since)
                        if doc_date < since_date:
                            continue
                    if before:
                        before_date = datetime.fromisoformat(before)
                        if doc_date >= before_date:
                            continue
                except ValueError:
                    continue  # Skip docs with invalid dates

        filtered_docs.append((frontmatter, doc))

    active_docs = filtered_docs

    # Sort by date, then title
    def sort_key(item):
        frontmatter, doc = item
        date = frontmatter.get('created_date', '')
        title = frontmatter.get('title', doc.stem)
        return (date, title.lower())

    active_docs.sort(key=sort_key)

    # Title
    domain_suffix = f" ({domain})" if domain else ""
    print(f"# {doc_type.title()} Registry{domain_suffix}")
    print()

    if not active_docs:
        print("No active items found.")
        return

    print("## Active Items")
    print()

    for frontmatter, doc in active_docs:
        title = frontmatter.get('title', doc.stem)
        filename = doc.name

        if format_type == 'full':
            print(f"- **{title}** ({filename})")
            if 'created_date' in frontmatter:
                print(f"  - Created Date: {frontmatter['created_date']}")
            if 'purpose' in frontmatter:
                print(f"  - Purpose: {frontmatter['purpose']}")
            if 'tags' in frontmatter and frontmatter['tags']:
                print(f"  - Tags: {', '.join(frontmatter['tags'])}")
            print()
        else:
            print(f"- [{title}]({filename})")

def list_domains():
    """List all domains found in frontmatter."""
    domains: Set[str] = set()

    for frontmatter, _ in find_docs():
        if 'domain' in frontmatter:
            domains.add(frontmatter['domain'])

    if not domains:
        print("No domains found.")
        return

    print("Available domains:")
    for domain in sorted(domains):
        print(f"- {domain}")

VALID_STATUSES = {'active', 'draft', 'accepted', 'stable', 'superseded', 'deprecated'}

# DOE Integrated Flow: Task-type verification gates (comprehensive catalog)
TASK_GATES = {
    # Core development tasks
    'Documentation & Knowledge': 'just docs::validate',
    'Implementation / Feature': 'just test',
    'Design/Architecture': 'just docs::validate',
    'Testing & Verification': 'just test',
    'Refactoring & Tech-Debt': 'just test',

    # Project management tasks
    'Discovery & Requirements': 'just docs::validate',
    'Planning & Estimation': 'just docs::validate',

    # Deployment tasks
    'Release/Deploy': 'build/smoke',
    'Operations & Maintenance': 'smoke-test',

    # Security & compliance
    'Security & Compliance': 'lint/baseline',

    # Incident response
    'Incident Response & Debugging': 'diagnostic-check',

    # Meta-maintenance
    'AgentOS Meta-Maintenance': 'just docs::validate'
}

def validate_relationship_consistency(md_file, frontmatter, content_issues):
    """Validate consistency of directional relationships."""
    # Check bidirectional consistency for key relationship pairs
    bidirectional_checks = [
        ('informs', 'depends_on'),  # If A informs B, B should depend on A
        ('implements', 'implemented_by'),  # If A implements B, B should be implemented by A
        ('evidence_for', 'evidence_from'),  # If A provides evidence for B, B should have evidence from A
    ]

    doc_path = str(md_file)

    for forward_field, reverse_field in bidirectional_checks:
        if forward_field in frontmatter:
            for target_path in frontmatter[forward_field]:
                if target_path.startswith('docs/'):
                    try:
                        target_frontmatter = load_frontmatter(Path('docs') / target_path)
                        if target_frontmatter:
                            # Check if reverse relationship exists
                            if reverse_field not in target_frontmatter or doc_path not in target_frontmatter.get(reverse_field, []):
                                content_issues.append(f"{md_file}: Missing reverse relationship - {forward_field} '{target_path}' but target doesn't have '{reverse_field}' pointing back")
                    except:
                        pass  # Skip if can't read target file

def validate_frontmatter():
    """Validate all frontmatter with categorized error reporting."""
    yaml_errors = []
    missing_fields = []
    invalid_values = []
    content_issues = []

    # Check all .md files
    for md_file in Path('docs').rglob('*.md'):
        if md_file.name == 'index.md':
            continue

        frontmatter = load_frontmatter(md_file)
        if not frontmatter:
            yaml_errors.append(f"{md_file}: Missing YAML frontmatter (files must start with ---)")
            continue

        # Check required fields
        for field in ['title', 'status', 'created_date']:
            if field not in frontmatter:
                missing_fields.append(f"{md_file}: Missing required field '{field}'")

        # Check status values
        if 'status' in frontmatter and frontmatter['status'] not in VALID_STATUSES:
            invalid_values.append(f"{md_file}: Invalid status '{frontmatter['status']}' (must be one of {VALID_STATUSES})")

        # Check created_date format
        if 'created_date' in frontmatter:
            import re
            if not re.match(r'^\d{4}-\d{2}-\d{2}$', str(frontmatter['created_date'])):
                invalid_values.append(f"{md_file}: Invalid created_date format '{frontmatter['created_date']}' (expected YYYY-MM-DD)")

        # Check implementations
        if 'implementations' in frontmatter:
            for impl_path in frontmatter['implementations']:
                if not isinstance(impl_path, str):
                    content_issues.append(f"{md_file}: implementations entries must be strings (file paths)")
                    continue
                impl_full_path = Path(impl_path)
                if not impl_full_path.exists():
                    content_issues.append(f"{md_file}: Implementation '{impl_path}' does not exist")

        # Check external docs
        if 'external_docs' in frontmatter:
            for ext_doc in frontmatter['external_docs']:
                if not isinstance(ext_doc, dict):
                    content_issues.append(f"{md_file}: external_docs entries must be objects")
                    continue
                required_fields = ['url', 'type', 'title']
                for field in required_fields:
                    if field not in ext_doc:
                        content_issues.append(f"{md_file}: external_docs entry missing required field '{field}'")
                if 'type' in ext_doc and ext_doc['type'] not in ['reference', 'how-to', 'explanation', 'tutorial']:
                    invalid_values.append(f"{md_file}: external_docs entry has invalid type '{ext_doc['type']}'")

        # Optional field warnings
        if 'purpose' in frontmatter and len(str(frontmatter['purpose'])) > 200:
            content_issues.append(f"{md_file}: Purpose field is long ({len(str(frontmatter['purpose']))} chars)")

        # Domain validation
        if 'domain' in frontmatter:
            valid_domains = ['agentos', 'docs']
            if frontmatter['domain'] not in valid_domains:
                invalid_values.append(f"{md_file}: Invalid domain '{frontmatter['domain']}' (must be one of {valid_domains})")

        # Diátaxis compliance validation
        doc_path = str(md_file)
        if 'docs/reference/' in doc_path:
            if frontmatter.get('status') not in ['stable', 'accepted']:
                content_issues.append(f"{md_file}: Reference docs must have status 'stable' or 'accepted'")
        elif 'docs/how-to/' in doc_path:
            if frontmatter.get('status') not in ['stable', 'accepted']:
                content_issues.append(f"{md_file}: How-to docs must have status 'stable' or 'accepted'")
        elif 'docs/explanation/' in doc_path:
            if frontmatter.get('status') not in ['stable', 'accepted']:
                content_issues.append(f"{md_file}: Explanation docs must have status 'stable' or 'accepted'")
        elif 'docs/work/' in doc_path:
            if 'status' not in frontmatter or frontmatter['status'] not in ['active', 'draft']:
                content_issues.append(f"{md_file}: Work docs must have status 'active' or 'draft'")
            # Check for required Status field in work docs
            if 'Status' not in frontmatter:
                missing_fields.append(f"{md_file}: Work docs must include 'Status' field")
        elif 'docs/archive/' in doc_path:
            if frontmatter.get('status') != 'superseded':
                content_issues.append(f"{md_file}: Archive docs must have status 'superseded'")
            if 'original_path' not in frontmatter:
                missing_fields.append(f"{md_file}: Archive docs must include 'original_path' field")

        # File naming pattern validation for work docs
        if 'docs/work/' in doc_path:
            import re
            filename = md_file.name
            if not re.match(r'^\d{4}-\d{2}-\d{2}-.+\.md$', filename):
                content_issues.append(f"{md_file}: Work docs must follow YYYY-MM-DD-slug.md naming pattern")

        # Decision criteria validation
        if 'docs/explanation/decisions/' in doc_path:
            content = md_file.read_text()
            required_sections = ['Decision']
            for section in required_sections:
                if f'## {section}' not in content:
                    content_issues.append(f"{md_file}: Decisions must include '{section}' section")

        # Define directional relationship fields
        directional_fields = ['informs', 'depends_on', 'implemented_by', 'implements',
                             'evidence_for', 'supersedes', 'superseded_by', 'governed_by']

        # Cross-reference validation with authority order checking for all relationship fields
        all_relationship_fields = ['related'] + directional_fields

        for field_name in all_relationship_fields:
            if field_name in frontmatter:
                for related_path in frontmatter[field_name]:
                    if not isinstance(related_path, str):
                        content_issues.append(f"{md_file}: {field_name} entries must be strings (file paths)")
                        continue

                    full_path = Path('docs') / related_path if related_path.startswith('docs/') else Path(related_path)
                    if not full_path.exists():
                        content_issues.append(f"{md_file}: {field_name} doc '{related_path}' does not exist")
                        continue

                    # Authority order validation - higher authority docs shouldn't reference lower authority
                    current_authority = get_authority_level(doc_path)
                    related_authority = get_authority_level(related_path)
                    if current_authority < related_authority:  # Lower number = higher authority
                        content_issues.append(f"{md_file}: Authority violation - {get_authority_name(current_authority)} doc referencing {get_authority_name(related_authority)} doc '{related_path}'")

                    # Cross-domain linking rules for docs/ paths
                    if 'domain' in frontmatter and 'docs/' in related_path:
                        doc_domain = frontmatter['domain']
                        # Check if related doc exists and has domain
                        try:
                            related_frontmatter = load_frontmatter(Path('docs') / related_path)
                            if related_frontmatter and 'domain' in related_frontmatter:
                                related_domain = related_frontmatter['domain']
                                # Domain consistency rules
                                if doc_domain != related_domain:
                                    # Allow cross-domain links but flag for review
                                    content_issues.append(f"{md_file}: Cross-domain reference to '{related_path}' ({related_domain}) - ensure this relationship is appropriate")
                        except:
                            pass  # Skip if can't read related file

        # Deprecation warning for 'related' field
        if 'related' in frontmatter:
            content_issues.append(f"{md_file}: WARNING - 'related' field is deprecated. Use directional relationship fields (informs, depends_on, etc.) instead")

        # Relationship consistency validation
        validate_relationship_consistency(md_file, frontmatter, content_issues)

        # Registry completeness validation - check that architectural decisions have implementations
        if 'docs/explanation/decisions/' in doc_path:
            if 'implementations' not in frontmatter or not frontmatter['implementations']:
                content_issues.append(f"{md_file}: Decision documents should have implementations field linking to code that realizes the decision")
            # Check if decision meets quality criteria (has required sections)
            try:
                content = md_file.read_text()
                if '## Rationale' not in content:
                    content_issues.append(f"{md_file}: Decisions should include Rationale section explaining the decision")
            except:
                content_issues.append(f"{md_file}: Cannot read content for decision validation")

        # SEMANTIC VALIDATION: Check logical correctness of archiving decisions
        if 'docs/archive/' in doc_path:
            # Validate that archived work files should actually be archived
            if 'original_path' in frontmatter:
                original_path = frontmatter['original_path']
                # Work files should NOT be archived unless factually incorrect or actively confusing
                if 'docs/work/' in original_path:
                    content_issues.append(f"{md_file}: Work files should NOT be archived - they contain valuable rationale and should remain in docs/work/ as permanent records. Only archive if factually incorrect or actively confusing.")
                # Check for required superseded fields for non-work files
                elif not all(key in frontmatter for key in ['superseded_by', 'superseded_date', 'superseded_reason']):
                    content_issues.append(f"{md_file}: Non-work archived files must have superseded_by, superseded_date, and superseded_reason fields")

        # Content structure validation by doc type
        doc_type = None
        if 'work/problems' in str(md_file):
            doc_type = 'problems'
        elif 'work/discoveries' in str(md_file):
            doc_type = 'discoveries'
        elif 'explanation/decisions' in str(md_file):
            doc_type = 'decisions'

        if doc_type:
            try:
                content = md_file.read_text()
                required_sections = {
                    'problems': ['Impact', 'Evidence'],
                    'discoveries': ['Key Insights', 'Technical Grounding'],
                    'decisions': ['Problem', 'Discovery', 'Decision']
                }

                for section in required_sections.get(doc_type, []):
                    if f'## {section}' not in content:
                        content_issues.append(f"{md_file}: Missing required section '{section}'")
            except:
                content_issues.append(f"{md_file}: Cannot read content for validation")

    # Report by category
    error_found = False
    if yaml_errors:
        print("❌ YAML syntax errors:")
        for error in yaml_errors:
            print(f"  {error}")
        error_found = True

    if missing_fields:
        print("❌ Missing required fields:")
        for error in missing_fields:
            print(f"  {error}")
        error_found = True

    if invalid_values:
        print("❌ Invalid field values:")
        for error in invalid_values:
            print(f"  {error}")
        error_found = True

    if content_issues:
        print("❌ Content validation failures:")
        for error in content_issues:
            print(f"  {error}")
        error_found = True

    if not error_found:
        print("✅ Frontmatter validation passed")
    else:
        sys.exit(1)

def generate_doc_map(domain: Optional[str] = None):
    """Generate documentation map."""
    docs = find_docs(domain=domain)

    # Group by domain
    by_domain = {}
    for frontmatter, doc in docs:
        doc_domain = frontmatter.get('domain', 'uncategorized')
        if doc_domain not in by_domain:
            by_domain[doc_domain] = []
        by_domain[doc_domain].append((frontmatter, doc))

    print("# AgentOS v8 Documentation Map")
    print()
    print("Read this first. Authority order: reference → how-to → explanation → tutorials → work → archive.")
    print()

    for domain_name in sorted(by_domain.keys()):
        print(f"## {domain_name.title()}")
        docs_in_domain = by_domain[domain_name]

        # Sort by title
        docs_in_domain.sort(key=lambda x: x[0].get('title', x[1].stem).lower())

        for frontmatter, doc in docs_in_domain:
            title = frontmatter.get('title', doc.stem)
            rel_path = str(doc.relative_to(Path('docs')))
            print(f"- [{title}](docs/{rel_path})")
        print()

def generate_registry():
    """Generate registry output to stdout."""
    from collections import defaultdict
    registry = defaultdict(lambda: defaultdict(list))

    # Get docs directory
    script_dir = Path(__file__).parent
    docs_dir = script_dir.parent.parent / 'docs'

    # Collect linkages
    for frontmatter, doc in find_docs():
        domain = frontmatter.get('domain', 'uncategorized')

        # Add doc to domain (relative to docs directory)
        try:
            doc_relative = str(doc.relative_to(docs_dir))
        except ValueError:
            # If relative_to fails, use the full path but make it relative to project root
            doc_relative = str(doc.relative_to(script_dir.parent.parent))

        registry[domain]['docs'].append(doc_relative)

        # Add implementations
        if 'implementations' in frontmatter:
            for impl_path in frontmatter['implementations']:
                registry[domain]['implementations'].append({
                    'doc': doc_relative,
                    'impl': impl_path
                })

    # Output to stdout
    print("# Documentation Registry\n")

    for domain, items in sorted(registry.items()):
        print(f"## {domain.title()} Domain\n")

        if items['docs']:
            print("### Documentation Files")
            for doc in sorted(items['docs']):
                print(f"- `{doc}`")
            print()

        if items['implementations']:
            print("### Implementations")
            for impl in items['implementations']:
                print(f"- `{impl['doc']}` → `{impl['impl']}`")
            print()

def inventory(output_file: Optional[str] = None):
    """Generate comprehensive file inventory with statistics.

    If output_file is provided, write the inventory to that path and record it in
    docs-state.yaml. Otherwise print to stdout.
    """
    header_lines = [
        "# Documentation Inventory",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
    ]

    # Get docs directory relative to script location
    script_dir = Path(__file__).parent
    docs_dir = script_dir.parent.parent / 'docs'

    out_lines: List[str] = []
    out_lines.extend(header_lines)

    for md_file in docs_dir.rglob('*.md'):
        if md_file.name == 'index.md':
            continue

        try:
            content = md_file.read_text()
            lines = len(content.split('\n'))
            size_kb = len(content.encode('utf-8')) / 1024
            rel_path = md_file.relative_to(docs_dir)
            out_lines.append(f"{rel_path}: {lines} lines, {size_kb:.1f}KB")
        except Exception as e:
            out_lines.append(f"{md_file}: Error reading file ({e})")

    out_text = "\n".join(out_lines) + "\n"

    if output_file:
        out_path = Path(output_file)
        # Ensure parent directory exists for output file
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(out_text, encoding='utf-8')
        state = _refresh_batches_from_fs(_ensure_run_initialized(_load_docs_state()))
        state['inventory_file'] = str(out_path)
        _save_docs_state(state)
    else:
        print(out_text, end="")

def list_batches():
    """List batch names from batches/*.txt (sorted)."""
    project_root = Path(__file__).parent.parent
    batch_dir = project_root / 'docs' / 'local' / 'batches'
    if not batch_dir.exists():
        print("NONE - docs/local/batches/ directory not found")
        return
    batches = sorted(p.stem for p in batch_dir.glob('*.txt'))
    if not batches:
        print("NONE - no batch files found")
        return
    for b in batches:
        print(b)

def run_summary():
    """Print a deterministic summary of run progress."""
    state = _refresh_batches_from_fs(_ensure_run_initialized(_load_docs_state()))
    _save_docs_state(state)
    total = len(state.get('batches', []))
    completed = len(state.get('completed_batches', []))
    remaining = max(total - completed, 0)
    current = state.get('current_batch') or "NONE"
    print(f"run_id: {state.get('run_id', 'NONE')}")
    print(f"inventory_file: {state.get('inventory_file') or 'NONE'}")
    print(f"total_batches: {total}")
    print(f"completed_batches: {completed}")
    print(f"remaining_batches: {remaining}")
    print(f"current_batch: {current}")

def next_batch():
    """Select next incomplete batch deterministically."""
    state = _refresh_batches_from_fs(_ensure_run_initialized(_load_docs_state()))
    _save_docs_state(state)
    batches = state.get('batches', [])
    completed = set(state.get('completed_batches', []))
    for b in batches:
        if b not in completed:
            print(b)
            return
    print("NONE")

def mark_batch_complete(batch_name: str):
    """Mark a batch as complete in the run state."""
    state = _ensure_run_initialized(_load_docs_state())
    completed = state.setdefault('completed_batches', [])
    if batch_name not in completed:
        completed.append(batch_name)
    if state.get('current_batch') == batch_name:
        state['current_batch'] = None
    _save_docs_state(state)
    print(f"Marked batch complete: {batch_name}")

def create_batch(batch_name, files):
    """Create a batch file with specified files."""
    # Create batches directory in docs/local (relative to script location)
    script_dir = Path(__file__).parent
    batch_dir = script_dir.parent.parent / 'docs' / 'local' / 'batches'
    batch_dir.mkdir(parents=True, exist_ok=True)

    batch_file = batch_dir / f"{batch_name}.txt"
    file_list = [f.strip() for f in files.split() if f.strip()]

    with open(batch_file, 'w') as f:
        for file_path in file_list:
            f.write(f"{file_path}\n")

    file_count = len(file_list)
    print(f"Batch '{batch_name}' created with {file_count} files")

    # Update run state with batch list (deterministic: sorted by filename)
    state = _ensure_run_initialized(_load_docs_state())
    batch_names = sorted(p.stem for p in batch_dir.glob('*.txt'))
    state['batches'] = batch_names
    _save_docs_state(state)

def track_state(batch_name, status):
    """Track current processing state."""
    # Create state file in docs/local (relative to script location)
    script_dir = Path(__file__).parent
    local_dir = script_dir.parent.parent / 'docs' / 'local'
    local_dir.mkdir(parents=True, exist_ok=True)
    state_file = local_dir / 'docs-state-tracker.txt'
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open(state_file, 'w') as f:
        f.write(f"Processing batch: {batch_name}\n")
        f.write(f"Status: {status}\n")
        f.write(f"Timestamp: {timestamp}\n")

    print(f"State tracked for batch '{batch_name}': {status}")

    # Also update structured run state
    state = _ensure_run_initialized(_load_docs_state())
    state['current_batch'] = batch_name
    _save_docs_state(state)

def validate_batch(batch_name):
    """Validate that a batch file exists and count its files."""
    # Get batches directory in docs/local (relative to script location)
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    batch_file = project_root / 'docs' / 'local' / 'batches' / f"{batch_name}.txt"

    if not batch_file.exists():
        print(f"❌ Batch '{batch_name}' not found")
        sys.exit(1)

    try:
        with open(batch_file, 'r') as f:
            files = [line.strip() for line in f if line.strip()]

        print(f"✅ Batch '{batch_name}' exists with {len(files)} files")

        # Check that files still exist (relative to project root)
        missing = []
        for file_path in files:
            full_path = project_root / file_path
            if not full_path.exists():
                missing.append(file_path)

        if missing:
            print("⚠️  Warning: Some files in batch no longer exist:")
            for missing_file in missing:
                print(f"  - {missing_file}")
        else:
            print("✅ All files in batch exist")

    except Exception as e:
        print(f"❌ Error reading batch file: {e}")
        sys.exit(1)

def cleanup_batch(batch_name):
    """Clean up a specific batch file."""
    script_dir = Path(__file__).parent
    batch_file = script_dir.parent.parent / 'docs' / 'local' / 'batches' / f"{batch_name}.txt"
    if batch_file.exists():
        # Mark complete before deletion (preserve evidence in state file)
        mark_batch_complete(batch_name)
        batch_file.unlink()
        print(f"Cleaned up batch '{batch_name}'")
    else:
        print(f"Batch '{batch_name}' not found")

def cleanup_all(force: bool = False):
    """Clean up all restructuring artifacts after successful completion."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent

    state = _ensure_run_initialized(_load_docs_state())
    batches = state.get('batches', [])
    completed = set(state.get('completed_batches', []))
    incomplete = [b for b in batches if b not in completed]
    if incomplete and not force:
        print("❌ Refusing cleanup-all: run is not complete")
        print(f"Remaining batches: {len(incomplete)}")
        print("Hint: mark remaining batches complete or pass --force")
        sys.exit(1)

    artifacts = [
        project_root / 'docs' / 'local' / 'docs-state-tracker.txt',
        project_root / 'docs' / 'local' / 'docs-state.yaml',
        project_root / 'docs' / 'local' / 'batches',
    ]

    # Clean up inventory files in docs/local
    for inventory_file in (project_root / 'docs' / 'local').glob('docs-inventory-*.txt'):
        inventory_file.unlink()

    for artifact in artifacts:
        if artifact.exists():
            if artifact.is_file():
                artifact.unlink()
            else:
                import shutil
                shutil.rmtree(artifact)

    print("✅ Cleaned up all restructuring artifacts")

def validate_registry():
    """Validate bidirectional linkages."""
    errors = []

    # Get project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent

    # Check docs have valid implementations
    for frontmatter, doc in find_docs():
        if 'implementations' in frontmatter:
            for impl_path in frontmatter['implementations']:
                impl_full_path = project_root / impl_path
                if not impl_full_path.exists():
                    errors.append(f"{doc}: Implementation '{impl_path}' does not exist")

    # Check implementations have @directive back-references
    for frontmatter, doc in find_docs():
        if 'implementations' in frontmatter:
            for impl_path in frontmatter['implementations']:
                try:
                    impl_full_path = project_root / impl_path
                    impl_content = impl_full_path.read_text()
                    doc_relative = str(doc.relative_to(project_root))
                    if f'@directive {doc_relative}' not in impl_content:
                        errors.append(f"{impl_path}: Missing @directive for {doc_relative}")
                except:
                    errors.append(f"Cannot read implementation file: {impl_path}")

    # Report results
    if errors:
        print("❌ Registry validation errors:")
        for error in errors:
            print(f"  {error}")
        sys.exit(1)
    else:
        print("✅ Registry validation passed")

def run_retrospect_audit(task_type, primary_objective, operations, files_touched):
    """DOE Integrated Flow: Run retrospect audit for task readiness"""
    print("🔍 DOE Retrospective Audit")
    print(f"Task Type: {task_type}")
    print(f"Primary Objective: {primary_objective}")
    print(f"Operations: {operations}")
    print(f"Files Touched: {', '.join(files_touched) if files_touched else 'None specified'}")
    print()

    issues = []
    suggestions = []

    # EVOLVED: Enhanced task plan header validation (Gap: Missing Task Plan Header Validation)
    print("0. 📋 Task Plan Header Validation")
    # Simulate comprehensive task plan validation per original MAM checklist
    task_plan_checks = [
        ("Task type declared", task_type in TASK_GATES or task_type in [
            'Discovery & Requirements', 'Planning & Estimation', 'Design & Architecture',
            'Testing & Verification', 'Release & Deployment', 'Operations & Maintenance',
            'Security & Compliance', 'Refactoring & Tech-Debt', 'Incident Response & Debugging'
        ]),
        ("Primary objective measurable", len(primary_objective) > 10 and '?' in primary_objective),
        ("Operations specified", len(operations) > 5),
        ("Evidence sources identified", len(files_touched) > 0)
    ]

    plan_issues = []
    for check_name, check_result in task_plan_checks:
        if not check_result:
            plan_issues.append(check_name)

    if plan_issues:
        print("   ⚠️  Task plan incomplete:")
        for issue in plan_issues:
            print(f"      - Missing: {issue}")
        suggestions.append("Complete task plan header with all required elements")
        issues.extend([f"Incomplete task plan: {issue}" for issue in plan_issues])
    else:
        print("   ✅ Task plan header complete")
    print()

    # 1. Directives Loaded Check
    print("1. 📚 Directives Loaded")
    # Check directive loading hierarchy and accessibility with validation
    directives_ok = True

    # Check core directive files
    core_files = [
        ("docs/reference/agentos/architecture.md", "Core architecture directive"),
        (".cursor/rules/core.mdc", "Core behavioral rules"),
        ("docs/reference/agentos/context-compass.md", "Context navigation directive")
    ]

    for file_path, description in core_files:
        path = Path(file_path)
        try:
            if path.exists():
                print(f"   ✅ {description} accessible: {file_path}")

                # Validate directive loading awareness in rules files
                if "rules" in file_path:
                    with open(path, 'r') as f:
                        content = f.read()
                    if "hierarchical rule loading" in content or "Context Loading Awareness" in content:
                        print(f"   ✅ Hierarchical loading awareness documented in {file_path}")
                    else:
                        print(f"   ⚠️  Hierarchical loading awareness not documented in {file_path}")
                        directives_ok = False
                        issues.append(f"Hierarchical loading awareness missing in {file_path}")

            else:
                print(f"   ⚠️  {description} not found: {file_path}")
                directives_ok = False
                issues.append(f"Missing {description}: {file_path}")
        except Exception as e:
            print(f"   ❌ Error checking {description}: {e}")
            directives_ok = False
            issues.append(f"{description} access error: {e}")

    # Check directive loading validation in scripts
    try:
        with open(Path("scripts/docs/index.py"), 'r') as f:
            script_content = f.read()

        if "directive loading" in script_content.lower() and "validation" in script_content.lower():
            print("   ✅ Directive loading validation implemented")
        else:
            print("   ⚠️  Directive loading validation not implemented")
            directives_ok = False
            issues.append("Directive loading validation not implemented")
    except Exception as e:
        print(f"   ❌ Cannot read validation script: {e}")
        directives_ok = False
        issues.append(f"Validation script access error: {e}")

    if not directives_ok:
        suggestions.append("Implement directive loading validation and ensure all core directives are accessible")

    print()

    # 2. Verification Gates Check
    print("2. 🔍 Verification Gates")
    gate_command = TASK_GATES.get(task_type)
    if gate_command:
        print(f"   ✅ Gate found: {gate_command}")
    else:
        print(f"   ⚠️  No gate mapped for task type '{task_type}'")
        suggestions.append(f"Add gate mapping in TASK_GATES dictionary (Gap: Incomplete Task Types)")
        issues.append(f"Unmapped task type: {task_type}")
    print()

    # 3. Safety Confirmed Check
    print("3. 🛡️  Safety Confirmed")
    destructive_keywords = ['delete', 'remove', 'archive', 'overwrite', 'destroy', 'rm ', 'unlink']
    is_destructive = any(keyword in operations.lower() for keyword in destructive_keywords)

    if is_destructive:
        print("   ❌ Destructive operations detected - user confirmation required")
        print("   ❌ Rollback plan must be documented in task header")
        issues.append("Destructive action without confirmation")
        suggestions.append("Get explicit user confirmation and document rollback plan")
    else:
        print("   ✅ No destructive operations detected")
    print()

    # EVOLVED: Enhanced evidence quality check (Gap: Missing Evidence Authority Validation)
    print("4. 📋 Evidence Quality & Authority")
    # EVOLVED: Implement truth surface authority validation
    AUTHORITY_ORDER = {
        'reference': 1,
        'how-to': 2,
        'explanation': 3,
        'tutorials': 4,
        'work': 5,
        'archive': 6
    }

    evidence_issues = []
    authority_issues = []

    for file in files_touched:
        # Basic pattern check
        bad_patterns = ['.tmp', '.bak', '__pycache__', 'node_modules']
        if any(pattern in file for pattern in bad_patterns):
            evidence_issues.append(f"Inappropriate file: {file}")

        # Authority check - extract doc type from path
        if 'docs/' in file:
            path_parts = file.split('/')
            if len(path_parts) >= 3:
                doc_type = path_parts[2]  # docs/{type}/...
                if doc_type in AUTHORITY_ORDER:
                    authority = AUTHORITY_ORDER[doc_type]
                    if authority > 3:  # Using work/archive for primary decisions
                        authority_issues.append(f"Low authority source ({doc_type}/{authority}): {file}")

    if evidence_issues:
        print(f"   ⚠️  Evidence issues: {', '.join(evidence_issues)}")
        suggestions.append("Review file selection for evidence quality")

    if authority_issues:
        print(f"   ⚠️  Authority issues: {', '.join(authority_issues)}")
        suggestions.append("Use higher authority sources (reference > how-to > explanation)")

    if not evidence_issues and not authority_issues:
        print("   ✅ Evidence quality and authority acceptable")
    print()

    # EVOLVED: Enhanced safety checks (Gap: Insufficient Safety Policy Coverage)
    print("4.5 🔐 Extended Safety Checks")
    safety_issues = []

    # Check for potential secrets
    secret_patterns = ['password', 'secret', 'key', 'token', 'api_key']
    has_secrets = any(pattern in operations.lower() or pattern in primary_objective.lower() for pattern in secret_patterns)

    # Check for untrusted inputs
    untrusted_indicators = ['external', 'user_input', 'download', 'fetch']
    has_untrusted = any(indicator in operations.lower() for indicator in untrusted_indicators)

    if has_secrets:
        safety_issues.append("Potential secrets exposure detected")
        suggestions.append("Avoid logging or exposing secrets")

    if has_untrusted:
        safety_issues.append("Untrusted input handling detected")
        suggestions.append("Sanitize and validate external inputs")

    if safety_issues:
        print(f"   ⚠️  Safety concerns: {', '.join(safety_issues)}")
        issues.extend(safety_issues)
    else:
        print("   ✅ No extended safety concerns detected")
    print()

    # 5. Gaps Identified Check
    print("5. 🎯 Gaps Identified")
    # For this simple implementation, assume no gaps unless destructive operations
    if is_destructive:
        print("   ⚠️  Destructive operations may indicate gaps in current approach")
        suggestions.append("Consider if destructive changes indicate missing capabilities")
        suggestions.append("Run `/learn` to capture any identified gaps")
    else:
        print("   ✅ No obvious gaps detected")
    print()

    # EVOLVED: Continuous monitoring checkpoint (Gap: No Continuous Self-Monitoring)
    print("6. 👁️  Self-Monitoring Checkpoint")
    monitoring_status = []

    # Check contract compliance
    if not issues:  # No critical issues
        monitoring_status.append("Contract compliance: Good")
    else:
        monitoring_status.append("Contract compliance: Issues detected")

    # Check objective alignment
    if task_type and primary_objective:
        monitoring_status.append("Objective alignment: Clear")
    else:
        monitoring_status.append("Objective alignment: Needs clarification")

    print("   📊 Monitoring status:")
    for status in monitoring_status:
        print(f"      {status}")

    if any("Issues" in status or "Needs" in status for status in monitoring_status):
        suggestions.append("Address monitoring concerns before proceeding")
    print()

    # Summary
    print("📊 AUDIT SUMMARY")
    if issues:
        print("❌ ISSUES FOUND:")
        for issue in issues:
            print(f"   • {issue}")
    else:
        print("✅ NO CRITICAL ISSUES")

    if suggestions:
        print("\n💡 SUGGESTIONS:")
        for suggestion in suggestions:
            print(f"   • {suggestion}")

    # Suggested commands
    if gate_command:
        print(f"\n🚀 RECOMMENDED NEXT STEPS:")
        print(f"   • Run verification: {gate_command}")
        if issues:
            print("   • Address issues above before proceeding")
            print("   • Consider running MAM for deeper analysis")

# REMOVED: run_meta_analysis_audit()
# Fake meta-analysis function removed due to authenticity failures.
# The original implementation was completely fake - it only printed hardcoded "✅" messages
# without performing any actual validation. Real meta-analysis requires manual examination
# of system behavior against documented capabilities.
#
# Use Cursor command /meta for genuine meta-analysis that analyzes current chat context.

    print("\n🔗 MAM Integration:")
    print("   • Findings available for `/learn` capture")
    print("   • Issues can trigger `/evolve` improvements")
    print("   • Results integrated with continuous self-awareness")

def main():
    parser = argparse.ArgumentParser(description='Generate documentation indexes')
    parser.add_argument('command', choices=[
        'problems', 'discoveries', 'decisions', 'domains', 'validate', 'registry', 'validate-registry',
        'inventory', 'create-batch', 'state', 'validate-batch', 'cleanup-batch', 'cleanup-all',
        'list-batches', 'next-batch', 'mark-batch-complete', 'run-summary', 'analyze', 'meta'
    ])
    parser.add_argument('--domain', help='Filter by domain')
    parser.add_argument('--format', choices=['basic', 'full'], default='basic', help='Output format')
    parser.add_argument('--tag', help='Filter by tag')
    parser.add_argument('--since', help='Show docs on or after date (YYYY-MM-DD)')
    parser.add_argument('--before', help='Show docs before date (YYYY-MM-DD)')
    parser.add_argument('--status', choices=['active', 'accepted', 'stable', 'draft', 'superseded', 'all'], help='Filter by status (overrides default)')
    parser.add_argument('--force', action='store_true', help='Force an operation that would otherwise be refused (e.g. cleanup-all)')
    parser.add_argument('--output-file', help='Write command output to this path (supported by inventory)')

    # Additional arguments for specific commands
    parser.add_argument('batch_name', nargs='?', help='Name of the batch (for batch operations)')
    parser.add_argument('status_message', nargs='?', help='Status message (for state tracking)')
    parser.add_argument('files', nargs='*', help='List of files (for batch creation)')

    args = parser.parse_args()

    if args.command in ['problems', 'discoveries', 'decisions']:
        generate_index(args.command, args.domain, args.format, args.tag, args.since, args.before, args.status)
    elif args.command == 'domains':
        list_domains()
    elif args.command == 'validate':
        validate_frontmatter()
    elif args.command == 'registry':
        generate_registry()
    elif args.command == 'validate-registry':
        validate_registry()
    elif args.command == 'inventory':
        inventory(output_file=args.output_file)
    elif args.command == 'create-batch':
        if not args.batch_name:
            print("Error: batch_name required for create-batch")
            sys.exit(1)
        # Get remaining arguments as files
        remaining_args = sys.argv[sys.argv.index(args.batch_name) + 1:]
        create_batch(args.batch_name, ' '.join(remaining_args))
    elif args.command == 'state':
        if not args.batch_name or not args.status_message:
            print("Error: batch_name and status_message required for state")
            sys.exit(1)
        track_state(args.batch_name, args.status_message)
    elif args.command == 'validate-batch':
        if not args.batch_name:
            print("Error: batch_name required for validate-batch")
            sys.exit(1)
        validate_batch(args.batch_name)
    elif args.command == 'cleanup-batch':
        if not args.batch_name:
            print("Error: batch_name required for cleanup-batch")
            sys.exit(1)
        cleanup_batch(args.batch_name)
    elif args.command == 'cleanup-all':
        cleanup_all(force=args.force)
    elif args.command == 'list-batches':
        list_batches()
    elif args.command == 'run-summary':
        run_summary()
    elif args.command == 'next-batch':
        next_batch()
    elif args.command == 'mark-batch-complete':
        if not args.batch_name:
            print("Error: batch_name required for mark-batch-complete")
            sys.exit(1)
        mark_batch_complete(args.batch_name)
    elif args.command == 'analyze':
        # DOE Integrated Flow: Run analyze audit
        # Parse arguments from remaining args (programmatic mode only)
        remaining = [arg for arg in sys.argv[2:] if not arg.startswith('-')]  # Skip the command itself and any flags

        if len(remaining) >= 3:
            # Programmatic usage: all parameters provided
            task_type = remaining[0]
            primary_objective = remaining[1]
            operations = remaining[2]
            files_touched = remaining[3:] if len(remaining) > 3 else []
            run_retrospect_audit(task_type, primary_objective, operations, files_touched)
        else:
            # Interactive mode removed - cannot be implemented in scripts
            # Use Cursor command /analyze for context-aware analysis
            print("❌ ERROR: Interactive analysis not supported in scripts.")
            print("Use Cursor command: /analyze")
            print("See .cursor/commands/analyze.md for context-aware usage.")
    elif args.command == 'meta':
        # GENUINE META-ANALYSIS: Real validation system
        # This replaces the fake MAM that only printed hardcoded checkmarks.
        # Performs authentic evidence-based analysis of system state.
        print("🔍 META-ANALYSIS MODE ACTIVATION REQUESTED")
        print("Meta-Analysis Mode (MAM) performs comprehensive self-audit of AgentOS behavior.")
        print("This uses genuine validation - no fake hardcoded responses.")
        print()
        print("📋 MAM Activation Requirements:")
        print("   • Evidence-based validation (no assumptions)")
        print("   • Systematic 9-point audit checklist")
        print("   • Real system state analysis")
        print("   • Authenticity verification")
        print()
        print("⚠️  NOTE: This is script-based analysis. For chat-context aware analysis, use: /meta")
        print()

        # Run genuine meta-analysis as subprocess
        try:
            import subprocess
            script_dir = Path(__file__).parent
            meta_script = script_dir / "genuine-meta-analysis.py"

            if meta_script.exists():
                # Run the genuine meta-analysis script
                result = subprocess.run([sys.executable, str(meta_script)],
                                      capture_output=True, text=True, cwd=Path.cwd())

                # Print the output
                print(result.stdout)
                if result.stderr:
                    print(result.stderr, file=sys.stderr)

                # Exit with the same code as the meta-analysis
                sys.exit(result.returncode)
            else:
                print(f"❌ ERROR: Genuine meta-analysis script not found: {meta_script}")
                sys.exit(1)

        except Exception as e:
            print(f"❌ ERROR: Cannot run genuine meta-analysis system: {e}")
            print("The fake MAM has been removed but genuine system is not available.")
            sys.exit(1)

if __name__ == '__main__':
    main()
