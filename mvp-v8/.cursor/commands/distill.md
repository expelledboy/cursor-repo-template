---
title: "Documentation Distillation"
description: "Semantically compress verbose documentation into concise reference material"
usage: "/distill @file"
---
# @directive docs/explanation/decisions/2026-01-18-semantic-validation-mandate.md

# Documentation Distillation Instructions

You are a **Semantic Compressor**. Your goal is to maximize the information density of documentation by removing "Scaffolding" while preserving "Structure."

When running `/distill`, analyze the input content and apply the **Scaffolding Removal Protocol** and the appropriate **Compression Strategy**.

## The Scaffolding Removal Protocol

For any provided input, apply this 4-step transformation:

### 1. Analyze Structural Weight
Identify the **Immutable Truths** in the text. These are the elements that must retain 100% fidelity:
- **Directives**: Specific commands, API endpoints, configuration values.
- **Constraints**: "MUST," "NEVER," "ALWAYS" rules.
- **Logic**: The causal link between A and B (e.g., "Use X *because* Y").
- **External References**: NEVER delete external URLs.

### 2. Remove Scaffolding
Identify and remove content that was only needed *during creation*:
- **Temporal Context**: Dates, "currently," "recently," "in the future."
- **Author Context**: "I think," "We decided," "The team found."
- **Obsolete Paths**: Alternatives that were rejected or failed attempts.
- **Narrative Glue**: Transitional phrases ("Moving on to," "As mentioned above").

### 3. Densify the Format
Rewrite the remaining truth using high-density patterns:
- Convert **Paragraphs** → **Lists** or **Tables**.
- Convert **Prose Descriptions** → **Code/Config Schemas**.
- Convert **Stories** → **Rules**.

### 4. Verify Essence
Ensure the output passes the **functional equivalence test**:
- If the original said "Do X to avoid Y," the distillation MUST NOT lose the warning about Y.
- If the original listed 3 prerequisites, the distillation MUST list 3 prerequisites.

## Diátaxis-Aware Routing

Distillation is not just deletion; it is **Partitioning**. Valuable content must be routed to its correct Diátaxis home, not destroyed.

### The "Valuable Rationale" Rule
If a document contains **Valuable Rationale** (deep architectural reasoning, trade-off analysis, complex theory) that is NOT Scaffolding:
1.  **Do NOT Delete** it.
2.  **Extract** it to a separate `docs/explanation/` document.
3.  **Link** to it from the distilled Reference/How-to document.

### Content Routing Table

| Content Type | Action | Target Bucket | Output Mode |
|--------------|--------|---------------|-------------|
| **Fact / Spec / Contract** | Distill | `docs/reference/` | Contract Mode |
| **Procedure / Workflow** | Distill | `docs/how-to/` | Imperative Mode |
| **Deep Rationale / Theory** | Extract | `docs/explanation/` | Narrative Mode (Dense) |
| **Debate / History / Draft** | Delete | `docs/archive/` | N/A |

## Compression Strategies

Select the strategy that matches the input content type and **Partition** accordingly:

### Strategy A: The Extractor (For Research/Analysis)
*Trigger*: Input contains comparisons, benchmarks, decision history, AND final specs.
*Action*:
1. **Reference**: Extract the final Decision and Configuration to `docs/reference/`.
2. **Explanation**: If reasoning is complex, extract the "Why" to `docs/explanation/` (linked from Reference).
3. **Archive**: DELETE rejected alternatives and historical debates (or move to `docs/archive/` if legally required).

### Strategy B: The Operator (For Drafts/Notes)
*Trigger*: Input contains first-person narrative ("I did this"), troubleshooting logs, or raw stream-of-consciousness (e.g., `docs/local/`).
*Action*:
1. Extract the **Procedural Steps** (Actionable commands).
2. Extract the **Gotchas** (Warnings/Errors).
3. **DELETE** the narrative journey ("First I tried X, then Y").
4. **REFORMAT** into Diátaxis "How-to" format (Prerequisites, Steps, Verification).

### Strategy C: The Cryogenics (For Architecture/Theory)
*Trigger*: Input contains high-level concepts, philosophy, or obsolete implementation details (e.g., `docs/explanation/`).
*Action*:
1. Extract the **Invariants** (Rules that must not be broken).
2. Extract the **Definitions** (Glossary terms).
3. **DELETE** implementation specifics that are subject to change (specific library versions, file paths).
4. **Consolidate** into a high-density "Reference" or "Concept" document.

## The Core Essence Test
Before finalizing any distillation, ask:
1. **Can I execute the code?** (Did I lose a required config variable?)
2. **Do I know the constraints?** (Did I lose a "NEVER do this" warning?)
3. **Is it searchable?** (Did I retain the key keywords?)

If YES to all, the distillation is valid.

## Deterministic Validation (DOE Compliance)

Distillation is an **Execution** task that must be verified against **Directives**. You MUST run the following deterministic checks before considering the task complete:

1.  **Syntax Check**: Run `just lint` to verify frontmatter and markdown syntax.
2.  **Integrity Check**: Run `just test` (or `just docs::validate`) to verify broken links and required sections.
3.  **Semantic Check**: Run enhanced validation to ensure operations are logically correct (e.g., work files not archived, proper superseded fields).
4.  **Registry Check**: Run `just docs::validate-registry` (if available) to ensure bidirectional traceability.

**CRITICAL**: Validate both **form** (syntax/schema) AND **intent** (semantic correctness). Work files contain valuable rationale - NEVER archive them as "superseded". Only archive truly obsolete canonical material.

**NEVER** skip these checks. A semantic improvement that breaks the build is a net negative.
