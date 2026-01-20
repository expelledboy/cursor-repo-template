# Validation Strategy Decision Graph

**Purpose**: Select appropriate validation approach based on task type, complexity, and available resources.

**Status**: Initial Version
**Date**: 2026-01-14

---

## Decision Tree

### Step 1: Check CI Availability
**Question**: Is a CI/CD pipeline available and configured?

**If YES** → Use **CI as Primary Validation**
- CI workflows are highest authority (per truth surface hierarchy)
- Load: `docs/reference/agentos/validation-contract.md` (CI integration section)
- Confidence: 0.99
- **Stop here**

**If NO** → Proceed to Step 2

---

### Step 2: Check Test Availability
**Question**: Are automated tests available for this change?

**If YES** → Use **Automated Test Suite**
- Run test suite as primary validation
- Load: `docs/reference/agentos/validation-contract.md` (test execution section)
- Confidence: 0.95
- **Stop here**

**If NO** → Proceed to Step 3

---

### Step 3: Check Task Runner Commands
**Question**: Are executable commands/scripts available for validation?

**If YES** → Use **Command-Based Validation**
- Execute validation commands
- List exact commands and expected outcomes
- Load: `docs/reference/agentos/validation-contract.md` (command execution section)
- Confidence: 0.90
- **Stop here**

**If NO** → Proceed to Step 4

---

### Step 4: Determine Manual Validation Requirements
**Question**: What is the task complexity level?

**If Level 1** → **Basic Manual Validation**
- Visual review
- Smoke testing
- Brief checklist
- Confidence: 0.80

**If Level 2** → **Standard Manual Validation**
- Structured review process
- Standard verification checklist
- Documented validation steps
- Confidence: 0.75

**If Level 3-4** → **Comprehensive Manual Validation**
- Detailed validation protocol
- Multiple review checkpoints
- Stakeholder sign-off (if applicable)
- Confidence: 0.70

---

## Validation Gate Hierarchy

When multiple validation methods are available, use this priority:

1. **CI Workflows** (highest authority)
2. **Automated Tests**
3. **Task Runner Commands**
4. **Manual Validation** (lowest authority, but acceptable when others unavailable)

---

## Complexity-Specific Gates

### Level 1 (Minimal Rigor)
- Basic syntax/format checks
- Visual review
- Smoke test (if applicable)

### Level 2 (Standard Rigor)
- Standard test suite (if available)
- Code review checklist
- Integration smoke test

### Level 3 (Enhanced Rigor)
- Comprehensive test suite
- Security audit (if security-related)
- Performance testing (if performance-critical)
- Documentation review
- Design-decision checkpoint validation

### Level 4 (Maximum Rigor)
- Full test suite + coverage requirements
- Security audit + penetration testing (if applicable)
- Performance benchmarking
- Architecture review
- Stakeholder approval
- Phased validation with checkpoints

---

## Task-Type Specific Gates

### Execution Tasks
- Functional correctness
- Integration testing
- Regression prevention

### Architecture Tasks
- Design-decision checkpoint (Level 3-4)
- Architecture review
- Impact analysis validation
- Backward compatibility (if refactoring)

### Coordination Tasks
- Stakeholder alignment validation
- Communication protocol verification
- Process compliance check

---

## Fallback Strategy

If no validation gates are available:
1. Document what validation would be needed
2. List exact commands that should be run (if known)
3. Request user confirmation before proceeding
4. Capture gap: missing validation gates

---

## Examples

**Example 1**: Level 1 task, CI available
- **Strategy**: CI as primary validation
- **Gates**: CI workflow runs automatically
- **Confidence**: 0.99

**Example 2**: Level 3 task, tests available, no CI
- **Strategy**: Automated test suite
- **Gates**: Run full test suite, check coverage, security audit
- **Confidence**: 0.95

**Example 3**: Level 2 task, no CI, no tests, commands available
- **Strategy**: Command-based validation
- **Gates**: Run validation scripts, check outputs
- **Confidence**: 0.90

**Example 4**: Level 1 task, no automation available
- **Strategy**: Basic manual validation
- **Gates**: Visual review, smoke test
- **Confidence**: 0.80

---

## Integration with Task Lifecycle

This decision graph is used:
- **During Planning**: Determine verification gates for task plan header
- **Before Execution**: Confirm validation strategy
- **After Execution**: Execute selected validation gates
- **During Verification Phase**: Run validation and report results
