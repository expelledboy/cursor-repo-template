---
doc_status: stable
purpose: Define how to create evaluation frameworks for objectives.
intent: procedure
governed_by:
  docs/system/model/procedure-doc.md: Load if you need the contract for procedure docs
related:
  docs/system/model/objective-graph.md: Load if you need the objective graph contract
  docs/system/decision/introduce-objective-graph.md: Load if you need the decision that mandates evaluation frameworks
---

# Defining Evaluation Frameworks

## Purpose
Define evaluation frameworks that determine objective completion.

## Inputs
- Definition of done for the objective.
- Applicable contracts or test procedures.

## Evaluation Framework Schema
- `method: test|contract|manual`
- `evidence: <string>`
- `pass_criteria: <string>`
- `failure_action: <string>`

## Procedure
1) Identify existing contracts or tests that validate the objective.
2) If none exist, define a task-specific evaluation framework.
3) Record the evaluation framework in the objective graph using the required schema.
4) Ensure the evaluation framework produces evidence for completion.

## Validation
- Every objective includes an evaluation framework.
- Evaluation criteria are testable without ambiguity.

## Failure Modes
- Objectives have a definition of done but no evaluation method.
- Evaluation criteria rely on subjective judgment.
