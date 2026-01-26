---
doc_status: stable
purpose: Define how to create discovery procedures that locate authoritative sources.
intent: procedure
governed_by:
  docs/system/model/procedure-doc.md: Load if you need the contract for procedure docs
related:
  docs/dev/decision/prefer-authoritative-sources.md: Load if you need the decision this procedure applies
---

# Creating Discovery Procedures

## Purpose
Create procedures that discover authoritative sources before examples.

## Inputs
- The task outcome the procedure must achieve.
- The authoritative sources available to the project.
- The MCP servers that can access those sources.

## Procedure
1) Identify which sources are authoritative for the task (standards, vendor docs, internal policies).
2) Map each source to an MCP server capable of retrieving it.
3) Order discovery so standards and policies come before implementation examples.
4) Capture the discovery sequence in the procedure steps.
5) If no MCP is available for an authority, document how to get access without re-stating the content.
6) Keep the procedure focused on discovery and verification, not reproducing upstream material.

## Validation
- The procedure identifies authoritative sources before examples.
- The discovery order resolves standards before implementation examples.
- Fallbacks are explicit and scoped.

## Failure Modes
- The procedure embeds upstream content instead of linking to it.
- Discovery order produces examples before standards.
- Fallbacks are implicit or missing.
