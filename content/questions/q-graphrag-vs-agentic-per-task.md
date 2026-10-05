---
title: "What does the GraphRAG-vs-agentic-search benchmark conclude, task by task?"
kind: question
status: answered
priority: p0
created: 2026-08-14
updated: 2026-09-13
answered: 2026-09-13
last_checked: 2026-09-13
tags: [question, gap, llm-memory]
summary: "Posed as open in rag.md and graphrag.md, but the cited paper already has an answer the corpus does not report."
confidence: high
origin: "2026-08-12 speculation pass; persisted 2026-08-14"
publish: true
---

# What does the GraphRAG-vs-agentic-search benchmark conclude, task by task?

## Why Track This

Posed as open in [rag](../concepts/rag.md) and [graphrag](../concepts/graphrag.md), but the cited paper already has an answer the corpus does not report.

## Current State

**Answered 2026-09-13** by the ingest of [do-we-still-need-graphrag](do-we-still-need-graphrag.md). Per-task conclusions now in the vault (source §Observations 1–3 and Conclusions): agentic search narrows but does not close the dense→GraphRAG gap on multi-hop (+27.23 → +26.59 averaged under GraphSearch); GraphRAG stays strongest/most stable on complex multi-hop when its offline cost is amortized; dense RAG remains competitive on general QA; RL-trained agents beat their own training-free baselines but not strong training-free agentic pipelines (GraphSearch).
