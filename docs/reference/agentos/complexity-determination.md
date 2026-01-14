# Complexity Determination (Reference)

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Define complexity levels (1-4) and criteria to select them; used in task plan headers and workflow rigor.

## 1. Level definitions
| Level | Description | Typical duration | Key characteristics |
| --- | --- | --- | --- |
| 1 | Quick fix / simple change | Hours | Single component, low risk, minimal dependencies |
| 2 | Standard enhancement | Days | Multiple components, simple design decisions, moderate risk |
| 3 | Intermediate feature | Weeks | Subsystem impact, complex design decisions, high risk |
| 4 | System/architecture change | Weeks–months | System-wide impact, architectural decisions, critical risk |

## 2. Determination criteria
| Criterion | Level 1 | Level 2 | Level 3 | Level 4 |
| --- | --- | --- | --- | --- |
| Scope | Single component | Multiple components | Subsystem | System-wide |
| Design decisions | None/simple | Simple | Complex | Architectural |
| Risk | Low | Moderate | High | Critical |
| Effort | Hours | Days | Weeks | Months |
| Dependencies | None | Few | Many | Architectural |

## 3. Decision tree (text)
Start → Bug fix? Yes → Single component? → Level 1; Multiple → Level 2.
Else → Small enhancement? Yes → Self-contained? → Level 2; else → Level 3.
Else → Complete feature? Yes → Architectural implications? Yes → Level 4; else → Level 3.
Else → System-wide change? Yes → Level 4.

## 4. Escalation rules
- Complexity can only escalate (not de-escalate) during execution.
- Escalation requires explicit trigger and user confirmation.
- Update task plan header and load additional directives per new level.
- Document escalation in the report.

## 5. Example
Selected Level: 2
Rationale: Multiple components, simple design decision, moderate risk, effort=days, dependencies=few.
Header entry: record level, rationale, criteria, and workflow variation (Level 2).
