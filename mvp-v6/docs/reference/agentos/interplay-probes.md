# Interplay Probes

Status: Draft
Date: 2026-01-15
Purpose: Jump across Cursor features to test synergy per task.

## Probe P1: Rules + Manual Context
Trigger: SIG_U and SIG_F both present.
Test: compare SIG_U vs SIG_F; if conflict, ask user.
Log: precedence decision.

## Probe P2: Description Rules + Search
Trigger: SIG_D loaded and SIG_S used.
Test: record both; routing follows kernel precedence.
Log: query + matched cues.

## Probe P3: Parallel Sub-agents
Trigger: ambiguity or L2+.
Test: run parallel pattern sub-agents; synthesize.
Log: sub-agent outputs used.

## Probe P4: Pipeline Sub-agents
Trigger: ACT with validation needed.
Test: chain discovery -> implementation -> validator.
Log: handoff points.

## Probe P5: MCP vs Heuristics
Trigger: SIG_S suggests a pattern and MCP available.
Test: validate with MCP; if mismatch, prefer MCP.
Log: MCP result.

## Probe P6: Mentions as injection
Trigger: user @mentions files/folders/rules.
Test: treat mentioned artifacts as explicit injection (SIG_U/SIG_F); re-evaluate routing.
Log: what was mentioned + resulting routing decision.

## Probe P7: Composable rules vs monoliths
Trigger: a new instruction set is requested (rules/skills).
Test: split into minimal rules; measure whether guidance stays current after edits.
Log: number of rules + references used instead of copied text.
