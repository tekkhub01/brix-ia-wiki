---
id: llm-memory-context-evolution-2026
pageType: source
updatedAt: 2026-04-28T00:00:00Z
publish: true
---

# LLM Memory & Context Evolution — Deep Research

**Source:** Peter K. research notes (2026-04-28)  
**Type:** Technical review / State-of-the-art survey  
**Language:** Italian  
**Scope:** Evolution of memory/context handling in LLMs — from embeddings & quantization → RAG → Agentic RAG → Karpathy LLM Wiki  
**Date:** 2026-04-28

---

## Executive Summary

The document maps the complete evolution of memory/context strategies in modern LLM systems:

1. **Embedding-based context loading** — vector representation of knowledge, costly at scale → need quantization (QAT, KV cache compression)
2. **Traditional RAG** — retrieve-then-read with chunking, suffers from retrieval randomness, chunk fragmentation, grounded hallucinations
3. **Agentic RAG** — iterative, planning, re-retrieval, validation, multi-source orchestration (vector + lexical + graphs)
4. **GraphRAG** — knowledge graphs replace isolated chunks, multi-hop reasoning, structured relationships
5. **Karpathy LLM Wiki** — abandon retrieval at query time; synthesis at write time; persistent Markdown filesystem with cross-linking, linting, Obsidian as state memory
6. **NotebookLM case study** — hybrid RAG + long-context, context caching, span-level attribution, multi-modal ingestion, audio overviews as agentic orchestration

Key debates in community:
- **Wiki improvement vs degeneration**: Does automatic linking improve knowledge graph or create entropy?
- **RAG vs pure long-context**: Cost, scalability, focus, observability trade-offs
- **Graph integration with Wiki**: Hybrid approaches (LLM Wiki + GraphRAG) to reduce retrieval randomness

---

## Structure of the Research

### Section 1 — Theoretical Evolution
- Embeddings and quantization math
- RAG chunking problems (coverage gaps, near-miss retrieval)
- Agentic RAG pipeline (query decomposition → plan → retrieve → evaluate → re-retrieve → answer)
- GraphRAG using Neo4j/InfraNodus for multi-hop
- Karpathy's LLM Wiki as "write-time synthesis" replacing "query-time retrieval"

### Section 2 — LLM Wiki Deep Dive
- **Pattern**: raw/ → wiki/ → schema/, with ingest–query–lint loop
- **Where it shines**: second brain, technical documentation, stack: Obsidian + Claude/Ollama + InfraNodus
- **Problems**: over-linking → entropy, schema drift, cost of continuous updates
- **Community solutions**: stricter schemas, network metrics, aggressive linting, hybrid RAG/GraphRAG

### Section 3 — RAG vs Long-Context Advantages
- Efficiency & scalability (one-time embedding cost vs per-query reprocessing)
- Focus & noise reduction (targeted chunks vs entire haystack)
- Lower operational costs & simpler tuning
- Fresh data & governance (retriever-level ACLs)
- Observability & debug (logged retrieval chain)

### Section 4 — RAG Structural Limits
- Chunking / coverage / "almost right" results
- Grounded hallucinations despite context
- Static single-shot pipeline (no planning, no multi-hop)
- Operational complexity (data plumbing, incomplete indexing)

### Section 5 — Why Agentic RAG Emerges
- Iterative retrieval, not one-shot
- Better context quality through filtering
- Span-level attribution & validation
- Integration with structured data (SQL, graphs, APIs)
- Adaptive policies from logs

### Section 6 — NotebookLM Architecture (Case Study)
- Hybrid ingest: embeddings + large chunk size (pages/chapters)
- Agentic retrieval: query rewriting, hybrid search (vector + keyword)
- Context caching on GPU (90% latency reduction)
- Span-level attribution forcing citations per sentence
- Multi-modal ingestion: PDF + video (transcription + frame sampling)
- Audio overviews: dual-agent scriptwriting + TTS

---

## Key Entities to Synthesize

From this research, the following concepts/pages should be created as separate wiki syntheses with provenance:

- **Embedding** (concept)
- **Quantization** (technique: QAT, KV cache compression)
- **RAG (Retrieval-Augmented Generation)** (concept, with limitations)
- **Agentic RAG** (concept/architecture)
- **GraphRAG** (technique, knowledge graphs for multi-hop)
- **LLM Wiki (Karpathy pattern)** (concept/architecture)
- **Context Caching** (optimization technique, NotebookLM)
- **Span-Level Attribution** (grounding technique)
- **Long-Context Models** (category of models)
- **NotebookLM** (product/system, Google)

These should link back to this source page and to existing entity pages in the wiki (Claude, GLM 5.1, etc.) where relevant.

---

## Research Questions / Open Issues

- **Degeneration vs improvement**: Does constant auto-linking create entropic knowledge graphs? Need metrics to measure graph health.
- **Hybrid architectures**: Best practices for combining LLM Wiki with GraphRAG (when to store in wiki vs graph)?
- **Cost modeling**: Context caching vs RAG retrieval cost; trade-offs for on-premise vs cloud (NotebookLM).
- **Schema evolution**: How to manage schema changes in LLM Wiki without breaking backlinks?

---

---
## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Impeccable.style - AI Design Tool](../syntheses/impeccable-style-ai-design-tool.md)
- [NotebookLM (Google)](../concepts/notebooklm.md)
<!-- openclaw:wiki:related:end -->

**Next steps:** Extract sections for article integration; design concrete LLM Wiki + Graph architecture for OpenClaw/Obsidian stack.
