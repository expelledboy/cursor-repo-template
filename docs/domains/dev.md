---
doc_status: stable
purpose: Define the scope for development tooling and agent runtime setup.
intent: facts
domain_id: dev
domain_scope: Tooling, environment setup, and agent runtime integrations used in this repo.
domain_status: active
governed_by:
  docs/system/model/domain-doc.md: Load if you need the domain doc contract
governs:
  docs/dev/facts/agent-mechanics.md: Load if you need universal agent runtime constraints
  docs/dev/facts/cursor-mechanics.md: Load if you need Cursor-specific mechanics
  docs/dev/facts/opencode-mechanics.md: Load if you need OpenCode-specific mechanics
---

# Dev Domain

## Purpose
Define the scope and boundaries for development tooling and agent runtime use.

## Scope
- Local toolchain usage such as direnv, nix flake, and just.
- Agent runtime setup and skill discovery.
- MCP server usage for development workflows.

## Boundaries
- Does not define upstream tool behavior.
- Does not replace authoritative external documentation.
