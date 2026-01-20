---
title: "Spec: Active State (agentos.active-state/v2)"
status: stable
created_date: 2026-01-16
purpose: "Simple resumable state for agent conversations"
domain: agentos
---

# Spec: Active State (agentos.active-state/v2)

## Purpose
Simple resumable state for agent conversations.

## Structure
- **Frames**: Context snapshots with title/summary
- **Focus**: Current working frame
- **Links**: Navigation between frames

## Usage
- Use `/checkpoint` to save progress
- Use `/resume` to jump back
- Automatic state persistence