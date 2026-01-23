---
status: stable
purpose: Provide steps to set up the dev environment.
governed_by:
  docs/domains/dev.md: Dev domain governance
implements:
  docs/reference/dev/tool-stack.md: Tool stack facts
---

# Development Environment Setup

## Purpose
Set up the dev environment to match the tool stack facts.

## Steps
1) Install `nix` with flakes enabled.
2) Install `direnv`.
3) Install `just`.
4) Add the `direnv` hook to your shell config.
5) Enter the repo and run:
   - `direnv allow`
6) Verify tools:
   - `which nix`
   - `which direnv`
   - `which just`

## Cursor Integration
Cursor terminal does not auto-load `direnv`. Use:

```
direnv exec . just --list
```

## Troubleshooting
- If tools are missing, re-run `direnv allow`.
- If env vars are not applied, check `.envrc` and shell hook.
