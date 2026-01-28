---
doc_status: stable
purpose: Define the problem of missing doc-code traceability.
intent: problem
governed_by:
  docs/system/model/problem-doc.md: Load if you need the required fields for problem docs
related:
  docs/system/decision/require-doc-code-linking.md: Load if you need the decision that resolves this problem
---

# Problem: Missing Doc-Code Links

## Problem Statement
When docs and code are not explicitly linked, alignment cannot be verified and drift accumulates.

## Scope and Boundaries
- Applies to implementation changes that should map to documentation.
- Excludes purely conceptual docs with no implementation impact.

## Consequences
- Implementation changes are untraceable to requirements.
- Doc updates fail to propagate into code.
- Alignment checks miss gaps.

## Related Decisions
- Require doc-code linking.
