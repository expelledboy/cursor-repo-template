---
doc_status: stable
purpose: Define global rules for docs structure and authority.
intent: contract
governed_by:
  docs/system/core-values.md: Load if you need the non-negotiable values that constrain these rules
governs:
  docs/system/authority-model.md: Load to ensure authority rules follow governance
  docs/system/intent-model.md: Load to align intent vocabulary with governance rules
  docs/system/task-model.md: Load to align task vocabulary with governance rules
  docs/system/intent-task-matrix.md: Load to verify task mapping follows governance
  docs/system/model/docs-index-output.md: Load to ensure the docs-index contract follows governance
  docs/system/model/docs-domains-output.md: Load to ensure the docs-domains contract follows governance
  docs/system/model/docs-skills-output.md: Load to ensure the docs-skills contract follows governance
  docs/system/model/domain-doc.md: Load to ensure domain doc contracts follow governance
  docs/system/model/objective-graph.md: Load to ensure objective graph contracts follow governance
  docs/system/model/doc-code-linking.md: Load to ensure doc-code linking rules follow governance
  docs/system/model/reference-doc.md: Load to ensure reference doc contracts follow governance
  docs/system/model/problem-doc.md: Load to ensure problem contracts follow governance
  docs/system/model/decision-doc.md: Load to ensure decision contracts follow governance
  docs/system/model/procedure-doc.md: Load to ensure procedure contracts follow governance
  docs/system/procedure/creating-problem-docs.md: Load if you need the procedure for creating problem docs
  docs/system/procedure/promoting-operational-findings.md: Load if you need the procedure for promoting findings
  docs/system/system-rationale.md: Load to ensure rationale aligns with governance
implemented_by:
  scripts/docs/docs_validate.py: Load if you need to see enforcement of governance constraints
  scripts/docs/contract_specs.py: Load if you need the constants used by validation
related:
  scripts/docs/docs_index.py: Load if you need the tool that renders the governed_by DAG
---

# System Governance

## Scope
This document defines the structure, relationships, and authority rules for `docs/`.

## Required Frontmatter
- `doc_status`
- `purpose`
- `intent`

## Relationships
- `governs`: this document sets rules the target must follow.
- `governed_by`: this document must comply with the target.
- `implements`: this document operationalizes a governing document.
- `related`: contextual link with no authority implied.

### When to Use `related` vs `governs`
- Use `governs` when the target must obey constraints defined here.
- Use `related` when the target is relevant context but has no authority.
- Problem and decision docs link to each other with `related`, not `governs`.

## Relationship Load Hints
Relationship values are short, contextual load hints written from the perspective
of the current document. The hint should explain why the target is worth loading
given the current doc's intent and the likely task.

Tooling reads only the path keys, but authors should treat the value as a local
justification for loading the target, for example:

```
related:
  docs/system/problem/context-limits-break-correctness.md: Load if you need the failure mode that motivates this decision
```

```
related:
  docs/system/model/procedure-doc.md: Load if you need required fields to validate this procedure
```

### Load Hint Pattern
Use the pattern "Load if you need X to do Y" where X is missing context and Y
is the current doc's purpose or the likely task.

### Intent Pairing Guidance
- `decision` docs often link to `problem` docs for motivation.
- `procedure` docs often link to `contract` docs for validation.
- `rationale` docs often link to `facts` docs for precise rules.

## Contract Governance
Contract docs define required fields and sections for a doc type and must govern
the docs that implement them. Each problem, decision, or procedure doc must
include a `governed_by` link to its contract doc.

## External Sources
- Prefer links to authoritative sources instead of duplicating their content.
- Use `related` to surface external references that inform the current doc.

## Objective Graph
- The objective graph lives under `docs/work/` and is not committed.
- Subtasks must re-load the objective graph and run entry checks before execution.
- Realign after compaction, new sessions, or sub-agent starts.
- Docs under `docs/work/` are operational state and are excluded from canonical validation.
- Operational state is not authoritative and must not override canonicals.

## Metadata Rules
- Use `doc_status` for document lifecycle (`stable`, `draft`, `deprecated`).
- Use domain specific fields for content state, for example `decision_status`
  and `decision_date` on decision docs.
- Decision docs must use `decision_status` values (`accepted`, `rejected`, `superseded`, `reversed`)
  and `decision_date` in `YYYY-MM-DD` format.

## Relationship Usage Table
| Type | Use When | Example Hint |
| --- | --- | --- |
| `governed_by` | this doc must comply with target rules | Load if you need the constraints this doc must obey |
| `governs` | this doc sets rules for the target | Load to verify the target follows this contract |
| `implements` | this doc operationalizes a governing doc | Load to confirm this procedure matches the contract |
| `implemented_by` | code or config realizes this doc | Load to see how this rule is enforced in code |
| `related` | context only, no authority | Load if you need background that motivates this doc |

## Bidirectional Links
- `governs` must have a reverse `governed_by` link.
- `implements` must have a reverse `implemented_by` link.
- `related` links must be bidirectional.

## DAG Output Notes
- `just docs-index` renders the full governed_by DAG as a branching tree.
- Repeated nodes appear multiple times to preserve all paths.
- Use `--from <path>` to scope output to a specific entrypoint.

## Authority Rules
- Authority is inferred from the `governs` and `governed_by` graph.
- A document that `governs` another is higher authority.
- Resolve conflicts by following the `governed_by` chain upward.

## Domain Rule
- Canonical docs live under `docs/<domain>/` or `docs/system/`.
- Every domain has `docs/domains/<domain>.md` as a domain definition and index entry.
- Domain docs define scope and boundaries and do not govern other docs.
- Use `just docs-domains` to list indexed domains.

## Agent Skills
- Skills live under `agent/skills/` and use `SKILL.md` per skill.
- Use `just docs-skills` to list skills visible to the system.

## Intent Rule
- Intent describes how a document is used, not its authority.
- Valid intents are defined in `docs/system/intent-model.md`.

## Task Rule
- Valid tasks are defined in `docs/system/task-model.md`.
- Context loading uses the task to intent mapping.

## Compatibility
- Diataxis buckets are not required in `docs/`.
