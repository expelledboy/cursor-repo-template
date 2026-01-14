# Cursor IDE Integration

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Explain how to run commands under direnv inside Cursor.

## Problem

Cursor's integrated terminal does NOT automatically load direnv environments, even when the hook is configured in your shell config. This is a known limitation.

## Solution: Use `direnv exec .`

Always prefix commands in Cursor's terminal with `direnv exec .`:

```bash
# Instead of:
npm install
just test

# Use:
direnv exec . npm install
direnv exec . just test
```

## Why This Works

`direnv exec .` explicitly loads the direnv environment (including the Nix flake) before running the command, bypassing Cursor's terminal limitations.

## Verification

```bash
# In Cursor's terminal:
direnv exec . which node    # Should show nix store path
direnv exec . which just    # Should show nix store path
direnv exec . just --list   # Should list your just commands
```

## Alternative: Manual Activation

If you prefer, you can manually activate direnv in each Cursor terminal session:

```bash
eval "$(direnv hook zsh)"
direnv allow
cd .  # Trigger direnv to load
```

This needs to be done for each new terminal session.

## Regular Terminal Shells

Regular terminal shells (outside Cursor) work fine with direnv auto-loading. The issue is specific to Cursor's integrated terminal.

## Related docs
- Setup: `docs/how-to/dev/setup.md`
- Tool stack reference: `docs/reference/dev/tool-stack.md`
