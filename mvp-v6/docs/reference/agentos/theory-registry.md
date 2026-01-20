# Theory Registry (v6)

Status: Draft
Date: 2026-01-15
Purpose: A compact list of falsifiable hypotheses and the probes that test them.

## Status values
- Draft: proposed, not yet repeatedly tested
- Validated: repeatedly observed under probes (and SIG_T evidence when applicable)
- Falsified: probe results contradict the hypothesis
- Superseded: replaced by another theory ID

## Theories
| ID | Claim (falsifiable) | Primary probe(s) | Status |
|---|---|---|---|
| T1 | Tool outputs (SIG_T) reduce incorrect conclusions vs relying on search (SIG_S) alone. | P5, P2 | Draft |
| T2 | Parallel subagents reduce time-to-solution on ambiguous tasks without increasing error rate when outputs require SIG_T or SIG_U promotion. | P3 | Draft |
| T3 | Mentions reduce routing ambiguity when treated as explicit injections (SIG_U/SIG_F). | P6 | Draft |
| T4 | Skills/rules should remain composable; large monolithic rules increase stale guidance rate. | P7 | Draft |

## Promotion rule (minimal)
Promote a theory from Draft -> Validated only after:
- >= 3 successful probe runs recorded, and
- if the theory is about factual correctness, at least one run uses SIG_T evidence.
