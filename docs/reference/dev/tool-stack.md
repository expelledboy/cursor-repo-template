# Development Tool Stack (source of truth)

## Purpose
Reference for the development tool stack: direnv, just, and Nix Flake. How they work together and what each provides.

## Tool Stack

### direnv
**What it does**: Automatically loads/unloads environment variables and development shells when you `cd` into/out of a directory.

**Configuration**: `.envrc` file in project root.

**Key features**:
- Loads `.env` file automatically (if configured)
- Integrates with Nix flakes via `use flake`
- Can run arbitrary shell commands on directory entry

**Common patterns**:
```bash
# Load .env file
dotenv_if_exists .env

# Use Nix flake
use flake . --show-trace
```

### just
**What it does**: Task runner (like `make` but simpler). Provides project-specific commands.

**Configuration**: `justfile` in project root. (See [Justfile Reference](docs/reference/dev/justfile.md))

**Key features**:
- Simple syntax, no tabs required
- Auto-loads `.env` with `set dotenv-load := true`
- Groups commands with `[group('name')]`
- Private recipes with `[private]`

**Common patterns**:
```just
# Load .env automatically
set dotenv-load := true

# Export vars to child processes
set export := true

# Recipe with default
[group('dev')]
run:
  @echo "Running..."
```

### Nix Flake
**What it does**: Provides reproducible development environment with pinned dependencies.

**Configuration**: `flake.nix` in project root.

**Key features**:
- Declares development dependencies (Node.js, Python, tools, etc.)
- Ensures consistent versions across team
- Works with direnv via `use flake`

**Common patterns**:
```nix
devShell = pkgs.mkShell {
  buildInputs = with pkgs; [
    nodejs
    nodejs.pkgs.pnpm
    just
    git
  ];
};
```

## How They Work Together

1. **direnv** reads `.envrc` when you `cd` into the project
2. `.envrc` calls `use flake .` to activate the Nix development shell
3. **Nix Flake** provides the tools (Node.js, just, etc.)
4. **just** provides project commands, inheriting environment from direnv
5. `.env` file (if present) is loaded by both direnv and just

## Environment Variable Precedence

1. Process environment (exported in shell/CI)
2. `.env` file (loaded by direnv and just)
3. Defaults in code/justfile

## Related docs
- Setup: `docs/how-to/dev/setup.md`
- Cursor integration: `docs/how-to/dev/cursor-integration.md`
- Rationale: `docs/explanation/dev/tool-stack-rationale.md`
