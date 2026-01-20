---
title: "Diátaxis-Based External Source Classification"
created_date: 2026-01-16
purpose: "Classify external knowledge sources using Diátaxis principles"
domain: agentos
type: discovery
status: superseded
superseded_by: docs/explanation/decisions/2026-01-16-external-classification.md
superseded_date: 2026-01-18
superseded_reason: Discovery incorporated into architecture decision
---

## Observation
External knowledge sources can be classified using Diátaxis principles for appropriate handling.

## Key Insights
- External reference docs should be treated as authoritative sources
- External how-to guides provide procedural knowledge
- External explanations offer design rationale and context
- External tutorials serve learning purposes

## Technical Grounding
- Context7 provides reference documentation (Diátaxis: reference)
- Web tutorials offer learning materials (Diátaxis: tutorial)
- API documentation sites contain reference specs (Diátaxis: reference)
- External sources auto-classified when linked in reasoning

## Implications
- External content handled according to its knowledge type
- Appropriate caching and persistence based on Diátaxis role
- Consistent treatment of internal vs external knowledge
- Seamless integration across knowledge boundaries

## Used In
- [Diátaxis-Based External Source Classification](docs/explanation/decisions/2026-01-16-external-classification.md)
