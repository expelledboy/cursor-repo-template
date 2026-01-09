# just — Justfile Authoring Reference

`just` is a command runner: you write "recipes" in a `justfile` and run them with `just <recipe> [args…]`.
It is not a build system (all recipes behave like `.PHONY` in make).

This document is optimized for quickly and safely editing a `justfile`, while still indexing all major features.

---

## Quick start (minimum)

Create `justfile` at project root:

```just
default:
  @just --list

build:
  echo Building…

test: build
  echo Testing…
```

Run:

* `just` → runs the `[default]` recipe, or the first recipe if none is marked default
* `just --list` / `just --summary` → discover recipes
* `just --show <recipe>` → view a recipe
* `just --evaluate <expr-or-var>` → evaluate variables/expressions
* `just var=val` → override variable `var` with `val` (e.g. `just target=prod build`)

---

## Example A — A realistic, feature-dense justfile

```just
# Settings
set dotenv-load
set shell := ["bash", "-ceu"]          # strict-ish execution for linewise recipes
set working-directory := "."           # optional, explicit
# set quiet                            # uncomment to make all recipes quiet

# Variables / expressions
project := env("PROJECT", "myapp")
bin     := "target" / "release" / project
stamp   := datetime_utc("%Y%m%dT%H%M%SZ")

# Grouping + docs
[group("dev")]
[doc("Build release binary")]
build:
  cargo build --release

[group("dev")]
[doc("Run unit tests (optionally filtered)")]
test filter="":
  cargo test {{ if filter == "" { "" } else { f'-- {filter}' } }}

[group("ops")]
[confirm("Deploy to production?")]
deploy host user="deploy":
  rsync -av "{{bin}}" "{{user}}@{{host}}:/srv/{{project}}/"
  ssh "{{user}}@{{host}}" "systemctl restart {{project}}"

# Variadic args and forwarding wrapper
[group("tools")]
[no-exit-message]
git *args:
  @git {{args}}

# Script recipe (single process; good for multi-line constructs)
[script("bash")]
[group("tools")]
fmt:
  set -euo pipefail
  cargo fmt
  cargo clippy --all-targets -- -D warnings
```

Key ideas shown:

* dependencies (`test: build`)
* parameters with defaults (`filter=""`)
* expressions in `{{ … }}` substitutions
* quoting to avoid argument splitting (e.g. rsync/ssh arguments)
* variadic parameters (`*args`)
* `[confirm]`, `[group]`, `[doc]`
* `[script]` to get a single interpreter process for multi-line logic

---

## Mental model and core semantics

### Recipes

Syntax:

```just
name: dep1 dep2
  command
  command
```

* Indented lines are recipe body lines.
* Recipes stop on first failing line unless prefixed with `-` (ignore error).
* Lines starting with `@` are not echoed before execution.

### Default recipe

* `just` with no args runs the recipe with `[default]`, else the first recipe.

### Invoking multiple recipes

* `just a b c` runs them in that order (but dependencies run first).
* Use `--one` to forbid multiple recipe invocations.

### Dependencies

* Prior dependencies: `a: b c` run before `a`.
* Subsequent dependencies: `a: b && c d` run immediately after `a` completes.
* Within one `just` invocation, a recipe runs at most once *per unique argument list*.

### Working directory

* Default: recipes run in the directory containing the active `justfile`.
* `[no-cd]` runs in the directory where `just` was invoked.
* `set working-directory := "path"` overrides for all recipes.
* `[working-directory: "path"]` overrides per recipe.

---

## Parameters and argument passing

### Positional parameters (default)

```just
build target:
  echo "Building {{target}}"
```

Invoke: `just build mydir`

### Defaults

```just
test suite="all":
  cargo test --tests {{suite}}
```

### Variadic

* `+FILES` = one or more args
* `*FILES` = zero or more args
  They expand to a single space-separated string.

### Passing args to dependency

```just
default: (build "main")
build target:
  echo {{target}}
```

### Avoiding argument splitting (critical)

Substitution removes the caller’s quotes, so this is wrong:

```just
touchfile name:
  touch {{name}}         # name="a b" becomes 2 args
```

Fixes:

1. Quote the interpolation:

```just
touchfile name:
  touch '{{name}}'
```

2. Use positional arguments (global `set positional-arguments` or `[positional-arguments]`)
   and quote `"$@"` / `"$1"` in your shell.

3. Export parameters (`set export` or `$name` or `export param`) and reference `"$name"`.

### Parameter validation and options/flags

Use `[arg]` to:

* require regex pattern matches (`pattern="\d+"`)
* turn parameters into `--long` or `-s` options
* make flags that take no value (fixed `value="true"`)
* add help text (`help="Description"`)

Also: `just --usage <recipe>` prints a recipe’s usage.

---

## Variables, substitutions, expressions

### Assignments

```just
x := "hello"
y := x + " world"
p := "a" / "b"              # joins with slash
export Z := "exported"      # exported as env var
```

### Substitutions

In recipe bodies use `{{ expr }}`:

```just
say:
  echo {{x}}
```

Escape literal `{{` as `{{{{` (or other escaping approaches).

### Strings

* single `'...'`, double `"..."`, triple quoted indented `'''...'''` / `"""..."""`
* double strings support escapes; single strings do not
* `x'...'` = compile-time shell-expanded string (`~`, `$VAR`, `${VAR:-DEFAULT}`)
* `f'...'` = format string with `{{ expr }}` interpolations

### Backticks and `shell()`

* ``x := `command` `` captures stdout of a command (using configured shell).
* `shell(cmd, args...)` runs a shell snippet with positional args and captures stdout.

Backticks are a convenience; `shell()` is more general (variables as commands, args, etc.).

### Conditionals and regex

```just
arch := if os_family() == "windows" { "win" } else { "unix" }
ok   := if "hello" =~ "hel+o" { "true" } else { "false" }
# Unstable logical operators: &&, ||
val  := env("FOO", "") || "default"
```

### Built-in functions (index)

System: `arch()`, `os()`, `os_family()`, `num_cpus()`

Env: `env(key)`, `env(key, default)`

Executables: `require(name)`, `which(name)` (may be unstable)

Invocation/paths:
`invocation_directory()`, `invocation_directory_native()`,
`justfile()`, `justfile_directory()`,
`source_file()`, `source_directory()`,
`just_executable()`, `just_pid()`

Strings:
`append()`, `prepend()`, `encode_uri_component()`, `quote()`,
`replace()`, `replace_regex()`, `trim*()`, `capitalize()`, `snakecase()`, etc.

Paths:
Fallible: `absolute_path()`, `canonicalize()`, `extension()`, `file_name()`,
`file_stem()`, `parent_directory()`, `without_extension()`
Infallible: `clean()`, `join()`

Filesystem: `path_exists()`, `read()`

Control: `error(message)`

Hashes/UUID: `sha256()`, `sha256_file()`, `blake3()`, `blake3_file()`, `uuid()`

Random: `choose(n, alphabet)`

Datetime: `datetime(fmt)`, `datetime_utc(fmt)`

Semver: `semver_matches(version, requirement)`

Style: `style(name)`; constants like `BOLD`, `RED`, etc. exist

User dirs: `home_directory()`, `config_directory()`, `data_directory()`, etc.
(all `*_directory()` may be abbreviated to `*_dir()`)

### Constants (index)

`HEX`, `HEXLOWER`, `HEXUPPER`, `PATH_SEP`, `PATH_VAR_SEP`,
and terminal escape constants: `CLEAR`, `NORMAL`, `BOLD`, `ITALIC`, colors, etc.

---

## Execution modes: linewise vs shebang vs script

### Linewise recipes (default)

* Each recipe line runs in a new shell instance.
  Implications:
* shell variables don’t persist across lines
* `cd` doesn’t persist across lines

Workarounds:

* combine commands on one line: `cd dir && cmd`
* use `[script]` or shebang recipe for multi-line constructs / shared state

### Shebang recipes

If the first line of a recipe body starts with `#!`, `just` writes the body to a temp file and executes it.
Useful to run Python/Node/Ruby/etc recipes.

Notes:

* Shebang behavior differs across OSs; Windows does not natively support shebangs.
* Temp files may fail on `noexec` filesystems.

### Script recipes

`[script(COMMAND)]` runs the recipe body as a temp file passed to `COMMAND`.
An empty `[script]` uses `set script-interpreter := [...]` (default `sh -eu`).

Temp directory selection can be controlled via `--tempdir` / `JUST_TEMPDIR`, or settings.

---

## Organization: aliases, privacy, docs, groups

### Aliases

```just
alias b := build
```

### Private recipes / aliases

* Names starting with `_` are hidden from `--list` and `--summary`
* Or use `[private]`

### Doc comments

* `# comment` immediately preceding recipe appears in `just --list`
* Or use `[doc("…")]` / `[doc]` to suppress

### Groups

Use `[group("name")]` on recipes or modules; `just --groups` lists groups.

---

## Imports and modules

### Imports

`import "path/to/file.just"` includes another file into the current module scope.

* paths are relative to the importing file (or absolute); `~/` expands to home
* `import?` makes it optional
* duplicates can be allowed with `set allow-duplicate-recipes` / `set allow-duplicate-variables`

### Modules

`mod foo` loads a separate module file (searched via `foo.just`, `foo/mod.just`, `foo/justfile`, `foo/.justfile`)
Invoke module recipes via:

* `just foo bar`
* `just foo::bar`

Modules have their own settings and namespace isolation.
`mod?` makes a module optional.

---

## Settings (index)

Each setting may appear at most once per module unless duplicates are allowed.

Booleans can be set as `set name` (same as `set name := true`).

Common settings:

* `shell := ["cmd", "args…"]` (linewise recipes + backticks)
* `windows-shell := [...]` (overrides shell on Windows)
* `script-interpreter := [...]` (for empty `[script]`)
* `working-directory := "path"`
* `quiet` (disable echoing)
* `export` (export all just vars to environment)
* dotenv: `dotenv-load`, `dotenv-filename`, `dotenv-path`, `dotenv-required`, `dotenv-override`
* `positional-arguments`
* `ignore-comments`
* `fallback`
* `tempdir`
* `unstable` (enable unstable features)

Duplicates:

* `allow-duplicate-recipes`
* `allow-duplicate-variables`

---

## Attributes (index)

Recipe:

* `[default]`, `[doc(...)]`, `[group(...)]`, `[private]`
* `[no-cd]`, `[working-directory("...")]`
* `[confirm]` / `[confirm("prompt")]`, `--yes` bypasses confirmations
* `[no-quiet]`, `[no-exit-message]`
* `[positional-arguments]`
* `[parallel]` (dependencies in parallel)
* `[script]` / `[script("cmd")]`, `[extension(".ext")]`
* platform gating: `[unix]`, `[linux]`, `[macos]`, `[windows]`, `[openbsd]`
* `[metadata("...")]`
* `[arg(key, value...)]` for params:
    * `help="Help text"`
    * `long="long-flag"`, `short="s"`
    * `pattern="regex"`
    * `value="fixed-val"` (flag takes no value)

Aliases: `[private]`

Modules: `[group(...)]`, `[doc(...)]`

---

## CLI discovery and debugging (index)

Core:

* `just` / `just <recipe> [args…]`
* `just --list` / `--summary` (and `--unsorted`)
* `just --show <recipe>`
* `just --evaluate <expr-or-var>`
* `just --usage <recipe>`
* `just --dump` (`--dump-format json` exists)
* `just --choose` (uses chooser like `fzf`, configurable)
* `just --completions <shell>`
* `just --man`, `just --changelog`

Formatting:

* `just --fmt --unstable` (and `--check`)

Execution modifiers:

* `--shell` / `--shell-arg`
* `--working-directory`
* `--timestamp` (`--timestamp-format ...`)
* `--tempdir` / `JUST_TEMPDIR`
* `--unstable` / `JUST_UNSTABLE`
* `--set <variable> <value>` (override variable)

Other:

* `just --global-justfile` / `-g` uses well-known paths under home/config.

---

## Platform notes (Windows in particular)

* Default shell is `sh` even on Windows, unless you set `windows-shell`.
* Many path-returning functions use `\` on Windows; quote them unless using PowerShell/cmd.
* `invocation_directory()` may convert to Unix-style using `cygpath`; use `invocation_directory_native()` for raw Windows path.
* Shebang recipes behave differently on Windows; `[script]` is often the simplest cross-platform approach.

---

## Less common but supported features (index)

* Invoking other-directory justfiles via `just subdir/recipe` or `just subdir/`
* Fallback searching parent justfiles with `set fallback`
* Loading `.env` as environment vars (not just vars)
* Re-run on changes: use `watchexec just <recipe>`
* Parallel deps: `[parallel]`; parallel lines via GNU `parallel` shebang
* Signal handling: fatal signals, `SIGINFO` on BSD/macOS
* “Just scripts”: executable justfile with `#!/usr/bin/env just --justfile`
* Remote includes pattern: `import?` plus recipe that fetches file
* Node `package.json`-like PATH behavior via exporting `PATH`
