---
title: "AI Semantic Restructuring Guide"
status: stable
created_date: 2026-01-17
purpose: "Guide for AI agents performing semantic documentation restructuring"
domain: agentos
---

# AI Semantic Restructuring Guide

## Overview

This guide enables AI agents to perform intelligent semantic documentation restructuring using existing tools and chat-based interaction. When users invoke `/refine`, follow this guide to provide semantic comprehension, detailed analysis, and interactive restructuring.

## Core Principles

### Semantic Comprehension First
- **Analyze meaning, not just text**: Understand what documentation *means* and how concepts relate
- **Diátaxis awareness**: Recognize Reference/How-to/Explanation/Tutorial buckets and user intents
- **Relationship mapping**: Identify how content pieces connect conceptually
- **Context sensitivity**: Consider the broader documentation ecosystem

### Chat-Based Interactive Workflow
- **User approval required**: Present suggestions, wait for explicit approval/rejection/modification
- **Conversation continuity**: Use chat history to maintain context across batches
- **Transparent reasoning**: Explain analysis methodology and decision rationale
- **Educational value**: Help users understand documentation principles

### Existing Tools Only
- **No new scripts**: Rely solely on existing `just docs::*` commands
- **Deterministic operations**: Use tools for file operations, AI for intelligence
- **Tool composition**: Combine existing commands creatively for new workflows

### Context and Performance Awareness
- **10K token limit**: Respect LLM context windows in batch sizing
- **Semantic batching**: Group conceptually related content, not just files
- **Progressive disclosure**: Show analysis results incrementally
- **Performance optimization**: Minimize redundant operations

## Complete Process Workflow

### Phase 1: Initialization and Inventory
```
User Input: /refine
AI Action: Start semantic restructuring session

1. Generate comprehensive inventory
   Command: just docs-inventory
   Purpose: Get complete file list with basic metadata

2. Perform semantic preprocessing
   - Read frontmatter to understand Diátaxis classification
   - Extract key concepts from titles and content
   - Identify obvious cross-references and relationships
   - Flag potential Diátaxis misalignments

3. Report initial findings
   "Starting semantic documentation restructuring...
    Found X files across Y domains. Initial analysis shows Z potential opportunities."
```

### Phase 2: Intelligent Batching
```
AI Action: Create semantically coherent batches

1. Analyze content relationships
   - Group files discussing related concepts
   - Respect Diátaxis bucket boundaries unless realignment needed
   - Consider file sizes to stay within 10K token limits
   - Preserve dependency chains

2. Create deterministic batches
   Command: just docs-create-batch "semantic-batch-01" "file1.md file2.md file3.md"
   Purpose: Use existing tool for batch creation and tracking

3. Report batching strategy
   "Created X intelligent batches based on semantic relationships:
    - Batch 1: Core concepts (8 files, 9.2K tokens)
    - Batch 2: Advanced workflows (6 files, 8.7K tokens)
    - ..."
```

### Phase 3: Deep Semantic Analysis (Per Batch)
```
AI Action: Comprehensive analysis of each batch

For each batch:
1. Load batch content
   - Read all files in batch
   - Follow explicit cross-references to related content
   - Stay within context limits

2. Perform semantic analysis
   - Content comprehension: What does each piece explain?
   - Relationship mapping: How do concepts connect?
   - Diátaxis evaluation: Does content match intended user intent?
   - Gap identification: What's missing or incomplete?
   - Redundancy assessment: Semantic overlap vs. meaningful repetition

3. Generate restructuring suggestions
   - Consolidation opportunities
   - Diátaxis realignments
   - Gap-filling recommendations
   - Link optimization improvements

4. Validate suggestions
   - Ensure semantic meaning preservation
   - Check link integrity impact
   - Assess user experience implications
   - Verify Diátaxis compliance
```

### Phase 4: Interactive Review Presentation
```
AI Action: Present comprehensive suggestions for user review

Format each suggestion with:
1. Clear title and type
2. Detailed rationale explaining analysis
3. Specific impact assessment
4. Concrete implementation description
5. Before/after conceptual overview

Example presentation:
"## 📋 Batch Analysis: Core Concepts (8 files, 9.2K tokens)

### Semantic Findings
- 3 files explain 'decision trees' with 78% conceptual overlap
- Implementation details misplaced in Reference bucket
- Missing explanation of 'cognitive limits' concept
- Cross-references could be optimized for better flow

### Detailed Suggestions

#### 1. **Consolidate Decision Tree Explanations**
**Type**: Content Consolidation
**Rationale**: Files A, B, and C all explain decision tree concepts with significant overlap. File A provides the most comprehensive explanation with clearest examples. The variations in B and C add minimal value while increasing maintenance overhead.

**Semantic Analysis**:
- All three cover core decision tree structure
- File A includes practical examples, File B focuses on theory, File C has implementation details
- Users would benefit from single authoritative source with cross-references to specialized content

**Impact Assessment**:
- Reduces maintenance from 3 locations to 1
- Improves user discovery of comprehensive information
- Eliminates confusion from conflicting explanations
- Requires updating 4 inbound references

**Implementation**:
- Keep canonical explanation in `docs/explanation/decisions/restructuring-process-design.md`
- Move specialized content to separate focused files
- Add summary cross-references from consolidated location
- Update all inbound links automatically

#### 2. **Realign Diátaxis Buckets**
**Type**: Structural Reorganization
**Rationale**: Implementation details in Reference bucket violate Diátaxis principles. Reference should contain stable facts, not procedural implementation guidance.

**Semantic Analysis**:
- Reference bucket currently contains 'how to implement' content
- Users seeking authoritative facts get mixed with procedural content
- Clear separation needed for different user intents

**Impact Assessment**:
- Better information architecture for different user needs
- Improved maintenance (procedural content changes more frequently)
- Enhanced user experience for both learning and reference use cases

**Implementation**:
- Move implementation sections to `docs/how-to/` bucket
- Create proper Reference entries with links to How-to content
- Update authority order references

#### 3. **Fill Cognitive Limits Gap**
**Type**: Content Completion
**Rationale**: Multiple files reference 'cognitive limits' concept but none provide comprehensive explanation, leaving users without critical context.

**Semantic Analysis**:
- Concept appears in batching, analysis, and validation contexts
- Referenced as constraint but not explained as design principle
- Users need understanding to appreciate system design decisions

**Impact Assessment**:
- Completes user understanding of system constraints
- Provides context for design decisions
- Reduces support questions about 'why these limits'

**Implementation**:
- Create comprehensive explanation in appropriate bucket
- Add cross-references from all mentioning locations
- Include practical examples of limit impacts

### Review Request
Please review each suggestion above. For each one, indicate:
- **Approve**: Apply as described
- **Reject**: Do not implement
- **Modify**: Specify changes needed

Example: 'Approve 1, Modify 2 (move to different bucket), Reject 3'

Ready for your feedback on these suggestions."
```

### Phase 5: User Interaction Handling
```
AI Action: Process user feedback and prepare for application

1. Parse user response
   - Identify approved suggestions
   - Note modifications requested
   - Record rejections with reasoning if provided

2. Handle modifications
   - Clarify ambiguous requests
   - Validate modification feasibility
   - Update suggestion details based on user input

3. Confirm understanding
   "Understood. Applying:
   - Suggestion 1 as described
   - Suggestion 2 with modifications: [details]
   - Skipping suggestion 3 as requested

   Ready to proceed with implementation?"
```

### Phase 6: Batch Application and Validation
```
AI Action: Apply approved changes systematically

For each approved suggestion:
1. Execute implementation plan
   - Apply content changes
   - Update cross-references
   - Move files if needed

2. Use existing tools for deterministic operations
   Command: just docs-validate-batch "batch-name"
   Purpose: Ensure batch integrity maintained

3. Provide detailed feedback
   "✅ Applied suggestion 1: Consolidated decision tree content
   - Moved canonical explanation to restructuring-process-design.md
   - Updated 4 inbound references
   - Added cross-references to specialized content

   ✅ Applied suggestion 2: Realigned Diátaxis buckets
   - Moved implementation sections to how-to/ bucket
   - Created proper reference entries with links
   - Updated authority order references

   ⚠️ Suggestion 3 skipped as requested

   Batch complete. Moving to next batch..."

4. Validate overall changes
   - Check link integrity across documentation
   - Verify Diátaxis compliance maintained
   - Confirm Cursor integrations unaffected
```

### Phase 7: Session Completion
```
AI Action: Finalize restructuring session

1. Process all batches
2. Provide comprehensive summary
   "Semantic restructuring complete!

   Summary:
   - Processed X batches with Y total files
   - Applied Z suggestions across W files
   - Updated V cross-references
   - Improved Diátaxis compliance by P%
   - Reduced content redundancy by Q%

   All changes validated for link integrity and semantic preservation."

3. Cleanup artifacts
   Command: just docs-cleanup-all
   Purpose: Remove temporary batch files and state tracking
```

## Analysis Techniques

### Content Comprehension Methods

#### Frontmatter Analysis
- **Diátaxis Classification**: Map declared purpose to actual content
- **Domain Assessment**: Verify content belongs in declared domain
- **Status Evaluation**: Consider stability requirements
- **Relationship Mapping**: Use related/depends fields for context

#### Semantic Content Analysis
- **Concept Extraction**: Identify key terms and their explanations
- **Intent Classification**: Determine Reference/How-to/Explanation/Tutorial fit
- **Dependency Mapping**: Find prerequisite knowledge requirements
- **Gap Detection**: Identify missing explanations or incomplete processes

#### Cross-Reference Analysis
- **Inbound Links**: What content points to this?
- **Outbound Links**: What does this content reference?
- **Link Quality**: Are references appropriate and current?
- **Navigation Flow**: Does linking support user journeys?

### Suggestion Generation Framework

#### Consolidation Opportunities
- **Semantic Overlap**: >70% conceptual similarity with different clarity levels
- **Maintenance Burden**: Multiple locations requiring updates
- **User Confusion**: Conflicting or incomplete explanations
- **Authority Clarity**: One definitive source vs. distributed information

#### Structural Improvements
- **Diátaxis Misalignment**: Content not matching declared user intent
- **Domain Boundaries**: Content scattered across inappropriate domains
- **Hierarchy Issues**: Missing intermediate explanations
- **Navigation Problems**: Poor information flow between related topics

#### Content Completion
- **Process Gaps**: Referenced workflows without documentation
- **Concept Dependencies**: Prerequisites not explained
- **Example Shortages**: Theoretical content without practical application
- **Context Missing**: Background information required for understanding

## Communication Excellence

### Analysis Transparency
- **Methodology Explanation**: "I analyzed this by examining concept relationships..."
- **Evidence Presentation**: "Found this pattern in 3 files with these specific overlaps..."
- **Assumption Surfacing**: "This assumes users need X before understanding Y..."
- **Confidence Levels**: "High confidence this improves user experience because..."

### User-Centric Presentation
- **Progressive Detail**: Summary first, specifics on request
- **Actionable Format**: Clear approve/reject/modify options
- **Context Preservation**: Reference previous decisions and patterns
- **Educational Value**: Explain documentation principles as you work

### Error Prevention and Recovery
- **Validation Checks**: Confirm understanding before major changes
- **Rollback Options**: Clear paths to undo changes if needed
- **Impact Assessment**: Pre-change evaluation of consequences
- **Safety Nets**: Conservative approach with user confirmation

## Quality Assurance Standards

### Semantic Preservation
- **Meaning Integrity**: Changes don't alter intended meaning
- **Context Maintenance**: Surrounding information remains coherent
- **User Journey Continuity**: Learning paths remain intact
- **Authority Consistency**: Reference sources remain authoritative

### Technical Correctness
- **Link Resolution**: All references work after changes
- **Frontmatter Validity**: Schema compliance maintained
- **File System Integrity**: No broken paths or missing files
- **Tool Compatibility**: Existing commands continue working

### User Experience Quality
- **Discoverability**: Information remains findable
- **Comprehensibility**: Content clarity maintained or improved
- **Accessibility**: Different user intents still supported
- **Maintenance**: Future updates simplified

## Tool Integration Patterns

### Creative Use of Existing Tools
- **Inventory Analysis**: Use `just docs-inventory` output for semantic preprocessing
- **Batch State Tracking**: Use `just docs-state` for progress communication
- **Validation Integration**: Leverage `just docs-validate-batch` for change verification
- **Cleanup Coordination**: Use `just docs-cleanup-batch` for artifact management

### Chat-Based Enhancements
- **Context Accumulation**: Build understanding across batch processing
- **Decision Memory**: Reference previous approvals in new suggestions
- **Pattern Recognition**: Learn from user preferences and modify approach
- **State Preservation**: Use conversation history for session continuity

This guide serves as the comprehensive reference for AI agents performing semantic documentation restructuring. By following these principles and processes, AI agents can provide intelligent, user-approved documentation improvements using only existing tools and chat-based interaction.