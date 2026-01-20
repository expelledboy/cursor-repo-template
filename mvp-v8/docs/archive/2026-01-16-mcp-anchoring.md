---
title: "MCP Tool Evidence Auto-Anchoring"
created_date: 2026-01-16
purpose: "Automatically anchor MCP tool outputs to reasoning steps"
domain: agentos
type: research
status: superseded
superseded_by: docs/reference/agentos/cursor-integration-specs.md
superseded_date: 2026-01-18
superseded_reason: Distilled into Reference
---

# MCP Tool Evidence Auto-Anchoring

## Observation
Cursor's MCP tools produce evidence that can be automatically anchored to reasoning steps, eliminating manual evidence collection.

## Key Insights
- Tool outputs contain rich evidence for decision-making
- Automatic anchoring reduces user effort
- Evidence becomes immediately available in reasoning context
- Tool results can short-circuit ambiguous decision paths

## Technical Grounding
- **MCP Transports**: stdio (local CLI), SSE (server-sent events), Streamable HTTP (remote servers)
- **Protocol Capabilities**: Tools, Prompts, Resources, Roots, Elicitation
- **Configuration**: JSON in .cursor/mcp.json or ~/.cursor/mcp.json
- **Authentication**: Environment variables, OAuth for remote servers
- **Tool Execution**: Agent asks for approval by default, auto-run available
- **Official Documentation**: https://cursor.com/docs/context/mcp

## Implications
- Decisions incorporate comprehensive tool evidence automatically
- Reduced manual evidence gathering overhead
- More informed reasoning through rich tool outputs
- Tool integration becomes seamless in decision workflows
- External knowledge sources integrated by default

## Used In
- [Tool Evidence Integration](docs/explanation/decisions/2026-01-16-tool-evidence.md)