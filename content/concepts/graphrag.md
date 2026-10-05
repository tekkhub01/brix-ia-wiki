---
title: "GraphRAG"
category: concept
sources: [raw/notes/llm-memory-context-evolution-2026.md, sources/edge-et-al-from-local-to-global-a-graph-rag-approach-to-query-focused-summarization-arxiv-2404-16130.md, sources/sage-agentic-graph-memory-abs.md]
created: 2026-04-28
updated: 2026-10-04
verified: 2026-10-04
tags: [retrieval, knowledge-graph, rag]
aliases: [GraphRAG, Graph RAG]
confidence: high
summary: "Retrieval over an entity/relationship graph rather than isolated chunks. Wins decisively on global thematic queries; its cost is now being challenged by agentic search that can iterate."
volatility: warm
publish: true
---
# GraphRAG

**Type:** Retrieval augmentation technique using knowledge graphs  
**Key papers:** Microsoft GraphRAG (2024), IBM GraphRAG (2025), Neo4j ADK + GraphRAG (2025), agentic-GraphRAG wave (2026)  
**Motivation:** Classic RAG's vector-similarity retrieval is probabilistic; graphs enable logical, multi-hop reasoning

## How it differs from classic RAG

| Dimension | Classic RAG | GraphRAG |
|-----------|-------------|----------|
| Knowledge representation | Isolated text chunks (embeddings) | Nodes (entities) + edges (relationships) |
| Retrieval | Nearest neighbor in embedding space | Graph traversal (1-hop, 2-hop, arbitrary path) |
| Reasoning | Implicit in LLM | Explicit relationships (entity → relation → entity) |
| Coverage | Fragmented; depends on chunk boundaries | Holistic; entities linked across documents |
| Multi-hop | Hard (needs multiple retrievals) | Native (follow edges) |

## Two-phase process (Microsoft GraphRAG)

1. **Indexing phase**:
   - Extract entities & relationships from all documents (LLM-generated triples)
   - Build knowledge graph (nodes + community detection)
   - Generate community summaries (global + local)
2. **Retrieval phase**:
   - Map query to relevant graph nodes
   - Traverse graph to collect related entities & documents
   - Return structured context (entity list + relationships + source excerpts)

## Benefits

- Eliminates "almost right" retrieval: relationships constrain results
- Handles implicit knowledge (A related to B, B related to C → A related to C indirectly)
- Better for analytical queries ("compare X and Y across these reports")
- Natural for enterprise data (org charts, product trees, compliance hierarchies)

## Costs

- Graph construction expensive (LLM extraction + entity resolution)
- Storage: graphs > vector DBs
- Query latency: graph traversal + embedding fallback hybrid
- Schema design needed (ontology); not schema-less like vector DB

## Community tools

- **Neo4j + LLM** (codelabs.google.com/neo4j-adk-graphrag-agents)
- **InfraNodus** (graph + LLM Wiki integration)
- **Microsoft GraphRAG** (open-source, Python)
- **Epsilla GraphRAG** (built-in knowledge graph layer)

## Relationship to Agentic RAG

GraphRAG can be one retriever in an [[agentic-rag|Agentic RAG]] pipeline: the agent chooses whether to query vector DB or graph based on query type (factual vs relational).

## 2026: graph-native agents, and a live challenge to the premise

The field moved from "graph as a retriever" to **graph-native agents** — see the [*Survey of Agentic GraphRAG: From Retrieval-augmented Generation to Graph-native Agents*](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6713979). Representative work:

- **[GraphSearch](https://arxiv.org/pdf/2509.22009)** — agentic deep-searching workflow that iteratively and *jointly* queries textual chunks and the graph, rather than picking one retriever per query. Aimed squarely at multi-hop.
- **[SAGE](../sources/sage-agentic-graph-memory-abs.md)** — self-evolving agentic graph-memory engine (Wang et al., arXiv 2605.12061; abstract in vault dal 2026-10-04). The graph is maintained as associative memory rather than built once at index time: a **memory writer** builds it incrementally from interaction histories and a Graph Foundation Model **reader** retrieves and feeds back — after two self-evolution rounds it takes the best average rank on multi-hop QA, with 82.5/91.6 Recall@2/5 on NQ zero-shot. This is the closest neighbour to the [[llm-wiki-karpathy|LLM Wiki]] pattern from the graph side, and the abstract says why: both move the work to **write time** and treat the store as a first-class artifact — they differ in substrate (typed graph vs prose pages) and in whether the store improves itself from downstream feedback (SAGE yes; the wiki's compile loop is manual).

**The challenge, and what it actually found:** [*Do We Still Need GraphRAG? Benchmarking RAG and GraphRAG for Agentic Search Systems*](https://arxiv.org/html/2604.09666v1) (Fan, Xue, Liu, Tan) asks whether graph construction still earns its cost once the retriever can iterate. Its finding is **not** that GraphRAG is obsolete: agentic dense RAG *substantially improves* and **narrows** the gap, but GraphRAG **retains its advantage on complex multi-hop reasoning**. So the question is a cost-benefit one per query mix, not a verdict — graph construction stays expensive (LLM extraction + entity resolution), and an agent that re-queries adaptively recovers *part*, not all, of what traversal was buying.

Where GraphRAG still clearly wins: **global / thematic queries** — "what are the main themes across this corpus". The claim now has its primary source in the vault: [Edge et al., From Local to Global (arXiv 2404.16130)](../sources/edge-et-al-from-local-to-global-a-graph-rag-approach-to-query-focused-summarization-arxiv-2404-16130.md) — the Microsoft GraphRAG paper itself — which frames global questions as a **query-focused summarization task, not a retrieval task** (vector RAG has no mechanism to answer a question whose answer isn't in any single chunk) and reports **substantial improvements over a conventional RAG baseline on comprehensiveness and diversity** for sensemaking questions over ~1M-token corpora. Note the precision: the paper's measured axes are *comprehensiveness and diversity*, not accuracy, and the win is stated as "substantial improvement", not a percentage — the earlier "by a wide margin" phrasing was secondhand and is retired here. Win-rate percentages live in the paper body, not ingested.

## Relevant links

- [GraphRAG official site](https://graphrag.com)
- [Microsoft GraphRAG GitHub](https://microsoft.github.io/graphrag/)
- [IBM GraphRAG tutorial](https://www.ibm.com/it-it/think/tutorials/knowledge-graph-rag)

## See Also

- [[agentic-rag|Agentic RAG]]
- [[llm-wiki-karpathy|LLM Wiki (Karpathy Pattern)]]
- [[rag]] — links here
- [[structure-vs-iteration]] — synthesis drawing on this page

## Sources

- [llm-memory-context-evolution-2026](../sources/llm-memory-context-evolution-2026.md)
