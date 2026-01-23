---
governed_by:
  "docs/domains/dev.md": "Dev domain governance"
---

# Tool Stack Rationale

## Purpose
Explain why the dev tool stack was chosen.

## Why This Stack
- Reproducible environments with `nix`
- Automatic activation via `direnv`
- Documented commands via `just`

## Tradeoffs
- `nix` has a learning curve
- Cursor needs explicit `direnv exec`

## Alternatives
- Manual installs and ad hoc scripts
