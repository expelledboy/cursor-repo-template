# Task Classification (Semantic)

**Purpose**: Route tasks to appropriate workflow types using semantic understanding.

**Status**: Stable
**Date**: 2026-01-14

---

## How I Understand Task Types

I classify tasks by understanding their semantic meaning, not by evaluating code expressions. I recognize patterns in natural language and match them to workflow types.

---

## Execution Pattern

**Semantic Indicators**:
- Clear, specific objective stated
- Single domain focus evident
- Measurable outcome described
- Implementation-focused language
- Keywords: "implement", "add", "create", "build", "fix"

**When Unclear**:
- Use semantic search for: "tasks with clear objectives in [domain]"
- Look for similar requirements that mention "implement", "add", "create" with specific outcomes
- Check file context (globs) to understand domain

**Route**: `execution`
**Load**: `docs/reference/agentos/workflows/execution.md`
**Confidence**: High when objective is specific and measurable

**Example Patterns**:
- "Add user authentication with OAuth" → Execution (clear objective, single domain)
- "Implement payment processing" → Execution (implementation-focused)
- "Fix bug in login flow" → Execution (clear fix objective)

---

## Coordination Pattern

**Semantic Indicators**:
- Multiple stakeholders mentioned
- Consensus or alignment needed
- Cross-team dependencies
- Keywords: "coordinate", "align", "consensus", "stakeholder", "team"
- Multiple domains affected

**When Unclear**:
- Use semantic search for: "tasks requiring stakeholder coordination"
- Look for requirements mentioning multiple teams or stakeholders
- Check if multiple domains are involved

**Route**: `coordination`
**Load**: `docs/reference/agentos/workflows/coordination.md`
**Confidence**: High when coordination needs are explicit

**Example Patterns**:
- "Coordinate API changes across frontend and backend teams" → Coordination
- "Align design system with product requirements" → Coordination
- "Get consensus on authentication approach" → Coordination

---

## Architecture Pattern

**Semantic Indicators**:
- System-wide changes
- Architectural decisions needed
- Keywords: "refactor", "redesign", "architecture", "restructure", "migrate"
- Multiple domains affected
- Long-term impact mentioned

**When Unclear**:
- Use semantic search for: "architectural changes affecting [domains]"
- Look for requirements mentioning system-wide or structural changes
- Check if multiple components/modules affected

**Route**: `architecture`
**Load**: `docs/reference/agentos/workflows/architecture.md`
**Confidence**: High when architectural scope is clear

**Example Patterns**:
- "Refactor authentication system to support multiple providers" → Architecture
- "Redesign data layer for scalability" → Architecture
- "Migrate to new framework" → Architecture

---

## Direct Execution Pattern

**Semantic Indicators**:
- Simple, isolated change
- Single file or small scope
- No dependencies or risks
- Keywords: "typo", "small fix", "quick change"
- Minimal impact

**When Unclear**:
- Use semantic search for: "simple isolated changes"
- Check file context (globs) - single file edits suggest direct execution
- Assess scope - minimal changes suggest direct execution

**Route**: `direct`
**Load**: `docs/reference/agentos/workflows/direct.md`
**Confidence**: High when scope is minimal and isolated

**Example Patterns**:
- "Fix typo in README" → Direct
- "Update configuration value" → Direct
- "Add missing import" → Direct

---

## Semantic Search Integration

When classification is unclear:
1. Extract key concepts from requirement (domain, objective type, scope)
2. Use semantic search: "tasks like [requirement summary]"
3. Review similar patterns found
4. Match semantic patterns from search results
5. Document search terms and results in task plan header

---

## File Context Integration

When files are open (globs):
1. Check file patterns to understand domain
2. Load domain-specific semantic patterns
3. Use domain context to inform classification
4. Example: Editing `src/auth/**` → Likely authentication domain → Security-aware routing

---

## Fallback

If classification remains unclear after semantic understanding and search:
1. Request user clarification
2. Document uncertainty in task plan header
3. Load: `docs/reference/agentos/core-contract.md` (ambiguity resolution)
4. Proceed with best semantic match, noting uncertainty

---

## Integration with Other Decision Graphs

This classification happens first, then:
- Complexity assessment uses semantic understanding of scope/risk
- Workflow selection uses task type + complexity semantically
