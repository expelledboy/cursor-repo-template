# Settings
set dotenv-load := true
set export := true
set shell := ["bash", "-cu"]

mod agentos "scripts/agentos"

# Default Recipe
# ==============

[private]
default:
  @just --list --unsorted --list-submodules

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

# Cleanup
# =======

# Remove build artifacts and dependencies
[group('dev')]
[confirm]
clean:
  @echo "Clean build artifacts here"
  # Example: rm -rf dist node_modules, cargo clean, etc.
