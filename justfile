# Settings
set dotenv-load := true
set export := true
set shell := ["bash", "-cu"]

# Default Recipe
# ==============

default:
  @just --list --unsorted

# Project Setup
# =============

# Install project dependencies
[group('dev')]
init:
  @echo "Initialize your project here"
  # Example: pnpm install, npm install, pip install -r requirements.txt, etc.

# Development
# ============

# Start the development server
[group('dev')]
run:
  @echo "Start your development server here"
  # Example: pnpm start, npm run dev, python -m flask run, etc.

# Build & Preview
# ===============

# Build the project for production
[group('build')]
build:
  @echo "Build your project here"
  # Example: pnpm run build, npm run build, cargo build --release, etc.

# Preview the production build locally
[group('build')]
preview: build
  @echo "Preview your build here"
  # Example: pnpm run preview, npm run serve, python -m http.server, etc.

# Code Quality
# ============

# Lint the codebase
[group('quality')]
lint:
  @echo "Run your linter here"
  # Example: pnpm run lint, npm run lint, cargo clippy, etc.

# Format the codebase
[group('quality')]
format:
  @echo "Format your code here"
  # Example: pnpm exec prettier --write ., cargo fmt, etc.

# Type check
[group('quality')]
typecheck:
  @echo "Type check your code here"
  # Example: npx tsc --noEmit, mypy ., cargo check, etc.

# Testing
# =======

# Run tests
[group('test')]
test:
  @echo "Run your tests here"
  # Example: pnpm test, npm test, cargo test, pytest, etc.

# Run tests in watch mode
[group('test')]
test-watch:
  @echo "Run tests in watch mode here"
  # Example: pnpm test:watch, npm test -- --watch, cargo watch -x test, etc.

# Generate test coverage report
[group('test')]
test-coverage:
  @echo "Generate test coverage here"
  # Example: pnpm test:coverage, npm test -- --coverage, cargo tarpaulin, etc.

# Documentation
# =============

# Generate comprehensive documentation index
[group('docs')]
docs-index *ARGS:
  python3 scripts/docs/docs_index.py {{ARGS}}

# Render a deterministic domain index
[group('docs')]
docs-domains:
  python3 scripts/docs/docs_domains.py

# Render a deterministic skills index
[group('docs')]
docs-skills:
  python3 scripts/docs/docs_skills.py

# Validate documentation frontmatter
[group('docs')]
docs-validate:
  python3 scripts/docs/docs_validate.py

agent_runtimes := "cursor codex"

# Link skills directories for agent tooling
[group('docs')]
@link-skills:
  mkdir -p agent/skills
  for runtime in {{agent_runtimes}}; do \
    mkdir -p ".${runtime}"; \
    [ -L ".${runtime}/skills" ] && continue; \
    [ -e ".${runtime}/skills" ] && [ ! -L ".${runtime}/skills" ] && { echo ".${runtime}/skills exists and is not a symlink"; exit 1; }; \
    ln -sfn ../agent/skills ".${runtime}/skills"; \
  done

# Sync skills into .cursor for tools that ignore symlinks
[group('docs')]
sync-skills:
  @mkdir -p agent/skills .cursor/skills
  @rsync -a --delete agent/skills/ .cursor/skills/
  @echo "Synced agent/skills to .cursor/skills"

# Cleanup
# =======

# Remove build artifacts and dependencies
[group('dev')]
[confirm]
clean:
  @echo "Clean build artifacts here"
  # Example: rm -rf dist node_modules, cargo clean, etc.
