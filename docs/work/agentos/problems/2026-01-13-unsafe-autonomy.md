# Problem: Unsafe Autonomy on Destructive Actions

**Status**: Draft
**Date**: 2026-01-13
**Scope**: system

## Statement
Destructive actions are attempted without explicit user confirmation.

## Evidence
User requirement: ask on destructive operations (2026-01-13).

## Impact
Unintended deletions or irreversible changes increase risk and reduce trust.

## Detection signals
- Destructive actions are proposed or executed without confirmation.
- Lack of a confirmation prompt in task output.
- User requests rollback after destructive changes.

## Notes
- Validation evidence: at least one destructive action attempted without explicit confirmation.
