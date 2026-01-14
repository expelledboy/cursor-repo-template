# Workflow Variations by Complexity (Reference)

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Define rigor per lifecycle step by complexity level; map to Tier loading, documentation, verification, and checkpoints. All 8 steps are mandatory; rigor varies.

## 1. Lifecycle rigor
| Step | Level 1 | Level 2 | Level 3 | Level 4 |
| --- | --- | --- | --- | --- |
| Intake | Minimal capture | Standard | Comprehensive | Enterprise |
| Classify | Minimal | Standard | Detailed | Detailed |
| Route | Tier1-2 | Tier1-3 | Tier1-4 | Tier1-4 (+Tier5 triggers) |
| Plan | Minimal header | Standard header | Comprehensive w/ checkpoints | Enterprise phased |
| Execute | Direct | Planned | Systematic | Phased with reviews |
| Verify | Basic (smoke) | Standard gates | Comprehensive gates | Enterprise gates (phased) |
| Report | Brief | Standard | Detailed | Enterprise w/ lessons |
| Anneal | Quick note | Standard | Comprehensive | Retrospective |

## 2. Documentation by level
| Level | Plan header | Design checkpoint | Report | Anneal |
| --- | --- | --- | --- | --- |
| 1 | Minimal | Optional (if material) | Brief | Quick |
| 2 | Standard | Optional (if material) | Standard | Standard |
| 3 | Comprehensive | Mandatory | Detailed | Comprehensive |
| 4 | Enterprise | Mandatory (may be multiple) | Enterprise | Retrospective |

Note: Local state in `docs/local/state/` may be used for active task tracking at any level, but it is non-evidence and must only be promoted according to `docs/reference/agentos/state-surface.md`.

## 3. Verification by level
| Level | Gate depth | CI alignment |
| --- | --- | --- |
| 1 | Basic smoke | Minimal |
| 2 | Standard | CI baseline |
| 3 | Comprehensive | CI + extended |
| 4 | Enterprise phased | CI + phased |

## 4. Tier loading mapping
| Level | Tier 1 | Tier 2 | Tier 3 | Tier 4 | Tier 5 |
| --- | --- | --- | --- | --- | --- |
| 1 | Core | Task-type | - | - | - |
| 2 | Core | Task-type | Complexity (L2) | - | - |
| 3 | Core | Task-type | Complexity (L3) | Phase (design checkpoint) | Triggered |
| 4 | Core | Task-type | Complexity (L4) | Phase (design checkpoint) | Triggered |

## 5. Design-decision checkpoint requirements
| Level | Required | Template level | Notes |
| --- | --- | --- | --- |
| 1 | Optional (if material) | Brief | Document if used |
| 2 | Optional (if material) | Basic | Document if used |
| 3 | Mandatory | Comprehensive | If none, state rationale |
| 4 | Mandatory (may be multiple) | Enterprise | If none, state rationale |
