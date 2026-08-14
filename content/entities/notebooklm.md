---
id: notebooklm
pageType: entity
sourceIds:
  - sources/llm-memory-context-evolution-2026.md
updatedAt: 2026-04-28T00:00:00Z
publish: true
---
# NotebookLM (Google)

**Type:** Source-grounded agentic RAG product  
**Developer:** Google (Gemini team)  
**Launch:** 2024 (public preview), iterated 2025–2026  
**Model backbone:** Gemini 1.5 Pro / Flash (2M context window)  
**Positioning:** "Your personal AI research assistant" — source-centric, not chat-centric

## Architecture (hybrid)

Contrary to popular belief, NotebookLM does **NOT** simply load all uploaded files into the 2M token context per query (too expensive, slow). It uses a hybrid:

1. **Ingest Phase**:
   - Upload up to 50 sources (~25M words total)
   - Chunk → embed → local semantic index for that notebook
   - Extract key entities & generate structured summaries per source
2. **Retrieval Phase** (agentic):
   - Agent rewrites user query
   - Hybrid search: vector similarity + exact keyword matching
   - Retrieves large chunks (pages/chapters, not sentences) thanks to Gemini's huge context
3. **Generation Phase**:
   - Retrieved chunks + query + system prompt ("answer ONLY from sources") → Gemini 1.5 Pro
   - Because retrievals are large but few, they fit comfortably in context window

## Why it's fast: Context Caching

Google's **Context Caching** (API feature) stores pre-processed source embeddings + system instructions in GPU RAM. Subsequent queries in same notebook skip recomputation → 90% latency reduction, lower cost.

## Why it's accurate: Span-Level Attribution

- **Constraint prompting**: model forced to act as transcriber/analyst with no external knowledge
- **Span attribution**: during generation, model emits hidden markers linking each output sentence to exact source chunk ID
- UI converts markers to clickable citations that highlight original PDF text
- If a sentence cannot be cited, it is often discarded or replaced with "not found in sources"

## Multi-modal ingestion

- PDFs, Google Docs, web URLs, slides, audio, YouTube videos
- Videos: background agent extracts transcript + samples key frames → treat as text for retrieval
- Single semantic query can pull a spoken concept from YouTube video and cross-reference with a PDF table

## Audio Overviews (Podcast Feature) — Agentic Orchestration Showcase

This is not a simple summary readout:

1. Agent 1 analyzes all sources → extracts main themes + debate points
2. Agent 2 (LLM) writes theatrical script between two speakers (male/female), including interruptions, laughs, "deep breath"
3. Script passed to TTS (DeepMind Audio / SoundStorm-like) → ultra-realistic voices with emotional inflections, overlapping speech

## Key takeaways for article

NotebookLM demonstrates that state-of-the-art agentic RAG combines:

1. **Large retrieval units** (chunks = pages, not sentences) enabled by long context
2. **Context caching** to eliminate per-query re-embedding cost
3. **Rigid grounding with inline citations** (span-level attribution) forcing mathematical provenance

## Connections to wiki concepts

- Implements **Agentic RAG** (query rewriting + hybrid retrieval + validation)
- Uses **knowledge graph concepts** implicitly (entity extraction, summaries, linking)
- Different from **LLM Wiki**: still retrieval-based; Wiki proposes eliminating retrieval
- Relevant to **on-premise agent design**: can we adopt context caching + span attribution locally?

## References

- LLM Memory Context Evolution research — this analysis
- [NotebookLM official](https://notebooklm.google.com)

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [Context Caching](context-caching.md)
- [RAG (Retrieval-Augmented Generation)](rag.md)
- [Span-Level Attribution](span-level-attribution.md)

### Related Pages

- [Agentic RAG](agentic-rag.md)
- [Claude (Anthropic)](claude-anthropic.md)
- [GLM 5.1](glm-5.1.md)
- [GraphRAG](graphrag.md)
- [LLM Wiki (Karpathy Pattern)](llm-wiki-karpathy.md)
- [Long-Context Models](long-context-models.md)
- [Quantization](quantization.md)
<!-- openclaw:wiki:related:end -->
