---
doc_status: stable
purpose: Define the procedure for promoting operational findings to canonical docs.
intent: procedure
governed_by:
  docs/system/model/procedure-doc.md: Load for structural requirements
  docs/system/governance.md: Authority for all procedures
related:
  docs/system/model/objective-graph.md: Schema this procedure operates on
  docs/system/procedure/maintaining-objective-graph.md: Parent procedure
---

# Procedure: Promoting Operational Findings

## Purpose
To ensure that operational insights, defects, and missing decisions discovered during execution are not lost. This procedure defines how to "flush" the `operational_findings` buffer from the Objective Graph into the canonical Governance DAG.

## Trigger
- Before closing a Root Objective (status `done`).
- When `operational_findings` accumulate significant items.
- When an agent is blocked by a missing decision.

## Steps

### 1. Review Findings
1. Load `docs/work/objective-graph.yaml`.
2. Inspect the `operational_findings` list for the active objective(s).

### 2. Classify and Action
For each finding, determine the appropriate canonical artifact:

- **Missing Logic/Ambiguity:**
  - Action: Create a **Problem Doc** (`docs/system/problem/<slug>.md`).
  - Trace: Link the Problem back to the Objective Graph example (if helpful) or describe the context.

- **Required Policy:**
  - Action: Create a **Decision Doc** (`docs/system/decision/<slug>.md`).
  - Constraint: Ensure it links to a Problem Doc (create one if missing).

- **Broken Mechanism:**
  - Action: Create a **Defect/Issue** (if using issue tracker) or a Problem Doc.

- **Noise/Temporary:**
  - Action: Discard.

### 3. Establish Provenance
1. In the new doc, add a `related` link to the relevant `objective_id` or context (optional, for traceability).
2. Ensure the new doc follows its specific Intent Model (governed_by, etc.).

### 4. Clear Buffer
1. Remove the processed finding from `operational_findings` in the YAML.
2. If the finding blocked an objective, update the objective's status.

## Verification
- Run `just docs-validate` to ensure new docs are valid DAG nodes.
- Confirm `operational_findings` is empty before marking the Root Objective as `done`.
