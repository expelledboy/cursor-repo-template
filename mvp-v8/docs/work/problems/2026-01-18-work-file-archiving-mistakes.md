---
title: "Incorrect Archiving of Work Files with Valuable Rationale"
status: active
created_date: 2026-01-18
domain: agentos
Status: active---

# Incorrect Archiving of Work Files with Valuable Rationale

## Observation
The agent repeatedly archives work documents (problems, discoveries) that contain valuable rationale and historical context, treating them as "superseded" when they are actually useful reference material.

## Impact
- **Lost Context**: Historical rationale explaining WHY decisions were made is lost
- **Broken Links**: Documents referencing the archived rationale become orphaned
- **Reduced Learning**: Future developers can't understand the reasoning behind system changes
- **Knowledge Degradation**: The system's understanding of its own evolution diminishes over time

## Evidence
- Problem documents about migration errors, schema adherence, etc. were archived despite containing valuable insights
- Decision documents now reference archive paths or have broken links
- Work files that explain systemic issues are treated as disposable rather than historical records

## Root Cause
Confusion between:
- **Archive**: Superseded/obsolete canonical material (old specs, deprecated features)
- **Work**: Research, problems, discoveries that remain valuable as historical context

Work documents contain "rationale" that explains WHY the system works the way it does, not specifications that become obsolete.

## Potential Solutions
1. **Rationale Preservation**: Work files with valuable rationale should remain in work/ indefinitely
2. **Status Distinction**: Use status fields to indicate "addressed" vs "superseded" rather than archiving
3. **Archiving Criteria**: Only archive truly obsolete material, never rationale-rich work documents
4. **Historical Value Assessment**: Evaluate work documents for ongoing reference value before archiving