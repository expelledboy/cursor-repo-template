# Documentation system rationale (why we structured it this way)

Purpose: Capture the "why" behind the Hybrid Diátaxis + Domain structure and Cursor routing, so agents know the intent and avoid blind rule-following.

## Goals
- Minimize context load while keeping sources of truth obvious.
- Separate intent buckets (reference / how-to / explanation / work / archive) to prevent mixing facts with drafts.
- Make Cursor agents reliable via Rules that route to the smallest authoritative set.

## Design choices
- **Four Quadrants (Diátaxis)**: We strictly separate content types to optimize for **Agent Context Window**:
  - **Tutorials** (`docs/tutorials/`): Learning-oriented. **Low signal** for coding tasks. Agents should ignore this when implementing features.
  - **How-to** (`docs/how-to/`): Task-oriented. **High signal** for execution.
  - **Reference** (`docs/reference/`): Information-oriented. **High signal** for constraints/contracts.
  - **Explanation** (`docs/explanation/`): Understanding-oriented. Useful for planning, noise for coding.
- **Hybrid Diátaxis + Domain**: Combine Diátaxis intent buckets (reference = facts, how-to = procedures, explanation = rationale) with domain folders (auth, deployment, testing, ui) so agents can route by both task type and topic, reducing conflict and scope creep.
- **Bidirectional Context Linking**: `docs/index.md` acts as the Map, explicitly listing the `.cursor/rules/*.mdc` (Router) for each domain. This couples content to context, ensuring agents can find the "Brain" (Rule) from the "Topic" (Index).
- **Authority order**: reference → how-to → explanation → tutorials → work → archive; resolves conflicts and keeps work notes non-authoritative.
- **Doc map first**: `docs/index.md` as the llms-txt-style index; agents read it first instead of loading the repo at random.
- **Routing layer**: `.cursor/rules/*.mdc` (flat .mdc for compatibility) enforce minimal context loading and doc update expectations.
- **Work vs. truth**: Drafts/notes live in `docs/work/**` with Status+date; stable facts move to reference/how-to/explanation and obsolete copies get a Superseded banner in archive.
- **Naming discipline**: Lowercase kebab-case; real dates (`YYYY-MM-DD`) in filenames/headers when dated docs are required.

## Anti-patterns this avoids
- Loading unrelated or outdated docs (Rules + doc map).
- Treating work notes as facts (authority order + work/ archive separation).
- Divergent instructions (single canonical references; supersede duplicates).
- Overloading agents with monolith docs (small, intent-specific canonicals).

## When to update this rationale
Update here if we change the doc structure, routing mechanism, or authority model (e.g., different rule format, new domain buckets, new authority order). Link the change in `docs/index.md` and adjust rules if needed.

## External evidence & compatibility notes (summary)
- **Cursor Rules** are the reliable context router; `.cursor/rules/*.mdc` (flat) work across Cursor versions where RULE.md folders may be ignored.
- **MCP config**: If project `.cursor/mcp.json` is not picked up, place the same config in `~/.cursor/mcp.json`; MCP is for external/volatile knowledge, not repo truths.
- **Skills**: YAML-frontmatter "skills" follow the progressive disclosure pattern; useful but optional—Rules remain primary.
- **Doc map (llms-txt-style)**: `docs/index.md` is the first-load, lightweight index; agents read it before loading other files instead of scanning the repo.
- **Hybrid Diátaxis + Domain**: Intent buckets + domain grouping align with human navigation and agent retrieval, reducing conflicts.

## Cursor behavior profile (meta-awareness)
- **Context loading**: With Rules present, Cursor loads minimal matching chunks; without Rules, it can over-pull. Always start from `docs/index.md` to avoid repo-wide scans.
- **Rule matching**: Flat `.mdc` files are applied; RULE.md folders can be ignored in some builds. Matches combine `alwaysApply`, `globs`, and `description`—scope globs/descriptions narrowly.
- **System Maintenance**: The documentation system is software.
  - If you add a **Domain** to `docs/index.md`, you must create/update a corresponding **Rule** in `.cursor/rules/`.
  - If you refactor docs, ensure the **Map** (`index.md`) and **Router** (`rules`) point to the new locations.
- **MCP**: Project `.cursor/mcp.json` may be skipped; global `~/.cursor/mcp.json` is a reliable fallback. Use MCP only for external/volatile info, not repo truths.
- **Skills**: Progressive disclosure (metadata first); optional. Rules stay primary for routing.
- **Agent loop**: read map → load minimal relevant docs → implement → verify → update reference first → **update rules/index if domain changes**.
