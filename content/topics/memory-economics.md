---
title: "The Economics of LLM Memory: Retrieval, Compilation, and Caching"
category: topic
sources: [raw/notes/llm-memory-context-evolution-2026.md]
created: 2026-08-12
updated: 2026-08-14
verified: 2026-08-12
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
| [[llm-wiki-karpathy]] | Cumulative tokens | 47K vs 305K (**84.6% saved**); projected 53.7–81.3% at 30 days | "a matched RAG baseline" (unspecified: classic or agentic) | 4-query run, then a 30-day projection |
| [[context-caching]] | Per-request price multiplier | read ≈0.1×, write 1.25× (5-min TTL) or 2× (1-hour TTL) | uncached input at 1× | break-even at 2 or 3 repeated requests |

Four different denominators (per-query multiplier, cumulative token count, per-request price multiplier, qualitative-only), two different time horizons that don't map onto each other (a "query" in the agentic-RAG table is not the same unit as a "request" in the caching table, and neither maps onto the 4-query / 30-day horizon the wiki study uses), and — most importantly — three different, non-interchangeable baselines.

## The unresolved seam: what is "a matched RAG baseline"?

The [[llm-wiki-karpathy|LLM Wiki]] compounding study (Wen & Ku, arXiv 2604.11243) reports 84.6% token savings against "a matched RAG baseline." It does not say whether that baseline is classic single-shot RAG or the 2026 production-standard agentic RAG stack — and [[rag|RAG]]'s own page is explicit that classic RAG is "the baseline to beat, not the deployed architecture." If the study's baseline was classic RAG, then the *actual* 2026 comparison — wiki vs the agentic RAG stack teams really run, which [[agentic-rag|Agentic RAG]] prices at 3–5× classic RAG per query — would show an even larger gap. But nobody has published that number. Multiplying 84.6% by the 3–5× agentic multiplier to manufacture an "wiki saves ~90-95% vs agentic RAG" headline would be inventing a statistic neither source states. This wiki declines to do that arithmetic; it flags the gap instead.

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
