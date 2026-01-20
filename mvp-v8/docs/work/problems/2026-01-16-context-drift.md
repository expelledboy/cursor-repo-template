---
title: "Context Window Drift Prevention"
status: active
created_date: 2026-01-16
purpose: "Multi-step agent reasoning can accumulate entropy and lose consistency as context windows fill"
domain: agentos
Status: active---

# Context Window Drift Prevention

## Description
Multi-step agent reasoning can accumulate entropy and lose consistency as context windows fill with natural language messages.

## Impact
Reasoning quality degrades over task duration, leading to inconsistent decisions and loss of initial task understanding.

## Evidence
Agent conversations naturally accumulate message history, diluting original intent and constraints through unstructured text growth.

## Related Decisions
- [YAML State Representation](docs/explanation/decisions/2026-01-16-yaml-state.md)