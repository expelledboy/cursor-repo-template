#!/usr/bin/env python3
"""
Minimal state management for context preservation.

DOE Registry - Bidirectional Linkages:
@directive docs/reference/agentos/state-management.md

# DOE Layer Declaration
DOE_LAYER = "execution"
DOE_RESPONSIBILITY = "Manage lightweight state preservation and context continuity"
DOE_GOVERNANCE = "docs/reference/agentos/doe-framework.md"
DOE_PRECEDENCE = 4
"""

import yaml
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional

class StateManager:
    """Minimal state management for context preservation."""

    def __init__(self):
        self.state_dir = Path("docs/local")
        self.state_file = self.state_dir / "agentos-state.yaml"
        self._ensure_state_dir()

    def _ensure_state_dir(self):
        """Ensure state directory exists."""
        self.state_dir.mkdir(parents=True, exist_ok=True)

    def save_context(self, context_type: str, metadata: Dict[str, Any]) -> str:
        """Save a lightweight context reference with metadata."""
        state = self._load_state()

        if 'contexts' not in state:
            state['contexts'] = {}

        context_id = f"{context_type}-{datetime.now().strftime('%Y%m%d-%H%M%S')}"

        state['contexts'][context_id] = {
            'timestamp': datetime.now().isoformat(),
            'type': context_type,
            'metadata': metadata,
            'active': True
        }

        # Keep only last 5 contexts to stay lightweight
        if len(state['contexts']) > 5:
            # Mark oldest as inactive instead of deleting
            oldest_key = min(state['contexts'].keys(),
                           key=lambda k: state['contexts'][k]['timestamp'])
            state['contexts'][oldest_key]['active'] = False

        self._save_state(state)
        return context_id

    def get_active_contexts(self) -> Dict[str, Any]:
        """Get currently active contexts."""
        state = self._load_state()
        contexts = state.get('contexts', {})

        # Return only active contexts
        return {k: v for k, v in contexts.items() if v.get('active', True)}

    def transfer_context(self, context_id: str, target_operation: str) -> Optional[Dict[str, Any]]:
        """Transfer context metadata to new operation."""
        state = self._load_state()
        contexts = state.get('contexts', {})

        if context_id not in contexts:
            return None

        source_context = contexts[context_id]

        # Create transfer metadata
        transfer = {
            'source_context': context_id,
            'source_type': source_context.get('type'),
            'timestamp': datetime.now().isoformat(),
            'target_operation': target_operation,
            'transferred_metadata': source_context.get('metadata', {}),
            'key_insights': source_context.get('metadata', {}).get('key_insights', []),
            'context_summary': source_context.get('metadata', {}).get('context_summary', '')
        }

        # Save transfer record
        if 'transfers' not in state:
            state['transfers'] = []

        state['transfers'].append(transfer)

        # Keep only last 10 transfers
        if len(state['transfers']) > 10:
            state['transfers'] = state['transfers'][-10:]

        self._save_state(state)
        return transfer

    def _load_state(self) -> Dict[str, Any]:
        """Load state from file."""
        if not self.state_file.exists():
            return {'version': 'agentos-state/v1', 'created': datetime.now().isoformat()}

        try:
            with open(self.state_file, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f) or {}
        except Exception:
            return {}

    def _save_state(self, state: Dict[str, Any]):
        """Save state to file."""
        with open(self.state_file, 'w', encoding='utf-8') as f:
            yaml.safe_dump(state, f, sort_keys=False)

# CLI interface for state management
def main():
    import argparse

    parser = argparse.ArgumentParser(description='AgentOS v9 State Management')
    subparsers = parser.add_subparsers(dest='command')

    # Save context
    save_parser = subparsers.add_parser('save', help='Save context')
    save_parser.add_argument('type', help='Context type')
    save_parser.add_argument('metadata', help='Metadata as JSON string')

    # List contexts
    subparsers.add_parser('list', help='List active contexts')

    # Transfer context
    transfer_parser = subparsers.add_parser('transfer', help='Transfer context')
    transfer_parser.add_argument('context_id', help='Context ID to transfer')
    transfer_parser.add_argument('operation', help='Target operation')

    args = parser.parse_args()

    manager = StateManager()

    if args.command == 'save':
        try:
            metadata = json.loads(args.metadata)
            context_id = manager.save_context(args.type, metadata)
            print(f"Context saved: {context_id}")
        except json.JSONDecodeError:
            print("Invalid JSON metadata")

    elif args.command == 'list':
        contexts = manager.get_active_contexts()
        if contexts:
            print("Active contexts:")
            for ctx_id, ctx_data in contexts.items():
                print(f"  {ctx_id}: {ctx_data.get('type')} ({ctx_data.get('timestamp')})")
        else:
            print("No active contexts")

    elif args.command == 'transfer':
        transfer = manager.transfer_context(args.context_id, args.operation)
        if transfer:
            print(f"Context transferred to {args.operation}")
            print(f"Key insights: {transfer.get('key_insights', [])}")
        else:
            print(f"Context {args.context_id} not found")

if __name__ == '__main__':
    main()