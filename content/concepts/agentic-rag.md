---
title: "Agentic RAG"
category: concept
sources: [raw/notes/llm-memory-context-evolution-2026.md]
created: 2026-04-28
updated: 2026-08-14
verified: 2026-08-12
tags: [retrieval, agents, rag]
aliases: [Agentic RAG]
confidence: high
summary: "Retrieval as a dynamic multi-round loop: plan, retrieve, critique, rewrite, reflect. The mainstream 2026 default, at 3-5x the per-query cost of classic RAG."
volatility: warm
publish: true
---
# Agentic RAG

**Type:** Architecture pattern / augmentation  
**First described:** 2025–2026 (industry adoption); mainstream default by mid-2026  
**Core:** Multiple LLM agents orchestrate the retrieval + validation pipeline iteratively

**The defining shift:** retrieval moves from a *static preprocessing step* to a *dynamic multi-round process* that adapts to intermediate reasoning state during inference. Classic RAG cannot adapt to what it learns halfway through answering; agentic RAG plans, retrieves, reasons, critiques, rewrites, and reflects in a loop until it is confident or hits its budget.

## Pipeline (vs classic RAG)

| Step | Classic RAG | Agentic RAG |
|------|-------------|-------------|
| 1. Query | Direct embedding | Agent rewrites/expands query |
| 2. Retrieval | Single top-k from vector DB | Multi-retriever (vector + lexical + SQL + graph); may iterate |
| 3. Validation | None (blind trust) | Agent checks span-level attribution; rejects unsupported claims |
| 4. Generation | LLM with context | LLM only after agent approves context |
| 5. Adaptation | Static pipeline | Policy learns from failures; adds steps per query class |

## Components

- **Query planner agent**: decomposes complex questions, identifies required data sources
- **Retriever agents**: one per source type (vector, keyword, SQL, API, graph)
- **Validator agent**: cross-checks answer against retrieved spans; demands citations
- **Router agent**: decides which retriever to call next based on intermediate results

## Benefits

- **Iterative retrieval**: if first retrieval incomplete, agent re-retrieves with refined query
- **Multi-source fusion**: combines text, tables, graphs, APIs
- **Reduced hallucinations**: validation step forces groundedness
- **Observability**: full trace of agent decisions (which retriever, why, failures)

## Trade-offs

- Higher latency (multiple LLM calls per query)
- More complex orchestration (needs agent framework)
- Cost: 3–5× classic RAG per query (but better accuracy may justify)
- Debugging requires tracing agent policies, not just retrieval scores

## Implementations

- **Weaviate Agentic RAG** (retriever + planner + verifier agents)
- **Moveworks Agentic RAG** (enterprise workflows)
- **IBM Watsonx** (agentic RAG with query decomposition)
- DIY: LangGraph is the common 2026 orchestration choice; LangChain/LlamaIndex with custom agent loops

## The 2026 reference stack

Converged production shape, in order:

1. **Query rewriting** — expand / decompose the raw question
2. **Hybrid retrieval** — BM25 *and* dense embeddings, not either alone
3. **Cross-encoder reranker** — rescore candidates jointly with the query
4. **Generator that can re-ask the retriever** — the agentic loop proper

Scaling work is mostly about controlling how much the loop costs: **[A-RAG](https://arxiv.org/pdf/2602.03442)** proposes hierarchical retrieval interfaces so the agent queries at the right granularity instead of paging through everything, and **[RELOOP](https://arxiv.org/pdf/2510.20505)** handles recursive retrieval with explicit multi-hop reasoners and planners for heterogeneous QA. On the graph side the equivalent is [GraphSearch](https://arxiv.org/pdf/2509.22009) — see [[graphrag|GraphRAG]].

The cost profile in the trade-offs above (3–5× classic RAG per query) still holds and is the reason budget-bounded loops are standard rather than optional.

## NotebookLM parallel

NotebookLM uses a limited form of Agentic RAG: query rewriting + hybrid retrieval + strict attribution, but doesn't expose multi-step planning publicly.

## Relationship to other concepts

- [[rag|RAG]] → classic single-shot retrieval
- [[graphrag|GraphRAG]] → uses knowledge graphs as retriever
- [[llm-wiki-karpathy|LLM Wiki]] → replaces retrieval entirely with pre-synthesis

## See Also

- [[graphrag|GraphRAG]]
- [[rag|RAG (Retrieval-Augmented Generation)]]
- [[llm-wiki-karpathy|LLM Wiki (Karpathy Pattern)]]
- [[span-level-attribution]] — links here
- [[notebooklm]] — links here
- [[structure-vs-iteration]] — synthesis drawing on this page
- [[grounding-across-architectures]] — synthesis drawing on this page
- [[memory-economics]] — synthesis drawing on this page
- [[notebooklm-hybrid-stack]] — synthesis drawing on this page
- [Prime Agent](../syntheses/prime-agent-self-improving-rlm-agent-primeintellect-ai.md) — sub-agent ricorsivi come chiamate di funzione, con harness che accumula stato; memory-wiki

## Sources

- [llm-memory-context-evolution-2026](../sources/llm-memory-context-evolution-2026.md)
