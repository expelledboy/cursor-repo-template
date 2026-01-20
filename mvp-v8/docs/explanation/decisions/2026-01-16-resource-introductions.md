---
title: "Decision: External Resource Introduction Caching"
status: accepted
created_date: 2026-01-16
purpose: "Cache high-level introductions to external resources"
domain: agentos
related:
  - docs/work/problems/2026-01-16-doc-management.md
  - docs/work/discoveries/2026-01-16-caching-introductions.md
---

# Decision: External Resource Introduction Caching

## Decision
Addresses [Documentation Context Management](docs/work/problems/2026-01-16-doc-management.md) using insights from [External Resource Introduction Caching](docs/work/discoveries/2026-01-16-caching-introductions.md).
Cache high-level introductions to external resources to enable informed access and utilization decisions. Implement introduction caching for MCP tools, web URLs, and Context7 resources with Diátaxis classification.

## Trade-offs
- **Gained**: Informed resource access, reduced context waste, quality assessment before loading
- **Gained**: Cached metadata eliminates repeated access overhead
- **Lost**: Additional storage for introduction metadata
- **Lost**: Stale introduction data may not reflect current resource state
- **Risk**: Over-reliance on cached introductions vs fresh content
- **Risk**: Introduction quality varies by source reliability

## Implementation
- MCP tools: Resource introductions cached on first access
- Web URLs: Title, description, Diátaxis classification cached locally
- Context7: Structured introductions for reference materials
- Storage: Local cache with configurable TTL and refresh mechanisms
- Integration: Introductions displayed before full resource access

## Rationale
Introduction caching enables efficient external knowledge discovery by providing quality assessment without full context consumption. Cached metadata supports informed utilization decisions while reducing access overhead and improving knowledge integration effectiveness.

## Validation Criteria
- Introduction caching reduces full resource access by 60%
- Users can assess resource relevance in < 5 seconds
- Cached introductions remain accurate for 80%+ of resources
- Context window efficiency improved through selective loading
- Cache invalidation works for updated external resources

## See Also
- [External Resource Introduction Caching](docs/work/discoveries/2026-01-16-caching-introductions.md) - Technical grounding for introduction caching
- [Frontmatter Schema](docs/reference/docs/frontmatter-schema.md) - `external_docs` field for external resource references