# Decision Graph: routing (agentos.decision-graph/v1)

Status: Draft
Date: 2026-01-15
Purpose: Deterministically select a primary role (DISCOVER/SHAPE/ACT/CHECK/CLOSE) and what to load next.

```yaml
spec_version: agentos.decision-graph/v1
name: routing
description: choose primary role + loads
expression_language: string

nodes:
  - id: start
    type: decision_table
    hit_policy: first
    rules:
      - id: r_close
        when: "context.task.objective.lower().contains('summarize') or context.task.objective.lower().contains('report')"
        output: { route: CLOSE, confidence: 0.8, load: ["docs/reference/agentos/spec-decision-trace.md"] }

      - id: r_check
        when: "context.task.objective.lower().contains('test') or context.task.objective.lower().contains('verify') or context.task.objective.lower().contains('validate')"
        output: { route: CHECK, confidence: 0.85 }

      - id: r_act
        when: "context.task.objective.lower().contains('implement') or context.task.objective.lower().contains('change') or context.task.type == 'execution'"
        output: { route: ACT, confidence: 0.9 }

      - id: r_shape
        when: "context.task.objective.lower().contains('scope') or context.task.objective.lower().contains('plan') or context.task.objective.lower().contains('route')"
        output: { route: SHAPE, confidence: 0.75 }

      - id: r_default
        when: "true"
        output: { route: DISCOVER, confidence: 0.6 }
```

