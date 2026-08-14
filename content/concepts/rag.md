---
title: "RAG (Retrieval-Augmented Generation)"
category: concept
sources: [raw/notes/llm-memory-context-evolution-2026.md]
created: 2026-04-28
updated: 2026-08-12
verified: 2026-08-12
tags: [retrieval, rag, architecture]
aliases: [RAG, Retrieval-Augmented Generation]
confidence: high
summary: "The 2020 retrieve-then-generate baseline. Still the reference point, but by 2026 superseded in production by agentic multi-round retrieval and challenged on repeated-domain workloads by write-time compilation."
volatility: cold
publish: true
---
# RAG (Retrieval-Augmented Generation)

**Type:** foundational AI architecture pattern  
**Introduced:** 2020 (Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks")  
**Status:** Standard baseline; evolved into Agentic RAG, GraphRAG, LLM Wiki

## Core pipeline

1. **Ingest**: documents → chunked → embedded → stored in vector database
2. **Query**: user question → embedded → similarity search → top-k chunks retrieved
3. **Generation**: LLM receives question + retrieved chunks → produces answer grounded in sources

## Why RAG exists

- LLMs have fixed training cutoffs; cannot access fresh/private data
- Pure long-context is expensive (re-process all docs per query) and noisy
- RAG filters relevant passages at retrieval time, reducing token cost & distraction

## Classic limitations (that motivated Agentic RAG)

1. **Chunking problems**: rigid boundaries break concepts, lose metadata
2. **Retrieval randomness**: nearest neighbors not always most relevant; "almost right" results
3. **Single-shot**: no planning, no re-retrieval if initial results insufficient
4. **Grounded hallucinations**: model fills gaps even when context is semi-relevant but incomplete
5. **No multi-hop reasoning**: requires multiple queries; no chaining within single pipeline

## Trade-offs: RAG vs Long-Context

**RAG advantages** (vs pure long-context):
- Scalable to enterprise corpora (TB+); long-context windows still finite
- Lower token costs (only top-k chunks vs full document)
- Better focus (reduces distraction on irrelevant sections)
- Observability: retrieval chain is logged and debuggable
- Governance: ACLs at document/chunk level easier than vetting everything into context

**Long-context advantages**:
- No retrieval mismatch; entire document contiguous
- Handles cross-document connections naturally (if both fit)
- Simpler pipeline (no vector DB, no embedding model)

Empirical studies show ~10% of questions are answered only by RAG (scattered facts) vs long-context better for continuous narrative QA.

## Evolution path

RAG → **Agentic RAG** (orchestrated retrieval) → **GraphRAG** (graph-structured retrieval) → **LLM Wiki** (replaces retrieval with pre-synthesis)

## Status, 2026

Classic single-shot RAG is now the *baseline to beat*, not the deployed architecture. The defining shift is that retrieval stopped being a static preprocessing step and became a dynamic, multi-round process driven by the model's intermediate reasoning state — see [[agentic-rag|Agentic RAG]].

The current production stack is essentially never plain vector search. It is: query rewriting → hybrid retrieval (BM25 + dense embeddings) → cross-encoder reranker → generator that can re-ask the retriever. Each of those layers exists to patch one of the classic limitations listed above.

Two open fronts as of mid-2026:

- **Is graph structure still worth its cost once retrieval is agentic?** Benchmarks are now posing this directly ([*Do We Still Need GraphRAG?*](https://arxiv.org/html/2604.09666v1)) — an agent that can re-query iteratively recovers some of what graph traversal was buying. See [[graphrag|GraphRAG]].
- **Is retrieval worth its cost at all on repeated-domain workloads?** [[llm-wiki-karpathy|LLM Wiki]] measured 84.6% token savings against a matched RAG baseline by compiling at write-time instead. The saving is a function of topic concentration, so this is a workload question, not a verdict.

## References in this wiki

- [[agentic-rag|Agentic RAG]] — evolved pattern
- [[graphrag|GraphRAG]] — knowledge graph retrieval
- [[llm-wiki-karpathy|LLM Wiki]] — post-RAG paradigm
- [[notebooklm|NotebookLM]] — hybrid RAG + long-context product

## See Also

- [[agentic-rag|Agentic RAG]]
- [[graphrag|GraphRAG]]
- [[llm-wiki-karpathy|LLM Wiki (Karpathy Pattern)]]
- [[span-level-attribution]] — links here
- [[long-context-models]] — links here
- [[grounding-across-architectures]] — synthesis drawing on this page
- [[memory-economics]] — synthesis drawing on this page
- [[notebooklm-hybrid-stack]] — synthesis drawing on this page

## Sources

