# AgentOS v8 - Systematic AI Development Framework

AgentOS v8 is a comprehensive, self-contained framework for systematic AI-assisted software development. It implements a **Directive-Orchestration-Execution (DOE)** operating model that ensures reliable, deterministic outcomes through structured processes and automated validation.

## 🎯 What is AgentOS?

AgentOS v8 transforms chaotic AI development into a structured, predictable process. Unlike traditional AI tools that operate reactively, AgentOS provides:

- **Systematic Development Phases**: From initialization to archival through structured workflows
- **Deterministic Validation**: Automated quality gates ensure consistency and correctness
- **Self-Monitoring Capabilities**: Continuous alignment checking and gap identification
- **Context Optimization**: Intelligent context management prevents token overflow
- **Complete Traceability**: Bidirectional links between documentation and implementation

## 🚀 Quick Start

### Prerequisites
- **Cursor Editor** v2.0+ (for command integration)
- **Python 3.8+** (for validation scripts)
- **just** task runner (for automated workflows)

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd agentos-v8
   ```

2. **Initialize the system**:
   ```bash
   just docs::validate  # Verify documentation integrity
   ```

3. **Start developing**:
   Open in Cursor and use `/retrospect` to plan your first task.

## 📋 Core Concepts

### Directive-Orchestration-Execution (DOE)
AgentOS operates through three integrated layers:

- **Directives**: Documentation that defines "what" and "why" (rules, references, guides)
- **Orchestration**: AI reasoning that determines "how" (commands, workflows, planning)
- **Execution**: Deterministic actions that implement "what" (tools, validation, automation)

### Diátaxis Documentation Framework
AgentOS uses Diátaxis for structured documentation:

| Type | Purpose | When to Use | Location |
|------|---------|-------------|----------|
| **Reference** | Stable facts, contracts, specs | Need exact information | `docs/reference/` |
| **How-to** | Step-by-step procedures | Learn to perform tasks | `docs/how-to/` |
| **Explanation** | Context, rationale, architecture | Understand "why" | `docs/explanation/` |
| **Tutorial** | Learning journeys | Acquire skills | `docs/tutorials/` |

### Work Classification
All work is classified for systematic processing:

- **Work**: Drafts, analyses, plans (temporary)
- **Archive**: Historical records (permanent)
- **Reference/How-to/Explanation**: Canonical documentation

## 🛠️ Commands Overview

AgentOS v8 provides specialized Cursor commands for systematic development:

### Core Commands

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/retrospect` | DOE alignment audit | **Always start here** - Before any significant task |
| `/meta` | Meta-Analysis Mode | When you suspect alignment issues or need deep self-audit |
| `/learn` | Capture observations | When you discover problems, insights, or patterns |
| `/evolve` | Update system behavior | When validation reveals gaps or needed improvements |

### Development Workflow Commands

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/checkpoint` | Save current state | When you want to preserve progress for later resumption |
| `/resume` | Continue from saved state | When continuing interrupted work |
| `/trace` | Record decision traces | When you want optional audit trail of decisions |
| `/distill` | Semantic compression | When documentation needs to be condensed while preserving meaning |
| `/refine` | AI-guided restructuring | When documentation needs systematic improvement |
| `/branch` | Branch management | When managing parallel development branches |

## 📖 User Guide

### 1. Planning Your Work

**Always start with `/retrospect`** for interactive DOE alignment:

**In Cursor Chat:**
```
/retrospect "Implementation / Feature" "Users can log in securely" "create auth service, add login route, write tests" "src/auth.py, tests/"
```

**Planning Approach:**
1. **Prepare complete task details** following the guidance
2. **Call `/retrospect`** with all information in one command
3. **Receive comprehensive DOE audit** results immediately

**What it validates:**
- Task plan completeness and measurability
- Required directives loaded for your task type
- Safety considerations and risk assessment
- Evidence quality and authority sources
- Verification gates appropriate for task complexity

**Expected Output:**
- ✅ **Clear to proceed** - Task is well-planned and safe
- ⚠️ **Suggestions provided** - Address issues before proceeding
- ❌ **Issues found** - Task needs planning improvements

### 2. Understanding Task Types

AgentOS categorizes work to ensure appropriate validation:

| Task Type | Examples | Validation Level |
|-----------|----------|------------------|
| **Implementation / Feature** | New features, code changes | Full DOE audit |
| **Documentation & Knowledge** | Writing docs, restructuring | Registry validation |
| **System Evolution** | Updating rules/commands | Safety verification |
| **Analysis & Research** | Investigations, discoveries | Evidence quality |
| **Maintenance** | Bug fixes, cleanup | Basic validation |

### 3. Development Workflow

For systematic development with AgentOS v8:

**In Cursor Chat:**
```bash
# 1. Always start with chat-guided DOE alignment audit
/retrospect "Implementation / Feature" "Users can log in securely" "create auth service, add login route, write tests" "src/auth.py, tests/"
# → Provides complete DOE audit with pass/fail results and recommendations

# 2. If you discover issues or insights during work
/learn "Discovered that auth tokens need refresh logic"

# 3. If validation reveals system gaps
/evolve @problem-file  # Update system behavior based on learnings

# 4. Save progress for resumability
/checkpoint "Auth implementation checkpoint"

# 5. Resume later if needed
/resume
```

**Terminal Validation:**
```bash
# Validate system integrity
just lint                    # Frontmatter syntax
just test                    # Documentation validation
just docs::validate-registry # Bidirectional links
```

**Documentation Workflow:**
```bash
# For documentation restructuring
/refine @batch-file         # AI-guided restructuring
/distill @verbose-file      # Semantic compression
```

### 4. Documentation Standards

**Frontmatter Requirements:**
```yaml
---
title: "Document Title"
status: stable|draft|superseded
created_date: 2026-01-18
purpose: "Clear purpose statement"
domain: agentos|docs|core
---

# Content here...
```

**Key Rules:**
- Use lowercase kebab-case filenames
- Include `implementations:` for decisions with code
- Add `@directive` annotations to code files
- Maintain bidirectional traceability

### 5. Validation Gates

Run these commands to ensure system integrity:

```bash
# Basic validation (always run these)
just lint                    # Check YAML frontmatter syntax
just test                    # Run comprehensive documentation validation
just docs::validate-registry # Verify bidirectional traceability links

# Advanced diagnostics
just docs::doctor            # System health check and guidance
/retrospect [...]             # DOE alignment audit (in Cursor chat)
```

## 🏗️ Architecture Deep Dive

### Core Components

```
AgentOS v8/
├── docs/                    # Documentation system
│   ├── reference/          # Stable facts and contracts
│   ├── how-to/            # Procedures and workflows
│   ├── explanation/       # Rationale and architecture
│   ├── work/              # Drafts and temporary docs
│   ├── archive/           # Historical records
│   └── local/             # Memory bank (context persistence)
├── .cursor/
│   ├── commands/          # Cursor command definitions
│   └── rules/             # Behavioral directives
├── scripts/
│   └── docs/              # Validation and generation
└── schemas/               # Data structure definitions
```

### Key Files

| File | Purpose |
|------|---------|
| `docs/index.md` | Documentation map and authority order |
| `.cursor/rules/core.mdc` | Core behavioral directives |
| `.cursor/commands/retrospect.md` | DOE alignment audit |
| `scripts/docs/index.py` | Validation engine |
| `docs/local/active-context.yaml` | Context persistence |

### Context Optimization

AgentOS v8 implements advanced context management:

- **Hierarchical Loading**: Directives load progressively (~70% token reduction)
- **Memory Bank**: Persistent context across operations
- **Selective Compression**: Intelligent context management
- **Complexity Scaling**: Adaptive behavior based on task complexity

## 🔧 Maintenance & Contribution

### For Contributors

1. **Understand the System**:
   - Read `docs/index.md` first
   - Follow Diátaxis for documentation
   - Use `/retrospect` before changes

2. **Development Process**:
   ```bash
   # Plan your contribution
   /retrospect "Enhance validation" "Improve error messages" "update scripts" "scripts/docs/index.py"

   # Make changes following DOE
   # Test thoroughly
   just docs::validate
   ```

3. **Documentation Updates**:
   - Reference docs: For stable facts
   - How-to docs: For procedures
   - Explanation docs: For rationale
   - Work docs: For drafts (temporary)

### Quality Standards

**Must Pass Before Commit:**
- ✅ `just lint` - No syntax errors
- ✅ `just test` - No broken links
- ✅ `just docs::validate` - Schema compliance
- ✅ Registry validation - Bidirectional links
- ✅ `/retrospect` audit - DOE alignment

**Code Standards:**
- Include `@directive` annotations for traceable changes
- Update `implementations:` in decision documents
- Maintain metadata preservation
- Follow schema compliance

### System Evolution

AgentOS evolves through structured processes:

1. **Problem Discovery**: Use `/learn` to capture issues
2. **Validation**: Run comprehensive checks
3. **Evolution**: Use `/evolve` for system updates
4. **Verification**: Confirm improvements work

## 🐛 Troubleshooting

### Common Issues

**Commands not appearing in Cursor:**
- Ensure Cursor 2.0+ is installed
- Restart Cursor after adding commands
- Verify `.cursor/commands/` structure

**Validation failures:**
- Run `just docs::validate` for detailed errors
- Check frontmatter schema compliance
- Verify bidirectional links

**Context overflow:**
- Use `/retrospect` for complex tasks
- Enable compression in memory bank
- Break large tasks into phases

### Getting Help

1. **Check documentation**: `docs/index.md` provides navigation
2. **Run diagnostics**: `/retrospect` identifies alignment issues
3. **Review examples**: Check `examples/` for patterns
4. **Validate system**: `just docs::validate` ensures integrity

## 📚 Resources

### Key Documentation
- `docs/index.md` - System navigation and sources of truth
- `docs/reference/agentos/architecture.md` - Core operating model
- `docs/reference/agentos/context-optimization.md` - Context management
- `docs/how-to/` - Complete procedure guides

### Examples
- `examples/active-state.yaml` - State management patterns
- `examples/task-router.yaml` - Task routing examples

### Validation Scripts
- `scripts/docs/index.py` - Main validation engine
- `justfile` - Automated task runner

## 🎉 Success Stories

AgentOS v8 has successfully:
- **Achieved 100% self-containment** - All behavior explained within system
- **Implemented DOE alignment** - Systematic validation and execution
- **Integrated context optimization** - Efficient operation within constraints
- **Maintained full traceability** - Bidirectional documentation links
- **Enabled systematic evolution** - Structured improvement processes

## 🤝 Contributing

AgentOS v8 welcomes contributions that enhance systematic development:

1. **Start with `/retrospect`** to plan your contribution
2. **Follow DOE principles** in implementation
3. **Maintain documentation standards** throughout
4. **Run full validation** before submitting
5. **Document rationale** for architectural changes

---

**Ready to build systematically? Start with `/retrospect` and transform your AI development workflow!** 🚀