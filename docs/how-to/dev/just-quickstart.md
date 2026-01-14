# How to: Create and use a minimal `justfile`

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Provide a minimal, task-oriented `justfile` and usage steps.

This is a **how-to**: it assumes you already know what `just` is and you want a minimal working setup.

If you want the full language/feature reference, see `docs/reference/dev/justfile.md`.

## Goal

Create a tiny `justfile`, then run `just` commands reliably.

## Steps

1. **Create `justfile` at project root**

```just
set shell := ["bash", "-cu"]

target_host := "dev"

[private]
default:
  @just --list

# Build the project
[group('dev')]
build:
  echo "Building…"

# Test the project
[group('dev')]
test: build
  echo "Testing…"

deploy target=target_host: clean build
  echo "Deploying to {{target}}…"

[confirm]
clean:
  echo "Cleaning…"
```

2. **Discover and run recipes**

- `just` → runs the `[default]` recipe, or the first recipe if none is marked default
- `just --list` / `just --summary` → discover recipes
- `just --show <recipe>` → view a recipe
- `just --evaluate <expr-or-var>` → evaluate variables/expressions
- `just var=val` → override variable `var` with `val` (e.g. `just target=prod build`)

## Cursor note (direnv)

If your project uses `direnv`, prefer:

- `direnv exec . just --list`
- `direnv exec . just test`

## Related docs

- Reference: `docs/reference/dev/justfile.md`
- Tool stack: `docs/reference/dev/tool-stack.md`
- Cursor integration: `docs/how-to/dev/cursor-integration.md`
