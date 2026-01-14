# Design-Decision Templates (Reference)

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Complexity-scaled templates for design-decision checkpoints. Templates are selected by complexity level and must capture selected approach, rationale, and tradeoffs (tabular). Templates integrate with structured exploration phases from `docs/reference/agentos/structured-exploration.md`.

## Template selection
- Level 1: quick fix / simple enhancement
- Level 2: standard feature
- Level 3: complex feature / subsystem
- Level 4: system-level / architecture

## Minimum required fields (all levels)
- Component / decision name
- Options considered (>=2)
- Selected approach
- Rationale (why selected)
- Tradeoffs (tabular: options × criteria)

## Template blocks

**Note**: Templates integrate with structured exploration phases. See `docs/reference/agentos/structured-exploration.md` for phase definitions. Level 1-2: brief exploration (Phases 1-4 recommended, Phase 5 optional). Level 3-4: full exploration (all 5 phases mandatory).

### Level 1 (brief)
```
Decision: [name]

## Phase 1: Component Breakdown (brief)
Requirements/constraints: [key items only]

## Phase 2: Option Exploration (brief)
Options: [2-3 short bullets]

## Phase 3: Trade-off Analysis
Tradeoffs (table): options × 3-4 criteria

## Phase 4: Decision Documentation (brief)
Selected: [1-2 sentences]
Rationale: [1-2 sentences]

## Phase 5: Decision Verification (optional)
[Brief verification if used]
```

### Level 2 (basic)
```
Decision: [name]

## Phase 1: Component Breakdown (brief)
Requirements/constraints: [brief]

## Phase 2: Option Exploration (brief)
Options: [2-3 options, 1-2 sentences each]

## Phase 3: Trade-off Analysis
Tradeoffs (table): options × 4-5 criteria

## Phase 4: Decision Documentation (brief)
Selected + rationale: [2-3 sentences]
Implementation notes: [brief]

## Phase 5: Decision Verification (optional)
[Brief verification if used]
```

### Level 3 (comprehensive)
```
Decision: [name]

## Phase 1: Component Breakdown
Requirements/constraints/integration points: [bullets]
Dependencies: [list]

## Phase 2: Option Exploration
Options: [3-4 options, short description each]

## Phase 3: Trade-off Analysis
Tradeoffs (table): options × criteria (add weights if useful)
Risk assessment: [brief per option]

## Phase 4: Decision Documentation
Selected approach: [paragraph]
Rationale and evidence: [paragraph]
Discarded alternatives: [brief reasons]
Implementation guidance: [key steps/risks]

## Phase 5: Decision Verification (mandatory)
Verification against requirements: [checklist]
Verification against constraints: [checklist]
Verification against integration points: [checklist]
Risk assessment validation: [brief]
```

### Level 4 (enterprise)
```
Decision: [name]

## Phase 1: Component Breakdown
Requirements/constraints/integration points: [bullets]
Dependencies: [comprehensive list]

## Phase 2: Option Exploration
Options: [4+ options, concise descriptions]

## Phase 3: Trade-off Analysis
Tradeoffs (table): options × criteria (weighted)
Risk assessment: [detailed per option]

## Phase 4: Decision Documentation
Selected approach: [short paragraph]
Rationale and evidence: [short paragraph]
Discarded alternatives: [reasons]
Risks/mitigations: [bullets]
Implementation guidance: [bullets]

## Phase 5: Decision Verification (mandatory)
Verification against requirements: [comprehensive checklist]
Verification against constraints: [comprehensive checklist]
Verification against integration points: [comprehensive checklist]
Risk assessment validation: [detailed]
```

## Tradeoff table standard

### Format requirements

**Markdown table syntax**:
- Use standard markdown table format with pipes (`|`)
- Include header row with column names
- Include separator row with `---` or `:---:` for alignment
- Left-align text columns (default)
- Center-align numeric columns if using weights (optional)

**Table structure**:
- First column: Option name/identifier
- Subsequent columns: Criteria (one per column)
- One row per option explored
- Optional summary row at end (not required)

**Example structure**:
```markdown
| Option | Criterion1 | Criterion2 | Criterion3 |
|--------|------------|------------|------------|
| Option A | Value1 | Value2 | Value3 |
| Option B | Value1 | Value2 | Value3 |
```

### Column structure

**Minimum columns**: Option + 3 criteria (Level 1-2)
**Maximum columns**: Option + 6 criteria (Level 3-4)
**Option column**: First column, contains option identifier (e.g., "Option A: Direct library" or "A: Direct library")
**Criteria columns**: One column per decision criterion

**Column naming**:
- Option column: "Option" or "Approach"
- Criteria columns: Use specific, measurable criteria names
- Avoid generic names like "Pros" or "Cons" (use specific criteria instead)

### Row structure

**Option rows**: One row per option explored
- Minimum: 2 options (all levels)
- Maximum: 4+ options (Level 3-4)
- Each row represents one design option

**Optional summary row**: May include summary/comparison row at end (not required)
- Use sparingly, only if adds clarity
- Mark clearly as summary (e.g., "Summary" or "Comparison")

### Text guidelines

**Terseness**:
- Keep cell text brief (1-3 words or short phrases)
- Use abbreviations when clear (e.g., "High", "Med", "Low" instead of "High performance", "Medium performance", "Low performance")
- Avoid full sentences in cells
- Use consistent terminology across table

**Clarity**:
- Use consistent rating scales (e.g., High/Medium/Low, Good/Fair/Poor)
- Define scales if not obvious (e.g., "High = <10ms, Medium = 10-50ms, Low = >50ms")
- Use symbols sparingly (e.g., ✅/❌ only if adds clarity)

**Examples of good cell text**:
- "High", "Medium", "Low"
- "Fast", "Moderate", "Slow"
- "Low risk", "Medium risk", "High risk"
- "2 days", "1 week", "2 weeks"

**Examples of poor cell text**:
- "This option provides high performance but requires significant development time" (too verbose)
- "Good" (unclear what it means)
- "Option A is better" (comparative, not descriptive)

### Weight usage

**When to use weights**:
- Level 3-4 tasks only (optional for Level 1-2)
- When criteria have different importance
- When quantitative comparison is needed

**How to format weights**:
- Add weight column or include in criteria name (e.g., "Performance (weight: 0.3)")
- Use numeric weights (0.0-1.0) or percentages (0-100%)
- Show weighted scores if calculating (optional)
- Keep weight format consistent across table

**Example with weights**:
```markdown
| Option | Performance (0.4) | Maintainability (0.3) | Risk (0.3) | Weighted Score |
|--------|------------------|---------------------|------------|----------------|
| Option A | High (4) | Medium (3) | Low (2) | 3.3 |
| Option B | Medium (3) | High (4) | Medium (3) | 3.3 |
```

**Note**: Weights are optional; use only if they add clarity. Simple High/Medium/Low ratings are often sufficient.

### Examples by complexity level

**Level 1 (brief)**:
```markdown
| Option | Speed | Complexity | Risk |
|--------|-------|------------|------|
| A: Direct | Fast | Low | Low |
| B: Wrapper | Moderate | Medium | Low |
```

**Level 2 (basic)**:
```markdown
| Option | Dev Speed | Maintainability | Flexibility | Risk |
|--------|-----------|-----------------|-------------|------|
| A: Direct library | High | Medium | Low | Low |
| B: Custom wrapper | Low | High | High | Medium |
| C: Hybrid | Medium | Medium | Medium | Low |
```

**Level 3 (comprehensive)**:
```markdown
| Option | Performance | Maintainability | Scalability | Complexity | Risk | Cost |
|--------|-------------|-----------------|-------------|------------|------|------|
| A: Redis KV | Medium | High | Medium | Low | Low | Low |
| B: Redis Hash | High | Medium | High | Medium | Low | Low |
| C: Hybrid Cache | High | Medium | High | High | Medium | Medium |
```

**Level 4 (enterprise with weights)**:
```markdown
| Option | Performance (0.3) | Maintainability (0.2) | Scalability (0.3) | Risk (0.2) | Weighted |
|--------|------------------|----------------------|-------------------|------------|----------|
| A: Microservices | High (4) | Medium (3) | High (4) | Medium (3) | 3.5 |
| B: Monolith | Medium (3) | High (4) | Low (2) | Low (2) | 2.7 |
| C: Modular Monolith | Medium (3) | High (4) | Medium (3) | Low (2) | 2.9 |
```

## Usage
- Choose template level by task complexity.
- Use structured exploration phases (see `docs/reference/agentos/structured-exploration.md`).
- Level 1-2: Brief exploration (Phases 1-4 recommended, Phase 5 optional).
- Level 3-4: Full exploration (all 5 phases mandatory).
- Keep entries concise; no narrative prose beyond the template blocks.
- When an ADR is required, pull from the completed template.
