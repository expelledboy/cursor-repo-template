---
title: "Decision: Artifact Mention Incorporation"
status: accepted
created_date: 2026-01-16
purpose: "Allow user mentions to directly incorporate artifacts into reasoning flows"
domain: agentos
related:
  - docs/work/problems/2026-01-16-cursor-integration.md
  - docs/work/discoveries/2026-01-16-mention-incorporation.md
---

# Decision: Artifact Mention Incorporation

## Decision
Addresses [Cursor Integration Depth](docs/work/problems/2026-01-16-cursor-integration.md) using insights from [Mention-Based Artifact Incorporation](docs/work/discoveries/2026-01-16-mention-incorporation.md).
Allow user mentions to directly incorporate artifacts into active reasoning flows. Implement automatic condensation for large files and support for all Cursor mention types (@Files, @Code, @Docs, drag & drop).

## Trade-offs
- **Gained**: Conversational context loading, reduced manual effort, natural artifact integration
- **Gained**: Automatic condensation prevents context overflow
- **Lost**: Less explicit control over what gets included
- **Lost**: Condensation may lose some detail for very large files
- **Risk**: Over-inclusion of irrelevant context
- **Risk**: Condensation algorithms may miss important content

## Implementation
- Mention types: @Files & Folders (full), @Code (snippets), @Docs (documentation)
- Drag & drop support from sidebar to chat
- Automatic condensation for files > context limit
- Real-time incorporation during conversation flow
- Validation ensures mentions resolve to existing artifacts

## Rationale
Mention-based incorporation enables natural conversation-driven context loading while maintaining explicit user control through mention syntax. Automatic condensation ensures context efficiency without sacrificing reasoning quality. Integration with existing Cursor patterns provides familiar user experience.

## Validation Criteria
- Mention incorporation works for 95%+ of artifact types
- Context overflow prevented through automatic condensation
- Conversation flow uninterrupted by mention processing
- Users can incorporate artifacts in < 3 seconds
- Condensation preserves 90%+ of relevant content

## See Also
- [Cursor Mechanics Specification](docs/reference/agentos/cursor-mechanics.md) - Implementation guidance for mentions and evidence anchoring
- [Mention-Based Artifact Incorporation](docs/work/discoveries/2026-01-16-mention-incorporation.md) - Technical grounding for mention patterns