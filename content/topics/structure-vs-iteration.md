---
title: "Structure vs. Iteration: When Compiled Knowledge Earns Its Cost"
category: topic
sources: [raw/notes/llm-memory-context-evolution-2026.md]
created: 2026-08-12
updated: 2026-08-12
verified: 2026-08-12
tags: [architecture, knowledge-graph, write-time-synthesis, agents, cost]
aliases: [When to Build a Graph, Structure vs Adaptive Retrieval, Explicit Structure vs Iteration]
confidence: medium
summary: "Three architectures pay for structure at different times and amortize it differently: Agentic RAG never amortizes, GraphRAG pays once at index time, the LLM Wiki pays incrementally at ingest. All three are now being asked the same question from different directions — does adaptive iteration make the structure unnecessary?"
volatility: hot
publish: true
---
# Structure vs. Iteration: When Compiled Knowledge Earns Its Cost

[[graphrag|GraphRAG]], [[agentic-rag|Agentic RAG]], and [[llm-wiki-karpathy|LLM Wiki]] each answer a shared design question differently: when a query needs more than one hop of reasoning, do you build a persistent structure that encodes the hops in advance, or do you let an agent iterate its way there at query time? Each concept page describes its own answer; none of them lines the three up as one spectrum.

## The same question, asked from three directions

The [[graphrag|GraphRAG]] page names the challenge explicitly: [*Do We Still Need GraphRAG?*](https://arxiv.org/html/2604.09666v1) (Fan, Xue, Liu, Tan) benchmarks agentic dense RAG against GraphRAG for agentic search systems. Its finding is not a verdict either way: agentic iteration — an agent that re-queries adaptively — substantially improves on non-agentic dense RAG and **narrows** the gap to GraphRAG, but GraphRAG **retains its advantage on complex multi-hop reasoning**. So this is not "iteration made structure obsolete"; it's a per-query-mix cost-benefit judgement, and the honest reading is that the *margin* by which structure wins has shrunk, not that the win has disappeared. The [[llm-wiki-karpathy|LLM Wiki]] page poses the mirror-image question about itself in its own open-research section: does compilation still earn its cost once agentic retrieval exists to substitute for it? These are the same question, asked by two different lineages about their own overhead, and neither concept page notices that the other lineage is asking it too — nor does either have the equivalent of *Do We Still Need GraphRAG?*'s benchmark for its own case: nobody in this wiki has run the actual head-to-head between LLM Wiki compilation and agentic RAG on the same corpus and query mix, the comparison the graph lineage has already produced for itself.

## When structure is paid for, and how it's recovered

| Architecture | When cost is paid | How it's recovered | Unit of structure |
|---|---|---|---|
| [[agentic-rag]] | Every query, in full | Never amortized — the 3–5× multiplier is repaid per query with no persistent artifact left behind | none (the "structure" is a transient reasoning trace) |
| [[graphrag]] | Once, at corpus index time | Amortized across all future queries against that corpus | entity/relationship graph + community summaries |
| [[llm-wiki-karpathy]] | Incrementally, at each ingest (one source "touches 10–15 pages") | Amortized across all future queries and re-syntheses — this is the mechanism behind the compounding figures in the [[memory-economics]] article | compiled markdown pages + cross-links |

Read this way, Agentic RAG is the pure-iteration pole (it substitutes reasoning-at-query-time for structure entirely) and GraphRAG and LLM Wiki are both structure-first, differing mainly in *what* the structure is (typed graph vs prose pages) and in construction cost (entity resolution and ontology design vs an LLM read-and-write pass). The "do we still need this" question is really: has iteration gotten cheap enough, or structure gotten expensive enough, to flip which pole wins for a given workload?

## Where explicit structure still wins outright

Both graph and wiki lineages report the same category of query where iteration alone cannot substitute: global, thematic, cross-document questions. [[graphrag|GraphRAG]]'s page states this plainly — for global / thematic queries, community summaries beat vector-only retrieval, and "vector RAG has no mechanism to answer a question whose answer isn't in any single chunk." (The page's earlier "by a wide margin" phrasing was retired 2026-09-27 in favour of the Edge et al. paper's own measured axes — comprehensiveness and diversity — see [the source](../sources/edge-et-al-from-local-to-global-a-graph-rag-approach-to-query-focused-summarization-arxiv-2404-16130.md); this topic page quotes the retired formulation and is corrected here for consistency.) The LLM Wiki's own `index.md` (a content-oriented catalog of every page grouped by category, read first on every query per the LLM Wiki page's "How it works" section) serves the same function by a different mechanism: it *is* a standing global-thematic summary, maintained incrementally instead of computed at index time. Agentic RAG has no equivalent — its iteration loop can re-query, but nothing in the pattern as described builds a corpus-wide summary artifact that persists between queries. This is the concrete case for explicit structure: whenever the query is "what does the whole corpus say about X," something has to have already summarized the whole corpus, and no amount of per-query re-retrieval substitutes for that having been done in advance.

## Convergence: two structural lineages arriving at the same shape

The [[graphrag|GraphRAG]] page's 2026 update notes a shift from "graph as a retriever" to **graph-native agents**, and singles out **SAGE** (self-evolving agentic graph-memory engine) as "the closest neighbour to the [[llm-wiki-karpathy|LLM Wiki]] pattern from the graph side" — because SAGE maintains its graph as continuously-updated associative memory rather than building it once at index time. That is precisely the LLM Wiki's own ingest→query→lint loop, restated in graph terms instead of markdown terms. Two lineages that started from opposite premises (probabilistic chunk retrieval vs abandoning retrieval altogether) are converging on the same operational shape: an agent that owns a persistent structure and updates it incrementally, rather than a pipeline that rebuilds a structure from scratch or never builds one at all. Agentic RAG, by contrast, has no such convergence pressure — nothing in its 2026 reference stack (query rewriting → hybrid retrieval → reranking → re-ask loop) accumulates a persistent artifact between conversations, which is exactly why it never shows up in either page's amortization discussion.

## The unresolved comparison

Naming what's missing rather than filling it in: no source in this cluster benchmarks LLM Wiki compilation against GraphRAG construction on the same corpus. The LLM Wiki's 84.6% saving is measured against "a matched RAG baseline" (see [[memory-economics|the economics article]] for why that baseline is itself ambiguous), not against GraphRAG. GraphRAG's decisive win on global queries is measured against vector-only RAG, not against an LLM Wiki's `index.md`. Both claims of "structure earns its cost here" are real and separately sourced — but they are not the same comparison, and nothing in this wiki licenses stacking them into a ranking of GraphRAG vs LLM Wiki.

## See Also

- [[graphrag|GraphRAG]]
- [[agentic-rag|Agentic RAG]]
- [[llm-wiki-karpathy|LLM Wiki (Karpathy Pattern)]]
- [[memory-economics|The Economics of LLM Memory]]
- [[grounding-across-architectures|Grounding and Failure Modes Across Memory Architectures]]

## Sources

- [llm-memory-context-evolution-2026](../sources/llm-memory-context-evolution-2026.md)
