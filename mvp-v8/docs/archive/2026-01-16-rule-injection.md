---
title: "Rule-Based Context Injection"
created_date: 2026-01-16
purpose: "Cursor rules detect user intent and inject relevant context automatically"
domain: agentos
type: research
status: superseded
superseded_by: docs/reference/agentos/cursor-integration-specs.md
superseded_date: 2026-01-18
superseded_reason: Distilled into Reference
---

# Rule-Based Context Injection

## Observation
Cursor rules can detect user intent and inject relevant context into reasoning flows automatically.

## Key Insights
- Rules provide persistent, intent-aware context loading
- Context injection happens seamlessly during reasoning
- User intent drives automatic directive selection
- Reduces manual context management overhead

## Technical Grounding
- **Rule Types**: Always Apply, Apply Intelligently (AI decides), Apply to Specific Files (glob patterns), Apply Manually (@ruleName)
- **Injection Timing**: Rules injected per request at start of model context, no automatic unloading
- **Auto-Attach**: Nested `.cursor/rules` directories attach when files in directory referenced
- **File References**: Rules can include files with @filename.ts syntax
- **Community Reports**: Glob rules only auto-attach when files referenced in chat, not merely opened
- **Official Documentation**: https://cursor.com/docs/context/rules

## Implications
- Reasoning starts with appropriate context automatically
- Context loading becomes proactive rather than reactive
- User experience improves through reduced manual setup
- More accurate reasoning through intent-aligned context
- External knowledge sources accessible through rule injection

## Used In
- [Dynamic Context Loading](docs/explanation/decisions/2026-01-16-dynamic-context.md)