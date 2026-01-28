---
doc_status: stable
purpose: Define the problem of context loss causing objective drift.
intent: problem
governed_by:
  docs/system/model/problem-doc.md: Load if you need the required fields for problem docs
related:
  docs/system/decision/introduce-objective-graph.md: Load if you need the decision that resolves this problem
---

# Problem: Context Loss Breaks Alignment

## Problem Statement
Context loss causes agents to drift from the original objective during subtasks.

## Scope and Boundaries
- Applies to multi-step tasks with nested subtasks.
- Includes compaction, new sessions, and sub-agent starts.

## Consequences
- Subtasks diverge from negotiated requirements.
- Implementation changes no longer match doc intent.
- Outcomes vary across sessions.

## Failure Modes if Ignored
- Subtasks accumulate scope creep.
- Different agents converge on different outcomes.

## Related Decisions
- Introduce objective graph.
