# Visual Maps Standards (Reference)

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Define standards for visual process maps (Mermaid diagrams) used as supplementary guidance in AgentOS reference docs.

---

## 1. Scope and intent
- Diagrams are supplementary; text contracts remain authoritative.
- Applies to reference docs that include visual process maps.
- All diagram content must already exist in the text.

## 2. Authority statement (required after every diagram)
> **Note:** This diagram is supplementary. The authoritative contract is in [Section X: Title] above. See `docs/reference/agentos/[file].md#[section-anchor]` for complete requirements.

Requirements:
- Present immediately after each diagram code block.
- Section link must reference the authoritative text section that the diagram summarizes.

## 3. Mermaid syntax conventions
- Format: `graph TD`
- Node IDs: camelCase (e.g., `checkDD`, `loadDir`)
- Decision nodes: `{Question?}` syntax
- Edge labels: `|label|`
- Line breaks inside labels: use `\n` (do not use HTML)
- No styling directives (allow default theme)
- No click actions or custom CSS

## 4. Content requirements
- Diagrams show structure/flow; text holds authority and nuance.
- Every decision/path in the diagram must exist in the text contract.
- Section references in authority statements must resolve to real anchors.

## 5. Placement rules
- Place diagrams immediately after the section they summarize.
- Follow with the authority statement before the next heading.

## 6. Accessibility
- Provide text description in surrounding prose; all information must be readable without the diagram.
- Avoid color-dependent meaning in diagrams.

## 7. Maintenance and validation
- Update diagrams whenever the underlying contract text changes.
- Validation script (`scripts/agentos/validate_visual_maps.py`) must check:
  - Mermaid block presence and `graph TD`
  - Authority statement presence
  - Section reference presence and resolution
- Include diagram review in doc/ADR changes that affect covered sections.

## 8. Files currently expected to host diagrams
- `docs/reference/agentos/behavior-spec.md` (task lifecycle)
- `docs/reference/agentos/routing.md` (routing decision tree)
- `docs/reference/agentos/self-improvement.md` (gap promotion flow)
- `docs/reference/agentos/verification-contract.md` (verification gate flow)

