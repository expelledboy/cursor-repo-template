---
status: stable
purpose: Provide minimal justfile usage steps.
governed_by:
  docs/domains/dev.md: Dev domain governance
implements:
  docs/reference/dev/justfile.md: Justfile spec
---

# `justfile` Quickstart

## Purpose
Create and use a minimal `justfile`.

## Minimal `justfile`
```
set shell := ["bash", "-cu"]

[private]
default:
  @just --list

[group('dev')]
build:
  echo "Building"

[group('dev')]
test: build
  echo "Testing"
```

## Run
- `just`
- `just --list`
- `just build`
