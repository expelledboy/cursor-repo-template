---
title: "Cursor Integration Mechanics"
status: stable
created_date: 2026-01-18
purpose: "Technical specification for Cursor features (rules, commands, MCP, traces)"
domain: agentos
external_docs:
  - https://cursor.com/docs/context/rules
  - https://cursor.com/docs/context/commands
  - https://cursor.com/docs/context/mcp
  - https://cursor.com/docs/context/semantic-search
  - https://cursor.com/docs/context/mentions
  - https://yaml.org/spec/1.2.2/
---

# Cursor Integration Mechanics

## Rule Injection

*   **Contract**: Rules inject at start of model context. No automatic unloading.
*   **Syntax**:
    *   `@filename.ts` to reference files
    *   `glob:**/*.md` to match patterns
*   **Rule Types**:
    *   **Always Apply**: Global context.
    *   **AI-Decided**: Agent selects based on intent.
    *   **Glob-Based**: Auto-attach when matching file referenced.
*   **Documentation**: https://cursor.com/docs/context/rules

## Command Control

*   **Storage**:
    *   Project: `.cursor/commands/*.md`
    *   Global: `~/.cursor/commands/*.md`
*   **Trigger**: `/command-name` prefix.
*   **Format**: Markdown files with `title`, `description`, `usage`.
*   **Scope**: Project-level overrides Global.
*   **Documentation**: https://cursor.com/docs/context/commands

## MCP Tool Anchoring

*   **Config**: `.cursor/mcp.json`
*   **Transports**: `stdio` (local), `sse` (server-sent).
*   **Auth**: Environment variables (never checked in).
*   **Behavior**: Tool outputs automatically anchor to reasoning steps.
*   **Documentation**: https://cursor.com/docs/context/mcp

## Semantic Search

*   **Contract**: Search runs *before* decision execution (Priming).
*   **Sync**: Every 5 minutes (differential).
*   **Privacy**: Source code encrypted/discarded after embedding. No storage.
*   **Documentation**: https://cursor.com/docs/context/semantic-search

## Trace Revelation

*   **Structure**:
    *   `trace_id`: Unique execution ID.
    *   `decision`: Final output.
    *   `confidence`: 0.0-1.0 score.
*   **Command**: `/trace` reveals current decision graph.
*   **Anchoring**: MUST link to Rules, Mentions, Searches used.

## Artifact Mentions

*   **Supported Types**:
    *   `@Files` / `@Folders`: Full content (auto-summarized if > limit).
    *   `@Code`: Specific snippets.
    *   `@Docs`: Documentation sets.
*   **Condensation**: Automatic summarization for large contexts.
*   **Documentation**: https://cursor.com/docs/context/mentions

## Data Representation (YAML)

*   **Spec**: YAML 1.2.2.
*   **Efficiency**: ~30-50% token reduction vs JSON.
*   **Usage**: Required for Active State and Frontmatter.
*   **Documentation**: https://yaml.org/spec/1.2.2/
