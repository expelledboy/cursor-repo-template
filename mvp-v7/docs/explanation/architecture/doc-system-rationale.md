# Documentation system rationale (v7)

Status: Draft
Date: 2026-01-15
Purpose: Preserve the “why” behind Hybrid Diátaxis + Domain for this fork.

## Goals
- Minimize context load while keeping sources of truth obvious.
- Separate content intents (facts vs procedures vs rationale vs drafts).
- Make Cursor agents reliable via rules that route to the smallest authoritative set.

## Design choices
- **Hybrid Diátaxis + Domain**: use Diátaxis buckets (reference/how-to/explanation/tutorials/work/archive) and domain folders inside each bucket.
- **Doc map first**: `docs/index.md` is the lightweight entrypoint.
- **Routing layer**: `.cursor/rules/*.mdc` narrows what gets loaded.
- **Work vs truth**: drafts go to `docs/work/**`; stable outcomes get promoted into reference/how-to/explanation.

## Authority order
reference → how-to → explanation → tutorials → work → archive

## When to update
Update this rationale if we change doc buckets, authority order, or routing mechanisms.

