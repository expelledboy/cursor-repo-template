# Task Classification Decision Graph

**Purpose**: Deterministically classify incoming tasks into task types.

**Status**: Initial Version
**Date**: 2026-01-14

---

## Decision Tree

### Step 1: Check Objective Clarity
**Question**: Does the task have a clear, unambiguous primary objective?

**If YES** → Route to: **Execution**
- Load: `docs/reference/agentos/alignment-mechanisms.md` (execution section)
- Confidence: 0.95
- **Stop here**

**If NO** → Proceed to Step 2

---

### Step 2: Check Stakeholder Involvement
**Question**: Are multiple stakeholders involved or is coordination required?

**If YES** → Route to: **Coordination**
- Load: `docs/reference/agentos/evolution-framework.md` (stakeholder coordination)
- Confidence: 0.90
- **Stop here**

**If NO** → Proceed to Step 3

---

### Step 3: Check Technical Complexity
**Question**: Does the task involve architectural decisions or system-wide changes?

**If YES** → Route to: **Architecture**
- Load: `docs/reference/agentos/architectural-patterns.md`
- Confidence: 0.85
- **Stop here**

**If NO** → Route to: **Direct Execution**
- Load: `docs/reference/agentos/alignment-mechanisms.md` (minimal workflow)
- Confidence: 0.95
- **Stop here**

---

## Fallback
If classification is unclear after all steps:
1. Request user clarification
2. Load: `docs/reference/agentos/coherence-contract.md` (ambiguity resolution section)
3. Document uncertainty in task plan header

---

## Task Types Reference
- **Execution**: Clear objective, straightforward implementation
- **Coordination**: Multiple stakeholders, requires alignment
- **Architecture**: System-wide changes, architectural decisions
- **Direct Execution**: Simple, isolated changes
