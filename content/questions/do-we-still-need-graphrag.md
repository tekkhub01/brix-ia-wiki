---
title: "Do We Still Need GraphRAG? (arXiv 2604.09666)"
kind: ingest-candidate
status: ingested
priority: p0
created: 2026-08-14
updated: 2026-09-13
sources: [https://arxiv.org/html/2604.09666v1]
last_checked: 2026-09-13
tags: [ingest, source, llm-memory]
summary: "Ingesting this would correct the corpus, not merely extend it."
confidence: high
origin: "2026-08-12 speculation pass; persisted 2026-08-14"
publish: true
---

# Do We Still Need GraphRAG? (arXiv 2604.09666)

## Why Track This

Fan, Xue, Liu, Tan. The verified abstract is more textured than the corpus's paraphrase: agentic dense RAG narrows but does not close the gap, and GraphRAG retains its advantage on complex multi-hop reasoning. The article text has been corrected once already from the abstract alone.

## Current State

**Ingested 2026-09-13** (full HTML, 87KB) as [sources/do-we-still-need-graphrag-ragsearch-benchmark-arxiv-2604-09666.md](../sources/do-we-still-need-graphrag-ragsearch-benchmark-arxiv-2604-09666.md).

## Result

The corpus's paraphrase holds and is now first-hand: agentic search substantially improves dense RAG and narrows the GraphRAG gap (multi-hop gap +27.23 → +26.59 single-shot vs GraphSearch; ~32% narrower vs second-best GraphRAG variant), but GraphRAG keeps the strongest, most stable performance on complex multi-hop reasoning, and dense RAG remains competitive on general QA at lower construction cost. RL-trained agents improve over their training-free baselines but do not consistently beat well-designed training-free pipelines (GraphSearch). Closes [q-graphrag-vs-agentic-per-task](q-graphrag-vs-agentic-per-task.md).
