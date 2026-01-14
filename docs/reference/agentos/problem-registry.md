# AgentOS Problem Registry

**Status**: Stable
**Date**: 2026-01-13
**Purpose**: Canonical list of known problems AgentOS must address (Reference/Contract).

---

## 1. Scope
- The registry records problems, not solutions.
- Problems are stable, additive, and never deleted.
- Superseded problems remain for traceability.

## 2. Required fields
- ID
- Title
- Status
- Scope
- Statement
- Evidence
- Impact
- Detection signals

## 3. ID format
- PRB-0001 (zero-padded, monotonic)
- IDs are assigned only when a problem is validated.

## 4. Status values
- Proposed: hypothesis captured, evidence incomplete.
- Validated: evidence accepted by maintainer.
- Superseded: replaced by another problem ID (must link).

## 5. Change rules
- Additions follow `docs/how-to/agentos/problem-intake.md`.
- Status changes require an evidence update.
- Superseded entries must reference the replacing ID.
- `docs/reference/agentos/traceability.md` must be updated for every new or superseded entry.

---

## 6. Registry
| ID | Title | Status | Scope | Statement | Evidence | Impact | Detection signals |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRB-0001 | Goal Drift Across Multi-Step Tasks | Validated | system | Agents lose the primary objective during multi-step work and optimize local sub-tasks instead. | User report (2026-01-13). | Primary requirements are missed or partially met, causing rework. | Plan lacks primary objective; sub-task changes without closing the primary requirement; user corrections on scope. |
| PRB-0002 | Context Instability and Opaque Memory | Validated | system | Context selection is unstable or opaque, causing inconsistent access to required directives. | User report: IDE rule loading and memories are opaque and can change behavior (2026-01-13). | Inconsistent directives lead to ambiguous or incorrect decisions. | Same task produces different outputs; missing canonical docs; constraints must be restated. |
| PRB-0003 | Unresolved Ambiguity in Requirements | Validated | system | Ambiguous requirements are not resolved immediately, leading to inconsistent outcomes. | User report: ambiguity must be resolved with the user and captured in docs (2026-01-13). | Behavior diverges from intent and is harder to correct later. | No clarifying questions on ambiguous input; intent corrections after implementation; missing documentation of resolutions. |
| PRB-0004 | Verification Gate Gaps and Decay | Validated | system | Verification gates are missing, stale, or not maintained, allowing regressions to slip through. | User requirement: continuously learn, create, and maintain quality gates (2026-01-13). | Changes ship without adequate validation, increasing regressions. | Tasks complete without a verification step; gates diverge from CI; regressions reappear. |
| PRB-0005 | Rationale Loss Across Evolution | Validated | system | Rationale for core design is lost over time, causing critical constraints to be removed. | User requirement: preserve why the core exists so evolution does not forget (2026-01-13). | Core behavior drifts or regresses when changes lack rationale. | Constraints removed without rationale; repeated debates about why rules exist; core changes without ADRs. |
| PRB-0006 | Routing Drift and Misrouting | Validated | system | Routing selection fails or drifts, causing the agent to load directives from the wrong domain. | User requirement: routing and route management are critical (2026-01-13). | Incorrect constraints and procedures lead to incorrect outcomes or wasted effort. | Task uses directives from a different domain; canonical docs not loaded; repeated user corrections about domain. |
| PRB-0007 | Registry Drift and Unmapped Work | Validated | system | Files requiring documentation are added or changed without updating their directive mapping. | User requirement: files that require documentation must be checked into git and documented (2026-01-13). | Docs and code diverge, and deterministic directive lookup fails. | New or changed files have no directive mapping; docs updated without implementation links; docs lack implementation links for changed code. |
| PRB-0008 | Unsafe Autonomy on Destructive Actions | Validated | system | Destructive actions are attempted without explicit user confirmation. | User requirement: ask on destructive operations (2026-01-13). | Unintended deletions or irreversible changes increase risk and reduce trust. | Destructive actions proposed or executed without confirmation; missing confirmation prompt; user requests rollback. |
| PRB-0009 | Non-Deterministic Execution | Validated | system | Ad-hoc or inconsistent execution steps produce non-repeatable outcomes. | User requirement: meta-planner with decision trees and runbooks (2026-01-13). | Behavior varies between runs, making verification and maintenance unreliable. | Similar tasks use different commands without documented reasons; steps not captured in deterministic tools; results differ across repeated runs. |
| PRB-0010 | Task Taxonomy Drift | Validated | system | Task types evolve without updating routing, verification, and documentation contracts. | User requirement: task taxonomy should evolve by adding and refining tasks as needed (2026-01-13). | New or changed task types are handled inconsistently and bypass required controls. | New task types appear without behavior spec or traceability updates; tasks routed without taxonomy entry; verification steps missing for new task types. |
| PRB-0011 | Bootstrap and Portability Gaps | Validated | system | New or poorly documented repos lack routing and directives, causing the agent to guess and misalign. | User requirement: AgentOS must be portable and bootstrap when directives are missing (2026-01-13). | Early tasks are misrouted or incomplete, delaying alignment. | Missing `docs/index.md` or routing rules; tasks proceed without canonicals; repeated clarifications about workflows. |
