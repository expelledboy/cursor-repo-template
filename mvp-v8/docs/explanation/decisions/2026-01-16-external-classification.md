---
title: "Decision: Diátaxis-Based External Source Classification"
status: accepted
created_date: 2026-01-16
purpose: "Classify external knowledge sources using Diátaxis principles"
domain: agentos
related:
  - docs/work/problems/2026-01-16-cursor-integration.md
  - docs/work/discoveries/2026-01-16-external-classification.md
---

# Decision: Diátaxis-Based External Source Classification

## Decision
Addresses [Cursor Integration Depth](docs/work/problems/2026-01-16-cursor-integration.md) using insights from [Diátaxis-Based External Source Classification](docs/work/discoveries/2026-01-16-external-classification.md).
Classify external knowledge sources using Diátaxis principles (reference, how-to, explanation, tutorial) for appropriate handling and persistence. Implement automatic classification when external sources are referenced in reasoning.

## Trade-offs
- **Gained**: Consistent external knowledge handling, appropriate caching/persistence, Diátaxis alignment
- **Gained**: Context efficiency through content-type aware loading
- **Lost**: Classification complexity for ambiguous external content
- **Lost**: Manual classification may be needed for edge cases
- **Risk**: Incorrect classification leading to inappropriate persistence
- **Risk**: Classification overhead for frequently changing external content

## Implementation
- Diátaxis mapping: reference (API specs), how-to (implementation guides), explanation (design docs), tutorial (learning materials)
- Automatic classification: URLs analyzed for content type indicators
- Caching strategy: reference/how-to cached persistently, tutorial/explanation cached temporarily
- Integration points: Context7 (reference), web searches (tutorial), external links in docs
- Validation: Content type consistency checked during reasoning

## Rationale
Diátaxis-based classification enables consistent handling of external knowledge while maintaining separation of concerns. Different content types require different persistence strategies and context treatment. Classification ensures external sources integrate seamlessly with internal documentation architecture.

## Validation Criteria
- External sources correctly classified for 90%+ of common patterns
- Context efficiency improved by 25% through appropriate caching
- Internal/external content treated consistently across Diátaxis boundaries
- Classification errors detected within reasoning workflows
- Manual override available for misclassified content

## See Also
- [Documentation Authority](docs/reference/docs/doc-authority.md) - Diátaxis framework reference
- [Diátaxis-Based External Source Classification](docs/work/discoveries/2026-01-16-external-classification.md) - Technical grounding for classification