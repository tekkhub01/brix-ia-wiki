---
pageType: source
id: source.sage-agentic-graph-memory-abs
title: "SAGE: A Self-Evolving Agentic Graph-Memory Engine (arXiv 2605.12061)"
sourceType: local-file
sourcePath: /home/brix-ia/.openclaw/workspace/wiki_sources/sage-agentic-graph-memory-abs.md
ingestedAt: 2026-10-04T04:26:41.309Z
updatedAt: 2026-10-04T04:26:41.309Z
status: active
date: 2026-05-12
tags: [source, llm-memory, ingest, graphrag, memory]
url: https://arxiv.org/abs/2605.12061
publish: true
---

# SAGE: A Self-Evolving Agentic Graph-Memory Engine for Structure-Aware Associative Memory

## Source
- Type: `local-file`
- Path: `/home/brix-ia/.openclaw/workspace/wiki_sources/sage-agentic-graph-memory-abs.md`
- Bytes: 3026
- Updated: 2026-10-04T04:26:41.309Z

## Content

## SAGE: A Self-Evolving Agentic Graph-Memory Engine for Structure-Aware Associative Memory

Wang, Zhao, Pan, Wang, Wang, Deng, Zhang. arXiv:2605.12061, v1 2026-05-12.
URL: https://arxiv.org/abs/2605.12061

### Abstract (verbatim, arXiv abs page, fetched 2026-10-04)

Long-term memory is becoming a central bottleneck for language agents. Existing RAG and GraphRAG systems largely treat memory graphs as static retrieval middleware, which limits their ability to recover complete evidence chains from partial cues, exploit reusable graph-structural roles, and improve the memory itself through downstream feedback. We introduce SAGE, a Self-evolving Agentic Graph-memory Engine that models graph memory as a dynamic long-term memory substrate. SAGE couples two roles: a memory writer that incrementally constructs structured graph memory from interaction histories, and a Graph Foundation Model-based memory reader to perform retrieval and provide feedback to the memory writer. We provide rigorous theoretical analyses supporting the framework. Across multi-hop QA, open-domain retrieval, domain-specific review QA, and long-term agent-memory benchmarks, SAGE improves evidence recovery, answer grounding, and retrieval efficiency: after two self-evolution rounds, it achieves the best average rank on multi-hop QA; in zero-shot open-domain transfer, it reaches 82.5/91.6 Recall@2/5 on NQ. Further results on LongMemEval and HaluMem show that training and reader-writer feedback improve multiple long-term memory and hallucination-diagnostic metrics, suggesting that self-evolving, structure-aware graph memory is a promising foundation for robust long-horizon language agents.

NOTE: the abstract on the arXiv page contains typos (Exsting, constucts, structrual, rigorooous, annalyses, retireval, traning, writer-). Recovered here to intended spelling; wording otherwise verbatim.

### Key facts for the corpus

- The thesis [graphrag](../concepts/graphrag.md) attributed to it secondhand ("closest neighbour to the LLM Wiki pattern from the graph side") is confirmed by the abstract itself: SAGE's object is exactly the memory graph that RAG/GraphRAG treat as "static retrieval middleware".
- Architecture = **writer + reader with feedback loop**: the writer incrementally builds graph memory from interaction histories, a Graph Foundation Model reader retrieves and feeds back. Self-evolution rounds are the training loop — this is the write-time-compilation pattern (LLM Wiki) transposed onto the graph side.
- Numbers: best average rank on multi-hop QA after **two** self-evolution rounds; **82.5 / 91.6 Recall@2/5** on NQ zero-shot; evaluated also on LongMemEval and HaluMem (hallucination diagnostics).
- For the hybrid Wiki+Graph synthesis: the two patterns are not competitors at the mechanism level — both move work to write time and make the store a first-class artifact; they differ in substrate (prose pages vs typed graph) and in whether the store self-improves from downstream feedback (SAGE yes; the wiki's compile loop is manual).

## Notes
<!-- openclaw:human:start -->
<!-- openclaw:human:end -->

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
