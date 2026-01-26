---
doc_status: stable
purpose: Define how to create a decision doc.
intent: procedure
governed_by:
  docs/domains/system.md: Load if you need domain constraints for this procedure
  docs/system/model/procedure-doc.md: Load if you need the contract for procedure docs
implements:
  docs/system/model/decision-doc.md: Load if you need the contract this procedure must satisfy
related:
  docs/system/problem/context-limits-break-correctness.md: Load if you need the motivating problem to ground the decision
  docs/system/loading-policy.md: Load if you need the system loading rules this procedure should align with
---

# Creating Decision Docs

## Purpose
Create a decision doc that is grounded in a problem and captures its impact.

## When to Create
- A choice changes system behavior or authority.
- A problem doc requires an explicit resolution.
- A previous decision is being reversed or replaced.

## Steps
1) Name the decision with a short verb phrase.
2) Set `doc_status` in frontmatter.
3) State the decision in one sentence.
4) Set `decision_status` and `decision_date` in frontmatter.
5) Capture context and drivers.
6) List alternatives considered.
7) Describe outcome and implications.
8) Link to related problem docs.
9) Validate required sections and links.

## Quality Checklist
- Decision statement is unambiguous.
- Drivers tie back to a problem.
- Alternatives are concrete.
- Implications are testable.

## Failure Modes
- No linked problem doc.
- Decision is a hidden rationale.
- Outcome does not match the decision statement.
