---
title: "System Evolution"
description: "Analyze context and intelligently evolve system behavior based on identified improvements"
usage: "/evolve"
---

# System Evolution Instructions

You are an **Intelligent System Architect**. Your goal is to analyze conversation context and proactively identify system improvements that need implementation.

## Enhanced Evolution Protocol

### Mode 1: Context Analysis (No Arguments)
When called as `/evolve` with no arguments, perform **Intelligent Context Evolution Analysis**:

#### Step 1: Conversation Context Mining
Analyze the recent conversation context (last 15-20 messages) for evolution opportunities:
- **Problem Discussions**: Issues identified that need system changes
- **Discovery Applications**: Insights that should modify system behavior
- **Improvement Suggestions**: Explicit recommendations for system enhancement
- **Gap Analyses**: MAM findings or architectural issues identified
- **User Critiques**: Feedback about system behavior or usability
- **Pattern Recognition**: Recurring issues indicating systemic problems

#### Step 2: Evolution Opportunity Assessment
Evaluate identified opportunities for evolution suitability:
- **Impact Level**: High/Medium/Low impact on system behavior
- **Feasibility**: Can the change be implemented through rules/commands/docs?
- **Urgency**: How critical is this improvement?
- **Dependencies**: Does it require other changes first?
- **Scope**: Local change vs systemic modification

#### Step 3: Intelligent Evolution Planning
For each suitable opportunity:
- **Extract Core Issue**: Distill the fundamental problem or insight
- **Determine Change Type**: Rules, Commands, Documentation, or Process
- **Identify Target Components**: Specific files that need modification
- **Plan Implementation**: Step-by-step changes needed
- **Assess Side Effects**: Potential impacts on other system components

#### Step 4: Prioritized Evolution Execution
Execute changes in priority order:
- **Critical Issues**: Immediate fixes for broken functionality
- **High-Impact Improvements**: Significant usability or reliability gains
- **Architectural Enhancements**: Structural improvements to system design
- **Process Optimizations**: Workflow and efficiency improvements

### Universal Evolution Processing

#### Step 5: Change Implementation
Apply changes following the adaptation protocol:
- **Rules** (`.cursor/rules/*.mdc`): Update behavioral constraints and routing
- **Commands** (`.cursor/commands/*.md`): Modify process instructions and interfaces
- **Documentation** (`docs/`): Update standards, procedures, and references
- **Processes**: Improve workflows and interaction patterns

#### Step 6: Validation and Testing
After each change:
- **Syntax Validation**: Ensure files are properly formatted
- **Logic Verification**: Check that changes implement intended behavior
- **Integration Testing**: Verify changes work with existing components
- **Regression Prevention**: Ensure no existing functionality is broken

#### Step 7: Documentation and Traceability
Complete the evolution:
- **Update Work Files**: Mark implemented changes as resolved
- **Create Decision Records**: For significant policy or architectural changes
- **Update References**: Ensure all documentation reflects new behavior
- **Traceability Links**: Connect changes back to original issues/insights

## Context Intelligence Features

### Proactive Evolution Triggers
Automatically identify evolution opportunities from:
- **MAM Audit Results**: System issues requiring behavioral changes
- **User Experience Problems**: Interface or usability issues
- **Architectural Flaws**: Design problems identified through analysis
- **Process Inefficiencies**: Workflow improvements discovered
- **Pattern-Based Insights**: Recurring issues indicating systemic problems

### Evolution Quality Assurance
- **Change Validation**: Each modification is tested and verified
- **Impact Assessment**: Side effects are identified and mitigated
- **Rollback Planning**: Critical changes include reversion strategies
- **Incremental Implementation**: Complex changes broken into testable steps

### Meta-Evolution Capabilities
- **Self-Improvement**: Evolution system learns from its own effectiveness
- **Pattern Recognition**: Identifies when similar issues require similar fixes
- **Effectiveness Tracking**: Monitors whether evolutions achieve intended results
- **Continuous Calibration**: Improves evolution intelligence over time

## Usage Examples

### Context Analysis Mode
```
/evolve
```
→ Analyzes recent conversation, identifies evolution opportunities, implements changes

### Evolution Results Example
```
🔍 EVOLUTION ANALYSIS COMPLETE

📋 IDENTIFIED OPPORTUNITIES:
1. HIGH: Fix /retrospect command architectural flaws
2. HIGH: Enhance MAM with architectural validation
3. MEDIUM: Implement context-aware command patterns

⚡ EXECUTING EVOLUTIONS:

1️⃣ EVOLVING: /retrospect command architecture
   ✓ Renamed command to /analyze for clarity
   ✓ Implemented context-aware conversation analysis
   ✓ Updated documentation and help text

2️⃣ EVOLVING: MAM self-awareness enhancement
   ✓ Added architectural validation layer
   ✓ Implemented interface compatibility checks
   ✓ Enhanced gap detection capabilities

3️⃣ EVOLVING: Context-aware command framework
   ✓ Created conversation analysis patterns
   ✓ Implemented semantic intent recognition
   ✓ Added progressive planning capabilities

✅ EVOLUTION COMPLETE
- 3 system components updated
- 2 new capabilities added
- 1 architectural issue resolved
```

## Integration with Learning System

### `/learn` Integration
- **Problem Capture**: `/learn` creates work files that become `/evolve` candidates
- **Discovery Application**: `/learn` insights guide system behavior improvements
- **Feedback Loop**: Evolution results inform future learning priorities

### `/retrospect` Integration
- **Planning Integration**: Evolution changes may require updated planning approaches
- **Validation Updates**: New system behaviors need corresponding validation rules
- **Process Alignment**: Ensure planning and evolution processes remain coherent

## Success Criteria

### Effective Evolution
- **Problem Resolution**: Identified issues are actually fixed
- **System Improvement**: Changes enhance rather than complicate the system
- **User Experience**: Evolutions improve usability and effectiveness
- **Maintainability**: Changes are well-documented and sustainable

### Intelligence Metrics
- **Context Understanding**: Accurately identifies genuine improvement opportunities
- **Change Quality**: Modifications are correct, complete, and well-implemented
- **Impact Prediction**: Anticipates side effects and dependencies
- **Evolution Learning**: System improves its evolution intelligence over time

## Related Documentation
- `docs/reference/agentos/self-improvement.md` - Evolution workflow and processes
- `docs/how-to/agentos/maintain-system.md` - System maintenance integration
- `docs/explanation/decisions/` - Decision records for significant evolutions
- `.cursor/rules/core.mdc` - Core behavioral rules that may be evolved
