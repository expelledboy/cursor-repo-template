# Batch 5: Command-Based Workflow - Deep Integration Analysis

**Status**: Draft
**Date**: 2026-01-15
**Event**: research
**Task**: Comprehensive analysis of Command-Based Workflow integration into AgentOS
**Batch**: 5 of 5 (UI Enhancement Pattern)
**Priority**: P3 (Low value, Medium effort, Low risk)
**Evidence**: Research analysis in this document; no implementation yet.
**Affected artifacts**: None yet (proposal in research stage).

**Note**: Research work preceding ADR creation for single-loop change (adapter enhancement).

---

## Executive Summary

This document provides in-depth analysis of integrating Command-Based Workflow (Cursor 2.0 commands) into AgentOS as an optional UI enhancement. Through multiple self-reflection cycles, we explore how commands can improve UX in Cursor while maintaining AgentOS's adapter boundary and core behavioral contracts.

**Key Insights:**
- Commands are purely UI layer, not core contract
- Commands must enforce AgentOS contracts, not replace them
- Optional enhancement for better Cursor UX
- Must maintain adapter boundary (commands are adapter, not core)

---

## Loop Selection

**Classification**: Single-loop change (adapter-only)
**Rationale**: Adds UI enhancement without changing core contracts. Commands are adapter layer, not core behavior.
**Action**: Update adapter docs, add validation script. No problem entry or ADR required (usability enhancement, not addressing existing problem).

---

## Initial Analysis: Understanding the Pattern

### Memory Bank's Command-Based Workflow

**What it is:**
- Cursor 2.0 commands (`/van`, `/plan`, `/creative`, `/build`, `/reflect`, `/archive`)
- Each command maps to a development phase
- Commands guide workflow progression
- Commands load phase-specific rules

**Why it works:**
- Better UX in Cursor (native command interface)
- Clear workflow progression
- Phase-specific guidance
- Reduces cognitive load (user knows which phase they're in)

**Evidence from Memory Bank:**
- Users report better workflow understanding
- Commands provide clear entry points
- Workflow progression is intuitive
- Commands enforce phase sequence

### Current AgentOS State

**What exists:**
- Task lifecycle: `intake → classify → route → plan → execute → verify → report → anneal`
- Behavioral contract (not UI-specific)
- Cursor adapter exists but no commands
- Adapter boundary clearly defined (rules load context, don't enforce behavior)

**Gap analysis:**
- No command-based entry points
- Users must manually follow lifecycle
- No phase-specific UI guidance
- Workflow progression not visually clear

---

## Self-Reflection Cycle 1: Deep Pattern Analysis

### Reflection Question 1: How do commands align with AgentOS's adapter boundary principle?

**Critical Analysis:**

**AgentOS Adapter Boundary:**
- Section 12: "IDE-specific routing rules may load context but must not change core behavior or override this spec"
- Section 7 (Adapter boundary): "Adapters may load context but must not override routing decisions"
- Adapters are UI layer, not core contract

**Command-Based Workflow:**
- Commands are Cursor 2.0 feature (UI layer)
- Commands can load rules and provide guidance
- Commands cannot enforce behavior (Cursor limitation)

**Alignment:**
- ✅ **Strong Alignment**: Commands are adapter layer, not core
  - Commands map to lifecycle phases (UI convenience)
  - Commands enforce contracts through guidance (not enforcement)
  - Commands don't change core behavior (lifecycle is unchanged)

- ⚠️ **Requires Careful Design**: Commands must not override core
  - Commands must enforce task plan header requirements
  - Commands must enforce lifecycle sequence
  - Commands must enforce AgentOS contracts

**Insight:** Commands are compatible with adapter boundary if designed to enforce contracts, not replace them.

### Reflection Question 2: What commands should map to which lifecycle phases?

**Command-to-Lifecycle Mapping:**

**Option A: Direct Phase Mapping (8 commands)**
- `/agentos-intake` → Intake phase
- `/agentos-classify` → Classify phase
- `/agentos-route` → Route phase
- `/agentos-plan` → Plan phase
- `/agentos-design` → Design-decision checkpoint
- `/agentos-execute` → Execute phase
- `/agentos-verify` → Verify phase
- `/agentos-report` → Report + Anneal phases

**Pros:**
- Direct mapping to lifecycle
- Clear phase boundaries
- Explicit phase progression

**Cons:**
- Too many commands (8 commands)
- Some phases are brief (intake, classify)
- May fragment workflow

**Option B: Grouped Phase Mapping (5 commands)**
- `/agentos-start` → Intake + Classify + Route (initialization)
- `/agentos-plan` → Plan phase
- `/agentos-design` → Design-decision checkpoint
- `/agentos-execute` → Execute phase
- `/agentos-verify` → Verify + Report + Anneal (completion)

**Pros:**
- Fewer commands (5 commands)
- Groups related phases
- More intuitive workflow

**Cons:**
- Less granular control
- Some phases grouped (may lose clarity)

**Option C: Hybrid Mapping (6 commands) - RECOMMENDED**
- `/agentos-start` → Intake + Classify + Route (initialization)
- `/agentos-plan` → Plan phase
- `/agentos-design` → Design-decision checkpoint (if needed)
- `/agentos-execute` → Execute phase
- `/agentos-verify` → Verify phase
- `/agentos-complete` → Report + Anneal (completion)

**Pros:**
- Balanced granularity (6 commands)
- Clear workflow progression
- Design checkpoint is explicit (important phase)
- Verify is separate (important phase)

**Cons:**
- Still more commands than Memory Bank (6 vs 6, but different structure)

**Insight:** Option C (6 commands) provides best balance of granularity and usability.

### Reflection Question 3: How do commands enforce AgentOS contracts?

**Contract Enforcement Strategy:**

**1. Task Plan Header Enforcement:**
- Commands must require task plan header
- Commands must validate header completeness
- Commands must guide user to complete missing fields

**2. Lifecycle Sequence Enforcement:**
- Commands must enforce lifecycle sequence
- Commands must prevent skipping phases
- Commands must guide to next phase

**3. Directive Loading Enforcement:**
- Commands must enforce directive loading (from Batch 2)
- Commands must validate required directives are loaded
- Commands must guide to load missing directives

**4. Design-Decision Checkpoint Enforcement:**
- `/agentos-design` must enforce structured exploration (from Batch 4)
- Commands must prevent execution without checkpoint (if required)
- Commands must validate checkpoint completeness

**5. Verification Enforcement:**
- `/agentos-verify` must enforce verification gates
- Commands must prevent completion without verification
- Commands must validate gate results

**Enforcement Mechanism:**
- Commands provide guidance and validation
- Commands check contract compliance
- Commands prevent progression if contracts violated
- Commands guide user to fix violations

## Command Enforcement Mechanism

**How Commands Enforce Contracts**:

1. **Contract Compliance Checks**:
   - Each command checks task plan header for required fields
   - Validates prerequisite phases are complete
   - Verifies directive loading plan includes required tiers
   - Checks design-decision checkpoint status (if required)

2. **Guidance and Validation**:
   - If violation detected, command provides specific guidance to fix
   - Command cannot block progression (Cursor limitation)
   - User can proceed, but violation is documented in task plan header
   - Validation script (`validate_commands.py`) catches violations later

3. **Sequence Validation**:
   - Each command checks task plan header for previous phase completion
   - If prerequisite phase not complete, command guides user to complete it
   - Command records phase completion in task plan header

4. **Self-Model Constraint**:
   - Commands cannot enforce behavior (per `self-model.md`: "I cannot enforce my own behavior")
   - Commands can guide and validate through observable artifacts (task plan header)
   - Validation scripts are the enforcement mechanism

**Insight:** Commands enforce contracts through guidance and validation, not hard enforcement (Cursor limitation).

---

## Self-Reflection Cycle 2: AgentOS-Specific Considerations

### Reflection Question 4: How do commands interact with existing AgentOS contracts?

**Contract Interaction Analysis:**

**Task Lifecycle (Section 4):**
- **Current**: All tasks follow same sequence
- **Proposed**: Commands map to lifecycle phases
- **Interaction**: ✅ Compatible - commands guide through lifecycle, don't change it

**Primary Objective Control (Section 5):**
- **Current**: Single primary objective required
- **Proposed**: Commands enforce primary objective declaration
- **Interaction**: ✅ Compatible - commands enforce requirement

**Routing Model (Section 8):**
- **Current**: Routing selects directives and domains
- **Proposed**: `/agentos-start` includes routing phase
- **Interaction**: ✅ Compatible - command guides routing, doesn't change model

**Context Loading Contract (Section 10):**
- **Current**: Directive loading plan required
- **Proposed**: Commands enforce loading plan (from Batch 2)
- **Interaction**: ✅ Compatible - commands enforce contract

**Design-Decision Checkpoint (Section 11):**
- **Current**: Required for material decisions
- **Proposed**: `/agentos-design` enforces structured exploration (from Batch 4)
- **Interaction**: ✅ Compatible - command enforces checkpoint

**Verification Contract (Section 14):**
- **Current**: Gates required, aligned with CI
- **Proposed**: `/agentos-verify` enforces gates
- **Interaction**: ✅ Compatible - command enforces contract

**Insight:** Commands enhance contract enforcement without changing contracts.

### Reflection Question 5: How do commands handle complexity-based workflow variations?

**Complexity Integration:**

**From Batch 3:**
- Level 1: Minimal rigor workflow
- Level 2: Standard rigor workflow
- Level 3-4: Comprehensive rigor workflow

**Command Adaptation:**

**Level 1 Tasks:**
- `/agentos-start` → Brief intake/classify/route
- `/agentos-plan` → Brief plan (or skip if very simple)
- `/agentos-design` → Skip (unless material decision)
- `/agentos-execute` → Direct implementation
- `/agentos-verify` → Basic verification
- `/agentos-complete` → Brief report/anneal

**Level 2 Tasks:**
- `/agentos-start` → Standard intake/classify/route
- `/agentos-plan` → Standard plan
- `/agentos-design` → Optional (if material decision)
- `/agentos-execute` → Planned implementation
- `/agentos-verify` → Standard verification
- `/agentos-complete` → Standard report/anneal

**Level 3-4 Tasks:**
- `/agentos-start` → Comprehensive intake/classify/route
- `/agentos-plan` → Comprehensive plan
- `/agentos-design` → Mandatory (structured exploration)
- `/agentos-execute` → Systematic implementation
- `/agentos-verify` → Comprehensive verification
- `/agentos-complete` → Comprehensive report/anneal

**Command Behavior:**
- Commands adapt guidance based on complexity level
- Commands enforce complexity-appropriate requirements
- Commands guide to next appropriate command

**Insight:** Commands adapt to complexity level while maintaining core contract enforcement.

### Reflection Question 6: How do commands maintain traceability?

**Traceability Requirements:**
- All decisions must be traceable
- Command usage must be auditable
- Workflow progression must be recorded

**Traceability Strategy:**

1. **Command Usage Record:**
   ```
   Command Usage:
   - /agentos-start: [timestamp, complexity determined]
   - /agentos-plan: [timestamp, plan created]
   - /agentos-design: [timestamp, checkpoint completed] (if used)
   - /agentos-execute: [timestamp, implementation completed]
   - /agentos-verify: [timestamp, gates passed]
   - /agentos-complete: [timestamp, task completed]
   ```

2. **Command Validation:**
   - Commands validate contract compliance
   - Commands record validation results
   - Commands prevent progression if validation fails

3. **Workflow Progression:**
   - Commands guide to next phase
   - Commands record phase transitions
   - Commands document skipped phases (if any)

4. **Integration with Task Plan Header:**
   - Commands update task plan header
   - Commands record command usage in header
   - Commands maintain header as source of truth

**Insight:** Commands maintain traceability through explicit records and validation.

---

## Self-Reflection Cycle 3: Implementation Details & Edge Cases

### Reflection Question 7: What is the implementation strategy?

**Implementation Plan:**

#### Step 1: Create Command Definitions
**Directory:** `.cursor/commands/` (new)

**Commands to Create:**
1. `agentos-start.md` - Intake + Classify + Route
2. `agentos-plan.md` - Plan phase
3. `agentos-design.md` - Design-decision checkpoint
4. `agentos-execute.md` - Execute phase
5. `agentos-verify.md` - Verify phase
6. `agentos-complete.md` - Report + Anneal

#### Step 2: Command Structure Template
**Each command must include:**

```markdown
# /agentos-[phase] - [Phase Name]

## Purpose
[Brief description of what this command does]

## AgentOS Contract Enforcement
- Enforces: [List of AgentOS contracts enforced]
- Validates: [List of validations performed]
- Guides: [List of guidance provided]

## When to Use
- [Conditions for using this command]
- [Prerequisites]

## What This Command Does
1. [Step 1 - contract enforcement]
2. [Step 2 - validation]
3. [Step 3 - guidance]
4. [Step 4 - next phase guidance]

## AgentOS Requirements
- Task plan header: [Requirements]
- Directive loading: [Requirements]
- Lifecycle sequence: [Requirements]

## Next Steps
- [Next command to use]
- [Conditions for progression]

## Complexity Adaptations
- Level 1: [Brief description]
- Level 2: [Standard description]
- Level 3-4: [Comprehensive description]
```

#### Step 3: Update Cursor Adapter Documentation
**File:** `docs/how-to/agentos/cursor-adapter.md` (enhancement)

**Add Section 7: Optional Commands**
```markdown
## 7. Optional Commands (UI Enhancement)

AgentOS commands are optional UI enhancements that map to lifecycle phases:

- `/agentos-start` - Intake + Classify + Route
- `/agentos-plan` - Plan phase
- `/agentos-design` - Design-decision checkpoint
- `/agentos-execute` - Execute phase
- `/agentos-verify` - Verify phase
- `/agentos-complete` - Report + Anneal

**Important:** Commands are adapter layer only. They enforce AgentOS contracts but do not replace core behavioral contracts. The task lifecycle and contracts remain authoritative.

Commands are located in `.cursor/commands/` and are optional. You can still use AgentOS without commands by manually following the lifecycle.
```

#### Step 4: Create Command Reference
**File:** `docs/reference/agentos/commands.md` (new, optional)

**Content:**
- Command descriptions
- Command-to-lifecycle mapping
- Contract enforcement details
- Complexity adaptations
- Usage examples

#### Step 5: Validation
**File:** `scripts/agentos/validate_commands.py` (new, optional)

**Validation Checks:**
- Commands enforce AgentOS contracts
- Commands don't override core behavior
- Commands guide through lifecycle correctly
- Commands adapt to complexity appropriately

### Reflection Question 8: What are the edge cases and risks?

**Edge Cases:**

1. **Command Skipping:**
   - **Case**: User skips commands, uses lifecycle directly
   - **Solution**: Commands are optional. If skipped, agent must still enforce all contracts through normal lifecycle. Commands are convenience, not requirement.
   - **Validation**: Validation scripts check contract compliance regardless of command usage
   - **Impact**: Low - commands are UI enhancement, not requirement

2. **Command Misuse:**
   - **Case**: User uses commands out of sequence
   - **Solution**: Commands validate sequence, guide to correct phase
   - **Impact**: Low - commands provide guidance, lifecycle is authoritative

3. **Contract Violation:**
   - **Case**: Command doesn't enforce contract correctly
   - **Solution**: Validation script checks command compliance
   - **Impact**: Medium - requires validation discipline

4. **Complexity Mismatch:**
   - **Case**: Command doesn't adapt to complexity correctly
   - **Solution**: Commands check complexity level, adapt guidance
   - **Impact**: Low - commands adapt based on task plan header

5. **Adapter Confusion:**
   - **Case**: Users think commands are core, not adapter
   - **Solution**: Explicit documentation that commands are optional UI layer
   - **Impact**: Medium - requires clear documentation

**Risks:**

1. **Authority Confusion:**
   - **Risk**: Commands mistaken for core contracts
   - **Mitigation**: Explicit documentation, commands reference core contracts
   - **Validation**: Check that commands don't override core

2. **Maintenance Burden:**
   - **Risk**: Commands require maintenance when contracts change
   - **Mitigation**: Commands reference core contracts, minimal duplication
   - **Validation**: Check that commands align with contracts

3. **Over-Engineering:**
   - **Risk**: Too many commands, complex workflow
   - **Mitigation**: 6 commands (balanced), optional usage
   - **Validation**: Check that commands simplify, not complicate

4. **Contract Enforcement Gaps:**
   - **Risk**: Commands don't enforce all contracts
   - **Mitigation**: Each command lists enforced contracts, validation checks
   - **Validation**: Check that all required contracts are enforced

**Insight:** Edge cases are manageable with proper documentation and validation.

---

## Final Enriched Recommendation

### Recommendation: Implement Optional Command-Based Workflow as UI Enhancement

**Rationale:**
After three reflection cycles, command-based workflow is clearly beneficial as an optional UI enhancement. It improves UX in Cursor while maintaining AgentOS's adapter boundary. Commands enforce contracts through guidance and validation, not hard enforcement, which aligns with Cursor's limitations and AgentOS's principles.

**Implementation:**
1. Create `.cursor/commands/` directory with 6 commands (new files)
2. Enhance `cursor-adapter.md` with command documentation (Section 7)
3. Create `commands.md` reference (new file, optional)
4. Create `validate_commands.py` script (new file, optional)

**Key Design Decisions:**
1. **6 Commands**: `/agentos-start`, `/agentos-plan`, `/agentos-design`, `/agentos-execute`, `/agentos-verify`, `/agentos-complete`
2. **Optional Usage**: Commands are UI enhancement, lifecycle is authoritative
3. **Contract Enforcement**: Commands enforce contracts through guidance and validation
4. **Complexity Adaptation**: Commands adapt to complexity level (from Batch 3)
5. **Adapter Boundary**: Commands are adapter layer, not core contract

**Success Criteria:**
- Commands created and documented
- Commands enforce AgentOS contracts
- Commands don't override core behavior
- Commands improve UX in Cursor
- Validation script passes
- Commands are optional (lifecycle works without them)

**Benefits:**
- Better UX in Cursor (native command interface)
- Clear workflow progression
- Phase-specific guidance
- Contract enforcement through guidance
- Maintains adapter boundary

**Tradeoffs:**
- ✅ Improves UX without changing core
- ✅ Maintains adapter boundary
- ⚠️ Adds maintenance burden (commands must stay in sync with contracts)
- ⚠️ Requires validation to ensure contract enforcement
- ⚠️ May cause authority confusion (mitigated by documentation)

---

## Required ADR

**ADR: Optional Command-Based Workflow as UI Enhancement**
- **Problem**: Usability enhancement (not addressing existing problem)
- **Decision**: Implement optional Cursor commands that map to AgentOS lifecycle phases
- **Alternatives**:
  - No commands (rejected - misses UX improvement opportunity)
  - Mandatory commands (rejected - violates adapter boundary, makes commands core)
- **Consequences**:
  - Improves UX in Cursor
  - Adds maintenance burden
  - Requires validation
  - Must maintain adapter boundary
- **Artifacts**:
  - `.cursor/commands/agentos-*.md` (6 commands)
  - `cursor-adapter.md` (enhanced)
  - `commands.md` (optional reference)
  - `validate_commands.py` (optional validation)

---

## Integration with Other Patterns

### With Hierarchical Loading (Batch 2):
- Commands load directives using hierarchical tiers
- Commands enforce tier-based loading
- Commands validate directive loading plan

### With Progressive Documentation (Batch 2):
- `/agentos-design` uses progressive templates
- Commands enforce template selection by complexity
- Commands validate template usage

### With Adaptive Complexity Model (Batch 3):
- Commands adapt to complexity level
- Commands enforce complexity-appropriate requirements
- Commands guide through complexity-based workflow

### With Structured Exploration (Batch 4):
- `/agentos-design` enforces structured exploration phases
- Commands validate phase completion
- Commands guide through exploration phases

### With Visual Process Maps (Batch 1):
- Commands can reference visual process maps
- Commands provide visual guidance
- Commands enhance workflow understanding

---

## Related Docs

- Integration analysis: `docs/work/agentos/improvement/2026-01-15-memory-bank-integration-analysis.md`
- Cursor adapter: `docs/how-to/agentos/cursor-adapter.md`
- Behavior spec: `docs/reference/agentos/behavior-spec.md`
- Cursor mechanics: `docs/reference/agentos/cursor-mechanics.md`

---

**Status**: Ready for implementation (optional)
**Next Action**: Implement optional commands (if desired, no ADR required for usability enhancement)

---

## Command Maintenance Strategy

**Keeping Commands in Sync with Contracts**:

1. **Validation Script**: `validate_commands.py` checks command-contract alignment
2. **Explicit References**: Commands reference contract sections explicitly (e.g., "See Section 4: Task Lifecycle")
3. **Contract Change Triggers**: When contracts change, commands must be reviewed
4. **Documentation**: Commands document which contracts they enforce

---

## Action Items

1. **Create Command Definitions**
   - Owner: [TBD]
   - Evidence: `.cursor/commands/` directory created with 6 command files
   - Completion: [ ] All 6 commands created with proper structure
   - Affected artifacts: `.cursor/commands/agentos-*.md` (6 files)

2. **Enhance cursor-adapter.md**
   - Owner: [TBD]
   - Evidence: Section 7 added with command documentation
   - Completion: [ ] Section 7 added, validated
   - Affected artifacts: `docs/how-to/agentos/cursor-adapter.md`

3. **Create commands.md (Optional)**
   - Owner: [TBD]
   - Evidence: Reference file created with command descriptions
   - Completion: [ ] File created (if desired)
   - Affected artifacts: `docs/reference/agentos/commands.md`

4. **Create Validation Script (Optional)**
   - Owner: [TBD]
   - Evidence: Script created and tested
   - Completion: [ ] Script passes, added to validation-scripts.md (if desired)
   - Affected artifacts: `scripts/agentos/validate_commands.py`

5. **Run Post-Implementation Micro-AAR**
   - Owner: [TBD]
   - Evidence: Micro-AAR note created in `docs/work/agentos/improvement/`
   - Completion: [ ] Micro-AAR completed, lessons learned captured
   - Affected artifacts: `docs/work/agentos/improvement/YYYY-MM-DD-commands-micro-aar.md`

---

## Post-Implementation Verification

After implementing this batch:

1. **Run MAM**: Use Meta Analysis Mode to validate behavior
   - Check: Task plan header present and complete
   - Check: Required directives loaded
   - Check: Contracts enforced
   - Check: Gaps captured if discovered

2. **Run Validation Scripts**: Execute batch-specific validation
   - `just agentos::validate-commands` (or equivalent, if created)

3. **Micro-AAR**: Capture lessons learned
   - What worked well?
   - What challenges were encountered?
   - What gaps were discovered?
   - Update improvement note with Micro-AAR results

4. **Integration Testing**: Test with previously implemented batches
   - Test commands with all patterns (hierarchical loading, complexity, structured exploration)

---

## Gap Capture During Implementation

During implementation, capture gaps per `docs/how-to/agentos/capture-gaps.md`:
- Missing or incorrect directives
- Unclear or missing steps
- Verification gate issues
- Ambiguity resolutions

Promote gaps to problems if they define new problems.

---

## Required ADR

**ADR Title**: Optional Command-Based Workflow as UI Enhancement

**Status**: Proposed (to be created, optional)
**Date**: [Will be set when ADR is created]
**Scope**: agentos
**Problem IDs**: Usability enhancement, no problem entry
**Supersedes**: (if applicable)

**Note**: This ADR is optional (usability enhancement). If created, it must follow `docs/reference/agentos/decision-record-format.md` for full format requirements.

**ADR Summary**:
- Decision: Implement optional Cursor commands that map to AgentOS lifecycle phases
- Alternatives: No commands (rejected - misses UX improvement opportunity), Mandatory commands (rejected - violates adapter boundary, makes commands core)
- Consequences: Improves UX in Cursor, adds maintenance burden, requires validation, must maintain adapter boundary
- Artifacts: `.cursor/commands/agentos-*.md` (6 commands), `cursor-adapter.md`, `commands.md` (optional), `validate_commands.py` (optional)
