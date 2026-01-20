# Decision Card: Complexity

Status: Draft
Date: 2026-01-15

## Dimensions
- Scope: files/systems touched
- Decisions: design choices required
- Risk: blast radius
- Dependencies: external coupling

## Levels
- L1: low across dimensions
- L2: moderate complexity
- L3: high complexity
- L4: critical complexity

## Rules
- Count High and Medium across dimensions.
- If High >= 3 -> L4.
- Else if High >= 2 -> L3.
- Else if High >= 1 or Medium >= 3 -> L2.
- Else -> L1.
