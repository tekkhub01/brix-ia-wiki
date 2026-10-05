---
title: "Long-Context Models"
category: concept
sources: [raw/notes/llm-memory-context-evolution-2026.md, sources/lost-in-the-middle-abs.md]
created: 2026-04-28
updated: 2026-10-04
verified: 2026-10-04
tags: [llm, context-window, architecture]
aliases: [Long Context, Long-Context Models]
confidence: medium
summary: "LLMs with context windows at or above 128k; the 2026 frontier tier is uniformly 1M with 128K max output. Complementary to retrieval rather than a replacement."
volatility: hot
publish: true
---
# Long-Context Models

**Type:** LLM architecture / capability class
**Definition:** LLMs designed to handle context windows ≥128k tokens — as of 2026 the frontier tier is uniformly 1M

## Examples (as of 2026-08)

**Claude (Anthropic)** — verified against the Models API / platform docs:

| Model | Context | Max output |
|-------|---------|-----------|
| Claude Fable 5 / Mythos 5 | 1M | 128K |
| Claude Opus 5 | 1M | 128K |
| Claude Opus 4.8 / 4.7 / 4.6 | 1M | 128K |
| Claude Sonnet 5 / 4.6 | 1M | 128K |
| Claude Haiku 4.5 | 200K | 64K |

Two things worth noting. **1M is now the default, not an opt-in** — on Claude Opus 5 the maximum context is also the default, with no beta header and no long-context price premium (this was the "200k standard / 1M extended" split that earlier revisions of this page described; that split is gone). And **max output is capped well below context** — 128K — with streaming required above ~16K to avoid SDK HTTP timeouts.

- **Gemini (Google)**, **GPT-class models**, **GLM 5.1** — earlier figures on this page (1M–2M / 128k–1M / 128k native) date from the April 2026 ingest and were **not** re-verified in the 2026-08 sweep. Treat as stale; re-check before quoting.

## Why context length matters

- Whole codebases, long documents, multi-document reasoning fit in a single prompt
- Reduces dependence on chunking + RAG retrieval for medium corpora
- Enables persistent agent state across sessions without external memory

> **Caveat posizionale — ora con fonte primaria in vault.** A bigger window does not
> mean the content is used well. [Lost in the Middle](../sources/lost-in-the-middle-abs.md)
> (Liu et al., arXiv 2307.03172, abstract ingerita 2026-10-04) misura la curva a U:
> performance highest at the beginning or end of the context, significantly degraded
> in the middle, **"even for explicitly long-context models"** — on multi-document QA
> and key-value retrieval. Two honest limits on the transfer: the paper is July 2023,
> pre-dating the 1M tier described above, and its tasks are about *locating* relevant
> information, not reasoning over it. The operational consequence for this vault's
> own pattern (compilazione + rilettura): a compiled page placed mid-context is not
> equivalent to the same page at the edges — ordering of what goes into the window
> is a design variable, not a detail.

## Inference cost

Attention is O(n²) over context length. Long-context inference is expensive without optimizations:

- **KV cache** — store computed attention states (linear memory in n)
- **[[context-caching|Context Caching]]** — reuse cached prefix across queries
- **[[quantization|Quantization]]** — compress KV tensors
- **PagedAttention / FlashAttention** — efficient memory layout

## Trade-off vs RAG

Long context ≠ retrieval replacement: at 1M tokens latency/cost still high, [[rag|RAG]] remains cheaper for very large corpora. Hybrid is common: RAG narrows to top-k chunks, long-context model reasons over them.

What changed in 2026 is that the *third* option got costed. [[llm-wiki-karpathy|LLM Wiki]] argues the cheapest large-corpus strategy is neither stuffing nor retrieving but **compiling once and re-reading the compilation** — with measured 84.6% token savings against a matched RAG baseline on a repeated-domain workload. Long context is what makes that compilation cheap to *consult*; caching is what makes it cheap to consult *repeatedly*.

## See Also

- [[context-caching|Context Caching]]
- [[rag|RAG (Retrieval-Augmented Generation)]]
- [[llm-wiki-karpathy|LLM Wiki (Karpathy Pattern)]]
- [[notebooklm]] — links here
- [[quantization]] — links here
- [[memory-economics]] — synthesis drawing on this page
- [[notebooklm-hybrid-stack]] — synthesis drawing on this page
- [Headroom](../syntheses/headroom-context-compression-layer-per-ai-agent-headroomlabs-ai.md) — riduce ciò che entra nella finestra invece di allargarla; memory-wiki

## Sources

- [llm-memory-context-evolution-2026](../sources/llm-memory-context-evolution-2026.md)
