---
title: "Problem Registry"
status: stable
created_date: 2026-01-18
purpose: "Canonical list of known problems AgentOS must address, with systematic tracking and resolution workflow"
domain: agentos
---

# Problem Registry (Reference)

## Purpose
Maintains a canonical registry of problems that AgentOS must address. Problems are validated issues requiring systematic resolution through the improvement workflow. The registry ensures problems are not forgotten, tracks resolution progress, and provides historical context for system evolution.

## Core Principles

### Problem vs Solution Focus
- **Records problems**, not proposed solutions
- **Stable and additive** - problems are never deleted
- **Evidence-based** - problems must be validated before entry
- **Actionable** - problems must be resolvable within system constraints

### Registry Lifecycle
- Problems persist until resolved or proven invalid
- Superseded problems remain for traceability
- Problem status tracks resolution progress
- Registry enables systematic improvement prioritization

## Registry Structure

### Problem ID Format
```
PRB-0001, PRB-0002, etc.
```
- Zero-padded, monotonic numbering
- Assigned only when problem is validated
- Never reused (maintains historical references)

### File Organization
```
docs/work/problems/
├── YYYY-MM-DD-problem-slug.md    # Individual problem docs
└── index.md                       # Registry index and summary
```

### Problem Document Template
```markdown
---
title: "Problem: [Descriptive Title]"
created_date: YYYY-MM-DD
domain: agentos | [specific domain]
Status: proposed | validated | resolved | invalid
problem_id: PRB-XXXX
severity: low | medium | high | critical
tags: [relevant tags]
related:
  - docs/explanation/decisions/[adr-that-addresses-this].md
  - docs/reference/[relevant-spec].md
---

# Problem: [Title]

## Statement
[Clear, concise problem statement]

## Context
[When and where the problem occurs]

## Impact
[Why this matters - business/technical consequences]

## Evidence
[Specific examples, metrics, user reports, error logs]

## Detection Signals
[How to identify this problem occurring]

## Current Workarounds
[How users/team currently cope with the problem]

## Proposed Investigation
[Initial thoughts on root cause and solution approaches]

## Related Problems
[Links to similar or related problems]
```

## Problem Status Definitions

### Proposed
- **Definition**: Problem hypothesis captured, evidence incomplete
- **Requirements**: Clear statement, initial impact assessment, detection signals
- **Next Steps**: Gather evidence, validate problem existence
- **Duration**: Typically < 1 week to validate

### Validated
- **Definition**: Evidence collected, problem confirmed as real and significant
- **Requirements**: Comprehensive evidence, impact quantification, reproducible detection
- **Next Steps**: Prioritize against other problems, initiate solution exploration
- **Duration**: Until solution implementation begins

### Resolved
- **Definition**: Problem addressed through implemented solution
- **Requirements**: Solution implemented, evidence of problem elimination, monitoring in place
- **Next Steps**: Monitor for recurrence, document lessons learned
- **Duration**: Ongoing monitoring period

### Invalid
- **Definition**: Problem determined not to exist or be significant
- **Requirements**: Evidence showing problem is not real, misidentified, or resolved elsewhere
- **Next Steps**: Remove from active consideration, document why invalid
- **Duration**: Permanent status

## Problem Severity Levels

### Critical
- **Impact**: System unusable, safety risks, legal compliance violations
- **Response Time**: Immediate (hours/days)
- **Resources**: Full team priority, executive involvement
- **Examples**: System crashes, security breaches, data loss

### High
- **Impact**: Major functionality broken, significant user pain, business revenue impact
- **Response Time**: Urgent (days/weeks)
- **Resources**: Dedicated team, stakeholder involvement
- **Examples**: Core features broken, performance degradation, integration failures

### Medium
- **Impact**: Annoying but work-aroundable, affects subset of users/features
- **Response Time**: Important (weeks/months)
- **Resources**: Scheduled work, cross-team coordination
- **Examples**: UI inconsistencies, performance issues, documentation gaps

### Low
- **Impact**: Minor annoyances, edge cases, nice-to-have improvements
- **Response Time**: When convenient (months/quarters)
- **Resources**: Backlog items, community contributions
- **Examples**: Small UI improvements, minor documentation issues

## Problem Resolution Workflow

### 1. Problem Validation
- **Entry Criteria**: Problem proposed with initial evidence
- **Activities**:
  - Review problem statement clarity
  - Assess evidence quality and completeness
  - Evaluate impact and severity
  - Confirm problem is within system scope
- **Exit Criteria**: Problem status changed to `validated`
- **Responsible**: Problem intake team or individual

### 2. Solution Exploration
- **Entry Criteria**: Validated problem ready for resolution
- **Activities**:
  - Form solution exploration team
  - Define solution requirements
  - Research solution options
  - Create solution proposal
- **Exit Criteria**: ADR created and accepted
- **Responsible**: Solution exploration team

### 3. Implementation
- **Entry Criteria**: ADR accepted with implementation plan
- **Activities**:
  - Execute implementation plan
  - Create/update tests and validation
  - Update documentation
  - Deploy solution
- **Exit Criteria**: Solution deployed and validated
- **Responsible**: Implementation team

### 4. Validation & Monitoring
- **Entry Criteria**: Solution deployed
- **Activities**:
  - Validate problem resolution
  - Monitor for recurrence
  - Measure solution effectiveness
  - Document lessons learned
- **Exit Criteria**: Problem status changed to `resolved`
- **Responsible**: Validation team

## Problem Registry Operations

### Adding New Problems
1. **Capture**: Create problem document in `docs/work/problems/`
2. **Validate**: Gather evidence, assess impact, assign severity
3. **Register**: Assign PRB-ID, add to registry index
4. **Prioritize**: Assess against existing problems for resolution priority

### Updating Problem Status
1. **Review**: Assess current status and progress
2. **Update**: Change status with justification
3. **Document**: Record status change rationale
4. **Communicate**: Notify stakeholders of status changes

### Problem Relationships
- **Parent/Child**: Complex problems decomposed into sub-problems
- **Duplicates**: Multiple reports of same problem consolidated
- **Dependencies**: Problems that cannot be resolved until others are addressed
- **Related**: Problems with overlapping causes or solutions

## Quality Assurance

### Problem Statement Quality
- **Clear**: Unambiguous, specific, measurable
- **Complete**: Includes context, impact, evidence
- **Actionable**: Can be resolved within system constraints
- **Testable**: Resolution can be validated

### Evidence Quality
- **Specific**: Concrete examples, metrics, timestamps
- **Reproducible**: Steps to reproduce or detect
- **Quantified**: Impact measurements, frequency data
- **Current**: Evidence from recent time periods

### Resolution Quality
- **Effective**: Problem actually resolved, not just symptoms addressed
- **Complete**: All aspects of problem addressed
- **Sustainable**: Solution prevents problem recurrence
- **Documented**: Resolution process and rationale captured

## Integration Points

### ADR System
- Problems spawn ADRs for significant changes
- ADRs reference problems they resolve
- Problem status tracks ADR progress
- Registry provides ADR context

### Improvement Workflow
- Problems feed into `/learn` → `/evolve` cycle
- Resolution progress tracked in registry
- Lessons learned captured for future problems

### Task System
- Problems can be addressed through regular tasks
- High-severity problems trigger dedicated efforts
- Problem resolution tracked in task outcomes

## Registry Maintenance

### Regular Reviews
- **Monthly**: Review problem status and progress
- **Quarterly**: Assess problem priorities and resource allocation
- **Annually**: Evaluate registry effectiveness and process improvements

### Metrics and Reporting
- **Problem Velocity**: Problems resolved per month
- **Severity Distribution**: Critical/high/medium/low breakdown
- **Resolution Time**: Average time from validation to resolution
- **Backlog Health**: Age and priority distribution

### Process Improvement
- **Retrospectives**: Regular reviews of problem resolution effectiveness
- **Template Updates**: Improve problem capture based on experience
- **Tooling Enhancements**: Better problem tracking and reporting tools

## Historical Problems Archive

### Superseded Problems
- Problems remain in registry for traceability
- Status changed to indicate historical resolution
- Original evidence preserved for context
- Links maintained to resolving ADRs

### Invalid Problems
- Problems determined not to be real issues
- Status changed to `invalid` with explanation
- Retained for future reference (prevent re-litigation)
- Evidence of invalidation documented

## Examples

### Critical Problem Example
```markdown
---
title: "Problem: System crashes on high load"
created_date: 2026-01-15
domain: agentos
Status: resolved
problem_id: PRB-0023
severity: critical
tags: [performance, stability, reliability]
related:
  - docs/explanation/decisions/2026-01-16-load-balancing-architecture.md
---

# Problem: System crashes on high load

## Statement
System becomes unresponsive and crashes when handling 1000+ concurrent requests.

## Context
Production deployment experiences failures during traffic spikes.

## Impact
- Service downtime costing $50K/hour
- Customer trust erosion
- Emergency response burden on team

## Evidence
- 12 crash incidents in Q4 2025
- Crash logs showing memory exhaustion
- Load testing demonstrates failure at 800 concurrent requests

## Detection Signals
- Memory usage > 90%
- Response times > 5 seconds
- Error rate > 1%

## Resolution
Implemented load balancing architecture with auto-scaling.
```

### Medium Problem Example
```markdown
---
title: "Problem: Documentation search is slow"
created_date: 2026-01-10
domain: docs
Status: validated
problem_id: PRB-0045
severity: medium
tags: [usability, performance, search]
---

# Problem: Documentation search is slow

## Statement
Users report documentation search takes 3-5 seconds to return results.

## Context
Internal documentation system with 500+ pages.

## Impact
- Reduced developer productivity
- Users avoid search, leading to outdated information usage
- Support burden on documentation maintainers

## Evidence
- User survey: 78% report slow search as major pain point
- Analytics: Average search time = 4.2 seconds
- Support tickets: 15 mentions of slow search in past month

## Detection Signals
- Search queries taking > 2 seconds
- User complaints about search performance
- Reduced search usage over time
```

## Related
- `docs/reference/agentos/decision-record-format.md` - ADR creation process
- `docs/reference/agentos/traceability.md` - Problem-decision tracking
- `docs/work/problems/index.md` - Registry index
- `docs/explanation/decisions/` - ADRs that resolve problems