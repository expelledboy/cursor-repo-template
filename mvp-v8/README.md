# AgentOS v8 - Systematic AI Development Framework

**Status**: Complete | **Version**: 8.0 | **Date**: 2026-01-18

AgentOS v8 is a comprehensive, self-contained framework for systematic AI-assisted software development. It implements **Directive-Orchestration-Execution (DOE)** operating model that ensures reliable, deterministic outcomes through structured processes and automated validation.

## 🎯 What Makes AgentOS Different

Unlike traditional AI tools that operate reactively, AgentOS v8 provides:

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

## 📚 Documentation

**📖 Complete User Guide**: `docs/README.md`
- Comprehensive introduction to AgentOS v8
- Getting started with your first task
- Understanding core concepts (DOE, Diátaxis, complexity levels)
- Using commands and workflows
- Contributing and maintenance guidelines

**🗺️ Documentation Map**: `docs/index.md`
- Navigation guide to all documentation
- Authority order and structure rules
- Reference to all system components

## 🛠️ Commands Overview

AgentOS v8 provides specialized Cursor commands for systematic development:

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/retrospect` | DOE alignment audit | **Always start here** - Before any significant task |
| `/meta` | Meta-Analysis Mode | When you suspect alignment issues or need deep self-audit |
| `/learn` | Capture observations | When you discover problems, insights, or patterns |
| `/evolve` | Update system behavior | When validation reveals gaps or needed improvements |
| `/checkpoint` | Save current state | When preserving progress for later resumption |
| `/resume` | Continue from saved state | When continuing interrupted work |
| `/trace` | Record decision traces | When optional audit trail is needed |
| `/distill` | Semantic compression | When documentation needs condensation |
| `/refine` | AI-guided restructuring | When systematic documentation improvement needed |
| `/branch` | Branch management | When managing parallel development branches |

## 🔧 Core Architecture

### Directive-Orchestration-Execution (DOE)
- **Directives**: Documentation defining "what" and "why"
- **Orchestration**: AI reasoning determining "how"
- **Execution**: Deterministic actions implementing "what"

### Diátaxis Documentation Framework
- **Reference**: Stable facts and contracts
- **How-to**: Step-by-step procedures
- **Explanation**: Context and rationale
- **Tutorial**: Learning journeys

### Context Optimization
- **Hierarchical Loading**: ~70% token reduction through tiered directive loading
- **Memory Bank**: Persistent context across operations
- **Selective Compression**: Intelligent context management
- **Complexity Scaling**: Adaptive behavior based on task complexity

## ✅ Validation & Quality

Run these commands to ensure system integrity:

```bash
# Basic validation (always run these)
just lint                    # Check YAML frontmatter syntax
just test                    # Run comprehensive documentation validation
just docs::validate-registry # Verify bidirectional traceability links

# Advanced diagnostics
just docs::doctor            # System health check and guidance
/retrospect                   # Interactive DOE alignment audit (in Cursor chat)
```

## 🎉 Key Achievements

AgentOS v8 has successfully:
- **Achieved 100% self-containment** - All behavior explained within system
- **Implemented DOE alignment** - Systematic validation and execution
- **Integrated context optimization** - Efficient operation within constraints
- **Maintained full traceability** - Bidirectional documentation links
- **Enabled systematic evolution** - Structured improvement processes

## 🤝 Contributing

1. **Start with `/retrospect`** to plan your contribution
2. **Follow DOE principles** in implementation
3. **Maintain documentation standards** throughout
4. **Run full validation** before submitting
5. **Document rationale** for architectural changes

---

**Ready to build systematically? Read `docs/README.md` and start with `/retrospect`!** 🚀