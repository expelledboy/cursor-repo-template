---
doc_status: stable
purpose: Define the problem of stale or fragmented external knowledge in tool workflows.
intent: problem
governed_by:
  docs/system/model/problem-doc.md: Load if you need the required fields for problem docs
related:
  docs/dev/decision/prefer-authoritative-sources.md: Load if you need the decision that resolves this problem
---

# Problem: External Knowledge Drift

## Problem Statement
Tool workflows degrade when non-authoritative sources are treated as authoritative.

## Scope and Boundaries
- Applies to tooling and runtime usage guidance in this repo.
- Includes internal standards and external vendor documentation.

## Consequences
- Agents follow outdated instructions.
- Conflicts appear between local docs and upstream sources.

## Related Decisions
- Prefer authoritative sources.
