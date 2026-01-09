# Getting Started with the Documentation System

This guide walks you through setting up and using the Software-Defined Documentation System in your project.

## Step 1: Understand the Structure

The documentation system uses a **Hybrid Diátaxis + Domain** structure:

- **`docs/reference/`** - Stable facts, contracts, configurations (single source of truth)
- **`docs/how-to/`** - Step-by-step procedures, runbooks
- **`docs/explanation/`** - Rationale, architecture, mental models
- **`docs/work/`** - Drafts, research, verification notes (with Status/Date)
- **`docs/archive/`** - Superseded content (with banners)

**Authority order**: reference → how-to → explanation → work → archive

## Step 2: Customize AGENTS.md

Edit `AGENTS.md` to replace any project-specific references. The file should describe:
- Your project's name
- Your project's specific domains (if known)
- Any project-specific verification expectations

## Step 3: Create Your First Domain

When you're ready to document your first project domain:

1. **Create the documentation files**:
   - `docs/reference/your-domain/config.md` (stable facts)
   - `docs/how-to/your-domain/setup.md` (procedures)
   - `docs/explanation/your-domain/architecture.md` (rationale)

2. **Create a Cursor Rule** (`.cursor/rules/20-your-domain.topic.mdc`):
   ```markdown
   ---
   description: your-domain, keywords, that, trigger, this, rule
   ---
   - Load these canonicals: `docs/reference/your-domain/config.md`, `docs/how-to/your-domain/setup.md`, `docs/explanation/your-domain/architecture.md`.
   - Invariants: [list any domain-specific constraints]
   - If changing config/contracts, update the reference doc first.
   ```

3. **Update `docs/index.md`**:
   Add a new section:
   ```markdown
   ## Your Domain
   - **Context Rule:** `.cursor/rules/20-your-domain.topic.mdc`
   - Reference: `docs/reference/your-domain/config.md`
   - How-to: `docs/how-to/your-domain/setup.md`
   - Explanation: `docs/explanation/your-domain/architecture.md`
   ```

## Step 4: Start Documenting

When creating new documentation:

1. **Ask yourself**: "What is the intent?"
   - Fact → `docs/reference/`
   - Procedure → `docs/how-to/`
   - Rationale → `docs/explanation/`
   - Draft/Research → `docs/work/YYYY-MM-DD-slug.md`

2. **Follow naming conventions**:
   - Lowercase kebab-case (e.g., `saml-config.md`, not `SAML_CONFIG.md`)
   - Use real dates in `YYYY-MM-DD` format (no placeholders)

3. **Update `docs/index.md`** when you add canonical docs

4. **Create/update rules** when you add new domains

## Step 5: Maintain the System

The system is "software" and requires maintenance:

- **When you add a domain**: Update both `docs/index.md` and create a corresponding `.cursor/rules/*.mdc`
- **When you refactor docs**: Update the Map (`index.md`) and Router (rules) to point to new locations
- **When you promote work docs**: Move from `docs/work/` to appropriate canonical location, add Superseded banner to work doc

## Common Patterns

### Adding a New Environment Variable

1. Update `docs/reference/config/environment.md` (if it exists) **first**
2. Update `docs/how-to/dev/env-setup.md` with setup instructions
3. Update deployment docs if needed

### Documenting a New Feature

1. Create explanation doc: `docs/explanation/feature/design.md`
2. Create reference doc: `docs/reference/feature/config.md` (if config needed)
3. Create how-to doc: `docs/how-to/feature/usage.md`
4. Update `docs/index.md` and create rule if it's a new domain

### Refactoring Existing Docs

See `docs/how-to/docs/content-aware-restructuring.md` for a systematic approach.

## Verification

To verify the system is working:

1. **Test context routing**: Ask an agent about a topic and verify it loads the correct canonical docs
2. **Test authority order**: Create conflicting info in work/ and reference/ - agent should prefer reference/
3. **Test self-maintenance**: Add a new domain and verify the agent updates both index.md and rules

## Next Steps

- Read `docs/explanation/architecture/doc-system-rationale.md` to understand the "why"
- Read `docs/how-to/docs/content-aware-restructuring.md` if you need to refactor existing docs
- Start documenting your first domain!
