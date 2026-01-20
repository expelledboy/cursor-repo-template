---
title: "Meta-Analysis Mode (MAM)"
status: stable
created_date: 2026-01-18
purpose: "Defines bounded self-audit capabilities for AgentOS to validate its own behavior using current context"
domain: agentos
---

# Meta-Analysis Mode (MAM) (Reference)

## Purpose
Provides a bounded, on-demand self-audit mechanism for AgentOS to validate its own behavior and alignment using only the current chat context and loaded directives. Serves as a systematic check when DOE alignment issues are suspected.

## Definition
Meta-Analysis Mode is a **bounded self-audit** that uses only:
- Current chat context window (no external logs)
- Loaded AgentOS directives and referenced artifacts
- No opaque memory or hidden state

## When to Use MAM

### Trigger Conditions
MAM should be requested by the agent when:
- AgentOS Meta-Maintenance tasks are initiated
- Failed AgentOS validation scripts occur
- Ambiguity resolutions change core behavior
- Destructive action requests or near-misses happen
- User requests alignment validation
- Continuous self-awareness detects persistent issues

### User Approval
MAM requires explicit user approval before activation to prevent unnecessary context usage.

## Audit Checklist

When MAM is approved, perform these checks in order:

### 1. Task Plan Header Completeness
- [ ] Task type declared and matches routing decisions
- [ ] Primary objective stated and measurable
- [ ] Complexity level determined with rationale
- [ ] Workflow variation selected appropriately
- [ ] Required directives identified
- [ ] Evidence sources declared with authority levels
- [ ] Verification gates defined

**Evidence**: Task plan header in current context

### 2. Directive Loading Compliance
- [ ] Required directives loaded before execution
- [ ] Context Compass intent constraints respected
- [ ] Directive tiers loaded in proper sequence
- [ ] Only allowed documentation types loaded for task intent

**Evidence**: Directive loading declarations in task plan

### 3. Evidence Source Validation
- [ ] Sources follow authority hierarchy (reference > how-to > explanation)
- [ ] Sources are current (not superseded or archived inappropriately)
- [ ] Sources directly support the primary objective
- [ ] Source accessibility confirmed

**Evidence**: Evidence source declarations and usage in context

### 4. Verification Gate Completeness
- [ ] Gates defined for task type and complexity
- [ ] Gate commands are valid and executable
- [ ] Gate sequence appropriate for task lifecycle
- [ ] Gate failure handling defined

**Evidence**: Verification gate declarations in task plan

### 5. Safety Compliance
- [ ] Destructive actions identified and confirmed
- [ ] Rollback plans documented for critical operations
- [ ] Safety policies followed throughout task
- [ ] No untrusted input handling without validation

**Evidence**: Safety declarations and destructive action confirmations

### 6. Gap Capture Status
- [ ] All discovered gaps documented as work notes
- [ ] Gap improvement events initiated where appropriate
- [ ] Gap promotion to problem registry when systemic

**Evidence**: Gap documentation and improvement event initiation

### 7. Contract Compliance
- [ ] DOE lifecycle phases followed correctly
- [ ] Authority order respected in all decisions
- [ ] Context usage within reasonable bounds
- [ ] Self-awareness checkpoints applied

**Evidence**: Contract adherence throughout task execution

## Output Format

### Successful Audit
```
✅ MAM Complete - No alignment issues detected
- Task plan: Complete and valid
- Directives: Properly loaded and compliant
- Evidence: Authoritative and current
- Gates: Comprehensive and executable
- Safety: All protocols followed
- Gaps: Captured and addressed
- Contracts: Fully compliant
```

### Issues Found
```
⚠️ MAM Complete - Alignment issues detected
❌ Issues requiring attention:
   • Task plan missing complexity assessment
   • Evidence sources include inappropriate archived docs
   • Verification gates not defined for task type

💡 Recommended actions:
   • Complete task plan header with missing elements
   • Replace archived sources with current references
   • Add verification gates for Implementation / Feature tasks
   • Consider `/learn` to capture planning improvement gap
```

### Gap Discovery
When MAM identifies gaps:
1. Immediately create work note with gap details
2. Propose improvement event type (micro-AAR, retrospective, postmortem)
3. Link to relevant MAM findings
4. Update traceability if core behavior affected

## Relationship to Self-Awareness

### Continuous vs Deep Audit
- **Self-Awareness Framework**: Continuous monitoring during normal task execution
- **MAM**: Deep, bounded audit when alignment issues suspected
- **Integration**: MAM validates self-awareness effectiveness and identifies systemic gaps

### Checkpoint Integration
MAM can be triggered by:
- Self-awareness detecting persistent contract violations
- Multiple user corrections indicating misalignment
- Verification gate failures suggesting planning issues
- User requests for alignment validation

## Bounded Nature

### Evidence Constraints
MAM operates only within current context boundaries:
- No access to external logs or hidden memory
- Only observable artifacts and declarations
- Current chat context window only
- No assumptions about unobservable state

### Scope Limitations
MAM cannot validate:
- Chat output quality directly (requires artifacts)
- External system behavior
- Long-term pattern effectiveness
- Unobservable internal processes

## Integration Points

### Command System
- `/retrospect` can trigger MAM for deeper analysis
- MAM findings feed into `/learn` for gap capture
- MAM results inform `/evolve` improvement decisions

### Improvement Workflow
MAM integrates with the self-improvement loop:
1. MAM detects alignment issues
2. `/learn` captures gaps as work notes
3. `/evolve` implements fixes based on MAM findings

### Verification System
MAM validates verification system effectiveness:
- Gate definition completeness
- Gate execution appropriateness
- Verification outcome reliability

## Success Criteria

### Effective MAM
- Identifies real alignment issues without false positives
- Provides actionable remediation steps
- Completes within reasonable context usage
- Integrates seamlessly with improvement workflow

### Process Integration
- MAM triggers are appropriate and not excessive
- Findings lead to actual improvements
- Process overhead is minimal compared to benefits
- User approval requirements are respected

## Related
- `docs/reference/agentos/self-awareness-framework.md` - Continuous monitoring
- `docs/reference/agentos/self-improvement.md` - Improvement workflow integration
- `docs/reference/agentos/architecture.md#doe-integrated-flow` - DOE compliance validation
- `.cursor/commands/retrospect.md` - MAM trigger integration