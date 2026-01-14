# Problem: Registry Drift and Unmapped Work

**Status**: Draft
**Date**: 2026-01-13
**Scope**: system

## Statement
Files requiring documentation are added or changed without updating their directive mapping.

## Evidence
User requirement: files that require documentation must be checked into git and documented (2026-01-13).

## Impact
Docs and code diverge, and the agent cannot deterministically locate the correct directive.

## Detection signals
- New or changed files have no documented directive mapping.
- Documentation is updated without linking to implementing files.
- Docs lack implementation links for changed code.

## Notes
- Validation evidence: at least one instance of code change without a corresponding directive update.
