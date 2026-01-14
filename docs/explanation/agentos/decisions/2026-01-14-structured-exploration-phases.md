# Decision: Structured Exploration Phases for Design-Decision Checkpoints

**Status**: Accepted
**Date**: 2026-01-14
**Scope**: agentos
**Problem IDs**: PRB-0005
**Ratified**: 2026-01-14
**Supersedes**: (none)

## Context

Design-decision checkpoints currently require documenting options, tradeoffs, selected approach, and rationale, but lack a systematic exploration methodology. This can lead to premature decisions, incomplete rationale preservation, and missed alternatives. The Creative Phase Methodology (inspired by Claude's "Think" tool) provides a structured 5-phase exploration process that enhances rationale preservation while maintaining AgentOS's explicit declaration and traceability principles.

Research analysis in `docs/work/agentos/improvement/2026-01-15-batch-4-creative-phase-methodology.md` demonstrates that structured exploration phases:
- Prevent premature implementation decisions
- Improve decision quality through systematic exploration
- Enhance rationale preservation (core AgentOS goal PRB-0005)
- Integrate seamlessly with existing progressive documentation templates (Batch 2) and complexity-based workflow variations (Batch 3)

## Decision

Implement 5-phase structured exploration methodology for design-decision checkpoints:

1. **Component Breakdown**: Understand component/decision in context (requirements, constraints, integration points, dependencies)
2. **Option Exploration**: Systematically explore 2-4 viable alternatives with brief descriptions
3. **Trade-off Analysis**: Tabular comparison of options against criteria (aligns with existing template requirement)
4. **Decision Documentation**: Document selected approach, rationale, discarded alternatives, implementation guidance (aligns with existing template requirement)
5. **Decision Verification**: Validate decision against requirements, constraints, integration points (separate from task verification gates)

**Complexity-based rigor:**
- **Level 1-2**: Optional structured exploration (if design decision exists, use brief exploration; Phases 1-4 recommended, Phase 5 optional)
- **Level 3-4**: Mandatory structured exploration (all 5 phases required when material design decision exists; if no material decision, document rationale for skipping)

Structured exploration phases enhance existing design-decision checkpoints without replacing them. Phases integrate with existing progressive documentation templates and maintain compatibility with complexity-based workflow variations.

## Alternatives

1. **Keep unstructured checkpoints** (rejected): Less rationale preservation, higher risk of premature decisions, incomplete exploration of alternatives
2. **Mandatory for all levels** (rejected): Too much overhead for simple decisions (Level 1-2), violates complexity-based efficiency principle
3. **Separate methodology outside checkpoints** (rejected): Breaks integration with existing templates, creates fragmentation, reduces traceability

## Consequences

**Positive:**
- Enhances rationale preservation (core AgentOS goal PRB-0005)
- Improves decision quality through systematic exploration
- Prevents premature implementation decisions
- Maintains flexibility through complexity-based rigor
- Integrates seamlessly with existing Batch 2 and Batch 3 patterns
- Preserves traceability and explicit declaration principles

**Negative:**
- Adds process overhead (complexity-based, so minimal for Level 1-2)
- Requires validation to ensure phases aren't skipped
- May slow down simple decisions slightly (but Level 1-2: brief exploration mitigates this)
- Requires maintenance of phase definitions and templates

**Neutral:**
- Phase 3 (Trade-off Analysis) and Phase 4 (Decision Documentation) map to existing template requirements, so minimal additional work
- Phase 5 (Decision Verification) is separate from task verification gates, so no conflict

## Why this worked

Structured exploration phases provide systematic methodology while maintaining AgentOS's core principles:
- **Explicit declaration**: Phase outputs are documented and preserved
- **Traceability**: Decision links to all phases, exploration process is auditable
- **Rationale preservation**: Each phase captures different aspects of rationale (context, alternatives, criteria, validation)
- **Complexity-based efficiency**: Optional for simple tasks, mandatory for complex tasks
- **Integration**: Enhances existing templates rather than replacing them

The complexity-based approach (optional L1-2, mandatory L3-4) aligns with the adaptive complexity model (Batch 3) and prevents over-engineering for simple decisions while ensuring thorough exploration for complex ones.

## Artifacts

- `docs/reference/agentos/structured-exploration.md` (new)
- `docs/reference/agentos/behavior-spec.md` (enhanced: Section 11 and design-decision checkpoint section)
- `docs/reference/agentos/design-decision-templates.md` (enhanced: phase integration)
- `docs/how-to/agentos/design-decision-structured-exploration.md` (new)
- `scripts/agentos/validate_design_decisions.py` (enhanced: phase validation)
- `docs/reference/agentos/directive-tiers.md` (enhanced: Tier 4 directives)
- `docs/reference/agentos/traceability.md` (enhanced: ADR entry)
