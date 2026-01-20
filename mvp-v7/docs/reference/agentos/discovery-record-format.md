# Discovery Record Format (v7)

Status: Draft
Date: 2026-01-15
Purpose: Capture stable learnings about Cursor feature interplay that constrain v7 schemas and behavior.

## Location and naming
- Location: `docs/explanation/agentos/discoveries/`
- Filename: `YYYY-MM-DD-<slug>.md` (kebab-case)

## ID format
V7-DIS-0001 (zero-padded, monotonic)

## Required fields (lean)
- Status (Draft | Accepted | Superseded)
- Date (YYYY-MM-DD)
- Scope (mvp-v7)
- Cursor features (subset: Rules, Mentions, Commands, Search, Tools/MCP)
- Discovery ID (V7-DIS-*)
- Observation (max 5 bullets)
- Implication (max 5 bullets)
- Artifacts (paths only)

## Template
```markdown
# Discovery: <short title>

Status: Draft
Date: YYYY-MM-DD
Scope: mvp-v7
Cursor features: Rules, Mentions
Discovery ID: V7-DIS-0001
Supersedes: (optional)

## Observation
- …

## Implication
- …

## Artifacts
- <path>
```

