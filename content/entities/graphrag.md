---
id: graphrag
pageType: entity
sourceIds:
  - sources/llm-memory-context-evolution-2026.md
updatedAt: 2026-08-12T00:00:00Z
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
- **[SAGE](https://arxiv.org/pdf/2605.12061)** — self-evolving agentic graph-memory engine; the graph is maintained as associative memory rather than built once at index time. This is the closest neighbour to the [[llm-wiki-karpathy|LLM Wiki]] pattern from the graph side.

**The challenge, and what it actually found:** [*Do We Still Need GraphRAG? Benchmarking RAG and GraphRAG for Agentic Search Systems*](https://arxiv.org/html/2604.09666v1) (Fan, Xue, Liu, Tan) asks whether graph construction still earns its cost once the retriever can iterate. Its finding is **not** that GraphRAG is obsolete: agentic dense RAG *substantially improves* and **narrows** the gap, but GraphRAG **retains its advantage on complex multi-hop reasoning**. So the question is a cost-benefit one per query mix, not a verdict — graph construction stays expensive (LLM extraction + entity resolution), and an agent that re-queries adaptively recovers *part*, not all, of what traversal was buying.

Where GraphRAG still clearly wins: **global / thematic queries** — "what are the main themes across this corpus" — where community summaries beat vector-only retrieval by a wide margin. Vector RAG has no mechanism to answer a question whose answer isn't in any single chunk.

## Relevant links

- [GraphRAG official site](https://graphrag.com)
- [Microsoft GraphRAG GitHub](https://microsoft.github.io/graphrag/)
- [IBM GraphRAG tutorial](https://www.ibm.com/it-it/think/tutorials/knowledge-graph-rag)

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Agentic RAG](agentic-rag.md)
- [CodeGraph — Pre-indexed code knowledge graph](../syntheses/codegraph-pre-indexed-code-knowledge-graph.md)
- [LLM Wiki (Karpathy Pattern)](llm-wiki-karpathy.md)
- [RAG (Retrieval-Augmented Generation)](rag.md)

### Related Pages

- [Claude (Anthropic)](claude-anthropic.md)
- [Context Caching](context-caching.md)
- [GLM 5.1](glm-5.1.md)
- [Long-Context Models](long-context-models.md)
- [NotebookLM (Google)](notebooklm.md)
- [Quantization](quantization.md)
- [Span-Level Attribution](span-level-attribution.md)
<!-- openclaw:wiki:related:end -->
