---
title: "Documentation Migration Guide"
status: stable
created_date: 2026-01-16
purpose: "Guide for migrating content between Diátaxis buckets and development tiers"
domain: docs
---

# Documentation Migration Guide

## Overview
Content flows between Diátaxis buckets (authoritative docs) and Development tiers (lifecycle management) as it evolves.

## Diátaxis Buckets (Authoritative)
- **reference**: Stable facts, schemas, contracts
- **how-to**: Procedures and runbooks
- **explanation**: Rationale and design decisions
- **tutorial**: Learning guides
- **work**: Draft canonical content
- **archive**: Superseded canonical content

## Development Tiers (Lifecycle)
- **work**: Valuable research and reusable knowledge
- **local**: Temporary development files (not committed)
- **archive**: Historical working content

## Migration Paths

### From Development to Diátaxis
```
Development Work → Diátaxis Work → Diátaxis Reference
    ↓              ↓              ↓
Valuable Research → Draft Canonical → Authoritative Facts
```

### Local Content Handling
```
Development Local → Discard or Promote to Work
    ↓                      ↓
Temporary Files → Valuable Research (if applicable)
```

### Archive Management
```
Diátaxis Archive → Development Archive
    ↓                      ↓
Superseded Canonical → Historical Working Content
```

## Decision Points
- **Promote to Diátaxis**: When content becomes generally useful and stable
- **Keep in Development**: When content is project-specific or evolving
- **Archive**: When content is no longer current but historically valuable
- **Discard**: When content has no future value

## Examples
- Research findings → Diátaxis explanation (design rationale)
- Implementation guides → Diátaxis how-to (procedures)

## External Knowledge Migration

### From Internal-Only to External-Integrated
- Identify reasoning gaps that could benefit from external knowledge
- Add external source anchors to existing decision flows
- Configure Context7 integration for reference documentation
- Update trace recording to capture external evidence

### External Source Classification
- Reference docs: API specs, technical specifications
- How-to: Guides, tutorials, implementation examples
- Explanation: Design docs, rationale, architectural discussions
- Tutorial: Learning materials, getting started guides
- Experimental results → Development work (research)
- Temporary notes → Development local (discard after use)