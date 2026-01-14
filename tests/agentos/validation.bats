#!/usr/bin/env bats
# @directive docs/reference/agentos/validation-scripts.md

setup() {
  repo_root="$(cd "${BATS_TEST_DIRNAME}/../.." && pwd)"
  temp_dir="$(mktemp -d)"
}

teardown() {
  rm -rf "${temp_dir}"
}

@test "validate_registry passes minimal scope" {
  mkdir -p "${temp_dir}/scripts/agentos"
  mkdir -p "${temp_dir}/tests/agentos"
  mkdir -p "${temp_dir}/docs/reference/agentos"
  cp "${repo_root}/scripts/agentos/validate_registry.py" "${temp_dir}/scripts/agentos/"
  cp "${repo_root}/scripts/agentos/validate_routing.py" "${temp_dir}/scripts/agentos/"
  cp "${repo_root}/tests/agentos/validation.bats" "${temp_dir}/tests/agentos/"
  impl="@implementation"
  cat > "${temp_dir}/docs/reference/agentos/validation-scripts.md" <<DOC
# Validation Scripts (Reference)

${impl} scripts/agentos/validate_registry.py
${impl} scripts/agentos/validate_routing.py
DOC
  cat > "${temp_dir}/AGENTS.md" <<'AGENTS'
# Agent Guide

## Registry Scope
- `scripts/agentos/**`
- `docs/reference/agentos/validation-scripts.md`
AGENTS

  run bash -c "cd \"${temp_dir}\" && python3 scripts/agentos/validate_registry.py"
  [ "$status" -eq 0 ]
  [[ "$output" == *"Registry validation passed"* ]]
}

@test "validate_registry fails on missing annotation" {
  mkdir -p "${temp_dir}/scripts/agentos"
  cat > "${temp_dir}/scripts/agentos/nope.sh" <<'SCRIPT'
#!/bin/sh
exit 0
SCRIPT
  cat > "${temp_dir}/AGENTS.md" <<'AGENTS'
# Agent Guide

## Registry Scope
- `scripts/agentos/**`
AGENTS

  run bash -c "cd \"${temp_dir}\" && python3 \"${repo_root}/scripts/agentos/validate_registry.py\""
  [ "$status" -ne 0 ]
  [[ "$output" == *"Files missing registry annotations"* ]]
}

@test "validate_routing passes minimal config" {
  mkdir -p "${temp_dir}/.cursor/rules"
  mkdir -p "${temp_dir}/docs/reference/agentos"
  cat > "${temp_dir}/.cursor/rules/20-test.mdc" <<'RULE'
---
description: test
---
- Load docs/reference/agentos/behavior-spec.md
RULE
  cat > "${temp_dir}/docs/reference/agentos/behavior-spec.md" <<'DOC'
# Behavior Spec
DOC
  cat > "${temp_dir}/docs/index.md" <<'INDEX'
# Documentation Map

## Test
- **Context Rule:** `.cursor/rules/20-test.mdc`
INDEX

  run bash -c "cd \"${temp_dir}\" && python3 \"${repo_root}/scripts/agentos/validate_routing.py\""
  [ "$status" -eq 0 ]
  [[ "$output" == *"Routing validation passed"* ]]
}

@test "validate_routing fails when doc ref missing" {
  mkdir -p "${temp_dir}/.cursor/rules"
  mkdir -p "${temp_dir}/docs"
  cat > "${temp_dir}/.cursor/rules/20-test.mdc" <<'RULE'
---
description: test
---
- Load docs/reference/agentos/missing.md
RULE
  cat > "${temp_dir}/docs/index.md" <<'INDEX'
# Documentation Map

## Test
- **Context Rule:** `.cursor/rules/20-test.mdc`
INDEX

  run bash -c "cd \"${temp_dir}\" && python3 \"${repo_root}/scripts/agentos/validate_routing.py\""
  [ "$status" -ne 0 ]
  [[ "$output" == *"Rule doc references missing"* ]]
}

@test "validate_core_list_sync passes minimal config" {
  mkdir -p "${temp_dir}/scripts/agentos"
  mkdir -p "${temp_dir}/docs/reference/agentos"
  mkdir -p "${temp_dir}/.cursor/rules"
  cp "${repo_root}/scripts/agentos/validate_core_list_sync.py" "${temp_dir}/scripts/agentos/"
  cp "${repo_root}/scripts/agentos/validation_utils.py" "${temp_dir}/scripts/agentos/"
  cat > "${temp_dir}/docs/reference/agentos/components.md" <<'DOC'
# AgentOS Components Inventory

## 1. Core contracts
- `docs/reference/agentos/behavior-spec.md`
DOC
  cat > "${temp_dir}/docs/index.md" <<'INDEX'
# Documentation Map

## AgentOS Framework
- Reference: `docs/reference/agentos/behavior-spec.md`
INDEX
  cat > "${temp_dir}/.cursor/rules/20-agentos.topic.mdc" <<'RULE'
---
description: agentos
---
- Load the AgentOS core docs (authoritative list in `docs/reference/agentos/components.md`):
  - `docs/reference/agentos/behavior-spec.md`
RULE
  cat > "${temp_dir}/docs/reference/agentos/behavior-spec.md" <<'DOC'
# Behavior Spec
DOC

  run bash -c "cd \"${temp_dir}\" && python3 scripts/agentos/validate_core_list_sync.py"
  [ "$status" -eq 0 ]
  [[ "$output" == *"Core list sync passed"* ]]
}

@test "validate_traceability passes minimal config" {
  mkdir -p "${temp_dir}/scripts/agentos"
  mkdir -p "${temp_dir}/docs/reference/agentos"
  mkdir -p "${temp_dir}/docs/explanation/agentos/decisions"
  cp "${repo_root}/scripts/agentos/validate_traceability.py" "${temp_dir}/scripts/agentos/"
  cp "${repo_root}/scripts/agentos/validation_utils.py" "${temp_dir}/scripts/agentos/"
  cat > "${temp_dir}/docs/reference/agentos/problem-registry.md" <<'DOC'
# AgentOS Problem Registry

## 6. Registry
| ID | Title | Status | Scope | Statement | Evidence | Impact | Detection signals |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRB-0001 | Test | Validated | system | Statement | Evidence | Impact | Signals |
DOC
  cat > "${temp_dir}/docs/reference/agentos/traceability.md" <<'DOC'
# AgentOS Traceability Map

| Problem ID | Decision Record | Artifacts |
| --- | --- | --- |
| PRB-0001 | `docs/explanation/agentos/decisions/2026-01-14-test.md` | `docs/reference/agentos/behavior-spec.md` |
DOC
  cat > "${temp_dir}/docs/explanation/agentos/decisions/2026-01-14-test.md" <<'DOC'
# Decision: Test
DOC
  cat > "${temp_dir}/docs/reference/agentos/behavior-spec.md" <<'DOC'
# Behavior Spec
DOC

  run bash -c "cd \"${temp_dir}\" && python3 scripts/agentos/validate_traceability.py"
  [ "$status" -eq 0 ]
  [[ "$output" == *"Traceability validation passed"* ]]
}

@test "validate_adr_format passes minimal config" {
  mkdir -p "${temp_dir}/scripts/agentos"
  mkdir -p "${temp_dir}/docs/explanation/agentos/decisions"
  cp "${repo_root}/scripts/agentos/validate_adr_format.py" "${temp_dir}/scripts/agentos/"
  cp "${repo_root}/scripts/agentos/validation_utils.py" "${temp_dir}/scripts/agentos/"
  cat > "${temp_dir}/docs/explanation/agentos/decisions/2026-01-14-test-adr.md" <<'DOC'
# Decision: Test ADR

**Status**: Accepted
**Date**: 2026-01-14
**Scope**: agentos
**Problem IDs**: PRB-0001

## Context
Context here.

## Decision
Decision here.

## Alternatives
Alternatives here.

## Consequences
Consequences here.

## Why this worked
Why it worked.

## Artifacts
- docs/reference/agentos/behavior-spec.md
DOC

  run bash -c "cd \"${temp_dir}\" && python3 scripts/agentos/validate_adr_format.py"
  [ "$status" -eq 0 ]
  [[ "$output" == *"ADR format validation passed"* ]]
}

@test "validate_improvement_notes passes minimal config" {
  mkdir -p "${temp_dir}/scripts/agentos"
  mkdir -p "${temp_dir}/docs/work/agentos/improvement"
  cp "${repo_root}/scripts/agentos/validate_improvement_notes.py" "${temp_dir}/scripts/agentos/"
  cp "${repo_root}/scripts/agentos/validation_utils.py" "${temp_dir}/scripts/agentos/"
  cat > "${temp_dir}/docs/work/agentos/improvement/2026-01-14-test.md" <<'DOC'
# Improvement: Test

**Status**: Draft
**Date**: 2026-01-14
**Event**: micro-aar
**Task**: test
**Evidence**: log
**Affected artifacts**: docs/reference/agentos/behavior-spec.md
DOC

  run bash -c "cd \"${temp_dir}\" && python3 scripts/agentos/validate_improvement_notes.py"
  [ "$status" -eq 0 ]
  [[ "$output" == *"Improvement notes validation passed"* ]]
}

@test "validate_verification_gates passes minimal config" {
  mkdir -p "${temp_dir}/scripts/agentos"
  mkdir -p "${temp_dir}/docs/reference/agentos"
  cp "${repo_root}/scripts/agentos/validate_verification_gates.py" "${temp_dir}/scripts/agentos/"
  cp "${repo_root}/scripts/agentos/validation_utils.py" "${temp_dir}/scripts/agentos/"
  cat > "${temp_dir}/docs/reference/agentos/behavior-spec.md" <<'DOC'
# AgentOS Behavior Specification

## 6. Task taxonomy
- Discovery & Requirements
- AgentOS Meta-Maintenance
DOC
  cat > "${temp_dir}/docs/reference/agentos/verification-gates.md" <<'DOC'
# Verification Gates Catalog (Reference)

| Task type | Gate | Command | Evidence source | Notes |
| --- | --- | --- | --- | --- |
| Discovery & Requirements | Baseline | `just test` | Task runner | Template |
| AgentOS Meta-Maintenance | AgentOS | `just agentos::validate-agentos` | Task runner | Template |
DOC
  cat > "${temp_dir}/justfile" <<'JUST'
mod agentos "scripts/agentos"

test:
  echo "ok"
JUST
  mkdir -p "${temp_dir}/scripts/agentos"
  cat > "${temp_dir}/scripts/agentos/mod.just" <<'JUST'
validate-agentos:
  echo "ok"
JUST

  run bash -c "cd \"${temp_dir}\" && python3 scripts/agentos/validate_verification_gates.py"
  [ "$status" -eq 0 ]
  [[ "$output" == *"Verification gates validation passed"* ]]
}
