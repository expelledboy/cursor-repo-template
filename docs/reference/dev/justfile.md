---
governed_by:
  "docs/domains/dev.md": "Dev domain governance"
implemented_by:
  "justfile": "Project justfile"
---

# `justfile` Reference

## Purpose
Define the core syntax and behavior of `justfile` used in this repo.

## Core Syntax
Recipe form:

```
name: dep1 dep2
  command
  command
```

## Execution Rules
- Recipes stop on first failure unless a line is prefixed with `-`.
- Lines prefixed with `@` do not echo before running.
- Dependencies run before the recipe.

## Parameters
- Positional parameters: `name target:`
- Defaults: `name target="default"`
- Variadic: `*ARGS` or `+ARGS`

## Substitution
- Use `{{ expr }}` for substitutions.
- Quote substitutions when arguments might contain spaces.

## Constraints
- Use `justfile` as the canonical task runner config.
- Keep recipes grouped and documented.
