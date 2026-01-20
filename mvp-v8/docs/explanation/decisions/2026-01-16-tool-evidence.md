---
title: "Decision: Tool Evidence Integration"
status: accepted
created_date: 2026-01-16
purpose: "Automatically anchor MCP tool outputs to reasoning steps"
domain: agentos
related:
  - docs/work/problems/2026-01-16-cursor-integration.md
  - docs/work/discoveries/2026-01-16-mcp-anchoring.md
---

# Decision: Tool Evidence Integration

## Decision
Addresses [Cursor Integration Depth](docs/work/problems/2026-01-16-cursor-integration.md) using insights from [MCP Tool Evidence Auto-Anchoring](docs/work/discoveries/2026-01-16-mcp-anchoring.md).
Automatically anchor MCP tool outputs to reasoning steps for immediate evidence incorporation. Implement tool result integration with OAuth authentication and environment variable support.

## Trade-offs
- **Gained**: Seamless evidence integration, reduced manual effort, comprehensive tool outputs
- **Gained**: Immediate result availability, enriched reasoning context
- **Lost**: Tool approval workflows may interrupt reasoning flow
- **Lost**: Additional complexity in evidence management
- **Risk**: Tool output noise diluting reasoning quality
- **Risk**: Authentication complexity for remote tools

## Implementation
- MCP transports: stdio (local), SSE (server-sent), Streamable HTTP (remote)
- Protocol capabilities: Tools, Prompts, Resources, Roots, Elicitation
- Configuration: JSON in `.cursor/mcp.json` or `~/.cursor/mcp.json`
- Authentication: Environment variables, OAuth for remote servers
- Tool execution: Agent asks for approval by default, auto-run available
- Anchoring: Automatic evidence attachment to reasoning steps

## Rationale
Tool evidence integration eliminates evidence collection bottlenecks while enriching decision contexts. MCP protocol provides standardized tool access across local and remote sources. Automatic anchoring maintains reasoning flow while ensuring comprehensive evidence availability.

## Validation Criteria
- Tool outputs automatically anchor to 95%+ of reasoning steps
- Evidence collection time reduced by 80%
- Tool integration doesn't interrupt reasoning flow inappropriately
- Authentication works for both local and remote tools
- Tool result quality maintained in decision contexts

## See Also
- [Cursor Mechanics Specification](docs/reference/agentos/cursor-mechanics.md) - Implementation guidance for MCP tool evidence anchoring
- [MCP Tool Evidence Auto-Anchoring](docs/work/discoveries/2026-01-16-mcp-anchoring.md) - Technical grounding for tool integration