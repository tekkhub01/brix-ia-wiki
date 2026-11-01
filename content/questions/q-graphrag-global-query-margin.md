---
title: "What is Microsoft GraphRAG's actual measured margin on global/thematic queries?"
kind: question
status: answered
priority: p1
created: 2026-08-14
updated: 2026-10-11
last_checked: 2026-10-11
tags: [question, gap, llm-memory]
summary: "graphrag.md asserts community summaries beat vector-only retrieval 'by a wide margin' with no number."
confidence: high
origin: "2026-08-12 speculation pass; persisted 2026-08-14"
publish: true
---

# What is Microsoft GraphRAG's actual measured margin on global/thematic queries?

## Why Track This

[graphrag](../concepts/graphrag.md) asserts community summaries beat vector-only retrieval 'by a wide margin' with no number.

## Current State

Answered directly by ingesting edge local to global graphrag.

## Next Action

Resolve by ingesting the linked candidate, or mark superseded if answered elsewhere.

## Resolution

**Answered 2026-10-11 (dreaming sweep).** The linked candidate was ingested 2026-09-27 (`sources/edge-et-al-from-local-to-global-a-graph-rag-approach-to-query-focused-summarization-arxiv-2404-16130.md`) and [graphrag](../concepts/graphrag.md) was corrected 2026-10-04. The honest answer to "what is the measured margin": **the paper does not report a single accuracy margin.** Its measured axes are *comprehensiveness and diversity* on sensemaking/global questions over ~1M-token corpora, stated as "substantial improvements" over a conventional RAG baseline — and global questions are framed as a query-focused summarization task, not a retrieval task, so a vector-RAG baseline has no mechanism to produce a comparable answer at all. Win-rate percentages live in the paper body (not ingested; deliberate scope limit — the abstract settles the claim's shape, the body would only add decimal points). The original "by a wide margin" phrasing is retired from the corpus; [graphrag](../concepts/graphrag.md) now carries the precise formulation.
