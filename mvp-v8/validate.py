#!/usr/bin/env python3
# @directive docs/explanation/decisions/2026-01-16-yaml-state.md
"""
Basic validation for AgentOS v8
"""

import yaml
import sys
from pathlib import Path

def validate_active_state(file_path):
    """Validate active state YAML"""
    try:
        with open(file_path) as f:
            data = yaml.safe_load(f)

        required = ['spec_version', 'state_id', 'updated_at', 'focus', 'frames']
        for field in required:
            if field not in data:
                print(f"Missing required field: {field}")
                return False

        if data['spec_version'] != 'agentos.active-state/v2':
            print("Invalid spec version")
            return False

        return True
    except Exception as e:
        print(f"Validation error: {e}")
        return False

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python validate.py <file>")
        sys.exit(1)

    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print("File not found")
        sys.exit(1)

    if 'active-state' in str(file_path):
        success = validate_active_state(file_path)
    else:
        print("Unknown file type")
        success = False

    sys.exit(0 if success else 1)
