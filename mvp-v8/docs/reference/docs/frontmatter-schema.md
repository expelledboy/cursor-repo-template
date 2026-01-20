---
title: "Frontmatter Schema Reference"
status: stable
created_date: 2026-01-16
purpose: "Complete specification for YAML frontmatter used across all documentation"
domain: docs
implemented_by:
  - scripts/docs/index.py
---

# Frontmatter Schema Reference

## Overview

All documentation files must include YAML frontmatter at the top, defining metadata for indexing, validation, and cross-referencing. This schema provides structured metadata while maintaining human editability.

## Schema Definition

### Required Fields

#### `title` (string)
Human-readable title of the document. Used in index generation and cross-references.

**Example:**
```yaml
title: "Decision: YAML State Representation"
```

#### `status` (enum)
Document lifecycle status. Determines inclusion in indexes and validation behavior.

**Valid Values:**
- `active`: Current/relevant content (problems, discoveries)
- `accepted`: Approved decisions and recommendations
- `stable`: Mature/reference content (specs, guides)
- `draft`: Work-in-progress or temporary content
- `superseded`: Replaced by newer content (includes `superseded_by` field)

**Example:**
```yaml
status: accepted
```

#### `created_date` (YYYY-MM-DD)
Creation/publication date in ISO format. Used for chronological sorting and filtering.

**Example:**
```yaml
created_date: 2026-01-16
```

### Optional Fields

#### `purpose` (string)
Brief description of the document's purpose. Maximum 200 characters recommended to avoid duplication with body content.

**Example:**
```yaml
purpose: "Use YAML for state representation to maintain reasoning consistency"
```

#### `domain` (enum)
Content domain for organization and filtering.

**Valid Values:**
- `agentos`: Core system functionality and architecture
- `docs`: Documentation system itself and processes

**Example:**
```yaml
domain: agentos
```

#### `tags` (array of strings)
Keyword tags for advanced filtering and discovery. Used with `--tag` filtering.

**Example:**
```yaml
tags: ["performance", "reasoning", "yaml"]
```

#### `related` (array of paths) - DEPRECATED
Cross-references to related documents. Validated to ensure links exist.

⚠️ **DEPRECATED**: Use directional relationship fields instead for deterministic traceability.

**Example:**
```yaml
related:
  - docs/work/problems/2026-01-16-context-drift.md
  - docs/work/discoveries/2026-01-16-yaml-efficiency.md
```

### Directional Relationship Fields

#### `informs` (array of paths)
Documents that this document provides information to or influences. Used for forward traceability.

**Example:**
```yaml
informs:
  - docs/explanation/decisions/2026-01-18-deterministic-relationships.md
  - docs/work/discoveries/2026-01-18-meta-learning-capability.md
```

#### `depends_on` (array of paths)
Documents that this document depends on for its information or context. Used for backward traceability.

**Example:**
```yaml
depends_on:
  - docs/reference/agentos/architecture.md
  - docs/reference/docs/frontmatter-schema.md
```

#### `implemented_by` (array of paths)
Code or implementation files that realize this document's specifications.

**Example:**
```yaml
implemented_by:
  - scripts/docs/index.py
  - .cursor/commands/analyze.md
```

#### `implements` (array of paths)
Documents (typically specs or decisions) that this document implements.

**Example:**
```yaml
implements:
  - docs/reference/agentos/architecture.md
  - docs/explanation/decisions/2026-01-16-frontmatter-schema.md
```

#### `evidence_for` (array of paths)
Documents that this document provides evidence or validation for.

**Example:**
```yaml
evidence_for:
  - docs/explanation/decisions/2026-01-16-deterministic-relationships.md
  - docs/work/problems/2026-01-18-nondeterministic-relationships.md
```

#### `supersedes` (array of paths)
Documents that this document replaces or makes obsolete.

**Example:**
```yaml
supersedes:
  - docs/work/discoveries/2026-01-16-old-discovery.md
```

#### `superseded_by` (array of paths)
Documents that replace this document. (Existing field, kept for backward compatibility)

#### `governed_by` (array of paths)
Documents that govern or constrain this document's content or behavior.

**Example:**
```yaml
governed_by:
  - docs/reference/agentos/architecture.md
  - docs/reference/docs/frontmatter-schema.md
```

#### `external_docs` (array of objects)
References to external resources. Enables linking to specifications, tutorials, and other external content.

**Schema:**
```yaml
external_docs:
  - url: "https://example.com/spec"
    type: "reference" | "how-to" | "explanation" | "tutorial"
    title: "External Resource Title"
```

**Example:**
```yaml
external_docs:
  - url: "https://yaml.org/spec/1.2.2/"
    type: "reference"
    title: "YAML 1.2.2 Specification"
```

#### `superseded_by` (path)
For `status: superseded` documents, indicates the replacement document.

**Example:**
```yaml
status: superseded
superseded_by: docs/reference/agentos/spec-active-state.md
```

#### `implementations` (array of strings)
File paths to implementation files that realize this documentation. Enables bidirectional traceability between docs and code. Each path should be relative to the project root.

**Example:**
```yaml
implementations:
  - scripts/agentos/validate_registry.py
  - scripts/agentos/validate_routing.py
```

**Validation:** Implementation files must exist, and must contain `@directive <doc-path>` annotations pointing back to this document.

### Inline Annotations

#### `@directive` Annotations
Code files can include inline `@directive docs/path/to/doc.md` annotations to establish traceability to governing documentation:

```python
# @directive docs/reference/agentos/behavior-spec.md
def execute_task(task):
    # This function implements the behavior spec
    pass
```

**Usage:**
- Place as top comment in implementation files
- Points to the documentation that governs the code
- Validated by `just docs::validate-registry` command
- Enables bidirectional doc-code traceability

## Validation Rules

### Automatic Validation (`just docs::validate`)
Provides categorized error reporting with the following categories:

#### Error Categories
- **❌ YAML syntax errors**: Invalid frontmatter syntax or structure
- **❌ Missing required fields**: `title`, `status`, `date` fields absent
- **❌ Invalid field values**: Wrong status enums, malformed dates, invalid types
- **❌ Content validation failures**: Missing sections, broken links, structure issues

#### Field Validation
- **Presence**: All `.md` files except `index.md` must have frontmatter
- **Required Fields**: `title`, `status`, `created_date` must be present
- **Status Enum**: Must be one of `active`, `draft`, `accepted`, `stable`, `superseded`, `deprecated`
- **Created Date Format**: Must match `YYYY-MM-DD` pattern
- **Cross-References**: All paths in relationship fields (`related`, `informs`, `depends_on`, `implemented_by`, `implements`, `evidence_for`, `supersedes`, `superseded_by`, `governed_by`) must exist
- **External Docs**: Must have `url`, `type`, `title`; `type` must be valid
- **Implementations**: File paths must exist and contain `@directive` annotations
- **Relationship Consistency**: Bidirectional relationships should be consistent (if A `informs` B, B should `depends_on` A)

### Content Structure Validation
Documents are validated for required sections based on type:

- **Problems** (`work/problems/`): Must include "Impact", "Evidence" sections
- **Discoveries** (`work/discoveries/`): Must include "Key Insights", "Technical Grounding" sections
- **Decisions** (`explanation/decisions/`): Must include "Decision" section (Problem/Discovery sections optional for focused decisions)

### Registry Validation (`just docs::validate-registry`)
Validates bidirectional traceability between docs and code:
- Implementation files must exist
- Code files must contain `@directive` annotations pointing back to docs
- Registry generation shows complete doc-code relationships

## Usage Examples

### Problem Document
```yaml
---
title: "Context Window Drift Prevention"
status: active
created_date: 2026-01-16
purpose: "Multi-step agent reasoning can accumulate entropy and lose consistency"
domain: agentos
tags: ["performance", "reasoning"]
related:
  - docs/work/discoveries/2026-01-16-yaml-efficiency.md
---
```

### Decision Document
```yaml
---
title: "Decision: YAML State Representation"
status: accepted
created_date: 2026-01-16
purpose: "Use YAML for state representation to maintain reasoning consistency"
domain: agentos
related:
  - docs/work/problems/2026-01-16-context-drift.md
  - docs/work/discoveries/2026-01-16-yaml-efficiency.md
---
```

### Reference Document
```yaml
---
title: "Spec: Decision Trace"
status: stable
created_date: 2026-01-16
purpose: "Optional structured record of decision paths for auditability"
domain: agentos
external_docs:
  - url: "https://yaml.org/spec/"
    type: "reference"
    title: "YAML Specification"
---
```

## Migration Notes

- All existing documents converted from inline metadata to YAML frontmatter
- Status and date information moved from body to frontmatter
- Cross-references established between related documents
- Validation implemented via `just docs::validate` and `just docs::lint`

## Related Documents

informs:
  - docs/explanation/decisions/2026-01-16-frontmatter-schema.md
  - docs/explanation/architecture/doc-system-rationale.md
  - docs/how-to/docs/writing-effective-docs.md