# Development Tool Stack Rationale

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Explain why the repo uses direnv + Nix Flake + just.

## Why This Stack?

We use **direnv + Nix Flake + just** to create a reproducible, self-documenting development environment.

## Goals

1. **Reproducibility**: Same tools/versions for all developers
2. **Simplicity**: Minimal setup steps
3. **Self-documentation**: Tool versions and commands are in version control
4. **Isolation**: Project dependencies don't pollute system

## How Each Tool Contributes

### Nix Flake: Reproducibility
- **Problem**: "Works on my machine" - different Node.js versions, missing tools
- **Solution**: Declare all dev dependencies in `flake.nix`
- **Result**: Everyone gets the same environment

### direnv: Automation
- **Problem**: Remembering to activate environments, load env vars
- **Solution**: Auto-loads when you `cd` into project
- **Result**: Zero-friction development

### just: Task Documentation
- **Problem**: Complex commands, forgotten workflows, inconsistent scripts
- **Solution**: Project-specific commands in `justfile`
- **Result**: `just --list` shows all available commands

## Trade-offs

### Pros
- ✅ Reproducible environments
- ✅ Version-controlled tooling
- ✅ Self-documenting commands
- ✅ Works across platforms (Linux, macOS)

### Cons
- ❌ Requires Nix (learning curve)
- ❌ Cursor integration needs workaround
- ❌ Initial setup time

## Alternatives Considered

- **Docker Compose**: Heavier, slower, more complex
- **asdf/nvm**: Doesn't handle all tools, requires manual setup
- **Make**: Less readable, tab-sensitive
- **npm scripts**: Language-specific, harder to document

## When to Use This Stack

**Good fit for**:
- Teams needing consistency
- Projects with multiple tools/languages
- Long-lived projects
- Open source projects

**Maybe not for**:
- Quick prototypes
- Single-developer projects
- Teams unfamiliar with Nix

## Related docs
- Tool stack reference: `docs/reference/dev/tool-stack.md`
- Setup guide: `docs/how-to/dev/setup.md`
