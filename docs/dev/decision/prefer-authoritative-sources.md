---
doc_status: stable
purpose: Record the decision to prefer authoritative sources and cache only for recall.
intent: decision
decision_status: accepted
decision_date: 2026-01-26
governed_by:
  docs/system/model/decision-doc.md: Load if you need the required fields for decision docs
related:
  docs/dev/problem/external-knowledge-drift.md: Load if you need the motivating problem for this decision
  docs/dev/procedure/creating-discovery-procedures.md: Load if you need the procedure that applies this decision
  docs/dev/procedure/caching-external-references.md: Load if you need the procedure that applies this decision
---

# Decision: Prefer Authoritative Sources

## Decision Statement
Prefer authoritative sources for external knowledge and cache only when rapid recall requires it.

## Context and Drivers
- Authority depends on the domain: vendor docs, standards, or internal policies.
- Transport (MCP) is not the source of authority.
- Local copies drift without active maintenance.

## Alternatives Considered
- Cache all external docs locally.
- Avoid external references entirely.

## Outcome and Implications
- Procedures must identify authoritative sources before choosing an access path.
- MCP servers are preferred when they provide access to those sources.
- Cached references are permitted only with a clear recall justification and refresh policy.

## Related Problems
- External knowledge drift.
