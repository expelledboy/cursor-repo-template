---
doc_status: stable
purpose: Define universal constraints and mechanics shared by all AI agent runtimes.
intent: facts
governed_by:
  docs/domains/dev.md: Authority for dev domain docs
related:
  docs/dev/facts/cursor-mechanics.md: Cursor-specific mechanics that extend these universals
  docs/dev/facts/opencode-mechanics.md: OpenCode-specific mechanics that extend these universals
---

# Fact: Universal Agent Mechanics

This document defines constraints and behaviors that apply to **all** AI coding agent runtimes (Cursor, OpenCode, Codex, Claude Code, etc.). Runtime-specific mechanics are documented in separate facts docs.

## Physical Constraints

### Finite Context Windows

All agent runtimes operate within token limits imposed by the underlying language model. This is a hard physical ceiling, not a soft guideline.

- Context windows range from ~8K to ~200K tokens depending on model
- Token limits include: system prompt, rules, conversation history, tool outputs, and file contents
- When limits are reached, something must be removed to make room

### Compaction is Inevitable

When context limits are reached, runtimes compact (summarize) conversation history to continue. This is automatic and not under user control in most runtimes.

**Consequences of compaction:**
- Early instructions may be lost or summarized into vague guidance
- Specific file contents read earlier may no longer be accessible
- Tool outputs from early in the session may be discarded
- The agent's understanding of "what we decided" can drift

### The Executability Principle

**An instruction not present in the active context window is effectively non-existent.**

- Do not rely on "training memory" or "previous session history"
- Do not assume the agent "remembers" decisions from early in a long session
- Critical constraints must be continuously re-injected or referenced

### Cost of Context Bloat

Loading unused context is a defect, not a safety margin.

- Irrelevant files crowd out relevant information
- The agent may focus on unrelated content
- Reasoning quality degrades as context fills with noise
- Token costs increase without benefit

## Context Discovery Patterns

### On-Demand Context Loading

Modern agents find context dynamically rather than requiring manual tagging of every file.

- **Grep/ripgrep**: Fast text search across codebase
- **Semantic search**: Find files by meaning, not just keywords
- **File globbing**: Pattern-based file discovery

**Best practice**: If you know the exact file, reference it. If not, let the agent find it.

### Progressive Loading

Skills, rules, and reference documents should be loaded on-demand based on relevance rather than front-loaded into every session.

- Skills are discovered at startup but content is loaded only when invoked
- Agent-decided rules load only when the agent determines relevance
- Reference files in skills are loaded progressively as needed

## Session Management

### When to Start a New Conversation

**Start fresh when:**
- Moving to a different task or feature
- The agent seems confused or keeps making the same mistakes
- You've finished one logical unit of work
- Agent effectiveness has noticeably decreased

**Continue the conversation when:**
- Iterating on the same feature
- The agent needs context from earlier in the discussion
- Debugging something the agent just built

### State Persistence Across Sessions

Agents do not retain memory between sessions. External state management is required for:

- Multi-step tasks that span sessions
- Recording decisions for future reference
- Tracking progress on complex objectives

This governance system provides `docs/work/objective-graph.yaml` for this purpose.

## Best Practices (Universal)

### Start with Plans

Planning before coding improves outcomes:

1. Describe what you want to build
2. Let the agent research the codebase
3. Review and refine the plan
4. Execute with clear acceptance criteria

### Provide Verifiable Goals

Agents perform best when they can verify their own success:

- Use typed languages with compiler feedback
- Configure linters that run automatically
- Write tests that define expected behavior
- Give clear signals for whether changes are correct

### Review Carefully

AI-generated code can look correct while being subtly wrong:

- Read the diffs, don't just accept
- The faster the agent works, the more important review becomes
- Watch for drift from architectural patterns

### Iterate on Setup

- Start simple; add rules only when you notice repeated mistakes
- Add commands/skills only after identifying workflows you repeat
- Don't over-optimize before you understand your patterns
