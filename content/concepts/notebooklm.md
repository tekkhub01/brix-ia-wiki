---
title: "NotebookLM (Google)"
category: concept
sources: [raw/notes/llm-memory-context-evolution-2026.md]
created: 2026-04-28
updated: 2026-11-01
verified: 2026-11-01
tags: [product, rag, agents, citations, caching]
aliases: [NotebookLM, Notebook LM]
confidence: medium
summary: "Google's source-grounded research product, and the clearest shipping example of the hybrid stack: agentic retrieval with large chunks, context caching, and span-level attribution. Backbone details below are as-described in April 2026 and not re-verified since."
volatility: hot
publish: true
---
# NotebookLM (Google)

**Type:** Source-grounded agentic RAG product
**Developer:** Google (Gemini team)
**Launch:** 2024 (public preview), iterated 2025–2026
**Positioning:** "Your personal AI research assistant" — source-centric, not chat-centric

> **Freshness caveat.** The architecture below was recorded from an April 2026 research pass which described a Gemini 1.5 Pro / Flash backbone with a 2M-token context window. That model generation is old relative to this page's date, and the specific backbone, source limits, and word counts have **not been re-verified**. Treat the *shape* of the stack as reliable and the *numbers* as needing a refresh. The architectural claims are what this wiki cites elsewhere; the version details are not.

> **Refresh 2026-11-01 (sweep, secondhand — practitioner/blog sources, not Google docs).**
> The product was **renamed to Gemini Notebook in July 2026** (per Jeff Su's March-2026
> walkthrough, updated). The 2026 feature wave is consistent with the hybrid-stack thesis
> this page holds: a **1M-token chat context window** with saved chat history and Goals;
> **Deep Research** and Web/Fast-Research source discovery inside the Sources Panel
> (the tool now finds its own sources — a drift from the strict "only what you upload"
> positioning); **Gemini 3-class reasoning** replacing the 1.5-era backbone; slide-level
> editing and PPTX export (Feb 2026); **Data Tables**; image (OCR) and CSV source types;
> prompt limit raised 500 → 10,000 characters; **Cinematic Video Overviews** on Google's
> VO video model (Ultra-only); live-syncing Google Docs/Slides/Sheets as sources; and
> notebooks usable as a source inside the Gemini app (Dec 2025/Jan 2026). The Google
> blog "Do your best research with NotebookLM" adds a secure cloud computer for code
> execution and report/chart/spreadsheet/slide output generation. None of this changes
> the retrieval/caching/attribution architecture above; it extends the generation side
> of the pipeline. Numbers remain secondhand until a primary Google source is ingested.

## Architecture (hybrid)

Contrary to popular belief, NotebookLM does **NOT** simply load all uploaded files into the context window per query (too expensive, too slow). It uses a hybrid:

1. **Ingest phase**
   - Upload up to 50 sources (~25M words total)
   - Chunk → embed → local semantic index scoped to that notebook
   - Extract key entities and generate structured summaries per source
2. **Retrieval phase (agentic)**
   - Agent rewrites the user query
   - Hybrid search: vector similarity + exact keyword matching
   - Retrieves **large** chunks (pages/chapters, not sentences), which the long context window makes affordable
3. **Generation phase**
   - Retrieved chunks + query + system prompt ("answer ONLY from sources")
   - Because retrievals are large but few, they fit comfortably in the window

The retrieval-unit choice is the interesting part: long context did not remove retrieval here, it changed the *granularity* of retrieval. See [[long-context-models]].

## Why it's fast: context caching

Google's context caching stores pre-processed source embeddings and system instructions server-side; subsequent queries in the same notebook skip recomputation. The research note records a ~90% latency reduction. See [[context-caching]] — note that the caching economics documented there are Anthropic's published multipliers, and Google's are not assumed to match.

## Why it's accurate: span-level attribution

- **Constraint prompting**: the model is forced to act as transcriber/analyst with no external knowledge
- **Span attribution**: during generation the model emits markers linking each output sentence to an exact source chunk ID
- The UI converts markers into clickable citations that highlight the original text
- If a sentence cannot be cited, it is often discarded or replaced with "not found in sources"

This is the product that made [[span-level-attribution]] a mainstream expectation rather than a research demo.

## Multi-modal ingestion

- PDFs, Google Docs, web URLs, slides, audio, YouTube videos
- Videos: a background agent extracts the transcript and samples key frames, then treats the result as text for retrieval
- A single semantic query can pull a spoken concept from a video and cross-reference it with a table in a PDF

## Audio Overviews — agentic orchestration in a consumer feature

Not a summary readout, but a small multi-agent pipeline:

1. Agent 1 analyzes all sources and extracts themes and points of disagreement
2. Agent 2 writes a two-speaker script, including interruptions and verbal texture
3. The script is passed to a TTS system producing voices with emotional inflection and overlapping speech

Worth noting as evidence that the agentic-orchestration pattern reached consumer product surface, not just developer tooling.

## Why this page matters to the topic

NotebookLM is the existence proof that the three ideas this wiki treats separately compose into one shipping system:

1. **Large retrieval units** enabled by long context
2. **Context caching** to eliminate per-query recomputation cost
3. **Rigid grounding with inline citations** enforcing provenance

It is also the counter-example to the strong form of the "retrieval is dead" claim — it has a very long context window and still retrieves. Contrast with [[llm-wiki-karpathy]], which proposes compiling at write time instead of retrieving at query time.

The assembled version of this argument lives in [[notebooklm-hybrid-stack]]; this page is the component description.

## See Also

- [[agentic-rag]] — the pattern NotebookLM implements
- [[context-caching]] — the mechanism behind its latency
- [[span-level-attribution]] — the mechanism behind its citations
- [[long-context-models]] — why large retrieval units are affordable
- [[notebooklm-hybrid-stack]] — the synthesis article

## Sources

- [llm-memory-context-evolution-2026](../sources/llm-memory-context-evolution-2026.md)
- [NotebookLM official](https://notebooklm.google.com) — not ingested
