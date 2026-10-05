---
title: "The Economics of LLM Memory: Retrieval, Compilation, and Caching"
category: topic
sources: [raw/notes/llm-memory-context-evolution-2026.md]
created: 2026-08-12
updated: 2026-09-13
verified: 2026-09-13
tags: [economics, retrieval, write-time-synthesis, caching, cost]
aliases: [Memory Economics, RAG vs Compilation Cost, LLM Memory Cost Models]
confidence: medium
summary: "Four architectures in this wiki each publish a cost claim — but in four incompatible units, over four different time horizons, against four different baselines. This article lays the numbers side by side rather than pretending they compose into one curve."
volatility: hot
publish: true
---
# The Economics of LLM Memory: Retrieval, Compilation, and Caching

Every concept page in this cluster makes an economic argument for its own approach. None of them share a unit. This article is not a reconciliation — the numbers genuinely do not reconcile — it is an inventory of exactly where they talk past each other, so that nobody accidentally chains them into a statistic none of the underlying sources support.

## The four numbers, as actually published

| Architecture | What's measured | Number | Baseline | Horizon |
|---|---|---|---|---|
| [[rag]] | Token cost | Qualitative only ("lower... only top-k chunks vs full document") | pure long-context stuffing | per query |
| [[agentic-rag]] | Per-query cost multiplier | 3–5× | classic (single-shot) RAG | per query |
| [[llm-wiki-karpathy]] | Cumulative tokens | 47K vs 305K (**84.6% saved**); projected 53.7–81.3% at 30 days | **specified as of 2026-09-13 ingest: the 305K figure is the paper's Long-Context baseline, not classic Chunk-RAG** — full-text ranking: Chunk-RAG 13.6K < Compounding 47K < Long-Context 305K | 4-query run, then a 30-day projection |
| [[context-caching]] | Per-request price multiplier | read ≈0.1×, write 1.25× (5-min TTL) or 2× (1-hour TTL) | uncached input at 1× | break-even at 2 or 3 repeated requests |

Four different denominators (per-query multiplier, cumulative token count, per-request price multiplier, qualitative-only), two different time horizons that don't map onto each other (a "query" in the agentic-RAG table is not the same unit as a "request" in the caching table, and neither maps onto the 4-query / 30-day horizon the wiki study uses), and — most importantly — three different, non-interchangeable baselines.

## The seam, closed (2026-09-13): what "a matched RAG baseline" actually was

This section used to flag the Wen & Ku study's baseline (arXiv 2604.11243) as unspecified — classic RAG or agentic RAG? The full text is now ingested (`sources/wen-ku-knowledge-compounding-under-the-agentic-roi-framework-arxiv-2604-11243.md`), and the answer was neither of the two guesses: the paper defines **two** stateless baselines, and the 305K figure is the **Long-Context** one (~70K tokens/query × 4). The three-way cumulative ranking over the four-query run is **Chunk-RAG 13.6K < Compounding 47K < Long-Context 305K**.

That reframes the corpus's most load-bearing number. The 84.6% saving is real but is a saving **against context stuffing, not against classic RAG** — against Chunk-RAG, compounding spends roughly 3.5× *more* raw tokens (47K vs 13.6K). The paper is explicit that this is the point: "Compounding does not minimize raw token cost; instead, it converts a portion of each query's expenditure into a persistent asset," and even at full saturation its per-query cost "typically remains above Chunk-RAG's flat 3.4K floor." The wiki-vs-RAG comparison the seam asked for — against classic or agentic chunk retrieval — is still unpublished; what the study actually beats is stuffing. The earlier warning against chaining 84.6% with the [[agentic-rag|Agentic RAG]] 3–5× multiplier stands, and is now reinforced: the multiplier was pointed at the wrong baseline.

## Caching complicates both sides of that comparison

[[context-caching|Context Caching]]'s economics apply *within* a single conversation's static prefix — they are not a competing architecture, they are a multiplier that can sit inside either the RAG stack or the LLM Wiki's own consultation cost. Neither the agentic-RAG 3–5× figure nor the LLM Wiki's 47K/305K figures state whether prompt caching was in effect during measurement. If the agentic RAG baseline in either study was run *without* caching, its true production cost (with caching) is lower than published; if the LLM Wiki's page-reading cost benefits from caching stable page content across a session, its savings are partly a caching effect double-counted as a compilation effect. Neither concept page discloses this, so the two numbers cannot be safely combined.

## What every number agrees on, qualitatively

Despite the incompatible units, there is one consistent qualitative thread across all four pages: **cost falls when the same information is consulted more than once, and the mechanism for capturing that reuse differs by architecture.**

- [[context-caching|Context Caching]] captures reuse *within* a session, at the token-prefix level, on a timescale of minutes (TTL-bounded).
- [[llm-wiki-karpathy|LLM Wiki]]'s compounding captures reuse *across* sessions, at the page level, on a timescale of the whole corpus's life — Wen & Ku's framing is explicit about this: it treats "LLM tokens... from consumables into capital goods."
- [[agentic-rag|Agentic RAG]] captures none of this — its 3–5× multiplier is a *per-query* cost with no amortization mechanism at all; every query re-pays for the iteration loop from scratch.
- [[rag|RAG]] captures partial reuse at the index level (embeddings computed once) but re-pays retrieval and reranking every query.

Ranked by how much of the total cost is amortized rather than repaid per query: LLM Wiki (amortizes ingestion across unlimited future queries) > RAG (amortizes embedding, not retrieval) > Agentic RAG (amortizes nothing extra beyond RAG's index) — with Context Caching functioning as a cross-cutting discount that can be laid on top of any of the three within a session.

## The variable that determines which one wins

Both the LLM Wiki study and the RAG page name the same swing variable, using different vocabulary: the LLM Wiki page calls it **topic concentration** (compounding saving of 53.7% at moderate concentration vs 81.3% at high concentration — the wiki spread thin across unrelated domains "amortizes nothing"), and the RAG page's own trade-off section implies the same thing when it notes long-context and RAG each win on different query shapes (scattered-fact vs continuous-narrative). Neither page states this as a formula; both point at the same knob. A synthesis worth stating plainly: **all of these cost claims are workload-conditioned, not architecture-conditioned.** None of the four numbers above is a property of RAG, Agentic RAG, the LLM Wiki, or caching in the abstract — each is a property of a specific workload run against that architecture, and none of the four studies used the same workload.

## See Also

- [[rag|RAG (Retrieval-Augmented Generation)]]
- [[agentic-rag|Agentic RAG]]
- [[llm-wiki-karpathy|LLM Wiki (Karpathy Pattern)]]
- [[context-caching|Context Caching]]
- [[long-context-models|Long-Context Models]]
- [[grounding-across-architectures|Grounding and Failure Modes Across Memory Architectures]]
- [[structure-vs-iteration|Structure vs. Iteration]]
- [[notebooklm-hybrid-stack]] — synthesis drawing on this page
- [Headroom](../syntheses/headroom-context-compression-layer-per-ai-agent-headroomlabs-ai.md) — un quinto numero, in unità ancora diverse: 15–20% sui coding agent, 60–95% su JSON; memory-wiki

## Sources

- [llm-memory-context-evolution-2026](../sources/llm-memory-context-evolution-2026.md)
