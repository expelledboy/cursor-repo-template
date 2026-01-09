# Content-Aware Documentation Restructuring

**Purpose**: Systematic methodology for restructuring documentation to eliminate duplication, separate concerns, and align with Diátaxis principles.

**When to use**: When documentation has grown organically and shows signs of:
- Duplication across multiple files
- Mixed concerns (facts + procedures + rationale in one file)
- Content in wrong categories (facts in explanation, procedures in reference)
- Work docs containing stable content that should be promoted
- Files that are too long or serve multiple purposes

**Prerequisites**:
- Understanding of Diátaxis framework (reference, how-to, explanation, tutorials, work, archive)
- Familiarity with the documentation system's authority order
- Understanding of context efficiency principles (tutorials are ignored during execution tasks)
- Access to all documentation files

---

## Overview

This process involves systematically analyzing all documentation files to identify restructuring opportunities, then executing changes in prioritized phases. The goal is to create a maintainable documentation structure where:

- **Reference** = Stable facts, contracts, configurations (single source of truth)
- **How-to** = Step-by-step procedures, runbooks (task-oriented, high signal for execution)
- **Explanation** = Rationale, architecture, mental models (understanding-oriented)
- **Tutorials** = Learning-oriented lessons (lowest authority; high token cost; ignored during execution tasks)
- **Work** = Drafts, research, verification notes (with Status/Date)
- **Archive** = Superseded content (with banners)

---

## Phase 0: Preparation

### 1. Create a Migration Tracker

Create a tracking document (e.g., `docs/work/plans/YYYY-MM-DD-doc-restructuring.md`) with:

- **Status tracking table**: One row per file with columns: Doc name, Current path, Intended home, Action, Notes, Status
- **Process notes**: Document decisions, questions, and findings
- **Summary section**: Track progress and key findings

### 2. Inventory All Files

```bash
find docs -name "*.md" -type f | sort > doc-inventory.txt
```

Count total files and verify you have the complete set. This ensures nothing is missed.

### 3. Define Scope and Priorities

- **Identify domains**: Group files by topic (auth/SSO, deployment, testing, UI, etc.)
- **Set priorities**: Which domains have the most duplication or issues?
- **Note constraints**: Any recent code changes that might invalidate docs?

---

## Phase 1: Discovery and Pattern Recognition

### Step 1.1: Read Files in Domain Batches

**Strategy**: Process 3-5 related files at a time to stay within context limits.

**For each batch:**
1. Read all files in the batch completely (not summaries)
2. Identify the primary intent of each file (reference, how-to, explanation, tutorials, work)
3. Note what each file does well vs. what needs improvement
4. Look for obvious overlaps or duplication

**What to look for:**
- **Duplication**: Same content in multiple files
- **Mixed concerns**: Facts + procedures + rationale in one file
- **Wrong category**: Facts in explanation docs, procedures in reference docs, learning content in how-to
- **Tutorials vs How-to confusion**: Learning-oriented content in how-to (should be tutorials), or task-oriented content in tutorials (should be how-to)
- **Work docs with stable content**: Verified facts that should be promoted
- **Size/complexity**: Very long files that mix multiple concerns

### Step 1.2: Build Mental Models

For each domain, create a mental model:
- What are the key concepts?
- What are the canonical sources of truth?
- What are the procedures?
- What is the rationale/architecture?

This helps identify where content should live.

### Step 1.3: Identify Patterns

**Common patterns to recognize:**

1. **Duplication patterns**:
   - Same config tables in multiple files
   - Same flow descriptions in multiple files
   - Same env var lists in multiple files

2. **Mixed concern patterns**:
   - Long how-to docs that include reference material
   - Reference docs that include step-by-step procedures
   - Explanation docs that include factual tables
   - Tutorials content in how-to docs (learning vs task-oriented)
   - How-to content in tutorials (task-oriented vs learning-oriented)

3. **Promotion patterns**:
   - Work docs with "verified facts" sections
   - Work docs with stable content and Status: Draft
   - Research docs with confirmed findings

4. **Tutorials patterns**:
   - Learning-oriented content in how-to docs (should be tutorials)
   - Task-oriented content in tutorials (should be how-to)
   - Onboarding guides in wrong category
   - Content that mixes learning with task execution

5. **Structural patterns**:
   - Files that are too long (>500 lines often indicates mixed concerns)
   - Files that serve multiple audiences
   - Files that are hard to navigate

---

## Phase 2: Deep Analysis

### Step 2.1: Compare Related Files Side-by-Side

**For files that might overlap:**

1. Read both files completely
2. Identify specific sections that overlap (note line numbers)
3. Identify unique content in each file
4. Identify gaps (content in one but not the other)
5. Identify conflicts (contradictory information)

**Example comparison:**
```
File A (saml-config-and-claim-mapping.md):
  - Lines 24-31: Entra app settings
  - Lines 10-22: Env vars table
  - Lines 33-39: Claim/role mapping

File B (sso.md):
  - Lines 5-20: Entra app settings (overlaps with A:24-31)
  - Lines 27-40: Env vars code block (overlaps with A:10-22)
  - Lines 22-25: File locations (unique to B)

Decision: Merge A + B → new saml-config.md, use A as base, add file locations from B
```

### Step 2.2: Apply Decision Framework

**For each overlap/issue, ask:**

1. **What is the intent?**
   - Fact → Reference
   - Procedure (task-oriented) → How-to
   - Learning/onboarding (study-oriented) → Tutorials
   - Rationale → Explanation
   - Draft/Research → Work

2. **Where should it live?**
   - Use Diátaxis framework
   - Consider authority order (reference > how-to > explanation > tutorials > work)
   - Consider context efficiency (tutorials ignored during execution tasks)
   - Consider discoverability (where would someone look for this?)
   - **Tutorials vs How-to**: Is this for learning/onboarding (tutorials) or task execution (how-to)?

3. **Which file is the better base?**
   - More complete/authoritative
   - Better structure
   - More recent/accurate
   - Better maintained

4. **What should be kept/removed/merged?**
   - Keep: Unique valuable content
   - Remove: Duplicates, outdated content
   - Merge: Complementary content

5. **Are there dependencies?**
   - Links that need updating
   - Cross-references
   - Other docs that reference this

### Step 2.3: Document Specific Findings

**For each file, document:**

- **Current state**: What it contains, what it does well
- **Issues**: Duplication, mixed concerns, wrong category
- **Proposed changes**: Merge, split, extract, promote, etc.
- **Specific details**: Line numbers, section names, content examples
- **Dependencies**: Links, cross-references, related files

**Example documentation:**
```
File: saml-config-and-claim-mapping.md
Current: Reference doc with env vars, Entra settings, claim mapping
Issues:
  - Entra settings duplicated in sso.md (lines 24-31 vs sso.md:5-20)
  - Env vars table duplicated in env-setup.md
Proposed: Merge with sso.md → saml-config.md, use as base, add file locations from sso.md
Dependencies: Referenced by saml-local-testing.md, security-model.md
```

---

## Phase 3: Decision Making

### Heuristics for Common Decisions

#### When Merging Files

**Decision criteria:**
- Both files cover the same topic
- Significant overlap (>30% similar content)
- One file is clearly more authoritative
- Merging reduces maintenance burden

**Process:**
1. Choose the better base file (more complete, better structure)
2. Identify unique content in the other file
3. Merge unique content into base
4. Update all references
5. Archive or delete the other file

#### When Splitting Files

**Decision criteria:**
- File is very long (>500 lines often indicates mixed concerns)
- File serves multiple purposes (facts + procedures + rationale)
- File serves multiple audiences
- Different sections have different update frequencies

**Process:**
1. Identify distinct concerns (facts, procedures, rationale)
2. Create new files for each concern
3. Extract content to appropriate files
4. Update original file or replace with links
5. Update all references

#### When Extracting Content

**Decision criteria:**
- Content is in the wrong category (facts in explanation, procedures in reference)
- Content is stable and should be promoted (work → reference)
- Content is duplicated and should be centralized

**Process:**
1. Identify the target location (reference, how-to, explanation, tutorials)
2. Extract content to new or existing file
3. Replace original with link or summary
4. Update all references

#### When Promoting Content

**Decision criteria:**
- Content is verified (not speculative)
- Content is stable (won't change frequently)
- Content is referenced elsewhere (used as source of truth)
- Content belongs in a canonical location

**Process:**
1. Verify content is accurate and stable
2. Move to appropriate canonical location
3. Update work doc with superseded banner or delete
4. Update all references

#### When Distinguishing Tutorials from How-to

**Decision criteria:**
- **Tutorials** = Learning-oriented, onboarding, "study" mode
  - Teaches concepts while doing
  - Guides someone new to the system
  - Focuses on understanding and building mental models
  - May include background context and "why" explanations
  - Agents ignore during execution tasks (context efficiency)
- **How-to** = Task-oriented, execution-focused, "work" mode
  - Provides steps to complete a specific task
  - Assumes familiarity with the system
  - Focuses on getting work done efficiently
  - Minimal background, maximum actionability
  - Agents load during coding/debugging (high signal)

**Process:**
1. Identify the primary intent (learning vs task execution)
2. Consider the audience (newcomer vs experienced user)
3. Consider context efficiency (will agents need this during execution?)
4. Move content to appropriate category
5. Update all references

### Quality Checks

**Before finalizing decisions, verify:**

- ✅ All files have been reviewed
- ✅ No assumptions made without reading files completely
- ✅ Specific evidence cited (line numbers, section names)
- ✅ Decisions align with Diátaxis principles
- ✅ Authority order is respected (reference > how-to > explanation > tutorials > work)
- ✅ Tutorials vs How-to distinction is clear (learning vs task-oriented)
- ✅ Context efficiency implications considered (tutorials ignored during execution)
- ✅ Dependencies are identified and will be updated

---

## Phase 4: Planning and Prioritization

### Step 4.1: Group Changes by Impact

**High impact (do first):**
- Eliminates significant duplication
- Fixes major structural issues
- Creates single sources of truth

**Medium impact:**
- Improves organization
- Separates concerns
- Makes content more discoverable

**Low impact:**
- Polish and cleanup
- Minor reorganizations
- Link updates

### Step 4.2: Create Implementation Phases

**Phase 1: Highest Priority**
- Most duplication
- Most structural issues
- Highest maintenance burden

**Phase 2: High Priority**
- Significant improvements
- Clear benefits
- Manageable scope

**Phase 3: Medium Priority**
- Good improvements
- Lower urgency
- Can be done incrementally

**Phase 4: Cleanup**
- Polish and refinement
- Link updates
- Final verification

### Step 4.3: Document the Plan

**For each phase, document:**

- **Scope**: Which files/domains
- **Changes**: Specific merges, splits, extractions
- **Dependencies**: What needs to happen first
- **Success criteria**: How to know it's complete
- **Estimated effort**: Rough time/complexity

---

## Phase 5: Execution

### Step 5.1: Execute Changes in Phases

**For each phase:**

1. **Prepare**: Review the plan, gather all files that will be changed
2. **Execute**: Make the changes (merges, splits, extractions)
3. **Update references**: Fix all links and cross-references
4. **Verify**: Check that changes are correct and complete
5. **Update tracker**: Mark files as done, note any issues

### Step 5.2: Update Documentation

**After each change:**

1. **Update docs/index.md**: Add/remove entries as needed
2. **Update cross-references**: Fix links in all affected files
3. **Add superseded banners**: For archived files
4. **Update work docs**: Add Status/Date if needed

### Step 5.3: Verify Quality

**Checklist:**

- ✅ No broken links
- ✅ All references updated
- ✅ Naming conventions followed (kebab-case, dates)
- ✅ Status fields present in work docs
- ✅ Superseded banners in archive files
- ✅ Authority order respected
- ✅ Single sources of truth established

---

## Phase 6: Verification and Completion

### Step 6.1: Final Review

**Review the restructured documentation:**

1. **Completeness**: All files reviewed and processed
2. **Accuracy**: Content matches codebase (for authoritative docs)
3. **Structure**: Files in correct categories
4. **Links**: All links work and point to correct locations
5. **Consistency**: Naming, formatting, structure consistent

### Step 6.2: Update Migration Tracker

**Finalize the tracker:**

- Mark all files as "done"
- Document any decisions or exceptions
- Note any remaining issues or future work
- Create summary of changes

### Step 6.3: Document Lessons Learned

**Capture for future:**

- What worked well?
- What was challenging?
- What would you do differently?
- What patterns emerged?
- What heuristics were most useful?

---

## Mental Models and Frameworks

### Diátaxis Framework

**Use as a lens for categorization:**

- **Reference** = "What is" (facts, contracts, invariants, configurations)
- **How-to** = "How to do" (procedures, steps, runbooks, troubleshooting; task-oriented, high signal for execution)
- **Explanation** = "Why/how it works" (rationale, architecture, mental models)
- **Tutorials** = "Learn by doing" (guided lessons; lowest authority; high token cost; ignored during execution tasks)
- **Work** = "Drafts and research" (temporary, with Status/Date)
- **Archive** = "Superseded" (with banners, historical record)

**Key distinction: Tutorials vs How-to**
- **Tutorials**: Learning-oriented, onboarding, "study" mode. Agents ignore during execution tasks.
- **How-to**: Task-oriented, execution-focused, "work" mode. Agents load during coding/debugging.
- If content teaches concepts while doing → Tutorials
- If content provides steps to complete a task → How-to

### Authority Hierarchy

**Use to resolve conflicts:**

```
reference → how-to → explanation → tutorials → work → archive
```

When docs disagree, the higher authority wins. Use this to decide what to promote and what to archive.

### Single Source of Truth

**Principle**: One canonical location per fact.

- Avoid duplication
- When duplicates exist, merge into most authoritative location
- Link from other locations rather than copy
- Update one place, not many

---

## Common Patterns and Red Flags

### Duplication Patterns

- Same config tables in multiple files
- Same flow descriptions in multiple files
- Same env var lists in multiple files
- Same troubleshooting steps in multiple files

### Mixed Concern Patterns

- Long how-to docs that include reference material
- Reference docs that include step-by-step procedures
- Explanation docs that include factual tables
- Tutorials content in how-to docs (learning-oriented content in task-oriented docs)
- How-to content in tutorials (task-oriented content in learning-oriented docs)
- Work docs with stable content that should be promoted

### Structural Issues

- Files >500 lines (often indicates mixed concerns)
- Files that serve multiple audiences
- Files that are hard to navigate
- Files with unclear purpose

### Quality Issues

- Content that doesn't match codebase (for authoritative docs)
- Missing links or broken references
- Outdated information
- Unclear structure or organization

---

## Decision Heuristics

### When to Merge

- Both files cover the same topic
- Significant overlap (>30% similar content)
- One file is clearly more authoritative
- Merging reduces maintenance burden

### When to Split

- File is very long (>500 lines)
- File serves multiple purposes
- File serves multiple audiences
- Different sections have different update frequencies

### When to Extract

- Content is in the wrong category (e.g., learning content in how-to, task content in tutorials)
- Content is stable and should be promoted
- Content is duplicated and should be centralized

### When to Promote

- Content is verified (not speculative)
- Content is stable (won't change frequently)
- Content is referenced elsewhere
- Content belongs in a canonical location

---

## Tips and Best Practices

### Reading Strategy

- **Read entire files**, not summaries
- **Look for structure**, not just content
- **Note what each section does** (fact, procedure, learning lesson, rationale)
- **Distinguish tutorials from how-to**: Is this for learning/onboarding (tutorials) or task execution (how-to)?
- **Track where information appears** multiple times

### Comparison Strategy

- **Side-by-side comparison** of related files
- **Identify unique vs shared** content
- **Find gaps** (content in one but not the other)
- **Find conflicts** (contradictory information)

### Documentation Strategy

- **Use a tracker** to record findings
- **Add detailed analysis** sections with specific examples
- **Document decisions** with rationale
- **Include line numbers** for precise targeting
- **Note files that are fine** as-is

### Quality Strategy

- **Verify against codebase** when docs claim authority
- **Check all links** after changes
- **Maintain consistency** with naming conventions
- **Respect authority order** in all decisions

---

## Troubleshooting

### What if files are too large to read?

- Read in sections, focusing on structure first
- Use grep/search to find specific content
- Read summaries/headings to understand organization
- Prioritize files with obvious issues

### What if there are conflicting decisions?

- Apply authority order (reference > how-to > explanation > tutorials > work)
- Use the more authoritative source
- Verify against codebase when possible
- Document the decision and rationale

### What if content doesn't fit neatly into categories?

- Consider the primary intent (what is the main purpose?)
- Consider the audience (who needs this information?)
- Consider the update frequency (how often does this change?)
- When in doubt, ask for clarification

### What if the process is taking too long?

- Focus on high-impact changes first
- Process in smaller batches
- Defer low-priority changes
- Document remaining work for future

---

## Success Criteria

**The restructuring is complete when:**

- ✅ All files have been reviewed
- ✅ Duplication eliminated or minimized
- ✅ Concerns separated (facts, procedures, learning lessons, rationale)
- ✅ Content in correct categories (tutorials vs how-to distinction clear)
- ✅ Single sources of truth established
- ✅ Context efficiency respected (tutorials properly isolated from execution tasks)
- ✅ All links and references updated
- ✅ Naming conventions followed
- ✅ Authority order respected
- ✅ Documentation is maintainable

---

## Related Documentation

- **Doc system rationale**: `docs/explanation/architecture/doc-system-rationale.md`
- **Doc map**: `docs/index.md`
- **Agent guide**: `AGENTS.md` (for authority order and conventions)

---

**Last Updated**: 2026-01-09
**Status**: Current
**Maintained by**: Documentation team
