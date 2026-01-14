# Problem: Context Instability and Opaque Memory

**Status**: Draft
**Date**: 2026-01-13
**Scope**: system

## Statement
Context selection is unstable and opaque, causing agents to act without consistent access to required directives.

## Evidence
- User report: IDE rule loading and hidden memories can lose fidelity and change behavior (2026-01-13).
- User report: memories are opaque and not inspectable by the agent (2026-01-13).

## Impact
Agents act with incomplete or inconsistent directives, increasing ambiguity and incorrect decisions.

## Detection signals
- Different outputs for the same task without repo changes.
- Missing citations to expected canonical docs.
- Requests to restate or reload already defined constraints.

## Notes
- Track whether required directives were explicitly loaded during the task.
- Validation evidence: at least two runs of the same task where the required directive set changed without repo changes.
