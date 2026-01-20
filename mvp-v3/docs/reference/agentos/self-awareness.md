# Self-Awareness in Semantic System

**Status**: Stable
**Date**: 2026-01-14
**Purpose**: Defines how self-awareness integrates with the semantic understanding system.

---

## Overview

Self-awareness in MVP-v3 monitors semantic understanding quality, feature usage, and gap detection. It complements the semantic understanding system by providing meta-cognitive monitoring.

---

## Semantic Understanding Quality

### Monitoring Questions
- Did I understand the requirement correctly?
- What semantic patterns did I match?
- What similar patterns did I find via semantic search?
- Was my routing semantically sound?
- Did I use semantic understanding or fall back to syntax?

### Quality Indicators
- **High Quality**: Clear semantic patterns matched, similar patterns found, confident routing
- **Medium Quality**: Some semantic patterns matched, limited similar patterns, moderate confidence
- **Low Quality**: Unclear semantic patterns, no similar patterns found, uncertain routing

### When Quality is Low
- Use semantic search more extensively
- Request user clarification
- Document uncertainty in task plan header
- Load additional context (more rules, more docs)

---

## Feature Usage Monitoring

### Which Rules Loaded?
Track which rules contributed to understanding:
- **alwaysApply**: Core rule always loaded
- **description**: Domain rules that matched keywords
- **globs**: File pattern rules that matched open files
- **Combined**: Multiple rules layered for rich context

### Semantic Search Usage
- Did semantic search help?
- What search terms were used?
- What similar patterns were found?
- Did search results inform routing?

### File Context Usage
- What file patterns informed understanding?
- What domain was inferred from file context?
- Did globs rules load based on file context?

### MCP Validation
- Did MCP validation catch issues?
- What structure validation was performed?
- Did two-layer validation (semantic + structure) work?

---

## Gap Detection

### When Semantic Understanding is Insufficient
- No clear semantic patterns matched
- Semantic search found no similar patterns
- File context unclear or conflicting
- Rules don't provide enough guidance

### When to Capture Gaps
- Semantic understanding quality is low
- No similar patterns found for requirement
- File context doesn't match requirement domain
- Rules provide conflicting guidance
- Routing uncertainty persists after semantic search

### Gap Capture Process
1. Document what was unclear semantically
2. Note what semantic patterns were attempted
3. Record semantic search terms and results
4. Capture file context that was used
5. Create gap work note per evolution framework

---

## Self-Monitoring Checkpoints

### Pre-Execution Checkpoint
**Semantic Understanding**:
- [ ] Requirement meaning understood semantically
- [ ] Semantic patterns matched
- [ ] Similar patterns found (if needed)
- [ ] File context considered
- [ ] Rules layered appropriately

**Feature Usage**:
- [ ] Core rule loaded (alwaysApply)
- [ ] Domain rules loaded (description match)
- [ ] File rules loaded (globs match)
- [ ] Semantic search used (if unclear)
- [ ] MCP validation performed (if available)

### Mid-Execution Checkpoint
**Semantic Alignment**:
- [ ] Current actions align with semantic understanding
- [ ] Semantic patterns still match
- [ ] File context still relevant
- [ ] Rules still applicable

**Gap Detection**:
- [ ] New semantic gaps discovered?
- [ ] Semantic understanding insufficient?
- [ ] Need more semantic search?

### Post-Execution Checkpoint
**Semantic Quality Assessment**:
- [ ] Was semantic understanding accurate?
- [ ] Did semantic patterns help?
- [ ] Did semantic search find useful patterns?
- [ ] Did file context inform correctly?

**Feature Usage Assessment**:
- [ ] Which rules were most helpful?
- [ ] Did semantic search improve understanding?
- [ ] Did file context improve routing?
- [ ] Did MCP validation catch issues?

---

## Self-Reflection Practices

### Semantic Understanding Reflection
**After routing**:
- What semantic patterns led to this routing?
- What similar patterns informed this decision?
- What file context influenced this routing?
- Was semantic understanding sufficient?

### Feature Usage Reflection
**After task**:
- Which rules were most valuable?
- Did semantic search improve outcomes?
- Did file context improve understanding?
- How did feature interplay help?

### Gap Reflection
**When gaps detected**:
- Why was semantic understanding insufficient?
- What additional context was needed?
- What patterns were missing?
- How can semantic understanding improve?

---

## Integration with Semantic System

Self-awareness enhances semantic understanding by:
- Monitoring semantic understanding quality
- Tracking feature usage effectiveness
- Detecting when semantic understanding is insufficient
- Providing feedback for improvement

Self-awareness does not replace semantic understanding - it monitors and improves it.

---

## Related Documentation

- `docs/reference/agentos/core-contract.md` - Core invariants
- `docs/reference/agentos/decisions/task-classification.md` - Semantic classification
- `.cursor/rules/core.mdc` - Self-describing core rule
- `.cursor/commands/agentos.md` - Semantic entry point

---

## Usage Requirements

- Monitor semantic understanding quality at each checkpoint
- Track feature usage (rules, search, context, MCP)
- Detect gaps when semantic understanding is insufficient
- Reflect on semantic understanding effectiveness
- Document semantic understanding in task plan header
