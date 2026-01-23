---
governed_by:
  "docs/reference/docs/system-governance.md": "System governance"
---

# Doc Relationships

## Relationship Types
- `governs`: this document sets rules that the target must follow.
- `governed_by`: this document must comply with the target.
- `implements`: this document operationalizes a governing document.
- `implemented_by`: a code or config artifact that realizes this document.
- `related`: contextual link with no authority implied.

## Precedence Inference
- If A `governs` B, then A has higher precedence than B.
- The governing chain is the authority chain.
- When in doubt, follow `governed_by` upward.

## Usage Rules
- Use `governs` to express hard constraints.
- Use `governed_by` to declare compliance.
- Use `implements` for procedural or concrete realization.
- Use `related` only when no authority is implied.

## Anti-Patterns
- Do not use `AGENTS.md` as a governor for canonical docs.
- Do not create cycles in `governs`/`governed_by`.
