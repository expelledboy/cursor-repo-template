---
doc_status: stable
purpose: Define hard constraints of Cursor and agent runtime environments.
intent: facts
governed_by:
  docs/domains/dev.md: Authority for dev domain docs
---

# Fact: Cursor and Agent Runtime Mechanics

## Context Loading Hierarchy
1. **System Rules:** Loaded first, always present.
2. **Description Rules:** Triggered by user query semantic match.
3. **Glob Rules:** Triggered by active file paths.
4. **Manual Context:** Explicitly added by user (@file).

## Physical Constraints
- **Finite Context:** Token limits are a hard physical ceiling.
- **Compaction:** When limits are reached, the system compacts history. Critical instructions **will be lost** if not re-injected.
- **Cost of Context:** Loading unused context is a defect. It crowds out relevant information and degrades reasoning.

## Correctness Principle
- An instruction not present in the active context window is effectively non-existent.
- Relying on "training memory" or "previous session history" is unsafe.
