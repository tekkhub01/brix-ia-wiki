---
pageType: source
id: source.cited-but-not-verified-abs
title: "Cited but Not Verified: Source Attribution in Deep Research Agents (arXiv 2605.06635)"
sourceType: local-file
sourcePath: /home/brix-ia/.openclaw/workspace/wiki_sources/cited-but-not-verified-abs.md
ingestedAt: 2026-10-04T04:26:25.394Z
updatedAt: 2026-10-04T04:26:25.394Z
status: active
date: 2026-05-07
tags: [source, llm-memory, ingest, attribution]
url: https://arxiv.org/abs/2605.06635
publish: true
---

# Cited but Not Verified: Parsing and Evaluating Source Attribution in LLM Deep Research Agents

## Source
- Type: `local-file`
- Path: `/home/brix-ia/.openclaw/workspace/wiki_sources/cited-but-not-verified-abs.md`
- Bytes: 3265
- Updated: 2026-10-04T04:26:25.394Z

## Content

## Cited but Not Verified: Parsing and Evaluating Source Attribution in LLM Deep Research Agents

Onweller, Lumer, Huber, Ramchandani, Subbiah, Feld. arXiv:2605.06635, v1 2026-05-07.
URL: https://arxiv.org/abs/2605.06635

### Abstract (verbatim, arXiv abs page, fetched 2026-10-04)

Large language models (LLMs) power deep research agents that synthesize information from hundreds of web sources into cited reports, yet these citations cannot be reliably verified. Current approaches either trust models to self-cite accurately, risking bias, or employ retrieval-augmented generation (RAG) that does not validate source accessibility, relevance, or factual consistency. We introduce the first source attribution evaluation framework that uses a reproducible AST parser to extract and evaluate inline citations from LLM-generated Markdown reports at scale. Unlike methods that verify claims in isolation, our framework closes the loop by retrieving the actual cited content, enabling human or model evaluators to judge each citation against its source. Citations are evaluated along three dimensions. (1) Link Works verifies URL accessibility, (2) Relevant Content measures topical alignment, and (3) Fact Check validates factual accuracy against source content. We benchmark 14 closed-source and open-source LLMs across three evaluation dimensions using rubric-based LLM-as-a-judge evaluators calibrated through human review. Our results reveal that even the strongest frontier models maintain link validity above 94% and relevance above 80%, yet achieve only 39-77% factual accuracy, while fewer than half of open-source models successfully generate cited reports in a one-shot setting. Ablation studies on research depth show that Fact Check accuracy drops by approximately 42% on average across two frontier models as tool calls scale from 2 to 150, demonstrating that more retrieval does not produce more accurate citations. These findings reveal a critical disconnect between surface-level citation quality and factual reliability, and our framework provides the evaluation infrastructure to assess the disconnect.

### Key facts for the corpus

- Sources the two numbers the corpus was already carrying secondhand: the **39–77% factual accuracy** range and the **~42% depth-related drop** are both in the abstract. The drop is measured as tool calls scale **from 2 to 150**, on two frontier models, averaged — "more retrieval does not produce more accurate citations" is the paper's own conclusion, not an inference.
- The framework is three-dimensional: **Link Works** (accessibility), **Relevant Content** (topical alignment), **Fact Check** (accuracy against retrieved source). Frontier models pass the first two (94%+, 80%+) and fail the third — the gap between a citation that *looks* right and one that *is* right.
- Method: reproducible **AST parser** over the Markdown of generated reports + rubric-based LLM-as-a-judge calibrated with human review. Citation verification by *re-fetching the cited page* — the same move this vault applies manually to its forward-sourced numbers (log 2026-08-26).
- Fewer than half of open-source models produce cited reports at all in one-shot: attribution is a trained capability, not a formatting instruction.

## Notes
<!-- openclaw:human:start -->
<!-- openclaw:human:end -->

## Related
<!-- openclaw:wiki:related:start -->
- No related pages yet.
<!-- openclaw:wiki:related:end -->
