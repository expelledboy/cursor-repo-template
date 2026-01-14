# /agentos-bootstrap - Bootstrap Repository

## Purpose
Bootstrap a new repository with AgentOS. This is a one-time setup command for initializing AgentOS in a new or poorly documented repository. Behavior is defined in canonical docs below.

## Lifecycle Entrypoint
- Covers: bootstrap mode (day-0 learning when directives are missing)
- Handoff: normal operation after bootstrap gates pass

## Canonical entrypoints (must read)
- docs/how-to/agentos/bootstrap-repo.md
- docs/reference/agentos/bootstrap-gates.md
- docs/reference/agentos/behavior-spec.md#15-self-improvement-loop
- docs/reference/agentos/architecture.md#2-supporting-contracts
- .cursor/rules/agentos/core.mdc

## Cursor rule loading
- Load core AgentOS directives for bootstrap mode.
- If phase rules do not auto-load, explicitly open `.cursor/rules/agentos/core.mdc`.

## Bootstrap process
1. **Detection**: Enter bootstrap mode when routing or directives are missing or unreliable.
2. **Inventory**: Capture evidence for CI, task runners, configs, repo structure, and docs.
3. **Extract workflows**: Document install, test, build, and deploy workflows based on evidence.
4. **Draft directives**: Create draft reference and how-to docs for critical domains.
5. **Create routing**: Update `docs/index.md` and create domain routing rules.
6. **Define registry scope**: Document which files require mapping in `AGENTS.md` under **Registry Scope** and start initial links.
7. **Produce analysis summary**: Write a bootstrap summary for human validation.
8. **Exit and ratify**: Use `docs/reference/agentos/bootstrap-gates.md` to confirm exit criteria.

## Exit criteria
Bootstrap is complete only when all of the following are true:
1. Inventory exists for CI, task runner, config, and repo structure.
2. Minimal workflows exist (install, test, build, deploy if relevant).
3. Draft directives exist for critical domains.
4. Routing exists (`docs/index.md` and domain rules).
5. Registry scope is defined and initial mapping exists.
6. A bootstrap analysis summary is produced for human validation.

## Adapter boundary
Commands are optional UI entrypoints. Core contracts live in docs/reference and must be followed.

## Next command
After bootstrap gates pass and human ratification, use `/agentos-init` to verify AgentOS is properly loaded, then proceed with normal task workflow using `/agentos-start`.
