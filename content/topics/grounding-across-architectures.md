---
title: "Grounding and Failure Modes Across Memory Architectures"
category: topic
sources: [raw/notes/llm-memory-context-evolution-2026.md]
created: 2026-08-12
updated: 2026-08-12
verified: 2026-08-12
tags: [grounding, citations, trust, evaluation, write-time-synthesis]
aliases: [Trust Axis, Groundedness vs Alignment, How Memory Architectures Fail]
confidence: medium
summary: "RAG, Agentic RAG, and the LLM Wiki each ground claims by a different mechanism and fail in a different place — read-time citation checking versus write-time compilation trust. The LLM Wiki's claim to 'inherent' provenance is weaker than it sounds once measured against span-level attribution's own central finding."
volatility: warm
publish: true
---
# Grounding and Failure Modes Across Memory Architectures

Every architecture in this cluster answers the same question — "why should I believe this claim?" — with a different mechanism, and each mechanism has a characteristic way of breaking. Read individually, the concept pages describe these failures in isolation. Placed side by side, they form a spectrum: from checking each generated sentence at read time, to trusting the process that produced a compiled page in the first place.

## Two vocabularies for the same failure

The topic guide (`schema.md`) draws a distinction the concept pages use without naming: **groundedness** (is the claim supported by *some* cited source) vs **alignment** (does the *specific* citation attached actually support it). [[span-level-attribution|Span-Level Attribution]]'s central empirical finding is exactly a groundedness/alignment gap stated in different words: "models are broadly good at identifying the right document and materially worse at identifying the precise supporting span within it. Document-level attribution is largely solved; span-level is not." On RAGTruth's ~18K labeled chunks, the median frontier model still fails groundedness on 5–8% of answers — and the characteristic 2026 failure mode is a *high* grounded-response score paired with a *low* alignment rate: the citation is real, the source is real, it just doesn't support that particular sentence.

## Where each architecture's failure actually happens

- **[[rag|RAG]]**: fails at generation time, silently. Classic RAG's defining failure is "grounded hallucination" — the model fills gaps even when the retrieved context is semi-relevant but incomplete, and there is no built-in mechanism to catch this because classic RAG has no forced citation step at all.
- **[[agentic-rag|Agentic RAG]]**: moves the check earlier, into the pipeline itself. Its validator agent is explicitly described as one that "checks span-level attribution; rejects unsupported claims" before generation is allowed to finish — i.e. it wires [[span-level-attribution|Span-Level Attribution]] in as a *gate*, not a post-hoc audit. This is the direct mechanical link between the two pages: agentic RAG doesn't invent a new grounding technique, it's the architecture that makes span-level attribution enforceable rather than optional.
- **[[llm-wiki-karpathy|LLM Wiki]]**: fails somewhere else entirely. There is no per-sentence citation check at read time — the wiki page states provenance is "inherent (notes directly link to source documents; synthesis traceable via edit history)." The failure mode this architecture is actually vulnerable to is not grounded hallucination per query, it's **compiled drift**: contradictions and stale claims accumulating *inside the wiki itself* over many ingest cycles, caught (or not) by the periodic lint pass rather than by a citation checker. Trust here is amortized into the compilation and linting process, not verified per answer.

## The gap the LLM Wiki's provenance claim doesn't close

This is worth stating explicitly because none of the three pages does: [[llm-wiki-karpathy|LLM Wiki]] frames its provenance as solved ("inherent... traceable"), but the granularity it operates at — a page or paragraph linking back to a source document via a `sources:` frontmatter field and inline wikilink citations — is *document-level* provenance, exactly the tier [[span-level-attribution|Span-Level Attribution]] identifies as "largely solved." The unsolved tier in that same page — precise span localization *within* a source, which is where 2026's real citation failures concentrate — is not addressed by the wiki pattern at all. The LLM Wiki inherits the solved part of the attribution problem for free (a page always knows which raw source it came from) and simply doesn't attempt the unsolved part (whether a specific compiled sentence is actually supported by a specific span of that source, versus the author-agent's paraphrase or synthesis drifting from it). Nothing in the LLM Wiki concept page's "Pros" list distinguishes these two tiers — it should.

## Multi-source synthesis: the shared blind spot

[*Cited but Not Verified*](https://arxiv.org/pdf/2605.06635), cited on the [[span-level-attribution|Span-Level Attribution]] page, finds that multi-source synthesis is where citation parsing and verification breaks down most for deep-research agents. This is precisely the operation [[llm-wiki-karpathy|LLM Wiki]] performs constantly and by design — a single source ingest "touches 10–15 pages," meaning most pages accumulate claims synthesized from many sources over time, not one. The LLM Wiki concept page does not connect its own core mechanic to this finding; the connection is only visible from the span-level-attribution side. This is an open risk, not a resolved one: the architecture that does the most multi-source synthesis in this cluster is also the one with the least-instrumented per-claim verification.

## What this means for trusting an answer, concretely

- If you're reading a RAG or Agentic RAG answer with visible citations: trust the *document* the citation points to more than the *sentence* it's attached to — that's the specific gap the benchmarks measure.
- If you're reading an LLM Wiki page: trust that it traces back to *a* real raw source more than you'd trust an uncited claim, but treat multi-source synthesis passages (most of them, after enough ingest cycles) with the same skepticism you'd apply to an unaudited span-level citation — the wiki has no equivalent check.
- Neither failure mode is solved by throwing more context at the model — [[long-context-models|Long-Context Models]]' own page notes the open question of *why* span-level localization fails even when the model has the whole document in context; more tokens in the window does not by itself fix an alignment problem.

## See Also

- [[span-level-attribution|Span-Level Attribution]]
- [[rag|RAG (Retrieval-Augmented Generation)]]
- [[agentic-rag|Agentic RAG]]
- [[llm-wiki-karpathy|LLM Wiki (Karpathy Pattern)]]
- [[memory-economics|The Economics of LLM Memory]]
- [[structure-vs-iteration|Structure vs. Iteration]]
- [[notebooklm-hybrid-stack]] — synthesis drawing on this page

## Sources

- [llm-memory-context-evolution-2026](../sources/llm-memory-context-evolution-2026.md)
