---
governed_by:
  "docs/domains/dev.md": "Dev domain governance"
implemented_by:
  "scripts/setup.py": "Setup automation"
  "justfile": "Task runner config"
---

# Development Tool Stack

## Purpose
Define the stable facts and constraints for the development tool stack.

## Tools (Facts)
- `direnv`: loads environment on directory entry
- `nix flake`: declares dev dependencies and versions
- `just`: task runner for project commands

## Integration Facts
1) `direnv` loads `.envrc` on entry
2) `.envrc` activates `nix flake`
3) `nix` provides tools
4) `just` executes recipes using the active environment

## Environment Precedence
1) Process environment
2) `.env` file
3) Defaults in code or `justfile`

## Constraints
- Cursor terminal does not auto-load `direnv`.
- Use explicit environment loading when needed.
