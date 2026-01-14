# Development Environment Setup

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Set up direnv, Nix Flake, and just for this repo.

## Prerequisites

- **Nix** with flakes enabled: [Install Nix](https://nixos.org/download.html)
- **direnv**: `nix profile install nixpkgs#direnv` or `brew install direnv`
- **just** (optional if in flake): `nix profile install nixpkgs#just` or `brew install just`

## Initial Setup

### 1. Configure direnv hook

Add to your shell config (`.zshrc`, `.bashrc`, etc.):

```bash
eval "$(direnv hook zsh)"  # or bash, fish, etc.
```

Reload your shell or run `source ~/.zshrc`.

### 2. Allow direnv in project

```bash
cd /path/to/project
direnv allow
```

This reads `.envrc` and activates the Nix flake.

### 3. Create `.env` file (optional)

```bash
cp .env.example .env
# Edit .env with your local values
```

### 4. Verify setup

```bash
# Check direnv is active
direnv status

# Check tools are available
which node  # Should show nix store path
which just  # Should show nix store path

# List available just commands
just --list
```

## Cursor IDE Integration

Cursor's terminal may not auto-load direnv. Use:

```bash
direnv exec . <command>
```

Example:
```bash
direnv exec . just test
direnv exec . npm install
```

See `docs/how-to/dev/cursor-integration.md` for more details.

## Common Tasks

### Add a new dependency to flake.nix

1. Edit `flake.nix`
2. Add package to `buildInputs`:
   ```nix
   buildInputs = with pkgs; [
     # ... existing packages
     your-new-package
   ];
   ```
3. Run `direnv allow` to reload

### Add a new just command

1. Edit `justfile`
2. Add recipe:
   ```just
   [group('dev')]
   your-command:
     @echo "Running your command"
   ```
3. Test: `just your-command`

### Update environment variables

1. Edit `.env` (or export in shell)
2. Restart processes that need the new vars
3. For build-time vars (like `VITE_*`), rebuild may be required

## Troubleshooting

### direnv not loading
- Check hook is in shell config: `grep direnv ~/.zshrc`
- Verify `.envrc` exists and is allowed: `direnv allow`
- Check direnv status: `direnv status`

### Tools not found
- Ensure flake.nix includes the tool in `buildInputs`
- Run `direnv allow` to reload
- Check Nix is working: `nix --version`

### Cursor terminal issues
- Always use `direnv exec . <command>` in Cursor
- See `docs/how-to/dev/cursor-integration.md` for details

## Related docs
- Tool stack reference: `docs/reference/dev/tool-stack.md`
- Cursor integration: `docs/how-to/dev/cursor-integration.md`
- Tool stack rationale: `docs/explanation/dev/tool-stack-rationale.md`
