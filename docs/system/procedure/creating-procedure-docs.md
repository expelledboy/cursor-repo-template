---
doc_status: stable
purpose: Define how to create a procedure doc.
intent: procedure
governed_by:
  docs/system/model/procedure-doc.md: Load if you need the contract for procedure docs
implements:
  docs/system/model/procedure-doc.md: Load if you need the contract this procedure must satisfy
related:
  docs/system/loading-policy.md: Load if you need the system loading rules this procedure should align with
---

# Creating Procedure Docs

## Purpose
Create a procedure doc that is precise and executable.

## When to Create
- A task needs repeatable steps.
- A decision introduces a new workflow.
- A procedure is implied but not documented.

## Steps
1) Name the procedure with an action phrase.
2) Set `doc_status` in frontmatter.
3) Define inputs and required context.
4) Write steps in order with expected outcomes.
5) Add validation checks.
6) Document failure modes and recovery.
7) Validate required sections and links.

## Quality Checklist
- Steps are minimal and ordered.
- Inputs are explicit.
- Validation is possible without guesswork.
- Failure modes include recovery actions.

## Failure Modes
- Steps are ambiguous.
- Inputs depend on hidden knowledge.
- Validation relies on unstated context.
