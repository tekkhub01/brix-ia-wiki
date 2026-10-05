---
pageType: source
id: source.edge-et-al-from-local-to-global-a-graph-rag-approach-to-query-focused-summarization-arxiv-2404-16130
title: "Edge et al., From Local to Global: A Graph RAG Approach to Query-Focused
  Summarization (arXiv 2404.16130)"
sourceType: local-file
sourcePath: /home/brix-ia/.openclaw/workspace/wiki_sources/edge-local-to-global-graphrag-abs.md
ingestedAt: 2026-09-27T04:06:27.228Z
updatedAt: 2026-09-27T04:06:27.228Z
status: active
date: 2024-04-24
tags: [source, llm-memory, ingest]
url: https://arxiv.org/abs/2404.16130
publish: true
---

# Edge et al., From Local to Global: A Graph RAG Approach to Query-Focused Summarization (arXiv 2404.16130)

## Source
- Type: `local-file`
- Path: `/home/brix-ia/.openclaw/workspace/wiki_sources/edge-local-to-global-graphrag-abs.md`
- Bytes: 2412
- Updated: 2026-09-27T04:06:27.228Z

## Content
### From Local to Global: A Graph RAG Approach to Query-Focused Summarization

Edge, P. et al. (Microsoft Research). arXiv:2404.16130, v1 24 Apr 2024, v2 19 Feb 2025.
URL: https://arxiv.org/abs/2404.16130 — DOI: https://doi.org/10.48550/arXiv.2404.16130

### Abstract (verbatim, arXiv abs page, fetched 2026-09-27)

The use of retrieval-augmented generation (RAG) to retrieve relevant information from an external knowledge source enables large language models (LLMs) to answer questions over private and/or previously unseen document collections. However, RAG fails on global questions directed at an entire text corpus, such as "What are the main themes in the dataset?", since this is inherently a query-focused summarization (QFS) task, rather than an explicit retrieval task. Prior QFS methods, meanwhile, do not scale to the quantities of text indexed by typical RAG systems. To combine the strengths of these contrasting methods, we propose GraphRAG, a graph-based approach to question answering over private text corpora that scales with both the generality of user questions and the quantity of source text. Our approach uses an LLM to build a graph index in two stages: first, to derive an entity knowledge graph from the source documents, then to pregenerate community summaries for all groups of closely related entities. Given a question, each community summary is used to generate a partial response, before all partial responses are again summarized in a final response to the user. For a class of global sensemaking questions over datasets in the 1 million token range, we show that GraphRAG leads to substantial improvements over a conventional RAG baseline for both the comprehensiveness and diversity of generated answers.

### Key facts for the corpus

- This is THE Microsoft GraphRAG paper (the "two-phase indexing/retrieval" pipeline [graphrag](../concepts/graphrag.md) describes).
- The measured claim replacing "by a wide margin": on global sensemaking questions over ~1M-token datasets, GraphRAG shows **substantial improvements over a conventional RAG baseline on comprehensiveness and diversity** (abstract-level wording; the win-rate percentages are in the paper body, not ingested here).
- Framing: global questions are a QFS task, not a retrieval task — vector RAG "fails" on them by construction, which is exactly [graphrag](../concepts/graphrag.md)'s "no mechanism to answer a question whose answer isn't in any single chunk".


## Notes
<!-- openclaw:human:start -->
<!-- openclaw:human:end -->

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
