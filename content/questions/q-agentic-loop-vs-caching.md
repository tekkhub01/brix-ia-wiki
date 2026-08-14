---
title: "Does Agentic RAG's iterative loop defeat prefix caching, or do cache reads offset the 3-5x cost?"
kind: question
status: proposed
priority: p1
created: 2026-08-14
updated: 2026-08-14
last_checked: 2026-08-14
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

## Next Action

Resolve by ingesting the linked candidate, or mark superseded if answered elsewhere.
