---
doc_status: stable
purpose: Define how to create a problem doc.
intent: procedure
governed_by:
  docs/domains/system.md: Load if you need domain constraints for this procedure
  docs/system/model/procedure-doc.md: Load if you need the contract for procedure docs
implements:
  docs/system/model/problem-doc.md: Load if you need the contract this procedure must satisfy
related:
  docs/system/decision/separate-intent-from-authority.md: Load if you need the decision that motivates explicit problem docs
  docs/system/loading-policy.md: Load if you need the system loading rules this procedure should align with
---

# Creating Problem Docs

## Purpose
Create a problem doc that is scoped, actionable, and linked to decisions.

## When to Create
- A new risk or misalignment appears.
- A decision is required and the problem is not recorded.
- The problem scope changed enough that the old doc is misleading.

## Steps
1) Name the problem with a short verb phrase.
2) Set `doc_status` in frontmatter.
3) Write a one sentence problem statement.
4) Define scope and boundaries.
5) Describe consequences if unresolved.
6) Link to the decision docs that address the problem.
7) Validate required sections and links.

## Quality Checklist
- Problem statement is specific and testable.
- Scope excludes solutions and procedures.
- Consequences describe concrete risk.
- At least one related decision is linked.

## Failure Modes
- The problem includes a solution.
- The scope is too broad to act on.
- No decision link exists.
