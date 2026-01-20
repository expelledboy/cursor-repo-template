---
title: "YAML Character Efficiency"
created_date: 2026-01-16
purpose: "YAML provides structured, character-efficient representation"
domain: agentos
type: research
status: superseded
superseded_by: docs/reference/agentos/cursor-integration-specs.md
superseded_date: 2026-01-18
superseded_reason: Distilled into Reference
---

# YAML Character Efficiency

## Observation
YAML provides structured, character-efficient representation that prevents entropy accumulation in context windows.

## Key Insights
- Structured format maintains consistency across reasoning steps
- Character efficiency reduces context window pressure
- Explicit structure prevents natural language drift

## Technical Grounding
- **YAML Specification**: YAML 1.2.2 standard (https://yaml.org/spec/1.2.2/)
- **Parsing**: `yaml.safe_load()` for safe YAML parsing in Python
- **Character Efficiency**: YAML uses ~30-50% fewer characters than equivalent JSON or natural language
- **Schema Validation**: Structured schemas enable validation before loading (e.g., `schemas/active-state.yaml`)
- **Human Readability**: YAML maintains human editability while providing machine parseability
- **State Representation**: Used in [Active State Spec](docs/reference/agentos/spec-active-state.md) for resumable workflows
- **Frontmatter**: YAML frontmatter used across all documentation files for metadata

## Implications
- State and decisions can be compactly represented
- Multi-step reasoning maintains fidelity
- Context windows can accommodate more structured information

## Used In
- [YAML State Representation](docs/explanation/decisions/2026-01-16-yaml-state.md)