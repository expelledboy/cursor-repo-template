# Validation Scripts (Reference)

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Defines the AgentOS validation scripts and their scope.

@implementation scripts/agentos/validate_registry.py
@implementation scripts/agentos/validate_routing.py
@implementation scripts/agentos/validation_utils.py
@implementation scripts/agentos/validate_core_list_sync.py
@implementation scripts/agentos/validate_traceability.py
@implementation scripts/agentos/validate_adr_format.py
@implementation scripts/agentos/validate_improvement_notes.py
@implementation scripts/agentos/validate_verification_gates.py
@implementation scripts/agentos/validate_agentos.py
@implementation scripts/agentos/validate_visual_maps.py
@implementation scripts/agentos/validate_directive_loading.py
@implementation scripts/agentos/validate_design_decisions.py
@implementation scripts/agentos/validate_complexity_workflow.py
@implementation scripts/agentos/validate_commands.py
@implementation scripts/agentos/mod.just
@implementation tests/agentos/validation.bats

---

## 1. Registry validation
- Script: `scripts/agentos/validate_registry.py`
- Command: `just agentos::validate-registry`
- Scope: `AGENTS.md` Registry Scope
- Requires: `python3`

## 2. Routing validation
- Script: `scripts/agentos/validate_routing.py`
- Command: `just agentos::validate-routing`
- Scope: `.cursor/rules/` (including `agentos/` isolation rules) and `docs/index.md`
- Requires: `python3`

## 3. Validation tests
- Script: `tests/agentos/validation.bats`
- Command: `just agentos::validate-tests`
- Requires: `bats`

## 4. Core list sync validation
- Script: `scripts/agentos/validate_core_list_sync.py`
- Command: `just agentos::validate-core-list`
- Scope: AgentOS core list in `docs/reference/agentos/components.md`, `docs/index.md`, and `.cursor/rules/20-agentos.topic.mdc`
- Requires: `python3`

## 5. Traceability validation
- Script: `scripts/agentos/validate_traceability.py`
- Command: `just agentos::validate-traceability`
- Scope: `docs/reference/agentos/problem-registry.md`, `docs/reference/agentos/traceability.md`, and `docs/explanation/agentos/decisions/`
- Requires: `python3`

## 6. ADR format validation
- Script: `scripts/agentos/validate_adr_format.py`
- Command: `just agentos::validate-adr-format`
- Scope: `docs/explanation/agentos/decisions/`
- Requires: `python3`

## 7. Improvement notes validation
- Script: `scripts/agentos/validate_improvement_notes.py`
- Command: `just agentos::validate-improvement-notes`
- Scope: `docs/work/agentos/improvement/`
- Requires: `python3`

## 8. Verification gates validation
- Script: `scripts/agentos/validate_verification_gates.py`
- Command: `just agentos::validate-verification-gates`
- Scope: `docs/reference/agentos/verification-gates.md` and task taxonomy
- Requires: `python3`

## 9. Visual maps validation
- Script: `scripts/agentos/validate_visual_maps.py`
- Command: `just agentos::validate-visual-maps`
- Scope: Mermaid diagrams in reference docs
- Requires: `python3`

## 10. Directive loading validation
- Script: `scripts/agentos/validate_directive_loading.py`
- Command: `just agentos::validate-directive-loading`
- Scope: `docs/reference/agentos/directive-tiers.md` table structure, `docs/reference/agentos/context-compass.md` selective loading protocol sections, `docs/reference/agentos/behavior-spec.md` directive loading plan format, tier sequence, deferral requirements, minimal mode documentation
- Requires: `python3`

## 11. Design-decision validation
- Script: `scripts/agentos/validate_design_decisions.py`
- Command: `just agentos::validate-design-decisions`
- Scope: `design-decision-templates.md` table formatting standards, `docs/reference/agentos/structured-exploration.md` Phase 3 table examples and criteria selection guidance, design-decision checkpoint how-to completeness, table format compliance validation
- Requires: `python3`

## 12. Complexity workflow validation
- Script: `scripts/agentos/validate_complexity_workflow.py`
- Command: `just agentos::validate-complexity-workflow`
- Scope: Complexity determination, workflow variations, behavior-spec, and how-to alignment
- Requires: `python3`

## 13. Command validation
- Script: `scripts/agentos/validate_commands.py`
- Command: `just agentos::validate-commands`
- Scope: `.cursor/commands/agentos-*.md` and command contract sections
- Requires: `python3`

## 14. AgentOS aggregate validation
- Script: `scripts/agentos/validate_agentos.py`
- Command: `just agentos::validate-agentos`
- Scope: runs all AgentOS validation scripts
- Requires: `python3`
