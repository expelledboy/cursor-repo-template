---
title: "Inconsistent Adherence to System Schemas and Patterns"
status: superseded
superseded_by: docs/explanation/decisions/2026-01-18-schema-compliance-enforcement.md
created_date: 2026-01-18
domain: agentos
original_path: docs/work/problems/2026-01-18-inconsistent-schema-adherence.md
---

> **Status: Superseded**
> Superseded by: [Decision: Mandatory Schema Compliance Enforcement](docs/explanation/decisions/2026-01-18-schema-compliance-enforcement.md)
> Date: 2026-01-18
> Reason: Problem addressed by systemic schema compliance requirements.

# Inconsistent Adherence to System Schemas and Patterns

## Observation
The agent repeatedly fails to follow established system schemas and patterns, such as not adding required `implementations:` fields to decisions or `@directive` annotations to implementation files, despite having access to the schema documentation.

## Impact
- **Broken Traceability**: Registry validation fails, bidirectional links don't work
- **Inconsistent Documentation**: Some documents follow patterns, others don't
- **Maintenance Burden**: Human intervention needed to fix metadata gaps
- **Trust Erosion**: Users lose confidence when the system doesn't follow its own rules

## Evidence
- Decision documents missing `implementations:` fields when they should have them
- Implementation files missing `@directive` annotations pointing back to governing docs
- Frontmatter corruption from not following validation protocols
- Multiple instances of metadata loss during file operations

## Root Cause
The agent has access to schema documentation and validation tools, but doesn't consistently apply them during document creation and modification operations. This appears to be a behavioral inconsistency rather than a knowledge gap.

## Potential Solutions
1. **Mandatory Checklist**: Add a document creation checklist to core rules that must be followed before marking any document as complete
2. **Automated Validation**: Run registry validation after every document modification
3. **Template Enforcement**: Use validated templates for all document types
4. **Behavioral Reinforcement**: Add rules that prevent document completion without proper metadata