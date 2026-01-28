---
doc_status: stable
purpose: Define how to validate doc contracts and resolve validation errors.
intent: procedure
governed_by:
  docs/system/model/procedure-doc.md: Load if you need the contract for procedure docs
implements:
  docs/system/model/procedure-doc.md: Load if you need the contract this procedure must satisfy
implemented_by:
  scripts/docs/docs_validate.py: Load if you need the validator that enforces doc contracts
related:
  docs/system/loading-policy.md: Load if you need the procedure that depends on valid contracts
  docs/system/decision/enforce-doc-contracts.md: Load if you need the decision that mandates validation
---

# Validating Doc Contracts

## Purpose
Validate doc contracts and resolve errors before changing or adding docs.

## When to Run
- After editing doc frontmatter or relationships.
- After adding new docs or changing governance links.
- Before committing doc changes.

## Inputs
- The docs tree under `docs/`.

## Procedure
1) Run `just docs-validate`.
2) If validation fails, read each error and resolve it before proceeding.
3) Re-run `just docs-validate` until it passes.

## Error Resolution Guide

### Missing `doc_status` or `purpose`
- Add the missing frontmatter fields.
- Use `doc_status: stable` unless the doc is explicitly draft or deprecated.

### Missing `intent`
- Add `intent` to frontmatter.
- Use `intent: contract` for rules and schemas.
- Use `intent: procedure` for step-by-step docs.
- Use `intent: problem` or `intent: decision` for problem or decision docs.

### Invalid `doc_status`
- Allowed values are `stable`, `draft`, `deprecated`.
- Update the value to one of the allowed values.

### Invalid `intent`
- Allowed values are defined in `docs/system/intent-model.md`.
- Update to one of the allowed intents.

### Missing `decision_status` or `decision_date`
- Decision docs must include `decision_status` and `decision_date`.
- Use `decision_status: accepted` unless the decision is rejected, superseded, or reversed.
- Use `decision_date: YYYY-MM-DD`.

### Invalid `decision_status`
- Allowed values are `accepted`, `rejected`, `superseded`, `reversed`.
- Update to one of the allowed values.

### Invalid `decision_date`
- Use the `YYYY-MM-DD` format.

### Relationship target does not exist
- Fix the path or create the missing target doc.

### Missing reverse `governed_by` or `governs`
- If `A governs B`, ensure `B` has `governed_by: A`.
- If `B is governed_by A`, ensure `A` lists `B` under `governs`.

### Missing reverse `implements` or `implemented_by`
- If a procedure `implements` a contract, add `implemented_by` to the contract.
- If a contract lists `implemented_by`, add `implements` to the procedure if applicable.

### Missing reverse `related`
- Add the reciprocal `related` link in the target doc.

### Missing doc-code link
- If a doc lists `implemented_by`, the target file must include `@implements <doc-path>`.
- Add the annotation to the target file or remove the `implemented_by` entry if it is not applicable.

## Validation
- `just docs-validate` exits with `Validation passed`.
