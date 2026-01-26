---
doc_status: stable
purpose: Define when and how to cache external references for skills.
intent: procedure
governed_by:
  docs/system/model/procedure-doc.md: Load if you need the contract for procedure docs
related:
  docs/dev/decision/prefer-authoritative-sources.md: Load if you need the decision this procedure applies
  docs/system/model/reference-doc.md: Load if you need the reference doc contract
  docs/system/procedure/creating-agent-skills.md: Load if you need the skill procedure that uses references
---

# Caching External References

## Purpose
Cache external references only when rapid recall is required.

## Inputs
- The skill that requires a cached reference.
- The external source URL.
- The refresh interval or condition.

## Procedure
1) Confirm that rapid recall is required for the task or workflow.
2) Create `agent/skills/<skill>/references/<name>.md`.
3) Add frontmatter with `intent: reference` and `source_url`.
4) Describe what the source contains and where to look, without restating it.
5) Record a refresh policy and a validation check.
6) Link the reference from the skill documentation.

## Validation
- The reference doc includes `source_url` and a refresh policy.
- The reference describes where to find content, not how to act on it.

## Failure Modes
- Cached content becomes the de facto source of truth.
- The reference includes actionable instructions or decisions.
- No refresh policy exists for a volatile source.
