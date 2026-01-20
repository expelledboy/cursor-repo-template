# MCP Tools Specification

**Status**: Initial
**Date**: 2026-01-14
**Purpose**: Specification for AgentOS MCP validation tools.

---

## Tool Overview

The AgentOS MCP server exposes 4 validation tools:

1. `validate_decision_graph` - Validate decision graph structure
2. `validate_command` - Validate command file format
3. `validate_rule` - Validate rule file format
4. `validate_mvp_coherence` - Comprehensive MVP coherence check

---

## Tool 1: validate_decision_graph

**Purpose**: Validate decision graph structure and format.

**Input**:
```json
{
  "graph_path": "docs/reference/agentos/decision-graphs/task-classification.md"
}
```

**Validation Checks**:
- File exists
- Required sections present: "Purpose", "Decision Tree"
- Decision tree has steps (### Step N:)
- Referenced files exist
- Format compliance

**Output Schema**: Standard validation result (see below)

**Example**:
```json
{
  "status": "pass",
  "message": "Decision graph validation passed",
  "details": [],
  "metadata": {
    "execution_time": 0.045,
    "scope": "decision_graph:docs/reference/agentos/decision-graphs/task-classification.md",
    "version": "1.0.0",
    "timestamp": "2026-01-14T12:00:00Z"
  }
}
```

---

## Tool 2: validate_command

**Purpose**: Validate command file format.

**Input**:
```json
{
  "command_path": ".cursor/commands/agentos-start.md"
}
```

**Validation Checks**:
- File exists
- Required sections: "Purpose", "Instructions for Agent", "Expected Outcome"
- Referenced decision graphs exist
- Referenced docs exist
- Format compliance

**Output Schema**: Standard validation result

**Example**:
```json
{
  "status": "warning",
  "message": "Command validation passed with 1 warning(s)",
  "details": [
    {
      "severity": "warning",
      "message": "Referenced decision graph does not exist: validation-strategy.md",
      "file": ".cursor/commands/agentos-start.md",
      "line": 12,
      "remediation": "Create decision graph at docs/reference/agentos/decision-graphs/validation-strategy.md"
    }
  ],
  "metadata": {
    "execution_time": 0.032,
    "scope": "command:.cursor/commands/agentos-start.md",
    "version": "1.0.0",
    "timestamp": "2026-01-14T12:00:00Z"
  }
}
```

---

## Tool 3: validate_rule

**Purpose**: Validate rule file format.

**Input**:
```json
{
  "rule_path": ".cursor/rules/agentos-core.mdc"
}
```

**Validation Checks**:
- File exists
- YAML frontmatter present (starts with `---`)
- Frontmatter has `description`, `alwaysApply`, or `globs`
- Referenced files exist
- Format compliance

**Output Schema**: Standard validation result

**Example**:
```json
{
  "status": "pass",
  "message": "Rule validation passed",
  "details": [],
  "metadata": {
    "execution_time": 0.028,
    "scope": "rule:.cursor/rules/agentos-core.mdc",
    "version": "1.0.0",
    "timestamp": "2026-01-14T12:00:00Z"
  }
}
```

---

## Tool 4: validate_mvp_coherence

**Purpose**: Comprehensive MVP coherence check.

**Input**:
```json
{
  "scope": "all" | "graphs" | "commands" | "rules"
}
```

**Validation Checks**:
- If `scope` is "all" or "graphs": Validate all decision graphs
- If `scope` is "all" or "commands": Validate all commands
- If `scope` is "all" or "rules": Validate all rules
- Aggregate results across all files

**Output Schema**: Standard validation result (aggregated)

**Example**:
```json
{
  "status": "warning",
  "message": "MVP coherence validation passed with 3 warning(s)",
  "details": [
    {
      "severity": "warning",
      "message": "Referenced file does not exist: docs/reference/agentos/alignment-mechanisms.md",
      "file": "docs/reference/agentos/decision-graphs/task-classification.md",
      "line": 16,
      "remediation": "Create file at docs/reference/agentos/alignment-mechanisms.md or fix reference"
    },
    {
      "severity": "warning",
      "message": "Referenced decision graph does not exist: validation-strategy.md",
      "file": ".cursor/commands/agentos-start.md",
      "line": 12,
      "remediation": "Create decision graph at docs/reference/agentos/decision-graphs/validation-strategy.md"
    }
  ],
  "metadata": {
    "execution_time": 0.156,
    "scope": "mvp_coherence:all",
    "version": "1.0.0",
    "timestamp": "2026-01-14T12:00:00Z"
  }
}
```

---

## Standard Output Schema

All tools return results following this JSON schema:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["status", "message", "details", "metadata"],
  "properties": {
    "status": {
      "type": "string",
      "enum": ["pass", "fail", "warning"]
    },
    "message": {
      "type": "string"
    },
    "details": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["severity", "message"],
        "properties": {
          "severity": {
            "type": "string",
            "enum": ["critical", "warning", "info"]
          },
          "message": {
            "type": "string"
          },
          "file": {
            "type": "string"
          },
          "line": {
            "type": "integer"
          },
          "column": {
            "type": "integer"
          },
          "remediation": {
            "type": "string"
          },
          "context": {
            "type": "string"
          }
        }
      }
    },
    "metadata": {
      "type": "object",
      "required": ["execution_time", "scope", "version", "timestamp"],
      "properties": {
        "execution_time": {
          "type": "number"
        },
        "scope": {
          "type": "string"
        },
        "version": {
          "type": "string"
        },
        "timestamp": {
          "type": "string",
          "format": "date-time"
        }
      }
    }
  }
}
```

---

## Status Values

- **pass**: No issues found
- **fail**: Critical issues found (must fix)
- **warning**: Warnings found (should fix)

---

## Severity Levels

- **critical**: Must fix (blocks functionality)
- **warning**: Should fix (may cause issues)
- **info**: Nice to fix (minor improvements)

---

## Path Conventions

All paths are relative to MVP root (no `mvp/` prefix):

- Decision graphs: `docs/reference/agentos/decision-graphs/*.md`
- Commands: `.cursor/commands/*.md`
- Rules: `.cursor/rules/*.mdc`
- Docs: `docs/reference/agentos/*.md`

---

## Error Handling

**File Not Found**:
- Returns `status: "fail"` with critical issue
- Provides remediation guidance

**Parse Errors**:
- Returns `status: "fail"` with critical issue
- Includes error message

**Missing References**:
- Returns `status: "warning"` (non-blocking)
- Lists all missing references

---

## Implementation

See `scripts/agentos/mcp_server.py` for implementation.

**CLI Usage**:
```bash
python3 scripts/agentos/mcp_server.py validate_decision_graph <path>
python3 scripts/agentos/mcp_server.py validate_command <path>
python3 scripts/agentos/mcp_server.py validate_rule <path>
python3 scripts/agentos/mcp_server.py validate_mvp_coherence [scope]
```

---

## Related Documentation

- `docs/how-to/agentos/mcp-setup.md` - Setup guide
- `docs/reference/agentos/validation-contract.md` - Validation principles
- `.cursor/commands/agentos-validate.md` - Command usage
