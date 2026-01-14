#!/usr/bin/env python3
# @directive docs/reference/agentos/validation-scripts.md

import os
import subprocess
import sys

SCRIPTS = [
    "scripts/agentos/validate_registry.py",
    "scripts/agentos/validate_routing.py",
    "scripts/agentos/validate_core_list_sync.py",
    "scripts/agentos/validate_traceability.py",
    "scripts/agentos/validate_adr_format.py",
    "scripts/agentos/validate_improvement_notes.py",
    "scripts/agentos/validate_verification_gates.py",
    "scripts/agentos/validate_visual_maps.py",
    "scripts/agentos/validate_directive_loading.py",
    "scripts/agentos/validate_design_decisions.py",
    "scripts/agentos/validate_complexity_workflow.py",
    "scripts/agentos/validate_commands.py",
]


def main():
    missing = [path for path in SCRIPTS if not os.path.exists(path)]
    if missing:
        print("Missing validation scripts:")
        for path in missing:
            print(f"  - {path}")
        return 1

    errors = False
    for path in SCRIPTS:
        print(f"Running {path}")
        result = subprocess.run([sys.executable, path])
        if result.returncode != 0:
            errors = True

    if errors:
        print("AgentOS validation failed")
        return 1

    print("AgentOS validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
