# Registry Specification (Reference)

**Status**: Stable
**Date**: 2026-01-13
**Purpose**: Defines the doc <-> code mapping protocol used to prevent drift.

---

## 1. Goal
Ensure every in-scope implementation file can be traced to its directive, and every directive can be traced to its implementation.

## 2. Strategy (default)
- **Default strategy**: Bidirectional annotations in code and docs.
- Alternative strategies are allowed only with an ADR and updated validation rules.

## 3. Annotation format (default)
### 3.1 In code
```
@directive <doc-path>
@domain <domain-name> (optional)
```

### 3.2 In docs
```
@implementation <src-path>
```

## 4. Scope
- The in-scope paths are repo-specific and must be documented in `AGENTS.md` under **Registry Scope**.
- The default scope includes source, tests, scripts, and config; excludes generated output and vendor paths.
- Local state under `docs/local/**` is out of scope and must not be mapped.

## 5. Validation rules
- **Completeness**: every in-scope file has at least one directive or implementation link.
- **Bidirectional**: each directive reference has a matching implementation reference and vice versa.
- **Path validity**: all referenced paths exist.

## 6. Enforcement
- A deterministic validation command must exist and be documented.
- Validation should run via the repo task runner when available.
- If the repo uses `just`, the default command is `just agentos::validate-registry`.
- If enforcement is not yet available, capture the gap in `docs/work/**` and link it to the problem registry.
- The default implementation is `scripts/agentos/validate_registry.py`.

## 7. Related docs
- `docs/how-to/agentos/maintain-registry.md`
