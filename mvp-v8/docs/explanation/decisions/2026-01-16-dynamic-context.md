---
title: "Decision: Dynamic Context Loading"
status: accepted
created_date: 2026-01-16
purpose: "Enable Cursor rules to detect user intent and inject relevant context automatically"
domain: agentos
related:
  - docs/work/problems/2026-01-16-cursor-integration.md
  - docs/work/discoveries/2026-01-16-rule-injection.md
---

# Decision: Dynamic Context Loading

## Decision
Addresses [Cursor Integration Depth](docs/work/problems/2026-01-16-cursor-integration.md) using insights from [Rule-Based Context Injection](docs/work/discoveries/2026-01-16-rule-injection.md).
Enable Cursor rules to detect user intent and inject relevant context into reasoning flows automatically. Implement hierarchical loading with explicit tier structure and rule-based triggers.

## Trade-offs
- **Gained**: Proactive context loading, reduced manual effort, intent-aware injection
- **Gained**: Hierarchical efficiency, tiered directive organization
- **Lost**: Rule complexity management, potential over-injection of context
- **Lost**: Explicit control vs automatic behavior
- **Risk**: Rule conflicts causing context noise
- **Risk**: Performance overhead of rule evaluation

## Implementation
- Rule types: always apply, AI-decided, file-specific, manual triggers
- Hierarchical tiers: core contracts (always) → task-type specific → complexity-based → phase-triggered
- Context injection happens per request at reasoning start
- Rules can include file references (@filename.ts) and conditional logic
- Validation ensures rule consistency and performance

## Rationale
Rule-based injection enables proactive context discovery while hierarchical loading manages token efficiency. Cursor rules detect user intent through file patterns, command usage, and content analysis. Combined approach provides rich, relevant context without manual selection overhead.

## Validation Criteria
- Context loading reduces manual selection by 80%
- Rule injection provides appropriate context for 95%+ of reasoning tasks
- Hierarchical loading maintains 30-50% token efficiency
- Rule conflicts detected and resolved automatically
- Explicit override mechanisms available when needed

## See Also
- [Cursor Mechanics Specification](docs/reference/agentos/cursor-mechanics.md) - Implementation guidance for rule-based context injection
- [Rule-Based Context Injection](docs/work/discoveries/2026-01-16-rule-injection.md) - Technical grounding for dynamic context loading
- [Cursor Rules](.cursor/rules/) - Project rules implementing dynamic context loading