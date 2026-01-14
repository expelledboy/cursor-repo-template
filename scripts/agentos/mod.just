# AgentOS validation recipes
# @directive docs/reference/agentos/validation-scripts.md

set working-directory := "../.."

validate-registry:
  python3 scripts/agentos/validate_registry.py

validate-routing:
  python3 scripts/agentos/validate_routing.py

validate-core-list:
  python3 scripts/agentos/validate_core_list_sync.py

validate-traceability:
  python3 scripts/agentos/validate_traceability.py

validate-adr-format:
  python3 scripts/agentos/validate_adr_format.py

validate-improvement-notes:
  python3 scripts/agentos/validate_improvement_notes.py

validate-verification-gates:
  python3 scripts/agentos/validate_verification_gates.py

validate-visual-maps:
  python3 scripts/agentos/validate_visual_maps.py

validate-directive-loading:
  python3 scripts/agentos/validate_directive_loading.py

validate-design-decisions:
  python3 scripts/agentos/validate_design_decisions.py

validate-complexity-workflow:
  python3 scripts/agentos/validate_complexity_workflow.py

validate-commands:
  python3 scripts/agentos/validate_commands.py

validate-agentos:
  python3 scripts/agentos/validate_agentos.py

validate-tests:
  bats tests/agentos/*.bats

alias doctor := validate-agentos
alias test := validate-tests
