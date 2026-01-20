---
title: "Restructuring Tools Reference"
status: stable
created_date: 2026-01-16
purpose: "Command reference for documentation restructuring tools"
domain: docs
---

# Restructuring Tools Reference

## Tool Commands

### File Inventory
```bash
just docs-inventory
```
Creates `docs-inventory-YYYYMMDD.txt` with all files and statistics for batching decisions.

### Batch Management
```bash
just docs-create-batch "batch-name" "file1.md file2.md"
just docs-state "batch-name" "status-message"
just docs-validate-batch "batch-name"
```

### Cleanup (Run Only After Complete Success)
```bash
just docs-cleanup-all
```
Removes all batch files, state tracking, and inventories.

## Tool Outputs

### Inventory Format
```
docs/file1.md: 45 lines, 2.1KB
docs/file2.md: 67 lines, 3.2KB
```

### Batch Files
```
batches/batch-name.txt:
docs/file1.md
docs/file2.md
```

## Integration Notes

- Tools are deterministic infrastructure only
- All intelligence and decisions remain with the agent
- Tools support systematic processing without constraining judgment
- Cleanup happens once entire restructuring process succeeds