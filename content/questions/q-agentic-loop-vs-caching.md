---
title: "Does Agentic RAG's iterative loop defeat prefix caching, or do cache reads offset the 3-5x cost?"
kind: question
status: partially-answered
priority: p1
created: 2026-08-14
updated: 2026-10-18
last_checked: 2026-10-18
tags: [question, gap, llm-memory]
summary: "agentic-rag.md and context-caching.md never reference each other on this, despite the invalidation hierarchy being directly relevant."
confidence: high
origin: "2026-08-12 speculation pass; persisted 2026-08-14"
publish: true
---

# Does Agentic RAG's iterative loop defeat prefix caching, or do cache reads offset the 3-5x cost?

## Why Track This

[agentic-rag](../concepts/agentic-rag.md) and [context-caching](../concepts/context-caching.md) never reference each other on this, despite the invalidation hierarchy being directly relevant.

## Current State

Answerable either by a paper costing agentic-loop caching, or by doing the arithmetic across both existing articles. Also listed as an Open Thread.

## Resolution (sweep 2026-10-18) — partially-answered by arithmetic across the two pages

The answer splits on one design choice, and both pages in the vault already
contain the pieces:

- **Append-style loop** (retrieval results added as new messages): the prefix
  never changes, so per the invalidation hierarchy in
  [context-caching](../concepts/context-caching.md) the tools+system
  cache survives every round; each round pays one cache *write* for the new
  spans and reads everything before it at ~0.1×. The 3–5× figure in
  [agentic-rag](../concepts/agentic-rag.md) is then mostly extra
  generated/processed tokens, not lost cache — and cache reads offset a real
  part of it.
- **Rebuild-style loop** (prompt re-assembled with different retrieved
  passages each round): the messages prefix changes every iteration → full
  invalidation at or after the first changed byte. There the 3–5× is paid
  with cache writes that are never read — the "silent invalidator" pattern.

So the loop does not *inherently* defeat prefix caching; the prompt-rebuild
implementation does. What remains genuinely open is the empirical split: how
much of the measured 3–5× is which mode in real 2026 stacks, and whether
retrieval-result reordering inside tool messages (append-with-mutation) counts
as a prefix change in practice. No external source found that measures this.

## Next Action

If ever worth measuring: one agentic-RAG run logged with
`cache_read_input_tokens` per round, append vs rebuild. Otherwise the
mechanism question is closed and the remainder is an implementation survey.
