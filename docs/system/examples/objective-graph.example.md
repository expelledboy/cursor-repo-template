---
doc_status: stable
purpose: Provide a fully exercised example of the objective graph YAML.
intent: examples
governed_by:
  docs/system/model/objective-graph.md: Load if you need the contract that governs objective graph examples
related:
  docs/system/model/objective-graph.md: Load if you need the objective graph schema
  docs/system/decision/introduce-objective-graph.md: Load if you need the rationale for objective graphs
  docs/system/procedure/objective-graph-realignment.md: Load if you need the realignment procedure
---

# Objective Graph Example

## Purpose
Show a complex, in-progress objective state that exercises the full YAML schema.

## Requirements Mapping (inline)
- Objective graph is operational state, not canonical docs: see `docs/system/governance.md`.
- Objective graph must be YAML with required fields: see `docs/system/model/objective-graph.md`.
- Entry checks must include objective restatement and scope confirmation: see `docs/system/decision/introduce-objective-graph.md`.
- Realignment requires loading required context after compaction/session resets: see `docs/system/procedure/objective-graph-realignment.md`.
- Evaluation frameworks must be explicit and evidence-based: see `docs/system/procedure/defining-evaluation-frameworks.md`.
- Doc deltas drive implementation tasks and trace links: see `docs/system/procedure/implementing-from-doc-deltas.md`.
- Doc-code linking uses explicit links between docs and code: see `docs/system/model/doc-code-linking.md`.

## Example objective graph (YAML)

```yaml
objective_graph_version: "objective-graph/v1"
graph_id: "OG-20260128-ALIGNMENT"
updated_at: "2026-01-28T16:52:00Z"

active_objective_id: "OBJ-ALIGNMENT-ROOT"
active_frame_id: "F-IMPL-VALIDATION"
phase: "ACT"
mode: "trial"

objectives:
  - objective_id: "OBJ-ALIGNMENT-ROOT"
    status: "active"
    parent_ids: []
    child_ids:
      - "OBJ-AUDIT-LINKS"
      - "OBJ-IMPLEMENT-LINKS"
      - "OBJ-VALIDATE-LINKS"
    definition_of_done: "Doc-code linking enforced and validated without scope drift."
    evaluation_framework:
      method: "test"
      evidence: "just docs-validate output"
      pass_criteria: "Validation passed; no missing @implements markers for code targets"
      failure_action: "Return to audit and update doc-code linking rules"
    entry_check:
      check_type: "checklist"
      check_steps:
        - "Confirm requirements docs are final and unchanged"
        - "Confirm objective chain and current scope"
      expected_outcome: "Scope confirmed; no new requirements"
      objective_restatement: "Implement doc-code linking and validate alignment."
      scope_confirmation: "No new rules beyond doc-code linking enforcement"
    required_context:
      - type: doc
        uri: "docs/system/model/doc-code-linking.md"
        load_condition: "Before modifying validation logic"
        authority: "docs/system/governance.md"
        priority: required
      - type: doc
        uri: "docs/system/procedure/implementing-from-doc-deltas.md"
        load_condition: "Before any implementation change"
        authority: "docs/system/governance.md"
        priority: required
      - type: code
        uri: "scripts/docs/docs_validate.py"
        load_condition: "Before adding validation logic"
        authority: "docs/system/model/doc-code-linking.md"
        priority: required
    optional_context:
      - type: doc
        uri: "docs/system/procedure/resolving-conflicts.md"
        load_condition: "If validation conflicts appear"
        authority: "docs/system/authority-model.md"
        priority: conditional
    current_step: "Implement doc-code link validation for non-doc targets"
    next_action: "Add missing @implements markers to code files flagged by validator"
    trace_links:
      - doc: "docs/system/model/doc-code-linking.md"
        code: "scripts/docs/docs_validate.py"
      - doc: "docs/system/procedure/implementing-from-doc-deltas.md"
        commit: "REQ-COMMIT-SHA"

  - objective_id: "OBJ-AUDIT-LINKS"
    status: "active"
    parent_ids: ["OBJ-ALIGNMENT-ROOT"]
    child_ids: []
    definition_of_done: "All docs with implemented_by have matching @implements in code."
    evaluation_framework:
      method: "manual"
      evidence: "Audit checklist saved in work notes"
      pass_criteria: "No missing @implements markers for any listed code target"
      failure_action: "Record missing links and update implementation objective"
    entry_check:
      check_type: "checklist"
      check_steps:
        - "Load doc-code linking contract"
        - "List docs with implemented_by"
      expected_outcome: "Audit scope defined"
      objective_restatement: "Audit current doc-code link coverage."
      scope_confirmation: "No changes to linking rules"
    required_context:
      - type: doc
        uri: "docs/system/model/doc-code-linking.md"
        load_condition: "Before auditing"
        authority: "docs/system/governance.md"
        priority: required
    optional_context: []
    current_step: "Scan implemented_by relationships"
    next_action: "Check each target for @implements header"
    trace_links:
      - doc: "docs/system/model/doc-code-linking.md"
        code: "scripts/docs/docs_validate.py"

  - objective_id: "OBJ-IMPLEMENT-LINKS"
    status: "active"
    parent_ids: ["OBJ-ALIGNMENT-ROOT"]
    child_ids: []
    definition_of_done: "Validation logic detects missing @implements markers."
    evaluation_framework:
      method: "test"
      evidence: "docs-validate output with link errors"
      pass_criteria: "Missing markers consistently reported"
      failure_action: "Refine linking rules or scope"
    entry_check:
      check_type: "checklist"
      check_steps:
        - "Confirm validation applies only to non-doc targets"
        - "Confirm @implements marker format"
      expected_outcome: "Validation scope confirmed"
      objective_restatement: "Add validation without breaking existing docs."
      scope_confirmation: "No new validation beyond doc-code linking"
    required_context:
      - type: code
        uri: "scripts/docs/docs_validate.py"
        load_condition: "Before editing validator"
        authority: "docs/system/model/doc-code-linking.md"
        priority: required
      - type: doc
        uri: "docs/system/model/doc-code-linking.md"
        load_condition: "Before changing validation rules"
        authority: "docs/system/governance.md"
        priority: required
    optional_context: []
    current_step: "Implement validator checks for @implements in code"
    next_action: "Run docs-validate to verify detection"
    trace_links:
      - doc: "docs/system/model/doc-code-linking.md"
        code: "scripts/docs/docs_validate.py"

  - objective_id: "OBJ-VALIDATE-LINKS"
    status: "blocked"
    parent_ids: ["OBJ-ALIGNMENT-ROOT"]
    child_ids: []
    definition_of_done: "Validation passes after @implements markers are applied."
    evaluation_framework:
      method: "test"
      evidence: "just docs-validate output"
      pass_criteria: "Validation passed"
      failure_action: "Return to OBJ-IMPLEMENT-LINKS"
    entry_check:
      check_type: "command"
      check_steps:
        - "just docs-validate"
      expected_outcome: "Validation output collected"
      objective_restatement: "Confirm system alignment after changes."
      scope_confirmation: "No changes beyond doc-code linking"
    required_context:
      - type: doc
        uri: "docs/system/procedure/validating-doc-contracts.md"
        load_condition: "Before running validation"
        authority: "docs/system/governance.md"
        priority: required
    optional_context: []
    current_step: "Await implementation completion"
    next_action: "Run validation and record evidence"
    trace_links:
      - doc: "docs/system/procedure/validating-doc-contracts.md"
        code: "scripts/docs/docs_validate.py"

frames:
  - frame_id: "F-ROOT"
    title: "Objective alignment kickoff"
    summary: "Aligned on doc-code linking scope and objective graph requirements."
    anchors:
      - type: doc
        uri: "docs/system/decision/introduce-objective-graph.md"
        load_condition: "Initial scope review"
        authority: "docs/system/governance.md"
        priority: required
    links:
      - to: "F-AUDIT"
        kind: "branch"
        note: "Split into audit vs implementation streams"

  - frame_id: "F-AUDIT"
    title: "Audit phase"
    summary: "Enumerated implemented_by targets and missing markers."
    anchors:
      - type: doc
        uri: "docs/system/model/doc-code-linking.md"
        load_condition: "Audit links"
        authority: "docs/system/governance.md"
        priority: required
    links:
      - to: "F-IMPL-VALIDATION"
        kind: "resume"
        note: "Return to implement validator"

  - frame_id: "F-IMPL-VALIDATION"
    title: "Validation implementation"
    summary: "Implementing validator checks for doc-code linking."
    anchors:
      - type: code
        uri: "scripts/docs/docs_validate.py"
        load_condition: "Edit validator"
        authority: "docs/system/model/doc-code-linking.md"
        priority: required
    links: []

rehydration:
  required_rules:
    - "system"
  required_docs:
    - "docs/system/governance.md"
    - "docs/system/model/doc-code-linking.md"
    - "docs/system/procedure/implementing-from-doc-deltas.md"
```
