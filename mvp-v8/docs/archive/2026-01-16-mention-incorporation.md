---
title: "Mention-Based Artifact Incorporation"
created_date: 2026-01-16
purpose: "User mentions directly incorporate artifacts into reasoning flows"
domain: agentos
tags: ["cursor", "integration", "ui"]
type: research
status: superseded
superseded_by: docs/reference/agentos/cursor-integration-specs.md
superseded_date: 2026-01-18
superseded_reason: Distilled into Reference
original_path: docs/work/discoveries/2026-01-16-mention-incorporation.md
---

# Mention-Based Artifact Incorporation

## Observation
User mentions of artifacts (@filename.ts, @Folders) directly incorporate them into active reasoning flows, enabling natural conversation-driven context loading.

## Key Insights
- **File References**: @Files & Folders incorporates entire files/folders with content overview
- **Code Snippets**: @Code enables granular control over specific code sections
- **Documentation Access**: @Docs provides access to documentation with custom doc addition
- **Drag & Drop**: Files can be dragged from sidebar directly into chat
- **Automatic Condensation**: Large files/folders automatically summarized to fit context limits
- **Official Documentation**: https://cursor.com/docs/context/mentions

## Technical Grounding
- **Cursor Mentions API**: Native Cursor feature for artifact incorporation
- **Syntax**: `@filename.ts`, `@Folders`, `@Code`, `@Docs` with automatic completion
- **Context Integration**: Mentions inject content directly into chat context
- **Condensation Algorithm**: Large files automatically summarized to fit context window limits
- **File System Access**: Mentions resolve to workspace files and folders
- **Real-time Processing**: Mentions processed during conversation flow without interruption

## Implications
- Reasoning context includes exactly what users intend through explicit signals
- Artifact integration becomes conversationally natural without command complexity
- Context loading happens seamlessly during chat flow
- Users can quickly reference any project artifact
- Reduces friction in evidence incorporation workflows

## Used In
- [Artifact Mention Incorporation](docs/explanation/decisions/2026-01-16-artifact-mention.md)