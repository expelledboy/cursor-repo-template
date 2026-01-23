---
status: stable
purpose: Onboard users into the documentation system.
governed_by:
  docs/domains/docs.md: Docs domain governance
  docs/reference/docs/system-governance.md: System governance
---

# Getting Started

## Purpose
Learn how to add a domain and keep docs aligned to precedence rules.

## Step 1: Create a Domain Node
Create `docs/domains/{domain}.md` using the lean template.

## Step 2: Create Canonicals
Create `reference`, `how-to`, and `explanation` docs for the domain.

## Step 3: Link Frontmatter
Add `governs` and `governed_by` links so precedence is explicit.

## Step 4: Verify
Run: `just docs-index`

## Next Steps
Add rules in `.cursor/rules/` for domain routing.
