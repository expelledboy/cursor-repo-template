# /agentos-init - Initialize AgentOS System

## Purpose
Load the core AgentOS system into context and provide a readiness report confirming the agent is operating according to AgentOS. Use this command to ensure all core directives are loaded and the agent is ready to work. Behavior is defined in canonical docs below.

## Lifecycle Entrypoint
- Covers: system initialization and readiness confirmation
- Handoff: ready for normal task workflow

## Canonical entrypoints (must read)
- docs/reference/agentos/components.md
- docs/reference/agentos/behavior-spec.md
- docs/reference/agentos/architecture.md
- docs/reference/agentos/routing.md
- docs/reference/agentos/context-compass.md
- docs/reference/agentos/safety-policy.md
- docs/reference/agentos/directive-tiers.md
- docs/reference/agentos/cursor-mechanics.md
- docs/reference/agentos/self-awareness-framework.md
- .cursor/rules/agentos/core.mdc
- .cursor/rules/20-agentos.topic.mdc

## Cursor rule loading
- Load all Tier 1 (Core) directives listed in `docs/reference/agentos/components.md`.
- Load AgentOS adapter rule if available.
- If phase rules do not auto-load, explicitly open `.cursor/rules/agentos/core.mdc` and `.cursor/rules/20-agentos.topic.mdc`.

## System readiness report
After loading core directives into context, the agent must provide a system readiness report that includes:
- Confirmation that core AgentOS directives are loaded
- Statement that the agent is operating according to AgentOS
- Summary of loaded directives (Tier 1 core)
- Confirmation of readiness for normal task workflow
- Reference to key AgentOS principles (lifecycle, authority order, routing, safety)

The report should be clear and user-facing, confirming operational readiness.

## Expected outcome
- All core AgentOS directives loaded into context
- System readiness report provided to user
- Agent confirmed operating according to AgentOS
- Ready for normal task workflow

## Adapter boundary
Commands are optional UI entrypoints. Core contracts live in docs/reference and must be followed.

## Next command
After readiness report confirms operational status, proceed with normal task workflow using `/agentos-start` for new tasks.
