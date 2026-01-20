---
title: "Writing Effective Documentation"
status: stable
created_date: 2026-01-16
purpose: "Guide for creating clear, well-structured documentation using v8's dual architecture"
domain: docs
---

# Writing Effective Documentation

## Overview
This guide helps you create clear, well-structured documentation following v8's documentation system. See `docs/reference/docs/doc-authority.md` for complete Diátaxis framework and content type selection criteria.

## Documentation Structure Basics
Before writing, understand the documentation system:
- **Diátaxis buckets**: Reference, how-to, explanation, tutorials, work, archive
- **Domain organization**: Group by functional area (agentos, docs, dev)
- **Authority order**: Reference facts override procedural guidance
- **Content lifecycle**: Work content matures into authoritative documentation

See `docs/reference/docs/doc-authority.md` for detailed content type selection guidance.

## Documentation Distillation

Use the `/distill` command to semantically compress verbose content into high-density reference material.

### Scaffolding vs. Structure
Effective distillation requires distinguishing between two types of content:

- **Scaffolding** (Remove): The context needed to *create* the knowledge.
    - Historical debates ("We considered A vs B...")
    - Temporal context ("Yesterday we found...")
    - Author narrative ("I think we should...")
    - Obsolete paths ("First we tried X, but it failed...")

- **Structure** (Keep): The load-bearing knowledge needed to *use* the system.
    - Final decisions ("Use A.")
    - Invariants & Constraints ("MUST NOT do X.")
    - Configuration schemas
    - Directives & Commands

### When to Use /distill vs /refine

| Use `/distill` when... | Use `/refine` when... |
|------------------------|-----------------------|
| You have a verbose "Work" or "Explanation" doc and want a concise "Reference" entry. | You have multiple fragmented docs and want to consolidate them. |
| You want to remove history/debate and keep only the verdict. | You want to organize content without losing detail. |
| You are optimizing for AI context window efficiency. | You are optimizing for human readability and structure. |
| **Output**: High-density "Contract" or "Imperative" mode. | **Output**: Standard Diátaxis format. |

### Target Output Modes

Distillation transforms content into one of two modes:

1.  **Imperative Mode** (for Procedures):
    *   *Original*: "We found that setting the timeout to 5s helps prevent hanging."
    *   *Distilled*: "Set timeout to 5s to prevent hangs."

2.  **Contract Mode** (for References):
    *   *Original*: "The system is designed to reject any request that doesn't have a valid auth token in the header."
    *   *Distilled*: "Invariant: Requests MUST include valid Auth header."

## Technical Detail Guidelines

### Discoveries: Include Actionable Technical Insights
**Purpose**: Document technical insights that enable better implementation.

**Include**:
- **What**: Key technical mechanisms and implementation patterns
- **Why**: Why this approach works better than alternatives
- **How**: Enough detail to implement or validate the approach
- **Examples**: Concrete code patterns, configuration examples

**Example Good Discovery**:
```markdown
# YAML Character Efficiency

## Key Insights
- YAML provides structured, character-efficient representation
- Explicit structure prevents natural language drift in multi-step reasoning
- Character efficiency reduces context window pressure

## Implementation Patterns
- Use YAML for state representation to maintain consistency
- Structure decision flows explicitly to prevent entropy
- Leverage YAML's format for compact context storage
```

### Decisions: Focus on Trade-offs and Validation
**Purpose**: Document choices that required analysis of alternatives.

**Include**:
- **Context**: What problem required a decision
- **Alternatives**: What other options were considered
- **Trade-offs**: What was gained/lost with this choice
- **Validation**: How to verify the decision was correctly implemented

**Example Good Decision**:
```markdown
# Decision: YAML State Representation

## Problem
[Context Window Drift Prevention](docs/work/problems/2026-01-16-context-drift.md)

## Discovery
[YAML Character Efficiency](docs/work/discoveries/2026-01-16-yaml-efficiency.md)

## Decision
Use YAML for state representation to maintain reasoning consistency.

## Trade-offs
- **Gained**: Character efficiency, structure, drift prevention
- **Lost**: Some human readability compared to prose
- **Risk**: YAML parsing complexity vs natural language flexibility

## Validation Criteria
- State files load within 2 seconds
- Multi-step reasoning maintains consistency across 10+ steps
- Context window usage reduced by 30%
```

### Reference: Exhaustive Technical Details
**Purpose**: Provide complete technical specifications.

**Include**:
- Complete API specifications
- Implementation requirements
- Edge cases and error handling
- Performance characteristics
- Migration guides

## Decision Identification Criteria

### Is This a Decision? (Check ALL that apply)
- [ ] Required active choice between meaningful alternatives
- [ ] Involved analysis of trade-offs and consequences
- [ ] Could have been implemented differently with different benefits
- [ ] Has clear criteria for validating correct implementation
- [ ] Represents a policy or architectural choice that affects multiple components

### If NOT a decision:
- **Document as discovery**: Technical insight about how something works
- **Include in how-to**: Step-by-step procedure
- **Add to reference**: Complete technical specification
- **Link from existing docs**: Reference in related decisions/discoveries

**Examples**:
- ✅ **Decision**: Choosing YAML over JSON for state representation (trade-offs analysis)
- ❌ **Not a decision**: Documenting that @mentions work in Cursor (existing feature)

## Terminology Precision

### Content Types
- **Drafts**: Content becoming canonical (Diátaxis work)
- **Research**: Valuable insights, may never become canonical (Development work)
- **Temporary**: Development artifacts, likely discarded (Local)
- **Historical**: Preserved for reference (Archive)
- **Canonical**: Authoritative, stable documentation (Diátaxis buckets)

### Technical Terms
- Use precise terms: "deterministic execution" not "consistent behavior"
- Define acronyms on first use: "YAML (YAML Ain't Markup Language)"
- Prefer specific terms: "context window drift" not "memory issues"

## Validation and Quality Checks

### Decision Quality Checklist
- [ ] Clear problem statement with evidence
- [ ] Discovery links explaining technical insights
- [ ] Alternative options explicitly considered
- [ ] Trade-offs explicitly stated (gains/losses)
- [ ] Implementation validation criteria provided
- [ ] Cross-references to related docs work
- [ ] Status and update criteria clear

### Discovery Quality Checklist
- [ ] Technical mechanism clearly explained with examples
- [ ] Implementation insights actionable for developers
- [ ] Why this approach works better than alternatives
- [ ] Links to related decisions and references
- [ ] Status indicates whether insight is active or incorporated

### General Quality Checklist
- [ ] Follows appropriate Diátaxis bucket or Development tier
- [ ] Uses precise terminology without jargon
- [ ] Includes working cross-references
- [ ] Has clear status and ownership
- [ ] Content is self-contained but well-linked
- [ ] Examples are concrete and realistic

## Common Pitfalls to Avoid

### 1. Wrong Content Type
- **Problem**: Research in reference docs, procedures in explanation
- **Fix**: Use the selection guide above, get feedback if unsure

### 2. Inconsistent Technical Detail
- **Problem**: Discoveries too vague, reference docs overwhelming
- **Fix**: Follow the technical detail guidelines for each content type

### 3. Decision Inflation
- **Problem**: Everything documented as "decisions"
- **Fix**: Use the decision identification criteria

### 4. Terminology Confusion
- **Problem**: "Drafts" vs "research" vs "temporary" used interchangeably
- **Fix**: Use precise terms from the terminology section

### 5. Missing Validation
- **Problem**: Decisions without clear implementation criteria
- **Fix**: Always include validation criteria for decisions

## Inline Annotations and Registry

### @directive Annotations
Use `@directive docs/path/to/doc.md` in code files to establish traceability to governing documentation:

```python
# @directive docs/reference/agentos/behavior-spec.md
def execute_task(task):
    # This function implements the behavior spec
    pass
```

**Best Practices:**
- Place as the first comment in implementation files
- Use full paths from project root (e.g., `docs/reference/agentos/behavior-spec.md`)
- Update when code moves to maintain traceability

### implementations Field
Link documentation to implementing code using the frontmatter `implementations` field:

```yaml
---
implementations:
  - scripts/agentos/validate_registry.py
  - scripts/agentos/validate_routing.py
---
```

**Validation:** Registry validation ensures bidirectional consistency between docs and code.

### Registry Commands
Use these commands to maintain and validate the documentation registry:

- `just docs::registry` - Generate current doc-code relationship map
- `just docs::validate-registry` - Validate all bidirectional linkages

## Advanced Validation Features

### Error Categories
Validation provides categorized errors for efficient debugging:

- **❌ YAML syntax errors**: Frontmatter parsing issues
- **❌ Missing required fields**: Absent `title`, `status`, `date`
- **❌ Invalid field values**: Wrong enums, malformed dates, invalid types
- **❌ Content validation failures**: Missing sections, broken links, structure issues

### Advanced Filtering
Use command-line options for sophisticated document queries:

```bash
# Filter by tags
just docs::list-decisions --tag performance

# Filter by date range
just docs::list-problems --since 2026-01-10

# Override status filtering
just docs::list-discoveries --status all
```

## Getting Help
- Review existing docs in the same category for style and structure
- Check cross-references work and provide value
- Get feedback from other contributors before finalizing
- Use the quality checklists to self-review

## Documenting External Knowledge Integration

### External Source Anchoring
When documenting features that integrate external knowledge:

- Specify the Diátaxis classification of external sources
- Include examples of external resource types
- Document caching and persistence strategies
- Provide guidance on when to use web URLs vs MCP tools

### Example External Integration Documentation
```markdown
## External Knowledge Integration

This feature integrates external knowledge sources:

- **Reference**: Context7 for API documentation (Diátaxis: reference)
- **How-to**: Web tutorials for implementation guidance (Diátaxis: how-to)
- **Caching**: Introductions cached locally, full content accessed on-demand
```